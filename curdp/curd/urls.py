
from django.urls import path
from . import views

urlpatterns = [
    path('',views.insert),
    path('show',views.show),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
   
]
