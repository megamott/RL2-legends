from .core.class_utils import BaseView


class QuestionList(BaseView):
    """ Question requests controller """

    def get(self, request):
        return {'message': 'good'}
