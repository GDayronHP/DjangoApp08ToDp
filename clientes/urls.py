from django.urls import path
from .views import ClienteList, ClienteDetail, Index

# router = routers.DefaultRouter()

# router.register('api/clientes', ClienteList, 'clienteList')

urlpatterns = [
    path('', Index, name='index'),
    path('clientes', ClienteList.as_view(), name = 'clienteList'),
    path('clientes/<int:pk>', ClienteDetail.as_view(), name = 'clienteDetail'),
]
