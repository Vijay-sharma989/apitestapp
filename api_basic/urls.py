# from .views import (article_list,article_detail,ArticleListView,ArticleDetailView,
#     GenericApiView,GenericDetails,ApiViewSet,GenericViewSet,ModelViewSet)
# from .views import FileDownload
from .views import ModelViewSet, FileDownloadListAPIView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article' ,ModelViewSet, basename='article')
# router.register('article' ,FileDownload, basename='article')



urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('download/<int:id>/',FileDownloadListAPIView.as_view())
    # path('viewset/<int:pk>/download',FileDownload.as_view()),
    # # path('article/', article_list),
    # path('article/',ArticleListView.as_view()),
    # # path('detail/<int:pk>', article_detail),
    # path('detail/<int:id>',ArticleDetailView.as_view()),
    # path('generic/article/',GenericApiView.as_view()),
    # path('generic/detail/<int:id>/',GenericDetails.as_view()),
]