from django.urls import path
from .views import set_background
from . import views
from .views import(
    PagesaapListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/',BlogCreateView.as_view(), name='post_new'),
    path('', PagesaapListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('set-background/', set_background, name='set_background'),
]


