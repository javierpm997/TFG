from GestorSQL import GestorSQL

class Plataforma(object):

    def __init__(self):
        pass
    def esUsuarioEspecialista(self, pIdUsuario, pContrasena):
        gestor = GestorSQL();
        resultadoSQL= gestor.execSQL('SELECT * from Usuario where idUsuario = ' + str(pIdUsuario) + ' and contraseña =\'' + str(pContrasena)+ '\';');
        if len(resultadoSQL)==0:
            return 0;
        resultadoSQL2 = gestor.execSQL('SELECT * from Especialista where idEspecialista = ' + str(pIdUsuario)+ ';')
        if len(resultadoSQL2)==0:
            return 0;

        if len(resultadoSQL) == 1 and len(resultadoSQL2)==1:
            return 1

        return -1

    def esUsuarioPaciente(self, pIdUsuario, pContrasena):
        gestor = GestorSQL();
        resultadoSQL = gestor.execSQL(
            'SELECT * from Usuario where idUsuario = ' + str(pIdUsuario) + ' and contraseña =\'' + str(
                pContrasena) + '\';');
        if len(resultadoSQL) == 0:
            return 0;
        resultadoSQL2 = gestor.execSQL('SELECT * from Paciente where idPaciente= ' + str(pIdUsuario) + ';')
        if len(resultadoSQL2) == 0:
            return 0;

        if len(resultadoSQL) == 1 and len(resultadoSQL2) == 1:
            return 1

        return -1

    def anadirUsuarioEspecialista(self, pNombre, pApellidos, pEmail, pContrasena):
        gestor = GestorSQL();
        resultadoSQL = gestor.execSQL('INSERT into Usuario (nombre, apellido, email, contraseña) VALUES (\'' + str(pNombre) + '\' , \'' + str(pApellidos) + '\' , \'' + str(pEmail) + '\' , \'' + str(pContrasena) + '\');')

        resultadoSQL2 = gestor.execSQL('SELECT idUsuario from Usuario where email= \'' + str(pEmail) + '\';')

        resultadoSQL3 = gestor.execSQL(
            'INSERT into Especialista (idEspecialista) VALUES (' + str(resultadoSQL2[0][0]) +');')

    def anadirUsuarioPaciente(self, pNombre, pApellidos, pEmail, pContrasena, pEspecialista):
        gestor = GestorSQL();
        resultadoSQL = gestor.execSQL('INSERT into Usuario (nombre, apellido, email, contraseña) VALUES (\'' + str(pNombre) + '\' , \'' + str(pApellidos) + '\' , \'' + str(pEmail) + '\' , \'' + str(pContrasena) + '\');')

        resultadoSQL2 = gestor.execSQL('SELECT idUsuario from Usuario where email= \'' + str(pEmail) + '\';')

        resultadoSQL3 = gestor.execSQL(
            'INSERT into Paciente (idPaciente, especialista) VALUES (' + '\'' +str(resultadoSQL2[0][0]) + '\' , \'' + str(pEspecialista) +'\');')



