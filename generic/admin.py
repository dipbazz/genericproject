from django.contrib import admin
from .models import ActivityLog, Address, Profile, Company
# Register your models here.


admin.site.register(ActivityLog)
admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Address)
