from django.urls import path
from . import views

urlpatterns = [
    path('user',views.UserView.as_view()),
    path('register',views.UserRegisterView.as_view()),
    path('userdetails',views.UserDetailsView.as_view()),
    path('addfavourite',views.AddFavourite.as_view()),
    path('deletefavourite',views.DeleteFavourite.as_view()),
    
]   