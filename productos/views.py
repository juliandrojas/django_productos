from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', { 'productos' : productos })
def detalle_producto(request, pk):
    # PK = PRIMARY KEY (parámetro en URL)
    # Recibe el modelo y la PK
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle_producto.html', { 'producto' : producto })
def crear_producto(request):
    if request.method == 'POST':
        # Almacenamos la información que viene del método POST
        form = ProductoForm(request.POST)
        # Si la información del producto es válida
        if form.is_valid():
            # Guardamos el producto
            form.save()
            # Redireccionamos
            return redirect('lista_productos')
    else: 
        # Si no es método POST, mandamos el formulario vacío
        form = ProductoForm()
    return render(request, 'productos/form_producto.html', { 'form' : form })
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        # Si la información del producto es válida
        if form.is_valid():
            # Guardamos el producto
            form.save()
            # Redireccionamos
            return redirect('detalle_producto', pk=producto.pk)
    else: 
        # Si no es método POST, mandamos el formulario vacío
        form = ProductoForm(instance=producto)
    return render(request, 'productos/form_producto.html', { 'form' : form })
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/confirmar_eliminacion.html', { 'producto' : producto })