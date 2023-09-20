from rest_framework.pagination import PageNumberPagination


class AllListsPaginator(PageNumberPagination):
    page_size = 5
