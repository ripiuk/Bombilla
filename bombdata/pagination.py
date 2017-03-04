from rest_framework.pagination import PageNumberPagination, Response
from django.shortcuts import render_to_response
class PageNumberPaginationDataOnly(PageNumberPagination):
    # Set any other options you want here like page_size

    def get_paginated_response(self, data):
        return Response(data)