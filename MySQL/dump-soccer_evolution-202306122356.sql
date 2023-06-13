-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: soccer_evolution
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `arriendo`
--

DROP TABLE IF EXISTS `arriendo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `arriendo` (
  `id_arriendo` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_arriendo` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '',
  `hora_arriendo` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '',
  `valor_arriendo` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '',
  `id__cliente` int(11) NOT NULL DEFAULT '0',
  `id_cancha` int(11) DEFAULT '0',
  PRIMARY KEY (`id_arriendo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arriendo`
--

LOCK TABLES `arriendo` WRITE;
/*!40000 ALTER TABLE `arriendo` DISABLE KEYS */;
/*!40000 ALTER TABLE `arriendo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arriendos_historial`
--

DROP TABLE IF EXISTS `arriendos_historial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `arriendos_historial` (
  `id_arriendos_historial` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` varchar(100) NOT NULL,
  `hora` varchar(100) NOT NULL,
  `valor` int(11) NOT NULL,
  `cancha` varchar(100) NOT NULL,
  `id_cliente` varchar(100) NOT NULL,
  PRIMARY KEY (`id_arriendos_historial`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arriendos_historial`
--

LOCK TABLES `arriendos_historial` WRITE;
/*!40000 ALTER TABLE `arriendos_historial` DISABLE KEYS */;
INSERT INTO `arriendos_historial` VALUES (51,'06/13/2023','10:00-11:00',40000,'Cancha Futbol','2'),(61,'16/06/2023','21:00-23:00',10000,'Cancha Basquetbol Gimnasio','1'),(62,'15/06/2023','19:00-20:00',10000,'Cancha Tenis Piso Arcilla','1'),(63,'0','0-0',3000,'Balón de fútbol','1'),(64,'22/06/2023','20:00-22:00',40000,'Cancha Futbol','1'),(65,'0','0-0',3000,'Balón de fútbol','1'),(66,'0','0-0',3000,'Balón de fútbol','1'),(67,'0','0-0',3000,'Balón de fútbol','1'),(68,'0','0-0',3000,'Balón de fútbol','1'),(69,'0','0-0',3000,'Balón de fútbol','1'),(70,'0','0-0',3000,'Balón de fútbol','1'),(71,'0','0-0',3000,'Balón de fútbol','1'),(72,'0','0-0',3000,'Balón de fútbol','1'),(73,'0','0-0',3000,'Balón de fútbol','1'),(74,'0','0-0',3000,'Balón de fútbol','1'),(75,'0','0-0',3000,'Balón de fútbol','1'),(76,'0','0-0',3000,'Balón de fútbol','1'),(77,'0','0-0',3000,'Balón de fútbol','1'),(78,'0','0-0',3000,'Balón de fútbol','1');
/*!40000 ALTER TABLE `arriendos_historial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bebida`
--

DROP TABLE IF EXISTS `bebida`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bebida` (
  `id_bebida` int(11) NOT NULL AUTO_INCREMENT,
  `sku_bebida` varchar(100) NOT NULL,
  `nombre_bebida` varchar(100) DEFAULT NULL,
  `imagen_bebida` varchar(100) DEFAULT NULL,
  `valor_bebida` int(11) DEFAULT NULL,
  `descripcion_bebida` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id_bebida`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bebida`
--

LOCK TABLES `bebida` WRITE;
/*!40000 ALTER TABLE `bebida` DISABLE KEYS */;
INSERT INTO `bebida` VALUES (1,'BEB001','Rehidratante azul','rehidratante_azul.png',1500,'Para recuperar electrolitos y tener un mejor rendimiento.'),(2,'BEB002','Rehidratante rojo','rehidratante_rojo.png',1500,'Para recuperar electrolitos y tener un mejor rendimiento.'),(3,'BEB001','Agua mineral','agua_chica.png',500,'Agua mineral 350cc.'),(4,'BEB004','Agua mineral','agua_grande.png',1000,'Agua mineral 500cc.'),(5,'BEB005','Jugo','jugo.png',2000,'Sabores: Piña, Durazno, Naranja'),(6,'BEB006','Bebida','bebida.png',2500,'Bebidas de fantasía');
/*!40000 ALTER TABLE `bebida` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `boleta`
--

DROP TABLE IF EXISTS `boleta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boleta` (
  `id_boleta` int(11) NOT NULL AUTO_INCREMENT,
  `numero_boleta` varchar(45) DEFAULT NULL,
  `valor_boleta` varchar(45) DEFAULT NULL,
  `fecha_boleta` varchar(45) DEFAULT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  `id_cancha` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_boleta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boleta`
--

LOCK TABLES `boleta` WRITE;
/*!40000 ALTER TABLE `boleta` DISABLE KEYS */;
/*!40000 ALTER TABLE `boleta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `caja`
--

DROP TABLE IF EXISTS `caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caja` (
  `id_caja` int(11) NOT NULL AUTO_INCREMENT,
  `id_trabajador` varchar(45) DEFAULT NULL,
  `monto_caja` varchar(45) DEFAULT NULL,
  `fecha_cierre_caja` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_caja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caja`
--

LOCK TABLES `caja` WRITE;
/*!40000 ALTER TABLE `caja` DISABLE KEYS */;
/*!40000 ALTER TABLE `caja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `camiseta`
--

DROP TABLE IF EXISTS `camiseta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `camiseta` (
  `id_camiseta` int(11) NOT NULL AUTO_INCREMENT,
  `sku_camiseta` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nombre_camiseta` varchar(70) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `imagen_camiseta` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `valor_camiseta` varchar(70) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `descripcion_camiseta` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id_camiseta`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camiseta`
--

LOCK TABLES `camiseta` WRITE;
/*!40000 ALTER TABLE `camiseta` DISABLE KEYS */;
INSERT INTO `camiseta` VALUES (4,'CAM001','Camisetas rojas','images/camiseta_roja.jpg','5000','12 camisetas de color rojo'),(5,'CAM002','Camisetas negras','images/camiseta_negra.jpg','5000','12 camisetas de color negro'),(6,'CAM003','Camisetas azules','images/camiseta_azul.jpg','5000','12 camisetas de color azul'),(7,'CAM004','Petos verdes','images/peto_amarillo.jpg','4000','12 petos de color verde'),(8,'CAM005','Petos blancos','images/peto_blanco.jpg','4000','12 petos de color blancos');
/*!40000 ALTER TABLE `camiseta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campeonato`
--

DROP TABLE IF EXISTS `campeonato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campeonato` (
  `id_campeonato` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_equipo` varchar(45) DEFAULT NULL,
  `valor_inscripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_campeonato`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campeonato`
--

LOCK TABLES `campeonato` WRITE;
/*!40000 ALTER TABLE `campeonato` DISABLE KEYS */;
/*!40000 ALTER TABLE `campeonato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancha`
--

DROP TABLE IF EXISTS `cancha`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancha` (
  `id_cancha` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cancha` varchar(45) DEFAULT NULL,
  `descripcion_cancha` varchar(45) DEFAULT NULL,
  `valor_cancha` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_cancha`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancha`
--

LOCK TABLES `cancha` WRITE;
/*!40000 ALTER TABLE `cancha` DISABLE KEYS */;
/*!40000 ALTER TABLE `cancha` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancha_basket`
--

DROP TABLE IF EXISTS `cancha_basket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancha_basket` (
  `id_cancha_basket` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cancha_basket` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `descripcion_cancha_basket` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `valor_cancha_basket` int(11) DEFAULT '0',
  `img_cancha_basket` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_cancha_basket`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancha_basket`
--

LOCK TABLES `cancha_basket` WRITE;
/*!40000 ALTER TABLE `cancha_basket` DISABLE KEYS */;
INSERT INTO `cancha_basket` VALUES (1,'Cancha Basquetbol Gimnasio','Cancha de basquetbol techada, con piso de parquet. Con una dimensión de 28 x 15 m. Nuestra cancha de Basketball tiene medidas profesionales para que tu experiencia sea de otro nivel.',10000,'images/cancha-basquetbal.jpg'),(2,'Cancha basquetbol Poliuretano','Cancha de basquetbol al aire libre con piso de poliuretano con capacidad de 5 jugadores por equipo.',8000,'images/cancha-basquetbal.jpg'),(3,'Cancha basquetbol Poliuretano 2','Cancha de basquetbol al aire libre con piso de poliuretano con capacidad de 5 jugadores por equipo.',8000,'images/cancha-basquetbal3.jpg');
/*!40000 ALTER TABLE `cancha_basket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancha_futbol`
--

DROP TABLE IF EXISTS `cancha_futbol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancha_futbol` (
  `id_cancha_futbol` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cancha_futbol` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `descripcion_cancha_futbol` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `valor_cancha_futbol` int(11) DEFAULT NULL,
  `img_cancha_futbol` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_cancha_futbol`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancha_futbol`
--

LOCK TABLES `cancha_futbol` WRITE;
/*!40000 ALTER TABLE `cancha_futbol` DISABLE KEYS */;
INSERT INTO `cancha_futbol` VALUES (1,'Cancha Futbol','Cancha de futbol de pasto natural con capacidad para 11 jugadores en cancha por equipo. Con una dimensión de 105 × 68 m, nuestra cancha de Football tiene medidas profesionales para que tu experiencia sea de otro nivel.',40000,'images/cancha-futbol.jpg'),(2,'Cancha Futbolito','Cancha de pasto sintetico con capacidad para 9 jugadores en cancha por equipo.',30000,'images/cancha-futbolito.jpg'),(3,'Fútbolito 2','Cancha de futbolito de pasto sintetico con capacidad (recomendada) para 7 jugadores en cancha por equipo.',25000,'images/cancha-futbolito2.jpg'),(4,'Fútbolito 3','Cancha de futbolito de pasto sintetico con capacidad (recomendada) para 7 jugadores en cancha por equipo.',25000,'images/cancha-futbolito3.jpg'),(5,'Cancha BabyFutbol Gimnasio','Cancha de baby futbol de hormigon pulido en gimnasio, espacio apto para campeonatos. Capacidad de la cancha para 5 jugadores en cancha por equipo.',7000,'images/cancha-babyfutbol.jpg'),(6,'Cancha BabyFutbol Pasto sintetico','Cancha de baby futbol de pasto sintetico y con capacidad para 5 jugadores en cancha por equipo. Canha ubicada al aire libre, lugar apto para campeonatos.',7000,'images/cancha-babyfutbol2.jpg');
/*!40000 ALTER TABLE `cancha_futbol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cancha_tenis`
--

DROP TABLE IF EXISTS `cancha_tenis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cancha_tenis` (
  `id_cancha_tenis` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cancha_tenis` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `descripcion_cancha_tenis` varchar(400) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `valor_cancha_tenis` int(11) DEFAULT NULL,
  `img_cancha_tenis` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_cancha_tenis`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cancha_tenis`
--

LOCK TABLES `cancha_tenis` WRITE;
/*!40000 ALTER TABLE `cancha_tenis` DISABLE KEYS */;
INSERT INTO `cancha_tenis` VALUES (1,'Cancha Tenis Piso Arcilla','Cancha de Tenis piso de arcilla. Con una dimensión de 23x8. Sin dudas nuestras canchas de Tenis tu experiencia de juego será de otro nivel.',10000,'images/arcilla-2.jpg'),(2,'Cancha Tenis Rápida','Cancha de tenis con piso GreenSet, la que permite una experiencia distinta, permitiendo que los botes sean mas cortos. Con una dimensión de 23.77x8.23. Nuestras canchas de Tenis tienen medidas profesionales para que tu experiencia sea de otro nivel.',10000,'images/tenis-pduro2.jpg'),(3,'Cancha Padel Gimnasio','Cancha Padel de blindex ya que cuenta con paletas modernas que facilitan el juego.Con una dimensión de 10x20 en sala apta para campeonatos.',10000,'images/padel-pista.jpg'),(4,'Cancha Padel Pasto','Cancha de padel al aire libre de pasto con una dimensión de 10x20 para que puedas jugar singles o dobles sin mayores contratiempos.',15000,'images/padel-pasto1.jpg');
/*!40000 ALTER TABLE `cancha_tenis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carro_compras`
--

DROP TABLE IF EXISTS `carro_compras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carro_compras` (
  `id_carro` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_producto` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `fecha` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `hora_inicio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `hora_fin` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `valor_producto` int(11) NOT NULL DEFAULT '0',
  `id_producto` int(11) NOT NULL DEFAULT '0',
  `id_cliente` int(11) DEFAULT '0',
  PRIMARY KEY (`id_carro`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carro_compras`
--

LOCK TABLES `carro_compras` WRITE;
/*!40000 ALTER TABLE `carro_compras` DISABLE KEYS */;
INSERT INTO `carro_compras` VALUES (109,'Cancha Futbol','06/10/2023','10:00','11:00',40000,1,2),(113,'Balón de fútbol','0','0','0',3000,1,2),(165,'Cancha Futbol','06/13/2023','10:00','11:00',40000,1,2),(192,'Balón de fútbol','0','0','0',3000,1,1);
/*!40000 ALTER TABLE `carro_compras` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`%`*/ /*!50003 TRIGGER `insertar_arriendo_historial` AFTER INSERT ON `carro_compras` FOR EACH ROW BEGIN
                INSERT INTO arriendos_historial (fecha, hora, valor, cancha, id_cliente)
                VALUES (NEW.fecha, CONCAT(NEW.hora_inicio, '-', NEW.hora_fin), NEW.valor_producto, NEW.nombre_producto, NEW.id_cliente);
            END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id__cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_cliente` varchar(45) DEFAULT NULL,
  `apellido_cliente` varchar(45) DEFAULT NULL,
  `direccion_cliente` varchar(45) DEFAULT NULL,
  `telefono_cliente` varchar(45) DEFAULT NULL,
  `correo_cliente` varchar(45) DEFAULT NULL,
  `comuna_cliente` varchar(45) DEFAULT NULL,
  `provincia_cliente` varchar(45) DEFAULT NULL,
  `region_cliente` varchar(45) DEFAULT NULL,
  `numero_compras` int(11) DEFAULT NULL,
  `comunas_id` int(11) NOT NULL,
  `campeonato_id_campeonato` int(11) NOT NULL,
  `promociones_id_promocion` int(11) NOT NULL,
  PRIMARY KEY (`id__cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comunas`
--

DROP TABLE IF EXISTS `comunas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comunas` (
  `id_comuna` int(11) NOT NULL AUTO_INCREMENT,
  `comuna` varchar(64) NOT NULL,
  `id_provincia` int(11) NOT NULL,
  PRIMARY KEY (`id_comuna`)
) ENGINE=InnoDB AUTO_INCREMENT=347 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comunas`
--

LOCK TABLES `comunas` WRITE;
/*!40000 ALTER TABLE `comunas` DISABLE KEYS */;
INSERT INTO `comunas` VALUES (1,'Arica',1),(2,'Camarones',1),(3,'General Lagos',2),(4,'Putre',2),(5,'Alto Hospicio',3),(6,'Iquique',3),(7,'Camiña',4),(8,'Colchane',4),(9,'Huara',4),(10,'Pica',4),(11,'Pozo Almonte',4),(12,'Tocopilla',5),(13,'María Elena',5),(14,'Calama',6),(15,'Ollague',6),(16,'San Pedro de Atacama',6),(17,'Antofagasta',7),(18,'Mejillones',7),(19,'Sierra Gorda',7),(20,'Taltal',7),(21,'Chañaral',8),(22,'Diego de Almagro',8),(23,'Copiapó',9),(24,'Caldera',9),(25,'Tierra Amarilla',9),(26,'Vallenar',10),(27,'Alto del Carmen',10),(28,'Freirina',10),(29,'Huasco',10),(30,'La Serena',11),(31,'Coquimbo',11),(32,'Andacollo',11),(33,'La Higuera',11),(34,'Paihuano',11),(35,'Vicuña',11),(36,'Ovalle',12),(37,'Combarbalá',12),(38,'Monte Patria',12),(39,'Punitaqui',12),(40,'Río Hurtado',12),(41,'Illapel',13),(42,'Canela',13),(43,'Los Vilos',13),(44,'Salamanca',13),(45,'La Ligua',14),(46,'Cabildo',14),(47,'Zapallar',14),(48,'Papudo',14),(49,'Petorca',14),(50,'Los Andes',15),(51,'San Esteban',15),(52,'Calle Larga',15),(53,'Rinconada',15),(54,'San Felipe',16),(55,'Llaillay',16),(56,'Putaendo',16),(57,'Santa María',16),(58,'Catemu',16),(59,'Panquehue',16),(60,'Quillota',17),(61,'La Cruz',17),(62,'La Calera',17),(63,'Nogales',17),(64,'Hijuelas',17),(65,'Valparaíso',18),(66,'Viña del Mar',18),(67,'Concón',18),(68,'Quintero',18),(69,'Puchuncaví',18),(70,'Casablanca',18),(71,'Juan Fernández',18),(72,'San Antonio',19),(73,'Cartagena',19),(74,'El Tabo',19),(75,'El Quisco',19),(76,'Algarrobo',19),(77,'Santo Domingo',19),(78,'Isla de Pascua',20),(79,'Quilpué',21),(80,'Limache',21),(81,'Olmué',21),(82,'Villa Alemana',21),(83,'Colina',22),(84,'Lampa',22),(85,'Tiltil',22),(86,'Santiago',23),(87,'Vitacura',23),(88,'San Ramón',23),(89,'San Miguel',23),(90,'San Joaquín',23),(91,'Renca',23),(92,'Recoleta',23),(93,'Quinta Normal',23),(94,'Quilicura',23),(95,'Pudahuel',23),(96,'Providencia',23),(97,'Peñalolén',23),(98,'Pedro Aguirre Cerda',23),(99,'Ñuñoa',23),(100,'Maipú',23),(101,'Macul',23),(102,'Lo Prado',23),(103,'Lo Espejo',23),(104,'Lo Barnechea',23),(105,'Las Condes',23),(106,'La Reina',23),(107,'La Pintana',23),(108,'La Granja',23),(109,'La Florida',23),(110,'La Cisterna',23),(111,'Independencia',23),(112,'Huechuraba',23),(113,'Estación Central',23),(114,'El Bosque',23),(115,'Conchalí',23),(116,'Cerro Navia',23),(117,'Cerrillos',23),(118,'Puente Alto',24),(119,'San José de Maipo',24),(120,'Pirque',24),(121,'San Bernardo',25),(122,'Buin',25),(123,'Paine',25),(124,'Calera de Tango',25),(125,'Melipilla',26),(126,'Alhué',26),(127,'Curacaví',26),(128,'María Pinto',26),(129,'San Pedro',26),(130,'Isla de Maipo',27),(131,'El Monte',27),(132,'Padre Hurtado',27),(133,'Peñaflor',27),(134,'Talagante',27),(135,'Codegua',28),(136,'Coínco',28),(137,'Coltauco',28),(138,'Doñihue',28),(139,'Graneros',28),(140,'Las Cabras',28),(141,'Machalí',28),(142,'Malloa',28),(143,'Mostazal',28),(144,'Olivar',28),(145,'Peumo',28),(146,'Pichidegua',28),(147,'Quinta de Tilcoco',28),(148,'Rancagua',28),(149,'Rengo',28),(150,'Requínoa',28),(151,'San Vicente de Tagua Tagua',28),(152,'Chépica',29),(153,'Chimbarongo',29),(154,'Lolol',29),(155,'Nancagua',29),(156,'Palmilla',29),(157,'Peralillo',29),(158,'Placilla',29),(159,'Pumanque',29),(160,'San Fernando',29),(161,'Santa Cruz',29),(162,'La Estrella',30),(163,'Litueche',30),(164,'Marchigüe',30),(165,'Navidad',30),(166,'Paredones',30),(167,'Pichilemu',30),(168,'Curicó',31),(169,'Hualañé',31),(170,'Licantén',31),(171,'Molina',31),(172,'Rauco',31),(173,'Romeral',31),(174,'Sagrada Familia',31),(175,'Teno',31),(176,'Vichuquén',31),(177,'Talca',32),(178,'San Clemente',32),(179,'Pelarco',32),(180,'Pencahue',32),(181,'Maule',32),(182,'San Rafael',32),(183,'Curepto',33),(184,'Constitución',32),(185,'Empedrado',32),(186,'Río Claro',32),(187,'Linares',33),(188,'San Javier',33),(189,'Parral',33),(190,'Villa Alegre',33),(191,'Longaví',33),(192,'Colbún',33),(193,'Retiro',33),(194,'Yerbas Buenas',33),(195,'Cauquenes',34),(196,'Chanco',34),(197,'Pelluhue',34),(198,'Bulnes',35),(199,'Chillán',35),(200,'Chillán Viejo',35),(201,'El Carmen',35),(202,'Pemuco',35),(203,'Pinto',35),(204,'Quillón',35),(205,'San Ignacio',35),(206,'Yungay',35),(207,'Cobquecura',36),(208,'Coelemu',36),(209,'Ninhue',36),(210,'Portezuelo',36),(211,'Quirihue',36),(212,'Ránquil',36),(213,'Treguaco',36),(214,'San Carlos',37),(215,'Coihueco',37),(216,'San Nicolás',37),(217,'Ñiquén',37),(218,'San Fabián',37),(219,'Alto Biobío',38),(220,'Antuco',38),(221,'Cabrero',38),(222,'Laja',38),(223,'Los Ángeles',38),(224,'Mulchén',38),(225,'Nacimiento',38),(226,'Negrete',38),(227,'Quilaco',38),(228,'Quilleco',38),(229,'San Rosendo',38),(230,'Santa Bárbara',38),(231,'Tucapel',38),(232,'Yumbel',38),(233,'Concepción',39),(234,'Coronel',39),(235,'Chiguayante',39),(236,'Florida',39),(237,'Hualpén',39),(238,'Hualqui',39),(239,'Lota',39),(240,'Penco',39),(241,'San Pedro de La Paz',39),(242,'Santa Juana',39),(243,'Talcahuano',39),(244,'Tomé',39),(245,'Arauco',40),(246,'Cañete',40),(247,'Contulmo',40),(248,'Curanilahue',40),(249,'Lebu',40),(250,'Los Álamos',40),(251,'Tirúa',40),(252,'Angol',41),(253,'Collipulli',41),(254,'Curacautín',41),(255,'Ercilla',41),(256,'Lonquimay',41),(257,'Los Sauces',41),(258,'Lumaco',41),(259,'Purén',41),(260,'Renaico',41),(261,'Traiguén',41),(262,'Victoria',41),(263,'Temuco',42),(264,'Carahue',42),(265,'Cholchol',42),(266,'Cunco',42),(267,'Curarrehue',42),(268,'Freire',42),(269,'Galvarino',42),(270,'Gorbea',42),(271,'Lautaro',42),(272,'Loncoche',42),(273,'Melipeuco',42),(274,'Nueva Imperial',42),(275,'Padre Las Casas',42),(276,'Perquenco',42),(277,'Pitrufquén',42),(278,'Pucón',42),(279,'Saavedra',42),(280,'Teodoro Schmidt',42),(281,'Toltén',42),(282,'Vilcún',42),(283,'Villarrica',42),(284,'Valdivia',43),(285,'Corral',43),(286,'Lanco',43),(287,'Los Lagos',43),(288,'Máfil',43),(289,'Mariquina',43),(290,'Paillaco',43),(291,'Panguipulli',43),(292,'La Unión',44),(293,'Futrono',44),(294,'Lago Ranco',44),(295,'Río Bueno',44),(296,'Osorno',45),(297,'Puerto Octay',45),(298,'Purranque',45),(299,'Puyehue',45),(300,'Río Negro',45),(301,'San Juan de la Costa',45),(302,'San Pablo',45),(303,'Calbuco',46),(304,'Cochamó',46),(305,'Fresia',46),(306,'Frutillar',46),(307,'Llanquihue',46),(308,'Los Muermos',46),(309,'Maullín',46),(310,'Puerto Montt',46),(311,'Puerto Varas',46),(312,'Ancud',47),(313,'Castro',47),(314,'Chonchi',47),(315,'Curaco de Vélez',47),(316,'Dalcahue',47),(317,'Puqueldón',47),(318,'Queilén',47),(319,'Quellón',47),(320,'Quemchi',47),(321,'Quinchao',47),(322,'Chaitén',48),(323,'Futaleufú',48),(324,'Hualaihué',48),(325,'Palena',48),(326,'Lago Verde',49),(327,'Coihaique',49),(328,'Aysén',50),(329,'Cisnes',50),(330,'Guaitecas',50),(331,'Río Ibáñez',51),(332,'Chile Chico',51),(333,'Cochrane',52),(334,'OHiggins',52),(335,'Tortel',52),(336,'Natales',53),(337,'Torres del Paine',53),(338,'Laguna Blanca',54),(339,'Punta Arenas',54),(340,'Río Verde',54),(341,'San Gregorio',54),(342,'Porvenir',55),(343,'Primavera',55),(344,'Timaukel',55),(345,'Cabo de Hornos',56),(346,'Antártica',56);
/*!40000 ALTER TABLE `comunas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo`
--

DROP TABLE IF EXISTS `equipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipo` (
  `id_equipo` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_equipo` varchar(45) DEFAULT NULL,
  `nombre_capitan` varchar(45) DEFAULT NULL,
  `id_cliente` varchar(45) DEFAULT NULL,
  `campeonato_id_campeonato` int(11) NOT NULL,
  PRIMARY KEY (`id_equipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo`
--

LOCK TABLES `equipo` WRITE;
/*!40000 ALTER TABLE `equipo` DISABLE KEYS */;
/*!40000 ALTER TABLE `equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estacionamiento`
--

DROP TABLE IF EXISTS `estacionamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estacionamiento` (
  `id_estacionamiento` int(11) NOT NULL AUTO_INCREMENT,
  `valor_estacionamiento` varchar(45) DEFAULT NULL,
  `estado_estacionamiento` varchar(45) DEFAULT NULL,
  `arriendo_id_arriendo` int(11) NOT NULL,
  PRIMARY KEY (`id_estacionamiento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estacionamiento`
--

LOCK TABLES `estacionamiento` WRITE;
/*!40000 ALTER TABLE `estacionamiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `estacionamiento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horarios`
--

DROP TABLE IF EXISTS `horarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `horarios` (
  `id_horarios` int(11) NOT NULL AUTO_INCREMENT,
  `inicio` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '0',
  `termino` varchar(100) DEFAULT '0',
  PRIMARY KEY (`id_horarios`),
  UNIQUE KEY `horarios_id_horario_IDX` (`id_horarios`) USING BTREE,
  KEY `horarios_Column1_IDX` (`id_horarios`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horarios`
--

LOCK TABLES `horarios` WRITE;
/*!40000 ALTER TABLE `horarios` DISABLE KEYS */;
INSERT INTO `horarios` VALUES (1,'10:00','11:00'),(2,'11:00','12:00'),(3,'12:00','13:00'),(4,'13:00','14:00'),(5,'14:00','15:00'),(6,'15:00','16:00'),(7,'16:00','17:00'),(8,'17:00','18:00'),(9,'18:00','19:00'),(10,'19:00','20:00'),(11,'20:00','21:00'),(12,'21:00','22:00'),(13,'22:00','23:00'),(14,'23:00','00:00');
/*!40000 ALTER TABLE `horarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantencion`
--

DROP TABLE IF EXISTS `mantencion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mantencion` (
  `id_mantencion` int(11) NOT NULL AUTO_INCREMENT,
  `id_trabajdor` varchar(45) DEFAULT NULL,
  `id_cancha` varchar(45) DEFAULT NULL,
  `nombre_trabajdor` varchar(45) DEFAULT NULL,
  `fecha_mantencion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_mantencion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantencion`
--

LOCK TABLES `mantencion` WRITE;
/*!40000 ALTER TABLE `mantencion` DISABLE KEYS */;
/*!40000 ALTER TABLE `mantencion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pelota`
--

DROP TABLE IF EXISTS `pelota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pelota` (
  `id_pelota` int(11) NOT NULL AUTO_INCREMENT,
  `sku_pelota` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `nombre_pelota` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `imagen_pelota` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `valor_pelota` int(11) NOT NULL,
  `descripcion_pelota` varchar(300) NOT NULL,
  `id_cliente` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_pelota`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pelota`
--

LOCK TABLES `pelota` WRITE;
/*!40000 ALTER TABLE `pelota` DISABLE KEYS */;
INSERT INTO `pelota` VALUES (1,'BAL001','Balón de fútbol','images/pelota_futbol.jpg',3000,'Balón de futbol, futbolito o baby futbol',NULL),(2,'BAL002','Balón de basketball','images/pelota_basket.jpg',3000,'Balón de basketball',NULL),(3,'BAL003','Pelotas de tenis','images/pelota_tenis.jpg',3000,'6 pelotas de tenis.',NULL);
/*!40000 ALTER TABLE `pelota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promociones`
--

DROP TABLE IF EXISTS `promociones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promociones` (
  `id_promocion` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion_promocion` varchar(45) DEFAULT NULL,
  `valor_promocion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_promocion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promociones`
--

LOCK TABLES `promociones` WRITE;
/*!40000 ALTER TABLE `promociones` DISABLE KEYS */;
/*!40000 ALTER TABLE `promociones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provincias`
--

DROP TABLE IF EXISTS `provincias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provincias` (
  `id_provincia` int(11) NOT NULL AUTO_INCREMENT,
  `provincia` varchar(64) NOT NULL,
  `id_region` int(11) NOT NULL,
  PRIMARY KEY (`id_provincia`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provincias`
--

LOCK TABLES `provincias` WRITE;
/*!40000 ALTER TABLE `provincias` DISABLE KEYS */;
INSERT INTO `provincias` VALUES (1,'Arica',1),(2,'Parinacota',1),(3,'Iquique',2),(4,'El Tamarugal',2),(5,'Tocopilla',3),(6,'El Loa',3),(7,'Antofagasta',3),(8,'Chañaral',4),(9,'Copiapó',4),(10,'Huasco',4),(11,'Elqui',5),(12,'Limarí',5),(13,'Choapa',5),(14,'Petorca',6),(15,'Los Andes',6),(16,'San Felipe de Aconcagua',6),(17,'Quillota',6),(18,'Valparaiso',6),(19,'San Antonio',6),(20,'Isla de Pascua',6),(21,'Marga Marga',6),(22,'Chacabuco',7),(23,'Santiago',7),(24,'Cordillera',7),(25,'Maipo',7),(26,'Melipilla',7),(27,'Talagante',7),(28,'Cachapoal',8),(29,'Colchagua',8),(30,'Cardenal Caro',8),(31,'Curicó',9),(32,'Talca',9),(33,'Linares',9),(34,'Cauquenes',9),(35,'Diguillín',10),(36,'Itata',10),(37,'Punilla',10),(38,'Bio Bío',11),(39,'Concepción',11),(40,'Arauco',11),(41,'Malleco',12),(42,'Cautín',12),(43,'Valdivia',13),(44,'Ranco',13),(45,'Osorno',14),(46,'Llanquihue',14),(47,'Chiloé',14),(48,'Palena',14),(49,'Coyhaique',15),(50,'Aysén',15),(51,'General Carrera',15),(52,'Capitán Prat',15),(53,'Última Esperanza',16),(54,'Magallanes',16),(55,'Tierra del Fuego',16),(56,'Antártica Chilena',16);
/*!40000 ALTER TABLE `provincias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regiones`
--

DROP TABLE IF EXISTS `regiones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regiones` (
  `id_region` int(11) NOT NULL AUTO_INCREMENT,
  `region` varchar(64) NOT NULL,
  `abreviatura` varchar(4) NOT NULL,
  `capital` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id_region`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regiones`
--

LOCK TABLES `regiones` WRITE;
/*!40000 ALTER TABLE `regiones` DISABLE KEYS */;
INSERT INTO `regiones` VALUES (1,'Arica y Parinacota','AP','Arica'),(2,'Tarapacá','TA','Iquique'),(3,'Antofagasta','AN','Antofagasta'),(4,'Atacama','AT','Copiapó'),(5,'Coquimbo','CO','La Serena'),(6,'Valparaiso','VA','valparaíso'),(7,'Metropolitana de Santiago','RM','Santiago'),(8,'Libertador General Bernardo OHiggins','OH','Rancagua'),(9,'Maule','MA','Talca'),(10,'Ñuble','NB','Chillán'),(11,'Biobío','BI','Concepción'),(12,'La Araucanía','IAR','Temuco'),(13,'Los Ríos','LR','Valdivia'),(14,'Los Lagos','LL','Puerto Montt'),(15,'Aysén del General Carlos Ibáñez del Campo','AI','Coyhaique'),(16,'Magallanes y de la Antártica Chilena','MG','Punta Arenas');
/*!40000 ALTER TABLE `regiones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajador`
--

DROP TABLE IF EXISTS `trabajador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajador` (
  `id_trabajador` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_trabajador` varchar(45) DEFAULT NULL,
  `apellido_trabajador` varchar(45) DEFAULT NULL,
  `fecha_nacimiento_trabajador` varchar(45) DEFAULT NULL,
  `direccion_trabajador` varchar(45) DEFAULT NULL,
  `comuna_trabajador` varchar(45) DEFAULT NULL,
  `provincia_trabajador` varchar(45) DEFAULT NULL,
  `region_trabajador` varchar(45) DEFAULT NULL,
  `sueldo_trabajador` varchar(45) DEFAULT NULL,
  `fecha_contratacion_trabajador` varchar(45) DEFAULT NULL,
  `comunas_id` int(11) NOT NULL,
  `caja_id_caja` int(11) NOT NULL,
  `mantencion_id_mantencion` int(11) NOT NULL,
  PRIMARY KEY (`id_trabajador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajador`
--

LOCK TABLES `trabajador` WRITE;
/*!40000 ALTER TABLE `trabajador` DISABLE KEYS */;
/*!40000 ALTER TABLE `trabajador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaccion`
--

DROP TABLE IF EXISTS `transaccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaccion` (
  `id_transanccion` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_tarjeta` varchar(100) NOT NULL,
  `fecha_transaccion` varchar(100) NOT NULL,
  `orden_compra` varchar(100) NOT NULL,
  `session` varchar(100) NOT NULL,
  `estado` varchar(100) NOT NULL,
  `id_cliente` varchar(100) NOT NULL,
  PRIMARY KEY (`id_transanccion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaccion`
--

LOCK TABLES `transaccion` WRITE;
/*!40000 ALTER TABLE `transaccion` DISABLE KEYS */;
INSERT INTO `transaccion` VALUES (1,'Débito','2023-06-13T01:59:25.262Z','FDEAWER4523D','2334567','AUTHORIZED','0');
/*!40000 ALTER TABLE `transaccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(64) NOT NULL,
  `apellido_usuario` varchar(64) NOT NULL,
  `correo_usuario` varchar(64) NOT NULL,
  `password_usuario` varchar(64) NOT NULL,
  `telefono_usuario` varchar(64) NOT NULL,
  `direccion_usuario` varchar(64) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'prueba de f3','prueba','prueba@gmail.com','12345','123123','prueba@gmail.com'),(2,'Usuario','De Prueba','prueba@gmail.com','1234567890','123123','prueba@gmail.com'),(3,'asdasdasd','De Prueba 3','prueba@gmail.com','1234567890','123123','prueba@gmail.com');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'soccer_evolution'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-12 23:56:45
