from django.urls import path
from .views import UserRegisterView,signup_view,ProfileView,AllDesignersView,AboutDesignerView,add_friend,UpdateProfile,addWorkView,addWork,changePrivacy,PasswordsChangeView,passwordSuccess
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('register/',UserRegisterView.as_view(),name="register"),
    path('profile/<str:username>/',ProfileView,name="profile"),
    path('profile/<str:username>/about/',AboutDesignerView,name="about_profile"),
    path('all/',AllDesignersView,name="designers"),
    path('register/', signup_view, name="register"),
    path('added/', add_friend, name="add-friend-view"),
    path('profile/edit/<int:pk>/', UpdateProfile.as_view(), name="edit_profile"),
    path('editwork/', addWorkView, name="edit_work"),
    path('addwork/', addWork, name="addwork"),
    path('privacy/', changePrivacy, name="change_privacy"),
    path('change_password/', PasswordsChangeView.as_view(template_name='edit_password.html'), name="change_password"),
    path('password_success/', passwordSuccess, name="password_success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
