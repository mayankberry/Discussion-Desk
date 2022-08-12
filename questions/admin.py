from django.contrib import admin
from questions.models import Ques, BlogComment
# Register your models here.

admin.site.register((BlogComment))
@admin.register(Ques)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)