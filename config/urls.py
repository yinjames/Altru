from django.contrib import admin
from django.urls import path, include

from donor.views import hero, home
urlpatterns = [
    #path('', hero, name='greetings'),
    #path('home/', home, name='home'),
    path('admin/', admin.site.urls),
    path('quizes/', include("quiz.urls")),
    path('', include("donor.urls")),
    path('accounts/', include('allauth.urls')),


]
