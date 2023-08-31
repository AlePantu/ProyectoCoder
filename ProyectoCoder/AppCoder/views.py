from django.shortcuts import render
from .models import *
from django.http import HttpResponse , HttpRequest
from .forms import CursoFormulario , ProfesorFormulario


# Create your views here.

def curso(req, nombre , camada):

    curso = Curso(nombre = nombre , camada = camada)
    curso.save()
    
    return HttpResponse(f"""
                        <p> Curso: {curso.nombre} - Camada: {curso.camada} agregado!<p>
                        """)

def lista_cursos(req):
    lista = Curso.objects.all()

    return render(req,"lista_cursos.html" , {"lista_cursos": lista})

def inicio(req):
    return render(req , "inicio.html")
    

def cursos(req):
    return render(req , "cursos.html")

def profesores(req):
    return render(req , "profesores.html")

def estudiantes(req):
    return render(req , "estudiantes.html")

def entregables(req):
    return render(req , "entregables.html")


def curso_formulario(req : HttpRequest):

    print('method' , req.method)
    print('post' , req.POST)


    if req.method == 'POST':

        miFormulario = CursoFormulario(req.POST)
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            curso = Curso(nombre = data["curso"] , camada = data["camada"])
            curso.save()
            return render (req , "inicio.html" , {"mensaje":"Curso creado con exito" })
        else:
            return render (req , "inicio.html" , {"mensaje":"Formulario Invalido" })
    else:

        miFormulario = CursoFormulario()

        return render(req, "curso_formulario.html" , {"miFormulario" : miFormulario})
    


def busqueda_camada(req):

    return render(req, "busquedaCamada.html" )

def buscar(req):

    if req.GET["camada"]:
        camada = req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains =camada)
        if cursos:
            return render(req , "resultadoBusqueda.html" ,{"cursos":cursos})
    else:

         return HttpResponse(f'No escribiste ninguna camada')


def listaProfesores(req):

        profesores = Profesor.objects.all()

        return render(req , "leerProfesores.html" , {"profesores" : profesores})


def crea_profesor(req : HttpRequest):

    print('method' , req.method)
    print('post' , req.POST)


    if req.method == 'POST':

        miFormulario = ProfesorFormulario(req.POST)
        if miFormulario.is_valid():

            print(miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            profesor = Profesor(nombre = data["nombre"] ,apellido = data["apellido"], email = data["email"] , profesion = data["profesion"])
            profesor.save()
            return render (req , "inicio.html" , {"mensaje":"Profesor creado con exito" })
        else:
            return render (req , "inicio.html" , {"mensaje":"Formulario Invalido" })
    else:

        miFormulario = ProfesorFormulario()

        return render(req, "profesorFormulario.html" , {"miFormulario" : miFormulario})
    

def eliminarProfesor(req , id):

    if req.method == 'POST' :

      profesor =  Profesor.objects.get(id = id)

      profesor.delete()

      profesores = Profesor.objects.all()

    return render(req , "leerProfesores.html" , {"profesores" : profesores})


def editarProfesor(req , id):

    profesor =  Profesor.objects.get(id = id)

    if req.method == 'POST':

        miFormulario = ProfesorFormulario(req.POST)
        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.apellido = data["apellido"]
            profesor.email = data["email"]
            profesor.profesion = data["profesion"]
            profesor.save()
            return render (req , "inicio.html" , {"mensaje":"Profesor actualizado con exito" })
        else:
            return render (req , "inicio.html" , {"mensaje":"Formulario Invalido" })
    else:

        miFormulario = ProfesorFormulario(initial={
            "nombre" :profesor.nombre,
            "apellido":profesor.apellido,
            "email": profesor.email,
            "profesion": profesor.profesion

        })

        return render(req, "editarProfesor.html" , {"miFormulario" : miFormulario , "id":profesor.id})


