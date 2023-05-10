from django.urls import path
from . import views
urlpatterns = [
path('mycv/', views.mycv, name='mycv'),
]
