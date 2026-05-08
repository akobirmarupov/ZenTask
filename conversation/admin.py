from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ChatRoom, Message, MessageAttachment


class MessageAttachmentInline(admin.TabularInline):
    model = MessageAttachment
    extra = 0
    readonly_fields = ['display_file']

    def display_file(self, obj):
        if obj.file_type == 'image' and obj.file:
            return mark_safe(
                f'<img src="{obj.file.url}" width="50" height="50" '
                f'style="border-radius: 50%; object-fit: cover; border: 1px solid #ddd;" />'
            )
        return "Fayl (Rasm emas)"
    display_file.short_description = "Preview"



@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_participants', 'course', 'vacancy', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['participants__username', 'course__title', 'vacancy__title']

    def display_participants(self, obj):
        return ", ".join([u.username for u in obj.participants.all()])
    display_participants.short_description = "Qatnashchilar"



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'room', 'short_text', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['sender__username', 'text']
    inlines = [MessageAttachmentInline] # Xabarga biriktirilgan fayllar pastida chiqadi

    def short_text(self, obj):
        return obj.text[:30] if obj.text else "Media xabar"
    short_text.short_description = "Xabar matni"



@admin.register(MessageAttachment)
class MessageAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_sender', 'file_type', 'display_image', 'original_name']
    
    def message_sender(self, obj):
        return obj.message.sender.username
    
    def display_image(self, obj):
        if obj.file_type == 'image' and obj.file:
            return mark_safe(
                f'<img src="{obj.file.url}" width="45" height="45" '
                f'style="border-radius: 50%; object-fit: cover;" />'
            )
        return obj.file_type
    display_image.short_description = "Rasm"