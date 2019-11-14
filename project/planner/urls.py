from django.urls import path
from users import views as users_views
from . import views

app_name = 'planner'
urlpatterns = [
    # ex: /planner/
    path('', views.home, name='home'),
    path('index/<int:plan_id>', views.index, name='index'),
    path('accountDetails',users_views.account_details,name='account_details'),
    path('accountEdit',users_views.account_edit,name='account_edit'),
    path('signup/', users_views.signup, name='signup'),
    path('addPlan/', views.add_plan, name='add_plan'),
    # ex: /event/5/
    path('<int:plan_id>/add/', views.add_event, name='add'),
    path('planIndex/', views.plan_index, name="plan_index"),
    path('<int:plan_id>/plan/', views.find_event, name='plan'),
    path('<int:plan_id>/results/', views.display_results, name='search_results'),
    path('<int:plan_id>/delete/<int:event_id>/', views.EventDelete.as_view(), name='delete_event'),
    path('<int:plan_id>/edit/<int:event_id>/', views.EventUpdateView.as_view(), name='edit_event'),
]
