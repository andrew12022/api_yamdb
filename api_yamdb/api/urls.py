from django.urls import include, path
from rest_framework import routers

from api.views import TitleViewSet, SignUpView, ReviewViewset, CommentViewset

router_v1 = routers.DefaultRouter()

router_v1.register(r'titles', TitleViewSet)
router_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews',
    ReviewViewset, basename='reviews'
)
router_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)',
    ReviewViewset,
    basename='review'
)
router_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/'
    r'comments',
    CommentViewset, basename='comments'
)
router_v1.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/'
    r'comments/(?P<comment_id>\d+)',
    CommentViewset, basename='comment'
)


urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/', include(router_v1.urls))
]
