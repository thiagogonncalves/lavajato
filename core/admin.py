from django.contrib import admin
from .models import Clientes
from .models import Servicos
from .models import OrdemServico

admin.site.register(Clientes)
admin.site.register(Servicos)
admin.site.register(OrdemServico)


