from django.contrib import admin
from contact_app.models import studentContact
# Register your models here.
class studentContactAdmin(admin.ModelAdmin):
    list_display=('id','name','fname','mobile','village')
admin.site.register(studentContact,studentContactAdmin)
