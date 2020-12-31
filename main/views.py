from django.shortcuts import render

# Create your views here.
from common.controllers.get_all_categories import *
from common.math_filters import *


def medication_symptoms(request):
    '''
    Main category display method
    '''

    context = {
        'categories': get_all_categories(),
    }
    return render(
        request,
        'main/medication_symptoms.html',
        context
    )
