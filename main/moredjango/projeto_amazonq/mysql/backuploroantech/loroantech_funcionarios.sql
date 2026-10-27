CREATE DATABASE  IF NOT EXISTS `loroantech` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `loroantech`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: loroantech
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `id_funcionario` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `telefone` varchar(30) DEFAULT NULL,
  `cargo` varchar(50) DEFAULT NULL,
  `salario` float DEFAULT NULL,
  `descricao` text,
  `data_nascimento` date DEFAULT NULL,
  `data_admissao` date DEFAULT NULL,
  `status` varchar(20) DEFAULT 'ativo',
  PRIMARY KEY (`id_funcionario`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'Luan Miguel De Freitas Vieira','luanmiguel.contato@outlook.com','+5511949022272','Diretor Executivo (CEO)',20000,'Fundador e Diretor Executivo da LoroanTech','2000-02-28','2020-04-03','ativo'),(2,'Ana Souza','ana.souza@loroantech.com','+5511999999991','Desenvolvedor Front-End Júnior',3500,'Responsável por manutenção e ajustes básicos no front','1999-05-12','2025-01-10','ativo'),(3,'Carlos Mendes','carlos.mendes@loroantech.com','+5511999999992','Desenvolvedor Front-End Pleno',6500,'Desenvolvimento de interfaces responsivas e integrações','1995-08-21','2025-01-10','ativo'),(4,'Fernanda Lima','fernanda.lima@loroantech.com','+5511999999993','Desenvolvedor Front-End Sênior',11000,'Líder técnico do time de front-end','1990-11-03','2025-01-10','ativo'),(5,'Rafael Torres','rafael.torres@loroantech.com','+5511999999994','Desenvolvedor Back-End Júnior',3800,'Auxilia em rotinas simples do servidor e banco de dados','2001-07-18','2025-01-10','ativo'),(6,'Juliana Castro','juliana.castro@loroantech.com','+5511999999995','Desenvolvedor Back-End Pleno',7000,'Implementa APIs e integrações de sistemas','1994-03-27','2025-01-10','ativo'),(7,'Marcos Silva','marcos.silva@loroantech.com','+5511999999996','Desenvolvedor Back-End Sênior',12000,'Arquiteto de soluções e responsável por escalabilidade','1988-09-14','2025-01-10','ativo'),(8,'Patrícia Gomes','patricia.gomes@loroantech.com','+5511999999997','Analista de QA',6000,'Responsável por testes e qualidade de software','1993-02-05','2025-01-10','ativo'),(9,'Rodrigo Alves','rodrigo.alves@loroantech.com','+5511999999998','UX/UI Designer',7000,'Criação de interfaces intuitivas e experiência do usuário','1996-12-20','2025-01-10','ativo'),(10,'Beatriz Fernandes','beatriz.fernandes@loroantech.com','+5511999999999','Tech Recruiter',5500,'Responsável por recrutamento e seleção de talentos de TI','1992-06-30','2025-01-10','ativo'),(11,'Tiago Oliveira','tiago.oliveira@loroantech.com','+5511999999980','Gerente de Projetos',9000,'Coordenação de times e cronogramas de entrega','1989-04-11','2025-01-10','ativo');
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-21 15:09:22
