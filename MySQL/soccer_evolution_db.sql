-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema evolution_soccer
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `evolution_soccer` ;

-- -----------------------------------------------------
-- Schema evolution_soccer
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `evolution_soccer` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `evolution_soccer` ;

-- -----------------------------------------------------
-- Table `evolution_soccer`.`regiones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`regiones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `region` VARCHAR(64) NOT NULL,
  `abreviatura` VARCHAR(4) NOT NULL,
  `capital` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = MyISAM
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`provincias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`provincias` (
  `id_provincia` INT NOT NULL AUTO_INCREMENT,
  `provincia` VARCHAR(64) NOT NULL,
  `region_id` INT NOT NULL,
  `regiones_id` INT NOT NULL,
  PRIMARY KEY (`id_provincia`),
  INDEX `fk_provincias_regiones_idx` (`regiones_id` ASC) VISIBLE)
ENGINE = MyISAM
AUTO_INCREMENT = 57
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`comunas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`comunas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comuna` VARCHAR(64) NOT NULL,
  `provincias_id_provincia` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comunas_provincias1_idx` (`provincias_id_provincia` ASC) VISIBLE)
ENGINE = MyISAM
AUTO_INCREMENT = 347
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`campeonato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`campeonato` (
  `id_campeonato` INT NOT NULL,
  `nombre_equipo` VARCHAR(45) NULL,
  `valor_inscripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`id_campeonato`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`promociones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`promociones` (
  `id_promocion` INT NOT NULL,
  `descripcion_promocion` VARCHAR(45) NULL DEFAULT NULL,
  `valor_promocion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_promocion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`cliente` (
  `id__cliente` INT NOT NULL,
  `nombre_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `apellido_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `direccion_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `telefono_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `correo_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `comuna_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `provincia_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `region_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `numero_compras` INT NULL DEFAULT NULL,
  `comunas_id` INT NOT NULL,
  `campeonato_id_campeonato` INT NOT NULL,
  `promociones_id_promocion` INT NOT NULL,
  PRIMARY KEY (`id__cliente`),
  INDEX `fk_cliente_comunas1_idx` (`comunas_id` ASC) VISIBLE,
  INDEX `fk_cliente_campeonato1_idx` (`campeonato_id_campeonato` ASC) VISIBLE,
  INDEX `fk_cliente_promociones1_idx` (`promociones_id_promocion` ASC) VISIBLE,
  CONSTRAINT `fk_cliente_comunas1`
    FOREIGN KEY (`comunas_id`)
    REFERENCES `evolution_soccer`.`comunas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cliente_campeonato1`
    FOREIGN KEY (`campeonato_id_campeonato`)
    REFERENCES `evolution_soccer`.`campeonato` (`id_campeonato`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cliente_promociones1`
    FOREIGN KEY (`promociones_id_promocion`)
    REFERENCES `evolution_soccer`.`promociones` (`id_promocion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`boleta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`boleta` (
  `id_boleta` INT NOT NULL,
  `numero_boleta` VARCHAR(45) NULL DEFAULT NULL,
  `valor_boleta` VARCHAR(45) NULL DEFAULT NULL,
  `fecha_boleta` VARCHAR(45) NULL DEFAULT NULL,
  `id_cliente` INT NULL DEFAULT NULL,
  `id_cancha` INT NULL DEFAULT NULL,
  PRIMARY KEY (`id_boleta`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`arriendo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`arriendo` (
  `id_arriendo` INT NOT NULL,
  `fecha_arriendo` VARCHAR(45) NULL DEFAULT NULL,
  `horas_arriendo` VARCHAR(45) NULL DEFAULT NULL,
  `balon_arriendo` VARCHAR(45) NULL DEFAULT NULL,
  `valor_arriendo` VARCHAR(45) NULL DEFAULT NULL,
  `id_cliente` INT NULL DEFAULT NULL,
  `cliente_id__cliente` INT NOT NULL,
  `boleta_id_boleta` INT NOT NULL,
  PRIMARY KEY (`id_arriendo`),
  INDEX `fk_arriendo_cliente1_idx` (`cliente_id__cliente` ASC) VISIBLE,
  INDEX `fk_arriendo_boleta1_idx` (`boleta_id_boleta` ASC) VISIBLE,
  CONSTRAINT `fk_arriendo_cliente1`
    FOREIGN KEY (`cliente_id__cliente`)
    REFERENCES `evolution_soccer`.`cliente` (`id__cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_arriendo_boleta1`
    FOREIGN KEY (`boleta_id_boleta`)
    REFERENCES `evolution_soccer`.`boleta` (`id_boleta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`caja`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`caja` (
  `id_caja` INT NOT NULL,
  `id_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `monto_caja` VARCHAR(45) NULL DEFAULT NULL,
  `fecha_cierre_caja` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id_caja`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`camisetas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`camisetas` (
  `id_camisetas` INT NOT NULL,
  `cantidad_camisetas` VARCHAR(45) NULL DEFAULT NULL,
  `color_camisetas` VARCHAR(45) NULL DEFAULT NULL,
  `arriendo_id_arriendo` INT NOT NULL,
  PRIMARY KEY (`id_camisetas`),
  INDEX `fk_camisetas_arriendo1_idx` (`arriendo_id_arriendo` ASC) VISIBLE,
  CONSTRAINT `fk_camisetas_arriendo1`
    FOREIGN KEY (`arriendo_id_arriendo`)
    REFERENCES `evolution_soccer`.`arriendo` (`id_arriendo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`cancha`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`cancha` (
  `id_cancha` INT NOT NULL,
  `nombre_cancha` VARCHAR(45) NULL DEFAULT NULL,
  `descripcion_cancha` VARCHAR(45) NULL DEFAULT NULL,
  `valor_cancha` VARCHAR(45) NULL DEFAULT NULL,
  `id_cliente` INT NULL DEFAULT NULL,
  `arriendo_id_arriendo` INT NOT NULL,
  PRIMARY KEY (`id_cancha`),
  INDEX `id_cliente_idx` (`id_cliente` ASC) VISIBLE,
  INDEX `fk_cancha_arriendo1_idx` (`arriendo_id_arriendo` ASC) VISIBLE,
  CONSTRAINT `fk_cancha_arriendo1`
    FOREIGN KEY (`arriendo_id_arriendo`)
    REFERENCES `evolution_soccer`.`arriendo` (`id_arriendo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`equipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`equipo` (
  `id_equipo` INT NOT NULL,
  `nombre_equipo` VARCHAR(45) NULL DEFAULT NULL,
  `nombre_capitan` VARCHAR(45) NULL DEFAULT NULL,
  `id_cliente` VARCHAR(45) NULL DEFAULT NULL,
  `campeonato_id_campeonato` INT NOT NULL,
  PRIMARY KEY (`id_equipo`),
  INDEX `fk_equipo_campeonato1_idx` (`campeonato_id_campeonato` ASC) VISIBLE,
  CONSTRAINT `fk_equipo_campeonato1`
    FOREIGN KEY (`campeonato_id_campeonato`)
    REFERENCES `evolution_soccer`.`campeonato` (`id_campeonato`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`estacionamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`estacionamiento` (
  `id_estacionamiento` INT NOT NULL,
  `valor_estacionamiento` VARCHAR(45) NULL DEFAULT NULL,
  `estado_estacionamiento` VARCHAR(45) NULL DEFAULT NULL,
  `arriendo_id_arriendo` INT NOT NULL,
  PRIMARY KEY (`id_estacionamiento`),
  INDEX `fk_estacionamiento_arriendo1_idx` (`arriendo_id_arriendo` ASC) VISIBLE,
  CONSTRAINT `fk_estacionamiento_arriendo1`
    FOREIGN KEY (`arriendo_id_arriendo`)
    REFERENCES `evolution_soccer`.`arriendo` (`id_arriendo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`mantencion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`mantencion` (
  `id_mantencion` INT NOT NULL,
  `id_trabajdor` VARCHAR(45) NULL DEFAULT NULL,
  `id_cancha` VARCHAR(45) NULL DEFAULT NULL,
  `nombre_trabajdor` VARCHAR(45) NULL DEFAULT NULL,
  `fecha_mantencion` VARCHAR(45) NULL,
  PRIMARY KEY (`id_mantencion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`pelota`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`pelota` (
  `id_pelota` INT NOT NULL,
  `nombre_pelota` VARCHAR(45) NULL DEFAULT NULL,
  `tipo_pelota` VARCHAR(45) NULL DEFAULT NULL,
  `cantidad_pelota` VARCHAR(45) NULL DEFAULT NULL,
  `valor_pelota` VARCHAR(45) NULL DEFAULT NULL,
  `arriendo_id_arriendo` INT NOT NULL,
  PRIMARY KEY (`id_pelota`),
  INDEX `fk_pelota_arriendo1_idx` (`arriendo_id_arriendo` ASC) VISIBLE,
  CONSTRAINT `fk_pelota_arriendo1`
    FOREIGN KEY (`arriendo_id_arriendo`)
    REFERENCES `evolution_soccer`.`arriendo` (`id_arriendo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `evolution_soccer`.`trabajador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `evolution_soccer`.`trabajador` (
  `id_trabajdor` INT NOT NULL,
  `nombre_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `apellido_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `fecha_nacimiento_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `direccion_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `comuna_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `provincia_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `region_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `sueldo_trabajdor` VARCHAR(45) NULL DEFAULT NULL,
  `fecha_contratacion_trabajador` VARCHAR(45) NULL DEFAULT NULL,
  `comunas_id` INT NOT NULL,
  `caja_id_caja` INT NOT NULL,
  `mantencion_id_mantencion` INT NOT NULL,
  PRIMARY KEY (`id_trabajdor`),
  INDEX `fk_trabajador_comunas1_idx` (`comunas_id` ASC) VISIBLE,
  INDEX `fk_trabajador_caja1_idx` (`caja_id_caja` ASC) VISIBLE,
  INDEX `fk_trabajador_mantencion1_idx` (`mantencion_id_mantencion` ASC) VISIBLE,
  CONSTRAINT `fk_trabajador_comunas1`
    FOREIGN KEY (`comunas_id`)
    REFERENCES `evolution_soccer`.`comunas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_trabajador_caja1`
    FOREIGN KEY (`caja_id_caja`)
    REFERENCES `evolution_soccer`.`caja` (`id_caja`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_trabajador_mantencion1`
    FOREIGN KEY (`mantencion_id_mantencion`)
    REFERENCES `evolution_soccer`.`mantencion` (`id_mantencion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
