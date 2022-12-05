from django.urls import path, include

from .import views 
from .views import article_list, article_detail, user_login, register, add_article, update_article,delete_article
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
		path('', views.article_list, name='article_list'), 
		path('article_detail/<slug:slug>/', views.article_detail, name='article_detail'),
		path('login/', LoginView.as_view(), name='user_login'), 
		path('logout/', LogoutView.as_view(), name='user_logout'), 
		path('signup/', views.register, name='register'),
		path('add/', views.add_article, name='add_article'),
		path('update/<slug:slug>/', views.update_article, name='update_article'),
		path('delete/<slug:slug>/', views.delete_article, name='delete_article'),
		path('password-change/', PasswordChangeView.as_view(), name='password-change'),
		path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
		path('social-auth/', include('ashiriblogapp/social_django,urls', namespace = 'social')),
]