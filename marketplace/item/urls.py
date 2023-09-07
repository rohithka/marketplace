from django.urls import path
from .import views

app_name = "item"

urlpatterns =[
    path("new",views.NewItem,name="new"),
    path("<int:pk>",views.detail,name="detail"),
    path("<int:pk>/delete/",views.delete,name="delete"),
    path("<int:pk>/edit/",views.EditItem,name="edit")
]