"""URL configuration for game app.

The `urlpatterns` list routes URLs to views.

The following list shows the mapping:
    / -> Home.
    /test/ -> Test.
    /login/ -> Login.
    /logout/ -> Logout.
    /register/ -> Account creation/registration.
    /game/ -> Game.
    /create_event -> Event creation.
    /profile/ -> User profile.
"""

from django.urls import path

from . import views


# URL to view routing.
urlpatterns = [
    path("", views.home, name="home"),
    path("test/", views.test, name="test"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("register/", views.register, name="register"),
    path("game/", views.game, name="game"),
    path("create_event/", views.create_event, name="create event"),
    path("profile/", views.profile, name="profile"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("events/", views.list_events, name="list events"),
    path("events/<int:event_id>/", views.event_details, name="event details"),
    path("events/<int:event_id>/update", views.update_event, name="update event"),
    path("events/<int:event_id>/delete", views.delete_event, name="delete event"),

    # Treasure chest CRUD operations.
    path("treasure_chests/", views.list_treasure_chests, name="list treasure chests"),
    path("treasure_chests/<int:treasure_chest_id>/", views.treasure_chest_details, name="treasure chest details"),
    path("treasure_chests/new/", views.create_treasure_chest, name="create treasure chest"),
    path("treasure_chests/<int:treasure_chest_id>/update/", views.update_treasure_chest, name="update treasure chest"),
    path("treasure_chests/<int:treasure_chest_id>/delete/", views.delete_treasure_chest, name="delete treasure chest"),
]
