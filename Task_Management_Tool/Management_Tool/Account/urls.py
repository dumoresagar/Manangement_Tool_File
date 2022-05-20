from django.urls import path
from Account.views import UserRegistionView,UserLoginView

urlpatterns = [
    path('register/',UserRegistionView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

]