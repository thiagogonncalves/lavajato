from django.shortcuts import render
from rest_framework import viewsets
from core.models import Cliente, Servico
from core.serializers import ClienteSerializer
from rest_framework.permissions import DjangoModelPermissions



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [DjangoModelPermissions]


class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ClienteSerializer
    # permission_classes = [DjangoModelPermissions]