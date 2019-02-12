from django.http import HttpResponse


def index( request ):
    return HttpResponse("Hello world, your're at the inventory index")
