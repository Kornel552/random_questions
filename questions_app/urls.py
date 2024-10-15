from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('edit/<int:item_id>', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('random/<int:topic_id>/', views.random_question_view, name='random_question'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('topic/<int:topic_id>/question/<int:question_id>/edit/', views.edit_question, name='edit_question'),
]