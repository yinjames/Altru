from django.contrib import admin

from .models import DonorAttitude  , DonorKnowledge, Champion, Team



admin.site.register(DonorAttitude)
admin.site.register(DonorKnowledge)
admin.site.register(Champion)
admin.site.register(Team)