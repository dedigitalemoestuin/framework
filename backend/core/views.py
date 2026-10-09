from django.http import HttpRequest, HttpResponse


def index(_: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, World!")
