print("MyTEST-app.urls")
from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/
    path('', views.redirectreq),
    # localhost:8000/shows
    path('shows', views.index),
    # localhost:8000/shows/new
    path('shows/new', views.new_show),
    # localhost:8000/shows/create
    path('shows/create', views.create_show),
    # localhost:8000/shows/<show_id>
    path('shows/<int:show_id>', views.display_show),
    # localhost:8000/shows/<show_id>/edit
    path('shows/<int:show_id>/edit', views.edit),
    # localhost:8000/shows/<show_id>/update
    path('shows/<int:show_id>/update', views.update),
     # localhost:8000/shows/<show_id>/delete
    path('shows/<int:show_id>/delete', views.delete),
    
        
]