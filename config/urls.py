from django.contrib import admin
from django.urls import include, path

app_name = "kanban"
urlpatterns = [
    path("kanban/", include("kanban.urls")),
    path('admin/', admin.site.urls),
]
