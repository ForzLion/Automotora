from django.shortcuts import render, redirect
from .models import Automovil, Marca
#importamos la mensajeria de django
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def listado(request):
    #consultaremos a la base de datos para decirle que me entregue
    #todos los automoviles
    autos = Automovil.objects.all()
    #llamamos al template y junton con ello le pasamos
    #datos, en este caso el listado de autos que existe en la BBDD
    return render(request, 'core/listado_automoviles.html',{
        'autos':autos
    })


def formulario(request):
    marcas = Marca.objects.all()
    #declaramos el diccionario de variables que se enviaran al template
    variables = {
        'marcas':marcas
    }

    #preguntaremos si la peticion es POST
    if request.POST:
        #instanciar un Automovil
        auto = Automovil()
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = int(request.POST.get('txtAnio'))
        #instanciamos una Marca
        marca = Marca()
        marca.id = int(request.POST.get('cboMarca'))
        #dejamos el objeto marca dentro del auto
        auto.marca = marca
        #teniendo todos los datos capturados desde
        #el template, guardamos el automovil en la BBDD
        try:
            auto.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/formulario_automovil.html',variables)


def eliminar(request, id):

    #para eliminar es necesario primero buscar el automovil
    auto = Automovil.objects.get(id=id)

    #una vez encontrado el automovil se procede a eliminarlo
    try:
        auto.delete()
        mensaje = "Eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje ="No se ha podido eliminar"
        messages.error(request, mensaje)
        
    #el redirect lo redirige por alias de una ruta
    return redirect(to="listado")

def modificar_automovil(request, id):

    marcas = Marca.objects.all()
    #buscamos el automovil en la BBDD por su ID
    auto = Automovil.objects.get(id=id)
    variables = {
        'marcas':marcas,
        'auto':auto
    }

    if request.POST:
        #si la peticion es POST recibimos las variables
        auto = Automovil()
        auto.id = int(request.POST.get('txtId'))
        auto.patente = request.POST.get('txtPatente')
        auto.modelo = request.POST.get('txtModelo')
        auto.anio = int(request.POST.get('txtAnio'))
        #para recibir la marca creamos un objeto de tipo Marca
        marca = Marca()
        marca.id = int(request.POST.get('cboMarca'))
        #le pasamos la marca completa al automovil
        auto.marca = marca

        #ahora procederemos a actualizar el automovil
        try:
            auto.save()
            messages.success(request, "Actualizado correctamente")
        except:
            messages.error(request, "No se ha podido actualizar")

        #le haremos un redirect al usuario de vuelta hacia el listado   
        return redirect('listado')

    return render(request, 'core/modificar_automovil.html', variables)
