from django.shortcuts import render
from django.core.paginator import Paginator

from producto.models import Producto


def all_products(request):
    productos = Producto.objects.productosActivos().order_by('titulo')

    paginator = Paginator(productos,6)
    pagina = request.GET.get('page',1)
    productos_paginados = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,productos_paginados.paginator.num_pages + 1)

    context = {
        "productos": productos_paginados,
        'paginas': paginas,
        'pagina_actual':pagina_actual
    }
    return render(request, "productos/all_productos.html", context)