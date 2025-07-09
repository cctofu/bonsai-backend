from django.urls import path
from .views import SpecificEntryView, VagueEntryView

urlpatterns = [
    path('specific/', SpecificEntryView.as_view(), name='specific-entry'),
    path('vague/', VagueEntryView.as_view(), name='vague-entry'),
]
