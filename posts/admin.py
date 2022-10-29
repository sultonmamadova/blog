from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_text", "is_draft")
    readonly_fields = ("created_at", "updated_at")
    list_editable = ("is_draft",)
    search_fields = (
        "title",
        "text",
        "author__username",
        "author__first_name",
        "author__last_name",
    )
    list_filter = ("is_draft",)

    def get_text(self, instance):
        return f"{instance.text:.300}"
