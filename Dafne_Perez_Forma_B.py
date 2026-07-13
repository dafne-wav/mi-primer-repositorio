#Funciones

def validar_codigo(codigo, peliculas):
    if not codigo or codigo.strip() == "":
        return False
    for c in peliculas.keys():
        if c.lower() == codigo.lower():
            return False
    return True

def validar_titulo(titulo):
    return titulo is not None and titulo.strip() != ""

def validar_genero(genero):
    return genero is not None and genero.strip() != ""

def validar_duracion(duracion_str):
    try:
        duracion = int(duracion_str)
        return duracion > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion in ['A', 'B', 'C']

def validar_idioma(idioma):
    return idioma is not None and idioma.strip() != ""

def validar_es_3d(es_3d_str):
    return es_3d_str.lower() in ['s', 'n']

def validar_precio(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_cupos(cupos_str):
    try:
        cupos = int(cupos_str)
        return cupos >= 0
    except ValueError:
        return False

def leer_opcion():
    while True:
        try:
            opcion_str = input("Ingrese opción: ")
            opcion = int(opcion_str)
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


def cupos_genero(genero, peliculas, cartelera):
    total_cupos = 0
    genero_buscado = genero.strip().lower()
    
    for codigo, datos in peliculas.items():
        if datos[1].lower() == genero_buscado:
            if codigo in cartelera:
                total_cupos += cartelera[codigo][1]
                
    print(f"El total de cupos disponibles es: {total_cupos}")


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    
    for codigo, datos_cartelera in cartelera.items():
        precio = datos_cartelera[0]
        cupos = datos_cartelera[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if codigo in peliculas:
                titulo = peliculas[codigo][0]
                resultados.append(f"{titulo}--{codigo}")
                
    if resultados:
        resultados.sort()
        print(f"Las peliculas encontradas son: {resultados}")
    else:
        print("No hay películas en ese rango de precios.")


def buscar_codigo(codigo, cartelera):
    for c in cartelera.keys():
        if c.lower() == codigo.lower():
            return True
    return False


def actualizar_precio(codigo, nuevo_precio, cartelera):
    if not buscar_codigo(codigo, cartelera):
        return False
        
    # Buscar la clave exacta original para actualizarla
    for c in cartelera.keys():
        if c.lower() == codigo.lower():
            cartelera[c][0] = nuevo_precio
            return True
    return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        return False

    es_3d_bool = True if es_3d.lower() == 's' else False
    
    peliculas[codigo] = [titulo, genero, int(duracion), clasificacion, idioma, es_3d_bool]

    cartelera[codigo] = [int(precio), int(cupos)]
    return True


def eliminar_pelicula(codigo, peliculas, cartelera):
    if not buscar_codigo(codigo, cartelera):
        return False
        
    clave_exacta = None
    for c in cartelera.keys():
        if c.lower() == codigo.lower():
            clave_exacta = c
            break
            
    if clave_exacta:
        del peliculas[clave_exacta]
        del cartelera[clave_exacta]
        return True
    return False

#Programa principal

cartelera = {
 'P101': [5990, 40],
 'P102': [7990, 0],
 'P103': [4990, 25],
 'P104': [6990, 12],
 'P105': [8990, 8],
 'P106': [7490, 3],
}
peliculas = {
 'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
 'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
 'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español',
False],
 'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
 'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
 'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles',
False],
}

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")

    opcion=leer_opcion()
    
    if opcion==1:
        print(cupos_genero(peliculas, cartelera))

    if opcion==2:
        busqueda_precio()

    if opcion==3:
        actualizar_precio()

    if opcion==4:
        if [validar_codigo, validar_titulo, validar_genero, validar_duracion, validar_clasificacion, validar_idioma, validar_es_3d, validar_precio, validar_cupos]:
            agregar_pelicula()

    if opcion==5:
        eliminar_pelicula
    
    if opcion==6:
        break





