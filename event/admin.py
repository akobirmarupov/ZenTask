from django.contrib import admin
from .models import Category, Event, Booking, ReminderLog

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'capacity', 'start_time')
    list_filter = ('category', 'start_time')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_time'


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'event')
    list_filter = ('event',)
    search_fields = ('user__username', 'event__title')


@admin.register(ReminderLog)
class ReminderLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'sent_at')
    readonly_fields = ('sent_at',)  # auto_now_add bo'lgani uchun faqat o'qish rejimida