from django.urls import path,include

from .views import registerUser,loginUser,logoutUser


app_name="users"
urlpatterns = [
    path("signup/",registerUser,name="signup"),
    path("login/",loginUser,name="login"),
    path("logout/",logoutUser,name="signout"),
    
]