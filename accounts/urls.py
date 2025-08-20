from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    #‘django.contrib.auth.urls' means that you introduce 
    # the default user management function from django.
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    
]