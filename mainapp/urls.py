from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('upload/', upload_excel, name='upload_excel'),
    path('check', views.ExcelFileListView.as_view(), name='ExcelFileListView'),

   # path('', react_template, name='react_temple'),
    #path('login/', login_view, name='login'),
    #path('home/', home_view, name='home'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
