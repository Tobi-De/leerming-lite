from django.urls import path

from . import views

app_name = "flashcards"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/edit/", views.edit, name="edit"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/show-answer/", views.show_answer, name="show_answer"),
    path("<int:pk>/show-question/", views.show_question, name="show_question"),
]
