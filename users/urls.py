from django.urls import  path
from .views import *
urlpatterns=[
    path('singup/', CreateUSerView.as_view(),name='singup'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/useredit/', UserProfileEditView.as_view(), name='edituser'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='userdelete'),


]