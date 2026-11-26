from django.shortcuts import render
from django.views.generic import ListView

from .models import Produto
from .models import Categoria
from .models import Cliente

# ==============================================================================
# VIEW 1: Exibição de Produtos em Formato de Cards / Catálogo
# ==============================================================================
class ProdutoListView(ListView):

    model = Produto   
    template_name = "produtos/lista_produtos.html"
    context_object_name = "produtos"
    queryset = Produto.objects.select_related("categoria")

class CategoriasListarView(ListView):
    
    model = Categoria   
    template_name = "produtos/lista_categorias.html"
    context_object_name = "categorias"
    #queryset = Produto.objects.select_related("categoria")

class ClientesListarView(ListView):
    model = Cliente   
    template_name = "produtos/lista_clientes.html"
    context_object_name = "clientes"
    #queryset = Produto.objects.select_related("categoria")
