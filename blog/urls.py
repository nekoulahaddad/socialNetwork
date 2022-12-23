from django.urls import path
#from . import views
from .views import HomeView,addNoteView,designView,AddPostView,UpdatePostView,DeletePostView,CategoryView,like_unlike_post,mark_all_as_read
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('designers/design/<int:pk>/', designView.as_view(),name="design-detail"),      #pk = primary key
    path('designers/add_post/', AddPostView.as_view(),name="add-post"),
    path('designers/add/', addNoteView,name="add"),
    path('designers/edit_post/<int:pk>/', UpdatePostView.as_view(),name="update-post"),
    path('designers/delete_post/<int:pk>/', DeletePostView.as_view(),name="delete-post"),
    path('designers/category/<str:cats>/', CategoryView,name="category"),
    path('markallasread/', mark_all_as_read, name='mark_all_as_read'),
    path('liked/', like_unlike_post, name='like-post-view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
