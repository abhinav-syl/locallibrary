from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'geeks', views.GeeksViewSet)
router.register(r'author', views.AuthorViewSet)



urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
