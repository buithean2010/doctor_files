from django.urls import path
from main import views

from main.view_classes.symptom_category import *

urlpatterns = [
    path("", SymptomCategoryView.as_view(), name="home"),
]
