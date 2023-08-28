
from django.urls import path
from .views import curso, lista_cursos , inicio , cursos , estudiantes , profesores , entregables

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso, name='Agregar Curso'),
    path('lista-cursos/', lista_cursos, name='Lista Cursos'),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos ,name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes , name='Estudiantes'),
    path('entregables/', entregables , name='Entregables'),
]