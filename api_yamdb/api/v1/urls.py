from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews.views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
)
from users.views import UserSignUpAPIView, UserViewSet, token_obtain

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')

v1_router.register(r'categories', CategoryViewSet, basename='categories')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'titles', TitleViewSet, basename='titles')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


auth_urls = [
    path('signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('token/', token_obtain, name='token'),
]


urlpatterns = [
    path('', include(v1_router.urls), name='api-root'),
    path('auth/', include(auth_urls)),
]
