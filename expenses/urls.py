from django.urls import path

from . import views

urlpatterns = [
    path("", views.expense_list, name="expense_list"),
    path("dodaj/", views.expense_create, name="expense_create"),
    path("edytuj/<int:pk>/", views.expense_update, name="expense_update"),
    path("usun/<int:pk>/", views.expense_delete, name="expense_delete"),
]