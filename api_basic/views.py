from django.conf import settings
from django.shortcuts import render
import os
from wsgiref.util import FileWrapper
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .customauth import CustomAuthenticate
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.
class ModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()


class FileDownloadListAPIView(generics.ListAPIView):
    #
    # def get(self, request):
    #     queryset = Article.objects.all()
    #     return Response(queryset)

    def get(self, request, id, format=None):
        queryset = Article.objects.get(id=id)
        file_handle = queryset.file.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/msword')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.file.name
        return response


    # def get(self, request, id, format=None):
    #     queryset = Article.objects.get(id=id)
    #     file_handle = os.path.join(settings.MEDIA_ROOT)
    #     document = open(file_handle, 'rb')
    #     response = HttpResponse(FileWrapper(document), content_type='application/msword')
    #     response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_handle)
    #     return response

# class GenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializers
#     queryset = Article.objects.all()
#
#
#
# class ApiViewSet(viewsets.ViewSet):
#     def list(self, request):
#         article = Article.objects.all()
#         serializer = ArticleSerializers(article, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ArticleSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializers(article)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializers(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
#
# class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     serializer_class = ArticleSerializers
#     queryset = Article.objects.all()
#     lookup_field = 'id'
#     authentication_classes = [TokenAuthentication]
#     # authentication_classes = [CustomAuthenticate]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#     # def put(self, request, id=None):
#     #     return self.update(request, id)
#     #
#     # def delete(self, request, id):
#     #     return self.destroy(request, id)
#
#
# class GenericDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializers
#     queryset = Article.objects.all()
#     lookup_field = 'id'
#     # authentication_classes = [CustomAuthenticate]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, id):
#         return self.retrieve(request, id)
#
#     def put(self, request, id):
#         return  self.update(request, id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
#
#
#
# class ArticleListView(APIView):
#     def get(self, request):
#         article = Article.objects.all()
#         serializer = ArticleSerializers(article, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ArticleSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class ArticleDetailView(APIView):
#
#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#
#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializers(article)
#         return Response(serializer.data)
#
#
#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializers(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
#
#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
#
#
# @api_view(['GET','POST'])
# def article_list(request):
#     if request.method == "GET":
#         article = Article.objects.all()
#         serializer = ArticleSerializers(article, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = ArticleSerializers(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializers(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ArticleSerializers(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)