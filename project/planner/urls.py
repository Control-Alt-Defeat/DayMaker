from django.urls import path
from users import views as users_views
from . import views

app_name = 'planner'
urlpatterns = [
    # ex: /planner/
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('accountDetails',users_views.account_details,name='account_details'),
    path('accountEdit',users_views.account_edit,name='account_edit'),
    path('signup/', users_views.signup, name='signup'),
    # ex: /event/5/
    path('add/', views.add_event, name='add'),
    path('plan/', views.find_event, name='plan'),
    path('results/', views.display_results, name='search_results'),
    path('delete/<int:event_id>/', views.EventDelete.as_view(), name='delete_event'),
    path('edit/<int:event_id>/', views.EventUpdateView.as_view(), name='edit_event'),
]
