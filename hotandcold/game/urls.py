"""URL configuration for game app.

The `urlpatterns` list routes URLs to views.
"""

from django.urls import path

from . import views


# URL to view routing.
urlpatterns = [
     # Core views.
    path("", views.home, name="home"),
    path("game/", views.game_list, name="game"),
    path("game/<int:event_id>", views.game, name="play game"),
    path("game_over/<int:participation_id>", views.game_over, name="game over"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),

    # Users and authentication.
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("register/", views.register, name="register"),
    path("users/<str:username>/", views.user_details, name="user"),
    path("update_email/", views.update_user_email, name="update user email"),
   
    # Event CRUD operations.
    path("events/", views.list_events, name="list events"),
    path("events/<int:event_id>/", views.event_details, name="event details"),
    path("events/new/", views.create_event, name="create event"),
    path("events/<int:event_id>/update", views.update_event, name="update event"),
    path("events/<int:event_id>/delete", views.delete_event, name="delete event"),

    # Treasure chest CRUD operations.
    path("treasure_chests/", views.list_treasure_chests, name="list treasure chests"),
    path("treasure_chests/<int:treasure_chest_id>/", views.treasure_chest_details, name="treasure chest details"),
    path("treasure_chests/new/", views.create_treasure_chest, name="create treasure chest"),
    path("treasure_chests/<int:treasure_chest_id>/update/", views.update_treasure_chest, name="update treasure chest"),
    path("treasure_chests/<int:treasure_chest_id>/delete/", views.delete_treasure_chest, name="delete treasure chest"),
]
