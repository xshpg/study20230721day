from rest_framework import viewsets
from rest_framework.response import Response

from editors.models import Editors
from editors.serializer import EditorSerializer
from utils.common import get_create_time_format,get_detail_format


class EditorViewSet(viewsets.ModelViewSet):
    queryset = Editors.objects.all()
    serializer_class = EditorSerializer
    ordering_fields = ['name','gender']
    filter_fields = ['name','address']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas = serializer.data
            datas = get_create_time_format(datas=datas)
            return self.get_paginated_response(datas)
        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_create_time_format(datas=datas)
        return Response(datas)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        datas = serializer.data
        datas = get_detail_format(datas=datas)
        return Response(datas)