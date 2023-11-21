from django.contrib import admin
from django_1.models import studentPublic,DjangoTable
# Register your models here.
class studentPublicAdmin(admin.ModelAdmin):
    list_display=('id','s_id','s_name','s_roll','s_dep')
admin.site.register(studentPublic,studentPublicAdmin)

class djangoTableAdmin(admin.ModelAdmin):
    list_display=('id','ids','names','balance')
admin.site.register(DjangoTable,djangoTableAdmin)