from django.urls import  path
from .import views
urlpatterns=[
    path('',views.homepageview,name='home'),
    path('navar/',views.navarpageview,name="navar"),
    path('userprofile/<str:pk>/',views.userProfilepaveview,name="userprofile_page"),
    path('login/',views.loginpageivew,name="login_page"),
    path('register/',views.registerpageview,name="register_page"),
    path('room/<str:pk>/',views.roompageview,name="room_page"),
    path('roomcreate',views.roomcreatepageview,name="roomcreate_page"),
    path('roomupdate/<str:pk>/',views.roomUpdatepageview,name="roomupdate_page"),
    path('roomdelete/<str:pk>/',views.roomdeletepageview,name="roomdelete_page"),
    path('messagedelete/<str:pk>/',views.messagesdeletepageview,name="delete_message"),
]