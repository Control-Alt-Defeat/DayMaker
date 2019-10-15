from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    # ex: /planner/
    path('', views.index, name='index'),
    # ex: /event/5/
    path('add/', views.add_event, name='add'),
    #path('<int:event_id>/', views.edit_event, name='edit'),
    path('plan/', views.find_event, name='plan'),
    path('results/', views.display_results, name='search_results'),
]
