from django.contrib import admin
from django.urls import path, include

from donor.views import home
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('quizes/', include("quiz.urls")),
    path('donor/', include("donor.urls")),


]
