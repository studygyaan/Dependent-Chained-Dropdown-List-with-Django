from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_changelist'),
    path('add/', views.StudentCreateView.as_view(), name='student_add'),
    path('<int:pk>/', views.StudentUpdateView.as_view(), name='student_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
   ]