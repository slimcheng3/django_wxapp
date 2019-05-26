from django.contrib import admin
from authorization.models import User

# Register your models here.
# admin.site.register(User)
@admin.register(User)
class authorizationUserAdmin(admin.ModelAdmin):
    exclude = ['openid']
    pass