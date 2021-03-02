from django.http import request
from django.shortcuts import render, redirect, HttpResponse
from books_authors_app.models import *


# Create your views here.
def view_books(request):
    libreria = Libro.objects.all() #descargo la lista de libros en base de datos
    context = {
        'lista' : libreria # envio todos los libros
    }

    return render(request, 'add_book.html', context)

def add_book(request):
    dato_titulo_form = request.POST['titulo_libro']             #extraigo el dato del titulo
    dato_descripcion_form = request.POST['descripcion_libro']   #extraigo el dato de la discripcion
    Libro.objects.create(title = f'{dato_titulo_form}', desc = f'{dato_descripcion_form}') #creo el libro en la base de datos

    return redirect('/')

def book_info(request, id_book):

    abrir_libro = Libro.objects.get(id=id_book) #obtengo la informacion del libro
    autor_libro = abrir_libro.libros_autores.all() #obtengo los autores asociados al libro
    lista_autores = Autor.objects.all().exclude(libros=id_book)#recupero los autores y excluyo a los autores que ya estan asociados
    context = {
        'info_libro' : abrir_libro,             #envio info del libro
        'autor' : autor_libro,                  #envio info de los autores del libro
        'autores_despliege' : lista_autores     #envio los autores restantes
    }
    return render(request, 'view_book.html', context)

def asignando_autor(request, id_book):
    id_autor = request.POST['id_autor']         #obtengo el id del autor para asignar al libro
    autor_asig = Autor.objects.get(id=id_autor) #ORM para traer el autor
    id_libro = Libro.objects.get(id=id_book)    #ORM obtengo el libro
    autor_asig.libros.add(id_libro)             # ORM para asiganar autor-libro

    return redirect(f'/view_book/{id_book}')

def view_authors(request):
    lis_authors = Autor.objects.all() #descargo la lista de autores desde base de datos
    context = {
        'lista' : lis_authors
    }
    return render(request, 'add_author.html', context)

def add_author(request):
    dato_nombre_form = request.POST['nombre_autor']         #extraigo el dato nombre
    dato_apellido_form = request.POST['apellido_autor']     #extraigo el dato apellido
    dato_notas_form = request.POST['notas_autor']           #extraigo el dato de las notas
    Autor.objects.create(first_name = f'{dato_nombre_form}', last_name = f'{dato_apellido_form}', notas = f'{dato_notas_form}') #creo el libro en la base de datos
    return redirect('/view_authors')

def author_info(request, id_author):
    abrir_autor = Autor.objects.get(id=id_author) #obtengo la informacion del autor
    libros_autor = abrir_autor.libros.all() #obtengo los libros asociados al autor
    lista_libros = Libro.objects.all().exclude(libros_autores=id_author)#recupero los libros y excluyo los libros que ya estan asociados
    context = {
        'info_autor' : abrir_autor,             #envio info del autor
        'libros' : libros_autor,                  #envio info de los autores del libro
        'libros_despliege' : lista_libros     #envio los libros restantes
    }
    return render(request, 'view_author.html', context)

def asignando_libro(request, id_author):
    id_libro = request.POST['id_libro']             #capturo numero id libro
    libro_asig = Libro.objects.get(id=id_libro)     #obtengo el libro de db
    autor_lib = Autor.objects.get(id=id_author)     #obtengo el autor de db
    autor_lib.libros.add(libro_asig)                #ORM para asignar autor-libro
    return redirect(f'/author_info/{id_author}')