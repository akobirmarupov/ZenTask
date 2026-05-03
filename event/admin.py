from django.contrib import admin
from .models import Category, SubCategory, Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ('title', 'duration_display', 'is_preview')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'category', 'price', 'students_count_display')
    list_filter = ('category', 'owner', 'created_at')
    search_fields = ('title', 'description')
    inlines = [LessonInline] 
    

    def students_count_display(self, obj):
        return obj.students_count()
    students_count_display.short_description = "O'quvchilar soni"

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'duration_display', 'is_preview')
    list_filter = ('course', 'is_preview')
    search_fields = ('title', 'course__title')