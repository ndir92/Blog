from django.urls import path

from django.urls import path
from app.views import List, detailView

urlpatterns = [
    path('', List.as_view(), name="home"),
    path('detail/<slug:slug>', detailView, name="detailView"),
]