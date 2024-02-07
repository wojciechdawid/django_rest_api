from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

# snippet_list = views.SnippetViewSet.as_view({
#     "get": 'list',
#     "post": 'create',
# })
#
# snippet_detail = views.SnippetViewSet.as_view({
#     "get": 'retrieve',
#     "put": 'update',
#     "patch": 'partial_update',
#     "delete": 'destroy',
# })
#
# snippet_highlight = views.SnippetViewSet.as_view({
#     "get": 'highlight',
# }, renderer_classes=[renderers.StaticHTMLRenderer])
#
# user_list = views.UserViewSet.as_view({
#     "get": "list",
# })
#
# user_detail = views.UserViewSet.as_view({
#     "get": "retrieve"
# })
#
# urlpatterns = [
#     # path("snippets/", views.snippet_list),
#     path("", views.api_root, name="api-root"),
#     path("snippets/", snippet_list, name='snippet-list'),
#     # path("snippets/<int:pk>/", views.snippet_detail),
#     path("snippets/<int:pk>/", snippet_detail, name='snippet-detail'),
#     path("snippets/<int:pk>/highlighted", snippet_highlight, name='snippet-highlighted'),
#     path("users/", user_list, name='user-list'),
#     path("users/<int:pk>/", user_detail, name='user-detail')
# ]

router = DefaultRouter()

router.register('snippets', views.SnippetViewSet, basename='snippet')
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path("", views.api_root, name="api-root"),
    path('', include(router.urls))
]

# urlpatterns = format_suffix_patterns(urlpatterns)