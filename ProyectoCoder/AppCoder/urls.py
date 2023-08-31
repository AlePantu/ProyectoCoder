
from django.urls import path
from .views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso, name='Agregar Curso'),
    path('lista-cursos/', lista_cursos, name='Lista Cursos'),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos ,name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes , name='Estudiantes'),
    path('entregables/', entregables , name='Entregables'),
    path('curso-formulario/' , curso_formulario , name='CursoFormulario'),
    path('busqueda-camada/' , busqueda_camada , name='BusquedaCamada'),
    path('buscar/' , buscar , name='Buscar'),
    path('lista-profesores/' , listaProfesores , name='ListaProfesores'),
    path('crea-profesor/' , crea_profesor , name='CreaProfesor'),
    path('elimina-profesor/<int:id>' , eliminarProfesor , name='EliminaProfesor'),
    path('editar-profesor/<int:id>' , editarProfesor , name='EditarProfesor')
]