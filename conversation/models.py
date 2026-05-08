from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model()



class ChatRoom(models.Model):
    participants = models.ManyToManyField(User, related_name="chat_rooms")
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('event.Course', on_delete=models.SET_NULL, null=True, blank=True)
    vacancy = models.ForeignKey('vacancies.Vacancy', on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']


class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    text = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender.username}: {self.text[:20] if self.text else 'Media file'}"


class MessageAttachment(models.Model):
    FILE_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('document', 'Document'),
    ]

    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="attachments")
    file = models.FileField(upload_to='chat_media/%Y/%m/%d/')
    file_type = models.CharField(max_length=20, choices=FILE_TYPES) # TO'G'RILANDI
    original_name = models.CharField(max_length=255, blank=True)
    file_size = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.file_type} for message {self.message.id}"