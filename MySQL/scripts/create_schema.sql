
USE soccer_evolution;

CREATE TABLE  regiones 
(
    id_region INT AUTO_INCREMENT,
    region VARCHAR(64) NOT NULL,
    abreviatura VARCHAR(4) NOT NULL,
    capital VARCHAR(64),
    PRIMARY KEY (id_region)
);
/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`provincias`
-- -----------------------------------------------------
*/
CREATE TABLE provincias 
(
  id_provincia INT AUTO_INCREMENT,
  provincia VARCHAR(64) NOT NULL,
  id_region INT NOT NULL,
  PRIMARY KEY (id_provincia)

);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`comunas`
-- -----------------------------------------------------
*/

CREATE TABLE comunas 
(
  id_comuna INT AUTO_INCREMENT,
  comuna VARCHAR(64) NOT NULL,
  id_provincia INT NOT NULL,
  PRIMARY KEY (id_comuna)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`campeonato`
-- -----------------------------------------------------*/
CREATE TABLE usuario 
(
  id_usuario INT AUTO_INCREMENT,
  nombre_usuario VARCHAR(64) NOT NULL,
  apellido_usuario VARCHAR(64) NOT NULL,
  correo_usuario VARCHAR(64) NOT NULL,
  password_usuario VARCHAR(64) NOT NULL,
  telefono_usuario VARCHAR(64) NOT NULL,
  direccion_usuario VARCHAR(64) NOT NULL,
  PRIMARY KEY (id_usuario)

);


CREATE TABLE campeonato 
(
  id_campeonato INT AUTO_INCREMENT,
  nombre_equipo VARCHAR(45) NULL,
  valor_inscripcion VARCHAR(45) NULL,
  PRIMARY KEY (id_campeonato)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`promociones`
-- -----------------------------------------------------*/
CREATE TABLE promociones 
(
  id_promocion INT AUTO_INCREMENT,
  descripcion_promocion VARCHAR(45),
  valor_promocion VARCHAR(45) ,
  PRIMARY KEY (id_promocion)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`cliente`
-- -----------------------------------------------------*/
CREATE TABLE cliente 
(
  id__cliente INT AUTO_INCREMENT,
  nombre_cliente VARCHAR(45) ,
  apellido_cliente VARCHAR(45) ,
  direccion_cliente VARCHAR(45),
  telefono_cliente VARCHAR(45),
  correo_cliente VARCHAR(45),
  comuna_cliente VARCHAR(45),
  provincia_cliente VARCHAR(45),
  region_cliente VARCHAR(45),
  numero_compras INT NULL DEFAULT NULL,
  comunas_id INT NOT NULL,
  campeonato_id_campeonato INT NOT NULL,
  promociones_id_promocion INT NOT NULL,
  PRIMARY KEY (id__cliente)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`boleta`
-- -----------------------------------------------------
*/
CREATE TABLE boleta 
(
  id_boleta INT AUTO_INCREMENT,
  numero_boleta  VARCHAR(45),
  valor_boleta VARCHAR(45) ,
  fecha_boleta VARCHAR(45) ,
  id_cliente INT,
  id_cancha INT,
  PRIMARY KEY (id_boleta)
);


/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`arriendo`
-- -----------------------------------------------------
*/
CREATE TABLE arriendo 
(
  id_arriendo INT AUTO_INCREMENT,
  fecha_arriendo VARCHAR(45),
  horas_arriendo VARCHAR(45),
  balon_arriendo VARCHAR(45),
  valor_arriendo VARCHAR(45),
  id_cliente INT,
  cliente_id__cliente INT NOT NULL,
  boleta_id_boleta INT NOT NULL,
  PRIMARY KEY (id_arriendo)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`caja`
-- -----------------------------------------------------
*/
CREATE TABLE caja 
(
  id_caja INT AUTO_INCREMENT,
  id_trabajador VARCHAR(45) ,
  monto_caja VARCHAR(45) ,
  fecha_cierre_caja VARCHAR(45),
  PRIMARY KEY (id_caja)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`camisetas`
-- -----------------------------------------------------
*/
CREATE TABLE camisetas 
(
  id_camisetas INT AUTO_INCREMENT,
  cantidad_camisetas VARCHAR(45) ,
  color_camisetas VARCHAR(45) ,
  arriendo_id_arriendo INT NOT NULL,
  PRIMARY KEY (id_camisetas)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`cancha`
-- -----------------------------------------------------
*/
CREATE TABLE cancha 
(
  id_cancha INT AUTO_INCREMENT,
  nombre_cancha VARCHAR(45) ,
  descripcion_cancha VARCHAR(45) ,
  valor_cancha VARCHAR(45) ,
  id_cliente INT,
  arriendo_id_arriendo INT NOT NULL,
  PRIMARY KEY (id_cancha)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`equipo`
-- -----------------------------------------------------
*/
CREATE TABLE equipo 
(
  id_equipo INT AUTO_INCREMENT,
  nombre_equipo VARCHAR(45),
  nombre_capitan VARCHAR(45),
  id_cliente VARCHAR(45) ,
  campeonato_id_campeonato INT NOT NULL,
  PRIMARY KEY (id_equipo)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`estacionamiento`
-- -----------------------------------------------------
*/
CREATE TABLE estacionamiento 
(
  id_estacionamiento INT AUTO_INCREMENT,
  valor_estacionamiento VARCHAR(45),
  estado_estacionamiento VARCHAR(45),
  arriendo_id_arriendo INT NOT NULL,
  PRIMARY KEY (id_estacionamiento)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`mantencion`
-- -----------------------------------------------------
*/
CREATE TABLE mantencion 
(
  id_mantencion INT AUTO_INCREMENT,
  id_trabajdor VARCHAR(45) ,
  id_cancha VARCHAR(45) ,
  nombre_trabajdor VARCHAR(45) ,
  fecha_mantencion VARCHAR(45),
  PRIMARY KEY (id_mantencion)
);


/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`pelota`
-- -----------------------------------------------------
*/
CREATE TABLE pelota 
(
  id_pelota INT AUTO_INCREMENT,
  nombre_pelota VARCHAR(45) NULL DEFAULT NULL,
  tipo_pelota VARCHAR(45) NULL DEFAULT NULL,
  cantidad_pelota VARCHAR(45) NULL DEFAULT NULL,
  valor_pelota VARCHAR(45) NULL DEFAULT NULL,
  arriendo_id_arriendo INT NOT NULL,
  PRIMARY KEY (id_pelota)
);

/*
-- -----------------------------------------------------
-- Table `evolution_soccer`.`trabajador`
-- -----------------------------------------------------
*/
CREATE TABLE trabajador 
(
  id_trabajador INT AUTO_INCREMENT,
  nombre_trabajador VARCHAR(45),
  apellido_trabajador VARCHAR(45),
  fecha_nacimiento_trabajador VARCHAR(45),
  direccion_trabajador VARCHAR(45),
  comuna_trabajador VARCHAR(45) ,
  provincia_trabajador VARCHAR(45) ,
  region_trabajador VARCHAR(45) ,
  sueldo_trabajador VARCHAR(45) ,
  fecha_contratacion_trabajador VARCHAR(45),
  comunas_id INT NOT NULL,
  caja_id_caja INT NOT NULL,
  mantencion_id_mantencion INT NOT NULL,
  PRIMARY KEY (id_trabajador)
);

