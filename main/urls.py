from django.urls import path
from main import views

from main.view_classes.symptom_category import *
from main.view_classes.part_symptoms import *

urlpatterns = [
    path("", SymptomCategoryView.as_view(), name="home"),
    path("part_symptoms/<int:cat_id>/",
         PartSymptomsView.as_view(), name="part_symptoms"),
]
