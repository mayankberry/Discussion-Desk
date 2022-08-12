from django.contrib import admin
from myapp.models import contact,Challenge,Answer
# Register your models here.

admin.site.register(contact),
admin.site.register((Answer)),
@admin.register(Challenge)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
