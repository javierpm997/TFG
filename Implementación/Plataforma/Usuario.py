import Plataforma

def esUsuario (pIdUsuario, pPassword):
    # Dado un id de Usuario y un password, busca esa dupla en la BD.
    # Devuelve un código, tal como se detalla a continuación
    # #SALIDA
    # codigo = 99 Error en la conexion a la base de datos
    # codigo = 0 Usuario no existe. Error en el id o en la contrasena
    # codigo = 1 Usuario existe, credenciales correctas
    consulta = 'SELECT * from Usuario where idUsuario = ' + str(pIdUsuario) + ' and contraseña =\'' + str(pPassword)+ '\';'#TODO Consulta
    datos, codigo = Plataforma.conexionConPlataforma(consulta=consulta)#TODO Consulta

    if len(datos)==0:
        codigo = 0
        return codigo
    else:
        codigo = 1
        return codigo

