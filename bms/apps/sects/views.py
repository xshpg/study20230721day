from rest_framework import viewsets
from rest_framework import permissions

from sects.models import Sects
from sects.serializer import SectSerializer



class SectViewSet(viewsets.ModelViewSet):
    queryset = Sects.objects.all()
    serializer_class = SectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    ordering_fields = ['id','name']
    filter_fields = ['name','create_user']
