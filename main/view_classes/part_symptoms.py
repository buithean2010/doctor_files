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
            part_id = int(self.request_params['part_id'])
        except:
            part_id = 1

        symptoms = get_symptoms_by_part_id(part_id)

        context = {
            'title': f'TIẾNG NHẬT Y TẾ | CÁC TRIỆU CHỨNG BỆNH LIÊN QUAN ĐẾN VÙNG {symptoms.first().part.name_vn} TRONG TIẾNG NHẬT',
            'symptoms': symptoms,
        }

        return context
