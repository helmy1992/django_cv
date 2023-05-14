from django.urls import path
from .views import list_view
urlpatterns = [
path('mycv/', mycv, name='mycv')
path('list/',list_view,name='list')
]
