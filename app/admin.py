from django.contrib import admin
from .models import file,Students,Faculty, User
# Register your models here.

class file_admin(admin.ModelAdmin):
    list_display=('name','date','files')

admin.site.register(file,file_admin)
admin.site.register(Students)
admin.site.register(Faculty)
admin.site.register(User)
