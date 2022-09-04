from django.urls import path

from products import views

urlpatterns = [
    path("", views.ProductCreateAPIView.as_view()),
    path("<int:pk>/", views.ProoductDetailAPIView.as_view()),
    path("<int:pk>/update/", views.ProoductUpdateAPIView.as_view()),
    path("<int:pk>/delete/", views.ProoductDestroyAPIView.as_view()),
]