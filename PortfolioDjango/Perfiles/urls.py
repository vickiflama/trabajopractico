from django.urls import path
from Portfolio.views import PerfilListView

urlpatterns= {
    path('', PerfilListView.as_view(), name='nosotreees') 
}