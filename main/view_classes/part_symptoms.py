from django.shortcuts import render
from .base import BaseView


from common.controllers.part_symptom_controller import *


class PartSymptomsView(BaseView):
    '''
    Display Symptoms for each body part
    '''

    def __init__(self):
        super().__init__("main/part_symptoms.html")

    def set_context(self):
        try:
            cat_id = int(self.request_params['cat_id'])
        except:
            cat_id = 1

        symptoms = get_parts_symptoms_by_subcategory1(cat_id)

        context = {
            'title': f'TIẾNG NHẬT Y TẾ | CÁC TRIỆU CHỨNG BỆNH LIÊN QUAN ĐẾN VÙNG {symptoms[-1]} TRONG TIẾNG NHẬT',
            'symptoms': symptoms,
        }

        return context
