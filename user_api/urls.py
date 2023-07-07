from django.urls import path
from . import views

urlpatterns =[ 
    path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
	path('upload', views.ExcelFileUploadView.as_view(), name='upload'),
	path('check-upload', views.ExcelFileListView.as_view(), name='check-upload'),
	path('current_user', views.get_current_user.as_view, name='current_user'),

]