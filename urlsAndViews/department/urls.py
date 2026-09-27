from django.urls import path, re_path, include
from department.views import index, slug_view, path_view, uuid_view, show_archive

urlpatterns = [
    re_path(r'^archive/(?P<archive_year>202[0-4])/$', show_archive),
    path('department/', include([
        path('<int:id>/', index),
        path('<uuid:uuid>/', uuid_view),
        path('<slug:slug>/', slug_view),
        path('<id>/', index),
        path('<path:path>/', path_view),
    ])),
]