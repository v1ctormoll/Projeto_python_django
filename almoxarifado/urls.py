from django.urls import path
from almoxarifado.views import createView, readView, updateView, deleteView

urlpatterns = [
    path('',readView, name='lista'),
    path('create/',createView, name='create'),
    path('update/<int:id>/', updateView, name='update'),
    path('delete/<int:id>/', deleteView, name='delete'),

]