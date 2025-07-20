from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegisteredUserLoginView

urlpatterns = [
    path('', views.root_redirect, name='root'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('addgoal/', views.add_goal_view, name='addgoal'),
    path('addtransaction/', views.add_transaction_view, name='addtransaction'),
    path('transaction/', views.transaction_view, name='transaction'),
]
