from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from courses import serializers, paginators
from courses.models import Category, Course, Lesson, Tag


# Create your views here.


class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True).all()
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePanigator

    def get_queryset(self):
        queries = self.queryset
        if self.action.__eq__('list'):
            q = self.request.query_params.get("q")
            if q:
                queries = queries.filter(name__icontains=q)

            category_id = self.request.query_params.get("category")
            if category_id:
                queries = queries.filter(category=category_id)

        return queries
        #Laydsbai hoc co id la pk
        #Nếu trên đường dẫn không có {course_id} thì không cần lấy pk

    @action(methods=['get'], url_path='lessons', detail=True)
    def lessons(self, request, pk):
        lessons = self.get_object().lesson_set.filter(active=True)
        q = request.query_params.get('q')
        if q:
            lessons = lessons.filter(subject__icontains=q)
        serializer = serializers.LessonSerializer(lessons, many=True, context={'request': request})

        return Response(serializer.data)

class LessonViewSet(viewsets.ViewSet,generics.RetrieveAPIView):
    queryset = Lesson.objects.filter(active=True).all()
    serializer_class = serializers.LessonSerializer


