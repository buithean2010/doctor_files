from django.shortcuts import render
from django.views import View


class BaseView(View):
    def __init__(self, tpl_name):
        self.template_name = tpl_name
        self.context = {}

    def get(self, request, *args, **kwargs):
        self.context = self.set_context()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        pass

    def set_context(self):
        pass
