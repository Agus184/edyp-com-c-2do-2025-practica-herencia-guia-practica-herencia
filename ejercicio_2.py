"""## Ejercicio 2: Análisis de Datos de Uso de la Tarjeta SUBE

Como parte de un proyecto de movilidad en el territorio argentino, el gobierno ha recolectado datos diarios del uso de la tarjeta SUBE para entender patrones de viaje y preferencias de transporte público. Tu tarea es procesar el archivo `"total-usuarios-por-dia.csv"` y extraer información clave. Debes implementar soluciones utilizando **Programación Orientada a Objetos (POO)** para estructurar el código (por ejemplo, clases para manejar datos y análisis) y **programación funcional** donde sea apropiado (como el uso de funciones `map`, `filter`, `reduce` para procesar listas de datos de manera eficiente y declarativa).

#### Requisitos Generales
- Lee el archivo CSV y procesa los datos en estructuras de datos adecuadas (por ejemplo, listas de diccionarios o objetos personalizados).
- Utiliza POO para crear clases como `AnalizadorSUBE` que encapsule métodos de análisis.
- Aplica principios funcionales para operaciones de agregación y filtrado, evitando bucles imperativos cuando sea posible.
- Maneja errores potenciales, como archivos inexistentes o datos inválidos.
- Muestra resultados de manera clara, utilizando prints o funciones de salida.

#### Tareas Específicas
1. **Análisis de Uso de Lancha**:
     - Implementa un método en tu clase que filtre datos por medio de transporte y calcule el máximo por mes.

2. **Análisis por Mes Ingresado**:
    - Solicita al usuario un mes (como número, ej. 1 para enero) y un año (como número, ej. 2020).
    - Determina el medio de transporte más utilizado en ese mes en ese año.
    - Usa map, filter y reduce para agrupar y comparar datos.

3. **Tendencias Mensuales**:
    - Analiza patrones estacionales en el uso del transporte público a lo largo de los meses.
    - Identifica posibles tendencias, como mayor uso en invierno (debido al clima) o verano.
    - Genera un resumen mensual con totales por medio de transporte, utilizando agregaciones funcionales.

4. **Promedio Mensual de Usuarios**:
    - Calcula el promedio de usuarios totales que utilizan la tarjeta SUBE cada mes.
    - Implementa un método que sume usuarios diarios y divida por el número de días en el mes.

5. **Orden Ascendente de Medios de Transporte**:
    - Muestra todos los medios de transporte ordenados de menor a mayor según su uso total en el año 2021.
    - Utiliza funciones de ordenamiento funcionales para procesar y mostrar la lista.

Recuerda documentar tu código con docstrings y comentarios. Asegúrate de que el programa sea modular y reutilizable, aplicando herencia si es necesario para extender funcionalidades."""


from collections import defaultdict
from functools import reduce
import csv


class sube_diccionario:
    def __init__(self, path_dict):
        self.path_dict = path_dict
        self.dict_data = self.get_dict(self.path_dict)

    def get_dict(self, path_dict):
        """
        Lee un archivo CSV y lo devuelve en formato dict:
        {
            "YYYY-MM-DD": {
                "total": int,
                "colectivo": int,
                "lancha": int,
                "subte": int,
                "tren": int
            }
        }
        """
        dict_data = {}
        try:
            with open(path_dict, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    key = row["indice_tiempo"]
                    dict_data[key] = {
                        "total": int(row["total"]),
                        "colectivo": int(row["colectivo"]),
                        "lancha": int(row["lancha"]),
                        "subte": int(row["subte"]),
                        "tren": int(row["tren"])
                    }
        except FileNotFoundError:
            print(f"Archivo no encontrado: {path_dict}")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return dict_data


class analizador_sube:
    def __init__(self, data):
        """
        Inicializa el analizador con los datos de uso de la SUBE.
        :param data: Diccionario con los datos procesados del archivo CSV.
        """
        self.data = data

    def analisis_uso_lancha_2020_mes(self):
        resumen = defaultdict(int)

        for fecha, fila in self.data.items():
            if fecha[:4] == "2020":
                mes = fecha[:7]  # "YYYY-MM"
                resumen[mes] += fila["lancha"]

        mes_max = max(resumen, key=resumen.get)
        cantidad_max = resumen[mes_max]

        return f"""El mes durante el año 2020 que más se utilizó "lancha" fue: {mes_max} con {cantidad_max} usos"""

    def analisis_uso_mes_ingresado(self, mes, anio):
        resumen = defaultdict(int)

        for fecha, fila in self.data.items():
            if fecha[:4] == str(anio) and fecha[5:7] == str(mes).zfill(2):
                resumen["lancha"] += fila["lancha"]
                resumen["colectivo"] += fila["colectivo"]
                resumen["subte"] += fila["subte"]
                resumen["tren"] += fila["tren"]

        transporte_max = max(resumen, key=resumen.get)
        cantidad_max = resumen[transporte_max]
        return f"""En {anio}-{str(mes).zfill(2)} el transporte más usado fue: {transporte_max} con {cantidad_max} usos"""

    def tendencias_mensuales(self):
        """
        Genera un resumen de totales por transporte y por mes.
        """
        resumen = defaultdict(lambda: defaultdict(int))

        for fecha, fila in self.data.items():
            mes = fecha[:7]  # YYYY-MM
            for transporte in ["lancha", "colectivo", "subte", "tren"]:
                resumen[mes][transporte] += fila[transporte]

        # Map → convertir dict en lista de strings con info
        resumen_lista = list(map(
            lambda kv: f"{kv[0]} → " + ", ".join([f"{t}: {c}" for t, c in kv[1].items()]),
            resumen.items()
        ))
        return "\n".join(resumen_lista)

    def promedio_usuarios_mensual(self):
        """
        Calcula el promedio mensual de usuarios totales.
        """
        resumen = defaultdict(list)

        # Agrupar totales por mes
        for fecha, fila in self.data.items():
            mes = fecha[:7]
            resumen[mes].append(fila["total"])

        # Reducir para sacar promedios
        promedios = {mes: reduce(lambda a, b: a + b, valores) / len(valores)
                     for mes, valores in resumen.items()}

        return "\n".join([f"{mes}: {round(prom, 2)} usuarios en promedio" for mes, prom in promedios.items()])

    def orden_ascendente_medios_de_transporte(self, anio=2021):
        """
        Muestra transportes ordenados de menor a mayor según uso total en un año.
        """
        resumen = defaultdict(int)

        for fecha, fila in self.data.items():
            if fecha[:4] == str(anio):
                for transporte in ["lancha", "colectivo", "subte", "tren"]:
                    resumen[transporte] += fila[transporte]

        # Orden ascendente con sorted
        ordenados = sorted(resumen.items(), key=lambda kv: kv[1])

        return "\n".join([f"{transporte}: {cantidad}" for transporte, cantidad in ordenados])


# Ejemplo de uso:
sube_dict = sube_diccionario("total-usuarios-por-dia.csv")
analizador = analizador_sube(sube_dict.dict_data)
print(analizador.tendencias_mensuales())
print(analizador.promedio_usuarios_mensual())
print(analizador.orden_ascendente_medios_de_transporte(2021))
print(analizador.analisis_uso_lancha_2020_mes())
print (analizador.analisis_uso_mes_ingresado(10, 2020))
