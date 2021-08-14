from django.http import HttpResponse
from django.views.generic import View


class QuestionList(View):
    """ Question requests controller """

    def get(self, request):
        return HttpResponse('hello')
