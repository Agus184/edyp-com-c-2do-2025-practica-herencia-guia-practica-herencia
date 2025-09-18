class biblioteca:
    def __init__(self,path_user,path_libros):
        self.path_user = path_user
        self.path_libros = path_libros

        self.libreria = self.get_libros()
        self.usuarios = self.get_users()
        
    def get_libros(self):
        return self.libreria

    def get_users(self):
        return self.usuarios

    def guardar_libros(self):
        return self.libreria


class libro:
    def __init__(self, ID, nombre, autor, anio_publicacion, genero, usuario=None, prestado=False):
        self.ID = ID
        self.nombre = nombre
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.genero = genero
        self.usuario = usuario
        self.prestado = prestado


class usuario:
    def __init__(self, ID, nombre, apellido, email, telefono, direccion, libros_prestados=None):
        self.ID = ID
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.libros_prestados = libros_prestados if libros_prestados else []


class analizador_biblioteca:
    def __init__(self, dict_user, dict_libros):
        self.dict_user = dict_user
        self.dict_libros = dict_libros
        self.libros_reserva = {}

    def identificar_lectores_de_honor(self):
        prestamos_usuario = {id: len(usuario.libros_prestados) for id, usuario in self.dict_user.items()}
        max_prestamos = max(prestamos_usuario.values())
        lista_honor = [usuario.nombre for id, usuario in self.dict_user.items() if len(usuario.libros_prestados) == max_prestamos]
        lista_users = "Los usuarios que llegaron al rango de lectores de honor son los siguientes:"
        for nombre in lista_honor:
            lista_users += f"\n\t-{nombre}"
        return lista_users

    def identificar_libros_sin_uso(self):
        libros_sin_uso = {id: libro for id, libro in self.dict_libros.items() if not libro.prestado}
        for id, libro in libros_sin_uso.items():
            print(f"Título: {libro.nombre}")
            rta = input("Deseas eliminar este libro de la librería (Si/No): ")
            if rta.lower() == "si":
                eliminado = self.dict_libros.pop(id)
                self.libros_reserva[id] = eliminado
        return self.libros_reserva

    def promedio_libros(self):
        total_libros = sum(len(user.libros_prestados) for user in self.dict_user.values())
        total_usuarios = len(self.dict_user)
        promedio = total_libros / total_usuarios if total_usuarios else 0
        return f"La cantidad promedio de libros prestados por usuario es {promedio:.2f}"

    def mas_antiguo(self):
        resultado = []
        for id_user, user in self.dict_user.items():
            if not user.libros_prestados:
                resultado.append(f"Usuario: {user.nombre}, Libro: N/A, Año: N/A")
            else:
                libro_anio = {id_libro: self.dict_libros[id_libro].anio_publicacion for id_libro in user.libros_prestados}
                id_mas_antiguo = min(libro_anio, key=libro_anio.get)
                libro_mas_antiguo = self.dict_libros[id_mas_antiguo]
                resultado.append(f"Usuario: {user.nombre}, Libro: {libro_mas_antiguo.nombre}, Año: {libro_mas_antiguo.anio_publicacion}")
        return "\n".join(resultado)

    def ranking_generos(self):
        genero_count = {}
        for libro in self.dict_libros.values():
            if libro.prestado:
                genero_count[libro.genero] = genero_count.get(libro.genero, 0) + 1
        generos_ordenados = sorted(genero_count.items(), key=lambda x: x[1], reverse=True)
        salida = "Ranking de géneros por popularidad:\n"
        for genero, cant in generos_ordenados:
            salida += f"{genero}: {cant} préstamos\n"

        top3 = generos_ordenados[:3]
        for genero, _ in top3:
            rta = input(f"Deseas agregar más ejemplares del género '{genero}'? (Si/No): ").lower()
            if rta == "si":
                for i in range(3):
                    nuevo_id = max(self.dict_libros.keys()) + 1
                    nombre_nuevo = input(f"Nombre del nuevo libro {i+1} del género '{genero}': ")
                    libro_nuevo = libro(nuevo_id, nombre_nuevo, "Autor Desconocido", 2025, genero)
                    self.dict_libros[nuevo_id] = libro_nuevo
                    salida += f"Se agregó el libro: {nombre_nuevo}\n"
        return salida


biblio = biblioteca("user.csv", "libros.csv")
analisis = analizador_biblioteca(biblio.usuarios, biblio.libreria)
