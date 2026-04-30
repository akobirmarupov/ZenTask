from django.db import models
from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Event(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.IntegerField()
    start_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    


class Booking(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'event')



class ReminderLog(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)