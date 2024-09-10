from django.contrib import admin
from .models import FormModel,DonateModel,UserDetailModel
# Register your models here.
class FormAdmin(admin.ModelAdmin):
    list_display=('FirstName','LastName')
    list_filter=('FirstName','competition')
admin.site.register(FormModel,FormAdmin)

class DonateAdmin(admin.ModelAdmin):
    list_filter=('Date',)
admin.site.register(DonateModel,DonateAdmin)
admin.site.register(UserDetailModel)