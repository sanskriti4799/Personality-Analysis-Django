from django.contrib import admin
from django.utils import timezone
from .models import Quest,Attempt
# Register your models here.


admin.site.register(Quest)
admin.site.register(Attempt)
