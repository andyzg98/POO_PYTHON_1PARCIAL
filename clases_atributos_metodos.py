class Arbol: #creo mi clase 
    #atributos
    #metodo constructor de la clase
    def __init__(self,altura,nombre,frutos,anillos):   
         #inicializar los atributos que posee 
       self.altura=altura
       self.nombre=nombre
       self.frutos=frutos
       self.anillos= anillos
    
    #funciones o metodos creadas
    def mostrar_caracteristicas(self):
        presentacion = ("mi nombre de arbol es : {}, mi altura es {} fruto : {} años arbolicos: {}") #Mensaje
        print(presentacion.format(self.nombre, self.altura, self.frutos,self.anillos)) #Usamos FORMAT
        
    def agregar_nombre(self):
        nombre=input("como se llama el arbol :")
        self.nombre=nombre
    def _altura(self):
        altura=input("altura del arbol: ")
        self.altura=altura
print("\n\n----ARBOLES----")
obj_arbol=Arbol(50,"pino","piñas",25) #inicializo paramentors
#obj_arbol.agregar_nombre()#modifico atributos de objeto
#obj_arbol._altura()
obj_arbol.mostrar_caracteristicas()

 #------------------------------------------------2---------------------------------
class Pelicula:
   def __init__(self,titulo,estreno,duracion,horafuncion):#constructor parametros inciales
      self.titulo=titulo
      self.estreno=estreno
      self.duracion=duracion
      self.horafuncion=horafuncion

      #funciones metodos propios
   def peli_caracteristicas(self):
        presentacion = ("titulo: {}, estreno:  {} duracion: {} horarios funcion : {}") #Mensaje
        print(presentacion.format(self.titulo,self.estreno, self.duracion, self.horafuncion)) #Usamos FORMAT

print("---------------peliculas--------------")      
obj_pelicula=Pelicula("harry Potter","no es estreno","2.20.10 horas","nocturna")
obj_pelicula.peli_caracteristicas()


#----------------------------------------------------------
class Cine:
    
    def __init__(self, nombre, direccion, salas, peliculas):
        self.nombre = nombre
        self.direccion = direccion
        self.salas = salas
        self.peliculas = peliculas
    
    def mostrar_peliculas(self):
        print(f"Películas en cartelera en {self.nombre}:")
        for pelicula in self.peliculas:
            print(f"- {pelicula}")
    
    def comprar_entrada(self, pelicula, sala, asiento):
        if pelicula in self.peliculas and sala in self.salas:
            print(f"Se compró una entrada para la película {pelicula} en la sala {sala}, asiento {asiento}")
        else:
            print("La película o la sala no están disponibles en este cine")
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_direccion(self):
        return self.direccion
    
    def __str__(self):
        return f"{self.nombre}, ubicado en {self.direccion}, tiene {self.salas} salas de cine"
obj_cine=Cine("supercines","quito",2,"harry potter")
obj_cine.__str__()

#-------------------------------------------------------
class Animal:
    
    def __init__(self, nombre, edad, especie, sonido):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.sonido = sonido
    
    def hacer_sonido(self):
        print(self.sonido)
    
    def obtener_edad(self):
        return self.edad
    
    def obtener_especie(self):
        return self.especie
    
    def obtener_nombre(self):
        return self.nombre
    
    def __str__(self):
        return f"{self.nombre} es un {self.especie} de {self.edad} años"



obj_animal=Animal("perro",1,"grandre","ladra")
obj_animal.__str__()
#--------------------------------------------------------------
class Coche:
    
    def __init__(self, marca, modelo, anio, color, velocidad_actual=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.velocidad_actual = velocidad_actual
    
    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        print(f"El coche {self.marca} {self.modelo} aceleró a {self.velocidad_actual} km/h")
    
    def frenar(self, decremento):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
        print(f"El coche {self.marca} {self.modelo} frenó a {self.velocidad_actual} km/h")
    
    def obtener_marca(self):
        return self.marca
    
    def obtener_modelo(self):
        return self.modelo
    
    def obtener_anio(self):
        return self.anio
    
    def obtener_color(self):
        return self.color
    
    def obtener_velocidad_actual(self):
        return self.velocidad_actual
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio}, {self.color})"

obj_coche=Coche("toyota","z1",2021,"azul")
obj_coche.__str__()

