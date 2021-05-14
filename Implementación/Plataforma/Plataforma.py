from GestorSQL import GestorSQL

class Plataforma(object):

    def __init__(self):
        self.GESTOR = GestorSQL()
    def esUsuarioEspecialista(self, pIdUsuario, pContrasena):
        esUsuario = self.__esUsuarioCorrecto(pIdUsuario,pContrasena)
        if esUsuario==0:
            return 0
        esEspecialista = self.__esIdDeEspecialista(pIdUsuario)
        if esEspecialista==0:
            return 0

        if esUsuario == 1 and esEspecialista==1:
            return 1

        return -1

    def esUsuarioPaciente(self, pIdUsuario, pContrasena):
        esUsuario = self.__esUsuarioCorrecto(pIdUsuario,pContrasena)
        if esUsuario == 0:
            return 0
        esPaciente = self.__esIdDePaciente(pIdUsuario)
        if esPaciente == 0:
            return 0

        if esPaciente == 1 and esUsuario == 1:
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



    def __esIdDeEspecialista(self, pIdEspecialista):
        gestor = GestorSQL();
        resultadoSQL = self.GESTOR.execSQL(
            'SELECT * from Especialista where idEspecialista = ' + str(pIdEspecialista) + ';')
        if len(resultadoSQL) == 0:
            return 0;

        if len(resultadoSQL) == 1 :
            return 1

        return -1
    def __esIdDePaciente(self, pIdPaciente):
        gestor = GestorSQL();
        resultadoSQL = gestor.execSQL('SELECT * from Paciente where idPaciente= ' + str(pIdPaciente) + ';')
        if len(resultadoSQL) == 0:
            return 0;

        if len(resultadoSQL) == 1 :
            return 1

        return -1

    def __esUsuarioCorrecto(self, pIdUsuario, pContraseña):
        gestor = GestorSQL();
        resultadoSQL = gestor.execSQL(
            'SELECT * from Usuario where idUsuario = ' + str(pIdUsuario) + ' and contraseña =\'' + str(
                pContraseña) + '\';');
        if len(resultadoSQL) == 0:
            return 0;
        else :
            return 1;