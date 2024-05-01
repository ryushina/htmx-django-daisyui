from django.db import models
from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "is_completed",
        "user",
        "created_at",
    )  # Fields to display in the admin list view
    list_editable = (
        "is_completed",
        "user",
    )  # Fields that can be edited directly in the list view
    list_filter = ("is_completed", "user")  # Filters on the right sidebar
    search_fields = ("description", "user__username")  # Fields that can be searched


# register models
admin.site.register(Todo, TodoAdmin)
