import random
#from itertools import chain
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from producto.models import Producto, Categoria


def buscar(request):
    query = request.GET.get('q')
    #if query is not None:
    productos = Producto.objects.buscar(query=query)
    categorias = Categoria.objects.categoriasActivas()
    context = {
        'query':query,
        'productos':productos,
        'categorias':categorias
    }
    return render(request, "productos/resultados.html", context)

def single(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    categoria_producto = producto.categoria.all().first()
    #productos_all_related = Producto.objects.filter(categoria=categoria_producto, active=True).exclude(id=producto.id)
    productos_all_related = Producto.objects.filtrar2(categoria_producto, producto.id)
    lista_productos_all_related = [x for x in list(productos_all_related)]
    """
    Esto es lo mismo que la lista comprimida de arriba
    lista_productos_all_related = []
    for item in productos_all_related:
        lista_productos_all_related.append(item)
    """
    random.shuffle(lista_productos_all_related)
    
    context={"producto":producto,
             "related_productos":lista_productos_all_related[0:6]}
    return render(request, "productos/single.html", context)


def all_products(request):
    #La primera vez que carga esta vista es NONE
    try:
        slug = request.GET.get('categoria')
    except:
        slug = None
    productos = Producto.objects.filtrar(slug=slug)   
    categorias = Categoria.objects.categoriasActivas()

    paginator = Paginator(productos,6)
    pagina = request.GET.get('page',1)
    productos_paginados = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1,productos_paginados.paginator.num_pages + 1)

    context = {
        "productos": productos_paginados,
        'paginas': paginas,
        'pagina_actual':pagina_actual,
        'categorias':categorias
    }
    return render(request, "productos/all_productos.html", context)