from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse , HttpRequest
from .forms import CursoFormulario

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