from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('ver_livro/<int:id>',views.ver_livros,name='ver_livros'),
    path('cadastrar_livro',views.cadastrar_livro,name='cadastrar_livro'),
    path('excluir_livro/<int:id>',views.excluir_livro, name='excluir_livro'),
    path('cadastrar_categoria',views.cadastrar_categoria,name='cadastrar_categoria'),
    path('cadastrar_emprestimo',views.cadastrar_emprestimo,name='cadastrar_emprestimo'),
    path('devover_livro',views.devover_livro, name='devover_livro'),
    path('alterar_livro',views.alterar_livro,name='alterar_livro'),
    path('meus_emprestimos',views.meus_emprestimos,name='meus_emprestimos'),
    path('processa_avaliacao',views.processa_avaliacao,name='processa_avaliacao')

]