#---------------------------------

class DispositivoIOT:
    
    def __init__(self, id_dispositivo, tipo, ubicacion, estado):
        self.id_dispositivo = id_dispositivo
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.estado = estado
    
    def encender(self):
        self.estado = "encendido"
        print(f"El dispositivo {self.id_dispositivo} ha sido encendido.")
    
    def apagar(self):
        self.estado = "apagado"
        print(f"El dispositivo {self.id_dispositivo} ha sido apagado.")
    
    def cambiar_ubicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"El dispositivo {self.id_dispositivo} ha sido movido a {self.ubicacion}.")
    
    def obtener_id(self):
        return self.id_dispositivo
    
    def obtener_tipo(self):
        return self.tipo
    
    def obtener_ubicacion(self):
        return self.ubicacion
    
    def obtener_estado(self):
        return self.estado
    
    def __str__(self): #datos del dispositivo  en string 
        return f"{self.tipo} ({self.id_dispositivo}) en {self.ubicacion}: {self.estado}"

#-------------------------------------
class Robot:
    
    def __init__(self, nombre, modelo, bateria):
        self.nombre = nombre
        self.modelo = modelo
        self.bateria = bateria
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        print(f"{self.nombre} ha sido encendido.")
    
    def apagar(self):
        self.encendido = False
        print(f"{self.nombre} ha sido apagado.")
    
    def cargar_bateria(self, tiempo_carga):
        if not self.encendido:
            print(f"{self.nombre} está apagado. No se puede cargar la batería.")
            return
        self.bateria += tiempo_carga
        print(f"La batería de {self.nombre} se ha cargado por {tiempo_carga} horas.")
    
    def mover(self, direccion, distancia):
        if not self.encendido:
            print(f"{self.nombre} está apagado. No se puede mover.")
            return
        print(f"{self.nombre} se está moviendo {direccion} {distancia} metros.")
        self.bateria -= 0.1 * distancia
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_modelo(self):
        return self.modelo
    
    def obtener_bateria(self):
        return self.bateria
    
    def obtener_encendido(self):
        return self.encendido
    
    def __str__(self):
        return f"{self.nombre} ({self.modelo}) con {self.bateria} horas de batería."


#-----------------------------------------------

class RedSocial:
    
    def __init__(self, nombre, usuarios):
        self.nombre = nombre
        self.usuarios = usuarios
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def eliminar_usuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
    
    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.obtener_nombre() == nombre:
                return usuario
        return None
    
    def publicar(self, usuario, mensaje):
        if usuario in self.usuarios:
            mensaje_publicado = f"{usuario.obtener_nombre()} publicó: {mensaje}"
            for otro_usuario in self.usuarios:
                if otro_usuario != usuario:
                    otro_usuario.recibir_mensaje(mensaje_publicado)
    
    def __str__(self):
        return f"{self.nombre} tiene {len(self.usuarios)} usuarios."


#---------------------------
class Antena:
    
    def __init__(self, marca, modelo, frecuencia):
        self.marca = marca
        self.modelo = modelo
        self.frecuencia = frecuencia
        self.estado = "apagada"
    
    def encender(self):
        self.estado = "encendida"
        print("Antena encendida.")
    
    def apagar(self):
        self.estado = "apagada"
        print("Antena apagada.")
    
    def ajustar_frecuencia(self, frecuencia):
        self.frecuencia = frecuencia
        print(f"Antena ajustada a {frecuencia} Hz.")
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.frecuencia} Hz)"


#------------------------------

class Mascota:
    
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
    
    def hacer_sonido(self):
        pass
    
    def moverse(self):
        pass
    
    def alimentarse(self):
        pass
    
    def __str__(self):
        return f"{self.nombre} ({self.especie}), {self.edad} años"

#------------------------
class Libro:
    
    def __init__(self, titulo, autor, editorial, año_publicacion, paginas):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_publicacion = año_publicacion
        self.paginas = paginas
    
    def obtener_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Año de publicación: {self.año_publicacion}")
        print(f"Páginas: {self.paginas}")
    
    def leer_pagina(self, numero_pagina):
        pass
    
    def __str__(self):
        return f"{self.titulo}, de {self.autor}"

obj_libro=Libro("algebra","anderson","ecuador",2023,300)
obj_libro.obtener_informacion()