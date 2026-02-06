from rest_framework import serializers
from .models import Note, Reminder, Notification


# -------------------------
# Note（表示用・簡易）
# -------------------------
class NoteSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title"]


# -------------------------
# Reminder
# -------------------------
class ReminderSerializer(serializers.ModelSerializer):
    note = NoteSimpleSerializer(read_only=True)
    note_id = serializers.PrimaryKeyRelatedField(
        queryset=Note.objects.all(), source="note", write_only=True
    )

    class Meta:
        model = Reminder
        fields = [
            "id",
            "note",
            "note_id",
            "remind_at",
            "is_done",
            "created_at",
        ]


# -------------------------
# Notification
# -------------------------
class NotificationSerializer(serializers.ModelSerializer):
    reminder = ReminderSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id",
            "message",
            "is_read",
            "created_at",
            "reminder",
        ]
