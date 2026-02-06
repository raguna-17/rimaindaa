from django.contrib import admin

from .models import Note, Reminder, Notification


# -------------------------
# Note Admin
# -------------------------
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "updated_at")
    list_filter = ("user",)
    search_fields = ("title",)
    ordering = ("-updated_at",)


# -------------------------
# Reminder Admin
# -------------------------
@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("note", "remind_at", "is_done", "created_at")
    list_filter = ("is_done", "remind_at")
    search_fields = ("note__title",)
    ordering = ("remind_at",)


# -------------------------
# Notification Admin
# -------------------------
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("message", "user__username")
    ordering = ("-created_at",)
