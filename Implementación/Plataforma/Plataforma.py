from GestorSQL import GestorSQL


class Plataforma(object):

    def __init__(self):
        self.GESTOR = GestorSQL()

    # USUARIO

    def esUsuarioEspecialista(self, pIdUsuario, pContrasena):
        # Dados un id de Usuario y una contraseña, detrmina si la dupla es correcta
        # (idUsuario y contraseña existen) y si es usuario Especialista
        #
        # CODIGOS DE DEVOLUCION:
        # -1: Error desconocido
        # 0: No es usuario correcto
        # 1: Usuario correcto pero no especialista
        # 2: Usuario correcto y especialista
        # 99: Error en la Base de Datos
        try:
            esUsuario = self.__esUsuarioCorrecto(pIdUsuario, pContrasena)
        except:
            return 99
        if esUsuario == 0:
            return 0

        try:
            esEspecialista = self.__esIdDeEspecialista(pIdUsuario)
        except:
            return 99
        if esEspecialista == 0:
            return 1

        if esUsuario == 1 and esEspecialista == 1:
            return 2

        return -1

    def esUsuarioPaciente(self, pIdUsuario, pContrasena):
        # Dados un id de Usuario y una contraseña, detrmina si la dupla es correcta
        # (idUsuario y contraseña existen) y si es usuario Especialista
        #
        # CODIGOS DE DEVOLUCION:
        # -1: Error desconocido
        # 0: No es usuario correcto
        # 1: Usuario correcto pero no paciente
        # 2: Usuario correcto y paciente
        # 99: Error en la Base de Datos
        try:
            esUsuario = self.__esUsuarioCorrecto(pIdUsuario, pContrasena)
        except:
            return 99
        if esUsuario == 0:
            return 0

        try:
            esPaciente = self.__esIdDePaciente(pIdUsuario)
        except:
            return 99
        if esPaciente == 0:
            return 1

        if esUsuario == 1 and esPaciente == 1:
            return 2

        return -1

    def __esUsuarioCorrecto(self, pIdUsuario, pContrasena):
        # Dado un ID y una contraseña devuelve si ese ID junto a esa contraseña son correctos
        # CODIGOS
        # 0: No es ID y contraseña correctos
        # 1: Es ID y contraseña correctos
        resultadoSQL = self.GESTOR.execSQL(
            'SELECT * from Usuario where idUsuario = ' + str(pIdUsuario) + ' and contrasena =\'' + str(
                pContrasena) + '\';');
        if len(resultadoSQL) == 0:
            return 0;
        else:
            return 1;

    def modificarUsuario(self, pIdUsuario, pNombre, pApellidos, pEmail, pContrasena):
        # modifica un nuevo usuario.
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que usuario existe
        nombreSQL = ''
        apellidosSQL = ''
        contrasenaSQL = ''
        emailSQL = ''

        if len(pNombre) != 0:
            nombreSQL = ', nombre = ' + '\'' + pNombre + '\''
        if len(pApellidos) != 0:
            apellidosSQL = ', apellidos = ' + '\'' + pApellidos + '\''
        if len(pContrasena) != 0:
            contrasenaSQL = ', contrasena = ' + '\'' + pContrasena + '\''
        if len(pEmail) != 0:
            emailSQL = ', email = ' + '\'' + pEmail + '\''
        try:
            resultadoSQL = self.GESTOR.execSQL('UPDATE Usuario SET idUsuario = \'' + str(
                pIdUsuario) + '\'' + nombreSQL + apellidosSQL + contrasenaSQL + emailSQL + ' WHERE idUsuario = \'' + str(
                pIdUsuario) + '\';')
        except:
            return 99

        return 0

    def cambiarContrasenaUsuario(self, pIdUsuario, pContrasena):
        # modifica contraseña de un usuario.
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que usuario existe
        nombreSQL = ''
        apellidosSQL = ''
        contrasenaSQL = ''
        emailSQL = ''

        try:
            resultadoSQL = self.GESTOR.execSQL(
                'UPDATE Usuario SET contrasena = \'' + pContrasena + '\' WHERE idUsuario = \'' + str(
                    pIdUsuario) + '\';')
        except:
            return 99

        return 0

    def eliminarUsuario(self, pIdUsuario):
        # Elimina un usuario. Ninguno de los valores dados puede ser nulo
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que ningun valor es nulo
        try:
            resultadoSQL = self.GESTOR.execSQL(
                'DELETE from Usuario WHERE idUsuario = ' + str(pIdUsuario) + ';')
        except:
            return 99
        return 0

    # ESPECIALISTA

    def __esIdDeEspecialista(self, pIdEspecialista):
        # Dado un ID devuelve si ese ID corresponde a un especialista
        # CODIGOS
        # 0: No es ID de especialista
        # 1: Es ID de especialista

        resultadoSQL = self.GESTOR.execSQL(
            'SELECT * from Especialista where idEspecialista = ' + str(pIdEspecialista) + ';')
        if len(resultadoSQL) == 0:
            return 0;

        if len(resultadoSQL) != 0:
            return 1

        return -1

    def anadirUsuarioEspecialista(self, pNombre, pApellidos, pEmail, pContrasena):
        # Añade un nuevo usuario Especialista. Ninguno de los valores dados puede ser nulo
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que ningun valor es nulo
        try:
            resultadoSQL = self.GESTOR.execSQL(
                'INSERT into Usuario (nombre, apellidos, email, contrasena) VALUES (\'' + str(
                    pNombre) + '\' , \'' + str(pApellidos) + '\' , \'' + str(pEmail) + '\' , \'' + str(
                    pContrasena) + '\');')

            resultadoSQL2 = self.GESTOR.execSQL('SELECT idUsuario from Usuario where email= \'' + str(pEmail) + '\';')

            resultadoSQL3 = self.GESTOR.execSQL(
                'INSERT into Especialista (idEspecialista) VALUES (' + str(resultadoSQL2[0][0]) + ');')
        except:
            return 99
        return 0


    def verUsuariosEspecialistas(self):
        # Devuelve una lista con todos los usuarios especialistas del sistema
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaUsuariosEspecialista = self.GESTOR.execSQL(
                'select * from Usuario inner join Especialista where Especialista.idEspecialista=Usuario.idUsuario;')
        except:
            return 99
        return listaUsuariosEspecialista


    # PACIENTE

    def __esIdDePaciente(self, pIdPaciente):
        # Dado un ID devuelve si ese ID corresponde a un paciente
        # CODIGOS
        # 0: No es ID de paciente
        # 1: Es ID de paciente
        resultadoSQL = self.GESTOR.execSQL('SELECT * from Paciente where idPaciente= ' + str(pIdPaciente) + ';')
        if len(resultadoSQL) == 0:
            return 0;

        if len(resultadoSQL) == 1:
            return 1

        return -1



    def cambiarEspecialistaDePaciente(self, pIdPaciente, pIdEspecialista):
        # Cambia el especialista asignado a un determinado paciente
        # CODIGOS
        #  0: OK
        # 99: Error en las llamadas a la BD
        try:
            resultadoSQL = self.GESTOR.execSQL('UPDATE Paciente SET especialista = \''+ str(pIdEspecialista) +'\' where idPaciente = \''+ str(pIdPaciente) + '\'')
        except:
            return 99
        return 0

    def verEspecialistaDePaciente(self, pIdPaciente):
        # Devuelve el ID del especialista del paciente
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            especialistaPaciente= self.GESTOR.execSQL(
                'SELECT especialista FROM Paciente WHERE idPaciente = \'' + str(pIdPaciente)+'\';')
        except:
            return 99
        return especialistaPaciente

    def verPacientesDeEspecialista(self, pIdEspecialista):
        # Devuelve la lista de pacientes del especialista
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaPacientes = self.GESTOR.execSQL(
                'SELECT Usuario.* FROM Paciente INNER JOIN Usuario WHERE especialista = \'' + str(pIdEspecialista) + '\' and idPaciente = idUsuario;')
        except:
            return 99
        return listaPacientes

    def verUsuariosPacientes(self):
        # Devuelve la lista de pacientes del especialista
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaPacientes = self.GESTOR.execSQL(
                'select * from Paciente inner join Usuario inner join Especialista inner join Usuario as usuarioEspecialista where Usuario.idUsuario=Paciente.idPaciente and Paciente.especialista = Especialista.idEspecialista and Especialista.idEspecialista = usuarioEspecialista.idUsuario;')
        except:
            return 99
        print(listaPacientes)
        return listaPacientes

    def verPaciente(self, pIdPaciente):
        # Devuelve la lista de pacientes del especialista
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaPacientes = self.GESTOR.execSQL(
                'SELECT * FROM Paciente INNER JOIN Usuario WHERE idPaciente = \'' + str(pIdPaciente) + '\' and idUsuario = idPaciente;')
        except:
            return 99
        return listaPacientes



    # TIPO ANALISIS

    def anadirTipoAnalisis(self, pNombreAnalisis, pDescripcion):
        # Dado un nombre y una descripción, guarda la definición de un tipo de análisis
        # CODIGOS
        #
        # 0: OK
        # 99: Error en la BD
        try:
            self.GESTOR.execSQL('INSERT INTO TipoAnalisis (nombreAnalisis, descripcion) VALUES (\'' + str(
                pNombreAnalisis) + '\' , \'' + str(pDescripcion) + '\');')
        except:
            return 99
        return 0

    def modificarTipoAnalisis(self, pIdTipoAnalisis, pNombreAnalisis, pDescripcion):
        # modifica un tipo de análisis
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que análisis existe
        nombreAnalisisSQL = ''
        descripcionSQL = ''

        if len(pNombreAnalisis) != 0:
            nombreAnalisisSQL = ', nombreAnalisis = ' + '\'' + pNombreAnalisis + '\''
        if len(pDescripcion) != 0:
            descripcionSQL = ', descripcion = ' + '\'' + pDescripcion + '\''

        try:
            resultadoSQL = self.GESTOR.execSQL('UPDATE TipoAnalisis SET idTipoAnalisis = \'' + str(
                pIdTipoAnalisis) + '\'' + nombreAnalisisSQL + descripcionSQL + ' WHERE idTipoAnalisis = \'' + str(
                pIdTipoAnalisis) + '\';')
        except:
            return 99

        return 0

    def eliminarTipoAnalisis(self, pIdTipoAnalisis):
        # elimina un tipo de análisis
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que análisis existe
        try:
            resultadoSQL = self.GESTOR.execSQL(
                'DELETE from TipoAnalisis WHERE idTipoAnalisis = ' + str(pIdTipoAnalisis) + ';')
        except:
            return 99

        return 0


    def verTiposAnalisis(self):
        # Devuelve la lista de pacientes del especialista
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaPacientes = self.GESTOR.execSQL(
                'SELECT * FROM TipoAnalisis;')
        except:
            return 99
        return listaPacientes
        pass

    # MENSAJES


    def verConversacion(self, pIdUsuario1, pIdUsuario2):
        # Dados dos IDs, devuelve los mensajes intercambiados entre ellos
        # CODIGOS
        # 99: Error en la BD

        try:
            listaMensajes = self.GESTOR.execSQL(
                'SELECT * from Mensaje where remitente = ' + str(pIdUsuario1) + ' or remitente = ' + str(
                    pIdUsuario2) + ' order by fecha;'
            )
        except:
            return 99
        return listaMensajes

    def enviarMensaje(self, pIdRemitente, pIdDestinatario, pContenido):
        #Dado un ID de un remitente y un id de un destinatario y el contenido del mensaje registra dicha informacion en la plataforma
        #CODIGOS
        #0: Correcto
        #99: Error en el registro del mensaje
        try:
            self.GESTOR.execSQL('INSERT INTO Mensaje (remitente, destinatario, fecha, contenido) VALUES (\'' + str(pIdRemitente) + '\', \'' + str(pIdDestinatario) + '\' , CURRENT_TIMESTAMP' + ', \'' + str(pContenido) + '\');' )
        except:
            return 99

        return 0

    def verConversacionesUsuario(self, pIdUsuario):
        #Dado un ID, devuelve el ID de los usuarios con los que mantiene conversaciones un usuario
        #CODIGOS
        #99: Error en la BD

        try:
            resultadoSQL = self.GESTOR.execSQL('select distinct remitente, destinatario from Mensaje where destinatario = '+ str(pIdUsuario) +' or remitente = '+str(pIdUsuario)+' ;')
        except:
            return 99
        listaConversaciones = []
        for i in range(len(resultadoSQL)):
            if resultadoSQL[i][0] != pIdUsuario and resultadoSQL[i][0] not in listaConversaciones:
                listaConversaciones.append(resultadoSQL[i][0])

            if resultadoSQL[i][1] != pIdUsuario and resultadoSQL[i][1] not in listaConversaciones:
                listaConversaciones.append(resultadoSQL[i][1])

        return listaConversaciones


    #ECG

    def verECGsPacienteFechaSubida(self, pIdPaciente):
        # Devuelve la lista de ECGs del paciente por fecha subida
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaECGs= self.GESTOR.execSQL(
                'SELECT * FROM ECG WHERE paciente = \'' + str(pIdPaciente) + '\' ORDER BY fechaSubida DESC;')
        except:
            return 99
        return listaECGs


    def verECGsPacientePorFechaAnalisisEspecialista(self, pIdPaciente):
        # Devuelve la lista de ECGs del paciente por fecha del analisis del especialista
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaECGs= self.GESTOR.execSQL(
                'SELECT * FROM ECG WHERE paciente = \'' + str(pIdPaciente) + '\' ORDER BY fechaAnalisis DESC;')
        except:
            return 99
        return listaECGs

    def verUltimoECGPaciente(self, pIdPaciente):
        # Devuelve el último ECG analizado por el especialista
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            ultimoECG= self.GESTOR.execSQL(
                'SELECT * FROM ECG WHERE paciente = \'' + str(pIdPaciente) + '\' ORDER BY fechaAnalisis DESC LIMIT 1;')
        except:
            return 99
        return ultimoECG


    def subirECG(self, idPaciente, idDispositivo, datos):
        # todo
        pass

    def analizar(self, pIdECG):
        # todo
        pass

    def verECG(self, pIdECG):
        # Devuelve un ECG
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            ECG= self.GESTOR.execSQL(
                'SELECT * FROM ECG WHERE idECG = \'' + str(pIdECG) + '\';')
        except:
            return 99
        return ECG


    def enviarEMail(self, pIdECG):
        # Devuelve un ECG
        # CODIGOS
        # 99: Error en las llamadas a la BD
        bd = self.__verEMailEspecialistaECG(pIdECG)
        if bd == 99:
            print("error 99")
            return 99
        print("Se envía eMail a" + bd)
        return 0


    def __verEMailEspecialistaECG(self, pIdECG):
        # Dado el id de un ECG, obtener eMail del Especialista asociado
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            email = self.GESTOR.execSQL(
                'SELECT email FROM ECG  INNER JOIN Usuario INNER Join Especialista WHERE ECG.idECG = \'' + str(pIdECG) + '\');')
            print('email: '+email)
        except:
            return 99
        return email



    #DISPOSITIVO


    def verDispositivosPaciente(self, pIdPaciente):
        # Devuelve la lista de dispositivos del paciente
        # CODIGOS
        # 99: Error en las llamadas a la BD
        try:
            listaDispositivos = self.GESTOR.execSQL(
                'SELECT * FROM Dispositivo WHERE paciente = \'' + str(pIdPaciente) + '\';')
        except:
            return 99
        return listaDispositivos



    def anadirDispositivo(self, pPaciente, pMarca, pModelo, pTipoAnalisis):
        # Dado un nombre y una descripción, guarda la definición de un tipo de análisis
        # CODIGOS
        #
        # 0: OK
        # 99: Error en la BD
        try:
            resultadoSQL = self.GESTOR.execSQL(
                'INSERT into Dispositivo (paciente, marca, modelo, tipoAnalisis) VALUES (\'' + str(
                    pPaciente) + '\' , \'' + str(pMarca) + '\' , \'' + str(pModelo) + '\' , \'' + str(
                    pTipoAnalisis) + '\');')
        except:
            return 99
        return 0

    def modificarDispositivo(self, pIdDispositivo, pPaciente, pMarca, pModelo, pTipoAnalisis):
        # modifica un dispositivo
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que usuario existe
        pacienteSQL = ''
        marcaSQL = ''
        modeloSQL = ''
        tipoAnalisisSQL = ''

        if len(str(pPaciente)) != 0:
            pacienteSQL = ', paciente = ' + '\'' + str(pPaciente) + '\''
        if len(str(pMarca)) != 0:
            marcaSQL = ', marca = ' + '\'' + str(pMarca) + '\''
        if len(pModelo) != 0:
            modeloSQL = ', modelo = ' + '\'' + str(pModelo) + '\''
        if len(pTipoAnalisis) != 0:
            tipoAnalisisSQL = ', tipoAnalisis = ' + '\'' + str(pTipoAnalisis) + '\''
        try:
            resultadoSQL = self.GESTOR.execSQL('UPDATE Dispositivo SET idDispositivo = \'' + str(
                pIdDispositivo) + '\'' + pacienteSQL + marcaSQL + modeloSQL + tipoAnalisisSQL + ' WHERE idDispositivo = \'' + str(
                pIdDispositivo) + '\';')
        except:
            return 99

        return 0

    def modificarTipoAnalisisDispositivo(self, pIdDispositivo, pIdTipoAnalisis):
        # Modifica el Análsis que se realiza a los ECG subidos por un Dispositivo
        # CODIGOS
        #
        # 0: OK
        # 99: Error en la BD
        try:
            resultadoSQL = self.GESTOR.execSQL(
                'UPDATE Dispositivo SET tipoAnalisis = (' + str(pIdTipoAnalisis) + ') WHERE idDispositivo = \'' + str(
                    pIdDispositivo) + '\' ;')
        except:
            return 99
        return 0

    def eliminarDispositivo(self, pIdDispositivo):
        # elimina un dispositivo
        # CODIGOS
        # 0: OK
        # 99: Error en las llamadas a la BD. Comprobar que análisis existe
        try:
            resultadoSQL = self.GESTOR.execSQL(
                'DELETE from Dispositivo WHERE idDispositivo = ' + str(pIdDispositivo) + ';')
        except:
            return 99

        return 0
