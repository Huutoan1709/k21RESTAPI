from rest_framework.pagination import PageNumberPagination

class CoursePanigator(PageNumberPagination):
    page_size = 2
