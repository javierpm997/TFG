-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: cardionline_pruebas
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Dispositivo`
--

DROP TABLE IF EXISTS `Dispositivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Dispositivo` (
  `idDispositivo` int NOT NULL AUTO_INCREMENT,
  `paciente` int NOT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idDispositivo`),
  KEY `idPaciente` (`paciente`),
  CONSTRAINT `Dispositivo_ibfk_1` FOREIGN KEY (`paciente`) REFERENCES `Paciente` (`idPaciente`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dispositivo`
--

LOCK TABLES `Dispositivo` WRITE;
/*!40000 ALTER TABLE `Dispositivo` DISABLE KEYS */;
INSERT INTO `Dispositivo` VALUES (2,3,'Biocare','IH-12PLUS'),(3,4,'Biocare','IH-12PLUS'),(4,6,'Biocare','IH-12PLUS'),(5,6,'ASPEL','ASPEKT 812'),(6,5,'ASPEL','ASPEKT 812'),(7,7,'ASPEL','ASPEKT 812');
/*!40000 ALTER TABLE `Dispositivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ECG`
--

DROP TABLE IF EXISTS `ECG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ECG` (
  `idECG` int NOT NULL AUTO_INCREMENT,
  `paciente` int NOT NULL,
  `dispositivo` int NOT NULL,
  `estado` int NOT NULL,
  `especialista` int NOT NULL,
  `fechaAnalisis` timestamp NULL DEFAULT NULL,
  `datos` longblob,
  `analisisAutomatico` text,
  `analisisEspecialista` text,
  `fechaSubida` timestamp NOT NULL,
  PRIMARY KEY (`idECG`),
  KEY `paciente` (`paciente`),
  KEY `especialista` (`especialista`),
  KEY `dispositivo` (`dispositivo`),
  KEY `estado` (`estado`),
  CONSTRAINT `ECG_ibfk_1` FOREIGN KEY (`paciente`) REFERENCES `Paciente` (`idPaciente`),
  CONSTRAINT `ECG_ibfk_2` FOREIGN KEY (`especialista`) REFERENCES `Especialista` (`idEspecialista`),
  CONSTRAINT `ECG_ibfk_3` FOREIGN KEY (`dispositivo`) REFERENCES `Dispositivo` (`idDispositivo`),
  CONSTRAINT `ECG_ibfk_4` FOREIGN KEY (`estado`) REFERENCES `Estado` (`idEstado`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ECG`
--

LOCK TABLES `ECG` WRITE;
/*!40000 ALTER TABLE `ECG` DISABLE KEYS */;
INSERT INTO `ECG` VALUES (3,3,2,1,1,NULL,NULL,NULL,NULL,'2021-05-05 00:13:21');
/*!40000 ALTER TABLE `ECG` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Especialista`
--

DROP TABLE IF EXISTS `Especialista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Especialista` (
  `idEspecialista` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`idEspecialista`),
  CONSTRAINT `Especialista_ibfk_1` FOREIGN KEY (`idEspecialista`) REFERENCES `Usuario` (`idUsuario`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Especialista`
--

LOCK TABLES `Especialista` WRITE;
/*!40000 ALTER TABLE `Especialista` DISABLE KEYS */;
INSERT INTO `Especialista` VALUES (1),(2);
/*!40000 ALTER TABLE `Especialista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Estado`
--

DROP TABLE IF EXISTS `Estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Estado` (
  `idEstado` int NOT NULL AUTO_INCREMENT,
  `estado` varchar(50) NOT NULL,
  `imagenSimbolo` longblob NOT NULL,
  `descripcion` text,
  PRIMARY KEY (`idEstado`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estado`
--

LOCK TABLES `Estado` WRITE;
/*!40000 ALTER TABLE `Estado` DISABLE KEYS */;
INSERT INTO `Estado` VALUES (1,'No Analizado',_binary '0','El ECG no est?? analizado'),(2,'OK',_binary '0','ECG esta OK'),(3,'Vigilar',_binary '0','Vigilar'),(4,'Acudir a consulta',_binary '0','Acudir a consulta');
/*!40000 ALTER TABLE `Estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mensaje`
--

DROP TABLE IF EXISTS `Mensaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Mensaje` (
  `idMensaje` int NOT NULL AUTO_INCREMENT,
  `remitente` int NOT NULL,
  `destinatario` int NOT NULL,
  `fecha` timestamp NOT NULL,
  `contenido` text NOT NULL,
  PRIMARY KEY (`idMensaje`),
  KEY `remitente` (`remitente`),
  KEY `destinatario` (`destinatario`),
  CONSTRAINT `Mensaje_ibfk_1` FOREIGN KEY (`remitente`) REFERENCES `Usuario` (`idUsuario`),
  CONSTRAINT `Mensaje_ibfk_2` FOREIGN KEY (`destinatario`) REFERENCES `Usuario` (`idUsuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mensaje`
--

LOCK TABLES `Mensaje` WRITE;
/*!40000 ALTER TABLE `Mensaje` DISABLE KEYS */;
INSERT INTO `Mensaje` VALUES (1,2,6,'2021-05-04 23:57:44','Hola! P??sate por mi consulta a las 7 ma??ana, por favor'),(2,6,2,'2021-05-04 23:58:13','Puede ser a las 7:30? Gracias!'),(3,2,6,'2021-05-04 23:58:31','Sin problema, nos vemos ma??ana!'),(4,2,7,'2021-05-04 23:59:15','Hola! P??sate por mi consulta a las 8 ma??ana, por favor'),(5,7,2,'2021-05-04 23:59:29','Ok!');
/*!40000 ALTER TABLE `Mensaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Paciente`
--

DROP TABLE IF EXISTS `Paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Paciente` (
  `idPaciente` int NOT NULL AUTO_INCREMENT,
  `especialista` int NOT NULL,
  PRIMARY KEY (`idPaciente`),
  KEY `especialista` (`especialista`),
  CONSTRAINT `Paciente_ibfk_1` FOREIGN KEY (`idPaciente`) REFERENCES `Usuario` (`idUsuario`) ON DELETE CASCADE,
  CONSTRAINT `Paciente_ibfk_2` FOREIGN KEY (`especialista`) REFERENCES `Especialista` (`idEspecialista`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paciente`
--

LOCK TABLES `Paciente` WRITE;
/*!40000 ALTER TABLE `Paciente` DISABLE KEYS */;
INSERT INTO `Paciente` VALUES (3,1),(4,1),(5,1),(6,2),(7,2);
/*!40000 ALTER TABLE `Paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TipoAnalisis`
--

DROP TABLE IF EXISTS `TipoAnalisis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TipoAnalisis` (
  `idAnalisis` int NOT NULL,
  `nombreAnalisis` varchar(50) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idAnalisis`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TipoAnalisis`
--

LOCK TABLES `TipoAnalisis` WRITE;
/*!40000 ALTER TABLE `TipoAnalisis` DISABLE KEYS */;
/*!40000 ALTER TABLE `TipoAnalisis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuario` (
  `idUsuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `contrase??a` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`idUsuario`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES (1,'Jaime','Trujillo Molto','key1','jaimetrujillo@gmail.com'),(2,'Jose Luis','Castillejo Prados','key1','joseluiscastillejoprados@gmail.com'),(3,'Santiago','Arjona Callejas','key1','santiagoarjonacallejas@gmail.com'),(4,'Jose Manuel','Melian Cantero','key1','josemanuelmeliancantero@gmail.com'),(5,'Sof??a','Maestro Vicent','key1','sofiamaestrovicent@gmail.com'),(6,'Pablo','Guardia Tejedor','key1','pabloguardiatejedor@gmail.com'),(7,'Claudia','De las Heras Segu??','key1','claudiadelasherassegui@gmail.com');
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13  2:27:02
