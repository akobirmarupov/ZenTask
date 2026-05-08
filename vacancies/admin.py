from django.contrib import admin

from vacancies.models import Vacancy, Skill, Requirement


class RequirementInline(admin.TabularInline):
    model = Requirement
    extra = 1

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active', 'job_type', 'created_at')
    search_fields = ('title', 'company_name', 'description')
    filter_horizontal = ('skills',)
    inlines = [RequirementInline]
    actions = ['make_active', 'make_hidden']

    @admin.action(description="Tanlangan vakansiyalarni faollashtirish")
    def make_active(self, request, queryset):
        queryset.update(status='active', is_active=True)

    @admin.action(description="Tanlangan vakansiyalarni muzlatish (hidden)")
    def make_hidden(self, request, queryset):
        queryset.update(status='hidden')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)