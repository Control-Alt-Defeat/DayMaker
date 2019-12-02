from django.urls import path
from . import views

app_name = 'planner'
urlpatterns = [
    # ex: /planner/
    path('', views.home, name='home'),
    # ex: /event/5/
    path('plan_index/', views.plan_index, name="plan_index"),
    path('edit_plan/<int:plan_id>', views.edit_plan, name="edit_plan"),
    path('delete_plan/<int:plan_id>', views.delete_plan, name="delete_plan"),
    path('<int:plan_id>/', views.event_index, name='index'),
    path('<int:plan_id>/add/', views.add_event, name='add'),
    path('<int:plan_id>/plan/', views.find_event, name='plan'),
    path('<int:plan_id>/results/', views.display_results, name='search_results'),
    path('<int:plan_id>/delete/<int:event_id>/', views.EventDelete.as_view(), name='delete_event'),
    path('<int:plan_id>/edit/<int:event_id>/', views.EventUpdateView.as_view(), name='edit_event'),
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories')
]
