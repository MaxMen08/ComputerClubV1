from django.urls import path
from .views import index, add_player, EditPlayers, DeletePlayers, player_detail, player_list, comp_detail, add_visit

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_player, name='add'),
    path('edit/<int:pk>/', EditPlayers.as_view(), name='edit'),
    path('delete/<int:pk>/', DeletePlayers.as_view(), name='delete'),
    path('player/<int:pk>/', player_detail, name='player_detail'),
    path('player_list/', player_list, name='player_list'),
    path('comp_detail/<int:pk>', comp_detail, name='comp_detail'),
    path('add_visit/', add_visit, name='add_visit'),
] 