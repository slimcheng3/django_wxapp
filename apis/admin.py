from django.contrib import admin
from apis.models import App
import hashlib

# Register your models here.
# admin.site.register(App)

@admin.register(App)
class apiAppAdmin(admin.ModelAdmin):
    exclude = ['appid']
    pass

    def save_model(self, request, obj, form, change):
        src = obj.category + obj.application
        src = hashlib.md5(src.encode('utf8')).hexdigest
        obj.appid = src
        super().save_model(request, obj, form, change)




