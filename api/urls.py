from django.urls import path
from .views import ReviewListAPIView, admin_only_view, login_view, mentor_only_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("admin-only/", admin_only_view),
    path("mentor-only/", mentor_only_view),
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
]
