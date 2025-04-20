#importamos el conector de mysql
import mysql.connector  # Importar el conector de mysql

class Articulos:
    def abrir(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="poobd",
                port=3307  
            )
            return conexion
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def alta(self, datos):
        conexion = self.abrir()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    sql = "INSERT INTO articulos (cantidad, descripcion, precio) VALUES (%s, %s, %s)"
                    cursor.execute(sql, datos)
                    conexion.commit()
            except mysql.connector.Error as err:
                print(f"Error al insertar datos: {err}")
            finally:
                conexion.close()

    def consulta(self, datos):
        conexion = self.abrir()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    sql = "SELECT cantidad, descripcion, precio FROM articulos WHERE codigo=%s"
                    cursor.execute(sql, datos)
                    return cursor.fetchall()  # devuelve una lista de tuplas
            except mysql.connector.Error as err:
                print(f"Error al consultar datos: {err}")
                return []
            finally:
                conexion.close()

    def recuperar_todos(self):
        conexion = self.abrir()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    sql = "SELECT codigo, cantidad, descripcion, precio FROM articulos"
                    cursor.execute(sql)
                    return cursor.fetchall()
            except mysql.connector.Error as err:
                print(f"Error al recuperar datos: {err}")
                return []
            finally:
                conexion.close()
    
    def baja(self, codigo):
        conexion = self.abrir()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    sql = "DELETE FROM articulos WHERE codigo=%s"
                    cursor.execute(sql, (codigo,))
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print("Artículo eliminado correctamente.")
                    else:
                        print("No se encontró un artículo con ese código.")
            except mysql.connector.Error as err:
                print(f"Error al eliminar el artículo: {err}")
            finally:
                conexion.close()