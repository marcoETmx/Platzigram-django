
from django.urls import path
from users import views
from django.views.generic import TemplateView

urlpatterns = [

    path(
        route='<str:username>/',
        view=TemplateView.as_view(template_name='users/detail.html'),
        name='detail'
    ),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('me/profile/', views.update_profile, name='update_profile'),
]
