from .models import cursos

# Create your views here.
def crear_curso(request):

    nombre = input("ingrese un nombre de curso: ")
    comision = input("ingrese un numero de curso: ")
    curso = Curso(nombre=nombre, comision=comision)
    curso.save()
    texto = f"curso registrado con exito."
    
    return HttpResponse(texto)

def mostrarCursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "cursos.html", contexto)