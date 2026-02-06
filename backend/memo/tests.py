import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from memo.models import Note, Reminder, Notification
from memo.serializers import (
    NoteSimpleSerializer,
    ReminderSerializer,
    NotificationSerializer,
)


# -------------------------
# Fixtures
# -------------------------
@pytest.fixture
def user1(db):
    return User.objects.create_user(username="user1", password="pass")


@pytest.fixture
def user2(db):
    return User.objects.create_user(username="user2", password="pass")


@pytest.fixture
def note1(user1):
    return Note.objects.create(user=user1, title="Note1")


@pytest.fixture
def note2(user2):
    return Note.objects.create(user=user2, title="Note2")


@pytest.fixture
def api_client(user1):
    client = APIClient()
    client.force_authenticate(user=user1)
    return client


# -------------------------
# Model Tests
# -------------------------
def test_note_str(note1):
    assert str(note1) == "Note1"


def test_reminder_creation(note1):
    remind_time = timezone.now()
    reminder = Reminder.objects.create(note=note1, remind_at=remind_time)
    assert reminder.note == note1
    assert reminder.is_done is False


def test_notification_creation(note1, user1):
    reminder = Reminder.objects.create(note=note1, remind_at=timezone.now())
    notification = Notification.objects.create(
        user=user1, reminder=reminder, message="Test"
    )
    assert notification.user == user1
    assert notification.reminder == reminder
    assert notification.is_read is False


# -------------------------
# Serializer Tests
# -------------------------
def test_note_serializer(note1):
    serializer = NoteSimpleSerializer(note1)
    assert serializer.data["title"] == "Note1"


def test_reminder_serializer(note1):
    reminder = Reminder.objects.create(note=note1, remind_at=timezone.now())
    serializer = ReminderSerializer(reminder)
    assert serializer.data["note"]["id"] == note1.id


def test_notification_serializer(note1, user1):
    reminder = Reminder.objects.create(note=note1, remind_at=timezone.now())
    notification = Notification.objects.create(
        user=user1, reminder=reminder, message="Hi"
    )
    serializer = NotificationSerializer(notification)
    assert serializer.data["reminder"]["id"] == reminder.id


# -------------------------
# API / View Tests
# -------------------------
def test_get_memos_queryset(api_client, note1, note2):
    response = api_client.get("/api/memos/")  # ルーターに合わせたURL
    assert response.status_code == status.HTTP_200_OK
    ids = [item["id"] for item in response.json()]
    assert note1.id in ids
    assert note2.id not in ids


def test_create_reminder_valid(api_client, note1):
    remind_time = timezone.now()
    data = {"note_id": note1.id, "remind_at": remind_time.isoformat()}
    response = api_client.post(
        "/api/reminders/", data, format="json"
    )  # ルーターに合わせる
    assert response.status_code == status.HTTP_201_CREATED
    # Notification が作られている
    reminder_id = response.data["id"]
    assert Notification.objects.filter(reminder__id=reminder_id).exists()


def test_create_reminder_invalid_note(api_client, note2):
    remind_time = timezone.now()
    data = {"note_id": note2.id, "remind_at": remind_time.isoformat()}
    response = api_client.post("/api/reminders/", data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_get_notifications_queryset(api_client, note1, user1):
    # Notification を事前作成
    reminder = Reminder.objects.create(note=note1, remind_at=timezone.now())
    notification = Notification.objects.create(
        user=user1, reminder=reminder, message="Test"
    )
    response = api_client.get("/api/notifications/")
    assert response.status_code == status.HTTP_200_OK
    ids = [n["id"] for n in response.json()]
    assert notification.id in ids
