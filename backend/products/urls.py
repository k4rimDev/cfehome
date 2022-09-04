from django.urls import path

from products import views

urlpatterns = [
    path("<int:pk>/", views.ProoductDetailAPIView.as_view()),
    path("", views.ProductCreateAPIView.as_view()) # Creation
]