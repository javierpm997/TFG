import mysql.connector
class GestorSQL(object):


    def __init__(self):
        # ATRIBUTOS
        self.__HOST = 'localhost'
        self.__USUARIO = 'root'
        self.__PASSWORD = "cardionline"
        self.__NOMBRE_DB = 'cardionline_pruebas'
        self.__CONEXION = None
    # METODOS PARA CONEXIÓN CON PLATAFORMA
    def __conexionConPlataforma(self):
        # Devuelve una conexión con la plataforma
        conexion = mysql.connector.connect(user=self.__USUARIO, database=self.__NOMBRE_DB, host=self.__HOST,
                                             password=self.__PASSWORD, auth_plugin= 'mysql_native_password')
        return conexion

    def execSQL(self, pConsulta):
        # Dada una consulta, devuelve el resultado de una consulta SQL
        print(pConsulta)
        if self.__CONEXION == None:
            self.__CONEXION = self.__conexionConPlataforma()

        cursor = self.__CONEXION.cursor()

        cursor.execute(pConsulta)

        if pConsulta.upper().startswith('SELECT'):
            datos = cursor.fetchall()
        else:
            self.__CONEXION.commit()
            datos = None

        # self.__CONEXION.close()     ¿¿ESTO SERíA CORRECTO??
        self.__CONEXION.close()
        cursor.close()
        self.__CONEXION = None

        return datos
