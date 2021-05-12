import Plataforma


def esPaciente (pId):
    # Dado un id de Paciente lo busca en la BD.
    # Devuelve un código, tal como se detalla a continuación
    # SALIDA
    # codigo = 0 No existe Paciente con este id
    # codigo = 1 Existe Paciente con este id
    # codigo = 98 Error desconocido en el programa
    # codigo = 99 Error en la conexión de la Base de Datos


    codigo = 0
    consulta = 'SELECT * from Paciente where idPaciente = ' + str(pId)+ ';'
    datos, codigo = Plataforma.conexionConPlataforma(consulta=consulta)

    if len(datos)==0:
        codigo = 0
        return codigo
    else:
        codigo = 1
        return codigo

    return 98