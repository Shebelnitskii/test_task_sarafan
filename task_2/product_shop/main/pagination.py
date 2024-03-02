from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 5
    max_page_size = 5

class CategoryPagination(BasePagination):
    page_size_query_param = 'category_page_size'

class SubCategoryPagination(BasePagination):
    page_size_query_param = 'subcategory_page_size'

class ProductPagination(BasePagination):
    page_size_query_param = 'product_page_size'