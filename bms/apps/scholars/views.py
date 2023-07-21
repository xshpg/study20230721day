from rest_framework import viewsets
from rest_framework import permissions

from scholars.models import Scholars
from scholars.serializer import ScholarSerializer


class ScholarViewSet(viewsets.ModelViewSet):
    queryset = Scholars.objects.all()
    serializer_class = ScholarSerializer
    permissions = (permissions.IsAuthenticated,)
    ordering_fields = ['name','age']
    filter_fields = ['name','address']


