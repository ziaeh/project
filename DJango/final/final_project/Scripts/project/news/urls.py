from django.urls import path
from.views import self_page 
urlpatterns = [
    path("", self_page, name="self-page")
    
]