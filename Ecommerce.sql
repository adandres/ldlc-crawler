-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 15, 2021 at 12:53 PM
-- Server version: 5.7.32
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Ecommerce`
--
CREATE DATABASE IF NOT EXISTS `Ecommerce` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Ecommerce`;

-- --------------------------------------------------------

--
-- Table structure for table `Alimentation`
--

CREATE TABLE `Alimentation` (
  `id` int(11) NOT NULL,
  `Désignation` varchar(255) NOT NULL,
  `Marque` varchar(255) DEFAULT NULL,
  `Modèle` varchar(255) DEFAULT NULL,
  `Puissance` int(11) DEFAULT NULL,
  `Certification 80 PLUS` varchar(255) DEFAULT NULL,
  `Norme 80 PLUS` varchar(255) DEFAULT NULL,
  `Modulaire` varchar(255) DEFAULT NULL,
  `Modularité` varchar(255) DEFAULT NULL,
  `Connecteur(s) alimentation` json DEFAULT NULL,
  `Taille de ventilateur` int(11) DEFAULT NULL,
  `Silencieux(se)` varchar(255) DEFAULT NULL,
  `Type d'Alimentation (PC)` varchar(255) DEFAULT NULL,
  `Format Alimentation` varchar(255) DEFAULT NULL,
  `Multi-GPU` json DEFAULT NULL,
  `Hauteur` float DEFAULT NULL,
  `Largeur` float DEFAULT NULL,
  `Longueur` float DEFAULT NULL,
  `Garantie commerciale` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Chipset`
--

CREATE TABLE `Chipset` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `GPU`
--

CREATE TABLE `GPU` (
  `id` int(11) NOT NULL,
  `Désignation` varchar(255) NOT NULL,
  `Marque` varchar(255) DEFAULT NULL,
  `Modèle` varchar(255) DEFAULT NULL,
  `Chipset graphique` varchar(255) DEFAULT NULL,
  `Marque du GPU` varchar(255) DEFAULT NULL,
  `Fréquence du chipset` varchar(255) DEFAULT NULL,
  `Fréquence boostée` varchar(255) DEFAULT NULL,
  `Overclockée` varchar(255) DEFAULT NULL,
  `Nombre de GPU` int(11) DEFAULT NULL,
  `Bus` varchar(255) DEFAULT NULL,
  `Taille mémoire vidéo` int(11) DEFAULT NULL,
  `Interface mémoire` varchar(255) DEFAULT NULL,
  `Fréquence mémoire vidéo` varchar(255) DEFAULT NULL,
  `Type de mémoire` varchar(255) DEFAULT NULL,
  `Processeurs de flux` varchar(255) DEFAULT NULL,
  `Support Direct X (version)` varchar(255) DEFAULT NULL,
  `Multi-GPU` varchar(255) DEFAULT NULL,
  `HD Ready` varchar(255) DEFAULT NULL,
  `Résolution(s) 4K UHD` varchar(255) DEFAULT NULL,
  `VR Ready (réalité virtuelle)` varchar(255) DEFAULT NULL,
  `Compatible VirtualLink` varchar(255) DEFAULT NULL,
  `Sorties vidéo` json DEFAULT NULL,
  `Nombre d'écran(s)` int(11) DEFAULT NULL,
  `DVI Dual-Link` varchar(255) DEFAULT NULL,
  `Connecteur(s) alimentation` varchar(255) DEFAULT NULL,
  `Type de refroidissement` varchar(255) DEFAULT NULL,
  `Consommation` int(11) DEFAULT NULL,
  `Low profile` varchar(255) DEFAULT NULL,
  `Format` varchar(255) DEFAULT NULL,
  `Nombre de slots PCI` varchar(255) DEFAULT NULL,
  `LED` varchar(255) DEFAULT NULL,
  `LED RGB` varchar(255) DEFAULT NULL,
  `Longueur` float DEFAULT NULL,
  `Largeur` float DEFAULT NULL,
  `Epaisseur` float DEFAULT NULL,
  `Garantie commerciale` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Mobo`
--

CREATE TABLE `Mobo` (
  `id` int(11) NOT NULL,
  `Désignation` varchar(255) NOT NULL,
  `Marque` varchar(255) DEFAULT NULL,
  `Modèle` varchar(255) DEFAULT NULL,
  `Support du processeur` json DEFAULT NULL,
  `Nombre de CPU supportés` int(11) DEFAULT NULL,
  `Chipset` varchar(255) DEFAULT NULL,
  `Format de mémoire` varchar(255) DEFAULT NULL,
  `Fréquence(s) Mémoire` json DEFAULT NULL,
  `Type de mémoire` varchar(255) DEFAULT NULL,
  `Technologie mémoire` varchar(255) DEFAULT NULL,
  `Capacité maximale de RAM par slot` varchar(255) DEFAULT NULL,
  `Capacité maximale de RAM` varchar(255) DEFAULT NULL,
  `Contrôleur graphique intégré` varchar(255) DEFAULT NULL,
  `Compatible coeur graphique intégré au CPU` varchar(255) DEFAULT NULL,
  `Chipset graphique` varchar(255) DEFAULT NULL,
  `Taille mémoire vidéo` varchar(255) DEFAULT NULL,
  `Connecteur(s) graphique` json DEFAULT NULL,
  `Nombre et Type de slots` varchar(255) DEFAULT NULL,
  `Type de multi-GPU` varchar(255) DEFAULT NULL,
  `Chipset Audio` varchar(255) DEFAULT NULL,
  `Nombre de canaux audio` int(11) DEFAULT NULL,
  `Nombre de ports/Contrôleur Ethernet` varchar(255) DEFAULT NULL,
  `Nombre de ports/Contrôleur Ethernet N°2` varchar(255) DEFAULT NULL,
  `Norme(s) réseau` varchar(255) DEFAULT NULL,
  `RAID supporté` varchar(255) DEFAULT NULL,
  `Connecteurs Disques` json DEFAULT NULL,
  `Modes RAID supportés` json DEFAULT NULL,
  `Nombre de connecteurs pour ventilateurs` int(11) DEFAULT NULL,
  `Connecteurs panneau arrière` json DEFAULT NULL,
  `Connecteurs additionnels` json DEFAULT NULL,
  `Ports USB` json DEFAULT NULL,
  `Format de carte mère` varchar(255) DEFAULT NULL,
  `Longueur` float DEFAULT NULL,
  `Largeur` float DEFAULT NULL,
  `Fonctionnalités d'Overclocking avancées` varchar(255) DEFAULT NULL,
  `LED` varchar(255) DEFAULT NULL,
  `Garantie commerciale` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Processeur`
--

CREATE TABLE `Processeur` (
  `id` int(11) NOT NULL,
  `Désignation` varchar(255) DEFAULT NULL,
  `Marque` varchar(255) DEFAULT NULL,
  `Modèle` varchar(255) DEFAULT NULL,
  `Modèle de processeur` varchar(255) DEFAULT NULL,
  `Support du processeur` varchar(255) DEFAULT NULL,
  `Fréquence CPU` float DEFAULT NULL,
  `Fréquence en mode Turbo` float DEFAULT NULL,
  `Fréquence du bus` varchar(255) DEFAULT NULL,
  `Nombre de core` int(11) DEFAULT NULL,
  `Nombre de Threads` int(11) DEFAULT NULL,
  `Plateforme (Proc.)` varchar(255) DEFAULT NULL,
  `Nom du core` varchar(255) DEFAULT NULL,
  `Finesse de gravure` varchar(255) DEFAULT NULL,
  `TDP` varchar(255) DEFAULT NULL,
  `Cache L1` varchar(255) DEFAULT NULL,
  `Cache L2` varchar(255) DEFAULT NULL,
  `Cache L3` varchar(255) DEFAULT NULL,
  `Compatibilité chipset carte mère` json DEFAULT NULL,
  `Chipset graphique` varchar(255) DEFAULT NULL,
  `Fréquence du chipset` varchar(255) DEFAULT NULL,
  `Fréquence boostée` varchar(255) DEFAULT NULL,
  `Contrôleur mémoire` varchar(255) DEFAULT NULL,
  `Type de contrôleur mémoire` varchar(255) DEFAULT NULL,
  `Fréquence(s) Mémoire` json DEFAULT NULL,
  `Virtualisation` json DEFAULT NULL,
  `Ventilateur fourni` varchar(255) DEFAULT NULL,
  `Garantie commerciale` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `RAM`
--

CREATE TABLE `RAM` (
  `id` int(11) NOT NULL,
  `Désignation` varchar(255) NOT NULL,
  `Marque` varchar(255) NOT NULL,
  `Modèle` varchar(255) DEFAULT NULL,
  `Type de mémoire` varchar(255) DEFAULT NULL,
  `Format de mémoire` varchar(255) DEFAULT NULL,
  `Capacité` int(11) DEFAULT NULL,
  `Fréquence(s) Mémoire` varchar(255) DEFAULT NULL,
  `Norme mémoire` varchar(255) DEFAULT NULL,
  `Spécification mémoire` varchar(255) DEFAULT NULL,
  `Nombre de barrettes` int(11) DEFAULT NULL,
  `Capacité par barrette` int(11) DEFAULT NULL,
  `LED` varchar(255) DEFAULT NULL,
  `LED RGB` varchar(255) DEFAULT NULL,
  `Radiateur` varchar(255) DEFAULT NULL,
  `Couleur radiateur` varchar(255) DEFAULT NULL,
  `Ventilateur fourni` varchar(255) DEFAULT NULL,
  `CAS Latency` int(11) DEFAULT NULL,
  `RAS to CAS Delay` int(11) DEFAULT NULL,
  `RAS Precharge Time` int(11) DEFAULT NULL,
  `RAS Active Time` int(11) DEFAULT NULL,
  `Tension` varchar(255) DEFAULT NULL,
  `Garantie commerciale` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Refroidissement`
--

CREATE TABLE `Refroidissement` (
  `id` int(11) NOT NULL,
  `Désignation` varchar(255) NOT NULL,
  `Marque` varchar(255) DEFAULT NULL,
  `Modèle` varchar(255) DEFAULT NULL,
  `Utilisation` varchar(255) DEFAULT NULL,
  `Support du processeur` json DEFAULT NULL,
  `Couleur` varchar(255) DEFAULT NULL,
  `Lumineux` varchar(255) DEFAULT NULL,
  `Couleur de LED` varchar(255) DEFAULT NULL,
  `Connecteur(s)` json DEFAULT NULL,
  `PWM` varchar(255) DEFAULT NULL,
  `Heat Pipe (Caloduc)` varchar(255) DEFAULT NULL,
  `Vitesse réglable` varchar(255) DEFAULT NULL,
  `Type de refroidissement` varchar(255) DEFAULT NULL,
  `TDP Max. CPU` int(11) DEFAULT NULL,
  `Diamètre ventilateur` int(11) DEFAULT NULL,
  `Niveau sonore maxi` varchar(255) DEFAULT NULL,
  `Vitesse de rotation mini` int(11) DEFAULT NULL,
  `Vitesse de rotation maxi` int(11) DEFAULT NULL,
  `Débit d'air maxi` varchar(255) DEFAULT NULL,
  `Compatibilité radiateur AIO` varchar(255) DEFAULT NULL,
  `Hauteur (ventilateur inclus)` float DEFAULT NULL,
  `Largeur (ventilateur inclus)` float DEFAULT NULL,
  `Profondeur (ventilateur inclus)` float DEFAULT NULL,
  `Hauteur` float DEFAULT NULL,
  `Largeur` float DEFAULT NULL,
  `Profondeur` float DEFAULT NULL,
  `Poids` float DEFAULT NULL,
  `Garantie commerciale` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Socket`
--

CREATE TABLE `Socket` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SpeedRAM`
--

CREATE TABLE `SpeedRAM` (
  `id` int(11) NOT NULL,
  `nom` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `SSD`
--

CREATE TABLE `SSD` (
  `id` int(11) NOT NULL,
  `Désignation` varchar(255) NOT NULL,
  `Marque` varchar(255) DEFAULT NULL,
  `Modèle` varchar(255) DEFAULT NULL,
  `Interface avec l'ordinateur` varchar(255) DEFAULT NULL,
  `Format de Disque` varchar(255) DEFAULT NULL,
  `Capacité` int(11) DEFAULT NULL,
  `Taille du cache` int(11) DEFAULT NULL,
  `Type de mémoire Flash` varchar(255) DEFAULT NULL,
  `NVMe` varchar(255) DEFAULT NULL,
  `Vitesse en lecture` int(11) DEFAULT NULL,
  `Vitesse en écriture` int(11) DEFAULT NULL,
  `IOPS` int(11) DEFAULT NULL,
  `Compatible TRIM` varchar(255) DEFAULT NULL,
  `Largeur` float DEFAULT NULL,
  `Hauteur` float DEFAULT NULL,
  `Profondeur` float DEFAULT NULL,
  `Poids` float DEFAULT NULL,
  `Garantie commerciale` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Alimentation`
--
ALTER TABLE `Alimentation`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Désignation` (`Désignation`);

--
-- Indexes for table `Chipset`
--
ALTER TABLE `Chipset`
  ADD UNIQUE KEY `nom` (`nom`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `GPU`
--
ALTER TABLE `GPU`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Désignation` (`Désignation`);

--
-- Indexes for table `Mobo`
--
ALTER TABLE `Mobo`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Désignation` (`Désignation`);

--
-- Indexes for table `Processeur`
--
ALTER TABLE `Processeur`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Désignation` (`Désignation`);

--
-- Indexes for table `RAM`
--
ALTER TABLE `RAM`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Désignation` (`Désignation`);

--
-- Indexes for table `Refroidissement`
--
ALTER TABLE `Refroidissement`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Désignation` (`Désignation`);

--
-- Indexes for table `Socket`
--
ALTER TABLE `Socket`
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Indexes for table `SpeedRAM`
--
ALTER TABLE `SpeedRAM`
  ADD UNIQUE KEY `id` (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Indexes for table `SSD`
--
ALTER TABLE `SSD`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Alimentation`
--
ALTER TABLE `Alimentation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `GPU`
--
ALTER TABLE `GPU`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Mobo`
--
ALTER TABLE `Mobo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Processeur`
--
ALTER TABLE `Processeur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `RAM`
--
ALTER TABLE `RAM`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `Refroidissement`
--
ALTER TABLE `Refroidissement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `SSD`
--
ALTER TABLE `SSD`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
