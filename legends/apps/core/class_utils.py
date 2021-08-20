from django.http import JsonResponse
from django.views.generic import View


class BaseView(View):
    """ Base View for any exception catching """

    def dispatch(self, request, *args, **kwargs):
        """ Rewrite view's dispatch method"""
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            return self._response({'message': e.message}, status=400)

        if isinstance(response, (list, dict)):
            return self._response(response)

        return response

    @staticmethod
    def _response(data, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list)
        )
