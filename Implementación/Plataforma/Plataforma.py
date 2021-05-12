import mysql.connector
import Especialista
import Paciente
import Usuario

HOST= 'localhost'
USUARIO='root'
PASSWORD = "cardionline"
NOMBRE_DB= 'cardionline_pruebas'


def conexionConPlataforma ():
    # Devuelve una conexión con la plataforma
    #
    # SALIDA
    # conexion
    # codigo = 0  OK
    # codigo = 99 Error en la BD
    # codigo = 98 Error desconocido

    codigo = 0
    conexion = mysql.connector.connect(user=USUARIO, database=NOMBRE_DB, host=HOST, password=PASSWORD)
    return conexion, codigo

def conexionConPlataforma (consulta):
    # Dada una consulta, devuelve el resultado de una consulta SQL
    #
    # SALIDA
    # datos Resultado de una consulta SQL
    # codigo = 0  OK
    # codigo = 99 Error en la BD
    # codigo = 98 Error desconocido

    codigo = 0
    conexion = mysql.connector.connect(user=USUARIO, database=NOMBRE_DB, host=HOST, password=PASSWORD)
    datos, codigo = execSQL(consulta, conexion)
    return datos, codigo


def execSQL(consulta, conexion):
    # Dada una consulta, devuelve el resultado de una consulta SQL
    #
    # SALIDA
    # datos Resultado de una consulta SQL
    # codigo = 0  OK
    # codigo = 99 Error en la BD
    # codigo = 98 Error desconocido
    codigo = 0
    cursor = conexion.cursor()
    cursor.execute(consulta)

    if consulta.upper().startswith('SELECT'):
        datos = cursor.fetchall()
    else:
        conexion.commit()
        datos= None

    conexion.close()
    cursor.close()

    return datos, codigo

def identificacionUsuario(pIdUsuario, pPassword):
    # Dado un id de Usuario y un password, busca esa dupla en la BD.
    # Devuelve un código, tal como se detalla a continuación
    # SALIDA
    # codigo = -1 Identificación incorrecta, contrasena y/o id incorrectos
    # codigo = 0 Usuario correctamente identificado sin un tipo asignado. No debería existir
    # codigo = 1 Usuario correctamente identificado tipo Especialista
    # codigo = 2 Usuario correctamente identificado tipo Paciente
    # codigo = 3 Uduario correctamente identificado tipo Paciente y Especialista (¡NO DEBERÍA OCURRIR ESTO!)
    # codigo = 99 Error en la conexión con la Base de Datos
    # codigo = 98 Error desconocido en el programa

    codigo = -1
    esPaciente = -1
    esEspecialista = -1

    esUsuario = Usuario.esUsuario(pIdUsuario, pPassword)
    if esUsuario == 0:  # Usuario con esa contrasena no existe
        return -1

    esPaciente = Paciente.esPaciente(pIdUsuario)
    esEspecialista = Especialista.esEspecialista(pIdUsuario)
    if esPaciente == 0 and esEspecialista == 0:
        return 0
    if esPaciente == 1 and esEspecialista == 0:
        return 1
    if esPaciente == 0 and esEspecialista == 1:
        return 2
    if esPaciente == 1 and esEspecialista == 1:
        return 3

    return -98
