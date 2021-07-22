from django.contrib import admin

from .models import DonorAttitude  , DonorKnowledge

admin.site.register(DonorAttitude)
admin.site.register(DonorKnowledge)