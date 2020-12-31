from django.shortcuts import render
from .base import BaseView


from common.controllers.get_all_categories import *


class SymptomCategoryView(BaseView):
    '''
    Main category display class
    '''

    def __init__(self):
        super().__init__("main/symptom_category.html")

    def set_context(self):
        context = {
            'categories': get_all_categories(),
        }
        return context
