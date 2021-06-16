from . import models


def simple_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        if '/admin/' not in request.path:
            models.Logs.objects.create(path=request.path, method=request.method)
        return response
    return middleware
