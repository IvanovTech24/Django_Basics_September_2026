from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f"The type is {type(id)}", content_type='text/plain')

def slug_view(request: HttpRequest, slug: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(slug)} and the slug is {slug}", content_type='text/plain')

def path_view(request: HttpRequest, path: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(path)} and the path is {path}", content_type='text/plain')

def uuid_view(request: HttpRequest, uuid: str) -> HttpResponse:
    return HttpResponse(f"The type is {type(uuid)} and the uuid is {uuid}", content_type='text/plain')

def show_archive(request, archive_year: int):
    return HttpResponse(f"The requested year is {archive_year}")