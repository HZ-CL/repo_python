from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_books),
    path('add_book', views.add_book),
    path('view_book/<id_book>', views.book_info),
    path('view_book/asignar_autor/<id_book>', views.asignando_autor),
    path('view_authors', views.view_authors),
    path('add_author', views.add_author),
    path('author_info/<id_author>', views.author_info),
    path('author_info/asignar_libro/<id_author>', views.asignando_libro)

]