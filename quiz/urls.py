from django.urls import path
from .views import get_all_questions, get_active_category, get_history_category, edit_active_status


urlpatterns = [
    path("questions/<int:pk>/", get_all_questions),
    path('category/active/', get_active_category),
    path('category/history/', get_history_category),
    path('category/set/inactive/<int:pk>/',edit_active_status )
]