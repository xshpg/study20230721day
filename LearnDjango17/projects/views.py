from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework import filters

from projects.models import Projects
from projects.serializer import ProjectModelSerializer



class ProjectList(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  GenericAPIView):
    filter_fields = ['name','tester','leader']
    ordering_fields = ['tester','leader']
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ProjectDetails(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)







































