from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article-list'), # api/memes/
    path('create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article-detail'),
]
