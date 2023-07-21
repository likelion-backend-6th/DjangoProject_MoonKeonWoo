from django.urls import path, re_path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<post>[-\w]+)/$',
            views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('tag/<tag_slug>/', views.post_list, name='post_list_by_tag'),
    # re_path(r'^tag/(?P<tag_slug>[ㄱ-힣a-zA-Z0-9_]+)/$', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
