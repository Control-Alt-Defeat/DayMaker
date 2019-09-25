from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    # ex: /planner/
    path('', views.index, name='index'),
    # ex: /event/5/
    path('add/', views.add_event, name='add'),
    path('<int:event_id>/', views.edit_event, name='edit'),
    ## ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    ## ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]