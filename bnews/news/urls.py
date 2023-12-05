from django.urls import path

from . import views
from .views import by_rubric, get_detail

urlpatterns = [

    path('catigory/<slug:slug>/', by_rubric, name='by_rubric'),
    path('', views.NewssAllView.as_view(), name='main'),
    path('single/<slug:slug>/', get_detail, name='get_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),


   ]
