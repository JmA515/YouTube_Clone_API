from django.urls import path
from . import views


urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<str:videoId>', views.CommentList.as_view()),
    path('comments/<int:pk>/<str:ld>', views.CommentDetail.as_view()),
    path('reply/', views.Reply.as_view()),
]