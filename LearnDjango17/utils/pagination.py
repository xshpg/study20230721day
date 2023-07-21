from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 's'
    max_page_size = 50
    page_size = 2




























