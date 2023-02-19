from django.urls import  path
from classroom import views


urlpatterns = [
    path('', imageView.as_view(), name = "d"),
]
