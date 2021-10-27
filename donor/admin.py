from django.contrib import admin
from django.contrib.admin.decorators import display

from import_export.admin import ImportExportModelAdmin

from .models import DonorAttitude  , DonorKnowledge, Champion, Team, Story, Faq



class DonorAttitudeAdmin(ImportExportModelAdmin):

    list_display  = ('q1', 'q3','q5', 'q7','q11', 'q12','q14', 'q15','quiz_score', 'consent_after_quiz','consent_after_story','consent_after_reward', 'consent_msg', 'no_consent_msg')

class DonorknowledgeAdmin(ImportExportModelAdmin):

    list_display  = ('gender', 'qualification', 'marital_status','q1', 'q2','q3','q4','q5', 'q6','q7', 'q8','q9','q10', )

admin.site.register(DonorAttitude, DonorAttitudeAdmin)
admin.site.register(DonorKnowledge, DonorknowledgeAdmin)
admin.site.register(Champion)
admin.site.register(Team)
admin.site.register(Story)
admin.site.register(Faq)