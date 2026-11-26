from django.urls import path



from .views import (
    ProdutoListView,
    CategoriasListarView,
    ClientesListarView,

)

app_name = "produtos"


urlpatterns = [
    path("", ProdutoListView.as_view(), name="lista"),
    path("categorias/", CategoriasListarView.as_view(), name="categorias"),
    path("clientes/", ClientesListarView.as_view(), name="clientes"),
    
]