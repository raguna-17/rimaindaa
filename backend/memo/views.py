from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Note, Reminder, Notification
from .serializers import (
    NoteSimpleSerializer,
    ReminderSerializer,
    NotificationSerializer,
)


# -------------------------
# Note
# -------------------------
class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSimpleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# -------------------------
# Reminder
# -------------------------
class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reminder.objects.filter(note__user=self.request.user)

    def perform_create(self, serializer):
        note = serializer.validated_data["note"]

        # 他人のNoteを指定してきたら拒否
        if note.user != self.request.user:
            raise PermissionDenied(
                "You cannot create a reminder for someone else's note."
            )

        reminder = serializer.save()

        # Notificationも作成
        Notification.objects.create(
            user=self.request.user,
            reminder=reminder,
            message=f"Reminder: {note.title} at {reminder.remind_at}",
        )


# -------------------------
# Notification
# -------------------------
class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
