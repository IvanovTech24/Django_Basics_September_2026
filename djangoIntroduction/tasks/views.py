from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from tasks.models import Task


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'tasks': Task.objects.all()
    }

    return render(request, 'index.html', context)

# def index(request: HttpRequest) -> HttpResponse:
#     all_tasks = Task.objects.all()
#     return HttpResponse(
#         '\n'.join(str(t) for t in all_tasks),
#         content_type="text/plain"
#     )
