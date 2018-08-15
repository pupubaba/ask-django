# blog/admin.py
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'created_at', 'updated_at']
    actions = ['make_draft', 'make_published']

    def content_size(self, post):
        return mark_safe('<strong>{}</strong>글자'.format(len(post.content)))
    content_size.short_description = '글자수'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}개의 포스팅을 Draft상태로 변경'.format(updated_count))
    make_draft.short_description = '지정 포스팅을 Draft상티로 변경합니다.'


    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}개의 포스팅을 Published상태로 변경'.format(updated_count))
    make_published.short_description = '지정 포스팅을 Published상티로 변경합니다.'
# admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display =  ['name']