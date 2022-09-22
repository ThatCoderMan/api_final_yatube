from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
comment_router = SimpleRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)
comment_router.register('comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),
    path('', include('djoser.urls.jwt')),
]
