from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'category_page_size'
    max_page_size = 5

class SubCategoryPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'subcategory_page_size'
    max_page_size = 5

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'subcategory_page_size'
    max_page_size = 5