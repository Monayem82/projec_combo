from django.contrib import admin
from home_page.models import stunetInfo
# Register your models here.

class studentInfoAdmin(admin.ModelAdmin):
    list_display=(['id','ids','Name','Roll','Dep','Code','Commnet'])
admin.site.register(stunetInfo,studentInfoAdmin)