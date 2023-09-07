from django.urls import path
from.views import home_page,enroll_page
urlpatterns = [
    path("", home_page, name="main-page"),
    path("enroll/",enroll_page, name='enroll-page'),
    
]