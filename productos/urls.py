from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>', views.detalle_producto, name='detalle_producto'),
    path('producto/nuevo', views.crear_producto, name='crear_producto'),
    path('producto/<int:pk>/editar/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]