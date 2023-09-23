from rest_framework.pagination import PageNumberPagination

from config.config import MAX_PRODUCTS_PER_PAGE


class AllListsPaginator(PageNumberPagination):
    page_size = MAX_PRODUCTS_PER_PAGE
