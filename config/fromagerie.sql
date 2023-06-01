-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 01 juin 2023 à 14:13
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;

--
-- Base de données : `fromagerie`
--
CREATE DATABASE IF NOT EXISTS `fromagerie` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `fromagerie`;

-- --------------------------------------------------------

--
-- Structure de la table `t_client`
--

CREATE TABLE IF NOT EXISTS `t_client` (
  `codcli` int(11) NOT NULL AUTO_INCREMENT,
  `genrecli` varchar(8) DEFAULT NULL,
  `nomcli` varchar(40) DEFAULT NULL,
  `prenomcli` varchar(30) DEFAULT NULL,
  `adresse1cli` varchar(50) DEFAULT NULL,
  `adresse2cli` varchar(50) DEFAULT NULL,
  `adresse3cli` varchar(50) DEFAULT NULL,
  `villecli_id` int(11) NOT NULL,
  `telcli` varchar(10) DEFAULT NULL,
  `emailcli` varchar(255) DEFAULT NULL,
  `portcli` varchar(10) DEFAULT NULL,
  `newsletter` int(11) DEFAULT NULL,
  PRIMARY KEY (`codcli`),
  KEY `villecli_id` (`villecli_id`),
  KEY `ix_t_client_nomcli` (`nomcli`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_communes`
--

CREATE TABLE IF NOT EXISTS `t_communes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dep` varchar(2) NOT NULL,
  `cp` varchar(5) DEFAULT NULL,
  `ville` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `commune_index` (`dep`,`cp`,`ville`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_conditionnement`
--

CREATE TABLE IF NOT EXISTS `t_conditionnement` (
  `idcondit` int(11) NOT NULL AUTO_INCREMENT,
  `libcondit` varchar(50) DEFAULT NULL,
  `poidscondit` int(11) DEFAULT NULL,
  `prixcond` decimal(10,0) DEFAULT NULL,
  `ordreimp` int(11) DEFAULT NULL,
  PRIMARY KEY (`idcondit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dept`
--

CREATE TABLE IF NOT EXISTS `t_dept` (
  `code_dept` varchar(2) NOT NULL,
  `nom_dept` varchar(50) DEFAULT NULL,
  `ordre_aff_dept` int(11) DEFAULT NULL,
  PRIMARY KEY (`code_dept`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dtlcode`
--

CREATE TABLE IF NOT EXISTS `t_dtlcode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `codcde` int(11) DEFAULT NULL,
  `qte` int(11) DEFAULT NULL,
  `colis` int(11) DEFAULT NULL,
  `commentaire` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_t_dtlcode_codcde` (`codcde`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dtlcode_codobj`
--

CREATE TABLE IF NOT EXISTS `t_dtlcode_codobj` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `detail_id` int(11) DEFAULT NULL,
  `objet_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `detail_id` (`detail_id`),
  KEY `objet_id` (`objet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dtlcode_idcondit`
--

CREATE TABLE IF NOT EXISTS `t_dtlcode_idcondit` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `detail_id` int(11) DEFAULT NULL,
  `conditionnement_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `detail_id` (`detail_id`),
  KEY `conditionnement_id` (`conditionnement_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_enseigne`
--

CREATE TABLE IF NOT EXISTS `t_enseigne` (
  `id_enseigne` int(11) NOT NULL AUTO_INCREMENT,
  `lb_enseigne` varchar(50) DEFAULT NULL,
  `ville_enseigne` varchar(50) DEFAULT NULL,
  `dept_enseigne` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_enseigne`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_entcde`
--

CREATE TABLE IF NOT EXISTS `t_entcde` (
  `codcde` int(11) NOT NULL AUTO_INCREMENT,
  `datcde` date DEFAULT NULL,
  `codcli` int(11) DEFAULT NULL,
  `timbrecli` float DEFAULT NULL,
  `timbrecde` float DEFAULT NULL,
  `nbcolis` int(11) DEFAULT NULL,
  `cheqcli` float DEFAULT NULL,
  `cdeComt` varchar(255) DEFAULT NULL,
  `barchive` int(11) DEFAULT NULL,
  `bstock` int(11) DEFAULT NULL,
  PRIMARY KEY (`codcde`),
  KEY `codcli` (`codcli`),
  KEY `commmande_index` (`cdeComt`,`codcli`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_objet`
--

CREATE TABLE IF NOT EXISTS `t_objet` (
  `codobj` int(11) NOT NULL AUTO_INCREMENT,
  `libobj` varchar(50) DEFAULT NULL,
  `tailleobj` varchar(50) DEFAULT NULL,
  `puobj` decimal(10,0) DEFAULT NULL,
  `poidsobj` decimal(10,0) DEFAULT NULL,
  `indispobj` int(11) DEFAULT NULL,
  `o_imp` int(11) DEFAULT NULL,
  `o_aff` int(11) DEFAULT NULL,
  `o_cartp` int(11) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `o_ordre_aff` int(11) DEFAULT NULL,
  PRIMARY KEY (`codobj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_poids`
--

CREATE TABLE IF NOT EXISTS `t_poids` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valmin` decimal(10,0) DEFAULT NULL,
  `valtimbre` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_poidsv`
--

CREATE TABLE IF NOT EXISTS `t_poidsv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `valmin` decimal(10,0) DEFAULT NULL,
  `valtimbre` decimal(10,0) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_role`
--

CREATE TABLE IF NOT EXISTS `t_role` (
  `codrole` int(11) NOT NULL AUTO_INCREMENT,
  `librole` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`codrole`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_utilisateur`
--

CREATE TABLE IF NOT EXISTS `t_utilisateur` (
  `code_utilisateur` int(11) NOT NULL AUTO_INCREMENT,
  `nom_utilisateur` varchar(50) DEFAULT NULL,
  `prenom_utilisateur` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `couleur_fond_utilisateur` int(11) DEFAULT NULL,
  `date_insc_utilisateur` date DEFAULT NULL,
  PRIMARY KEY (`code_utilisateur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_utilisateur_role`
--

CREATE TABLE IF NOT EXISTS `t_utilisateur_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `utilisateur_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `utilisateur_id` (`utilisateur_id`),
  KEY `role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `t_client`
--
ALTER TABLE `t_client`
  ADD CONSTRAINT `t_client_ibfk_1` FOREIGN KEY (`villecli_id`) REFERENCES `t_communes` (`id`);

--
-- Contraintes pour la table `t_communes`
--
ALTER TABLE `t_communes`
  ADD CONSTRAINT `t_communes_ibfk_1` FOREIGN KEY (`dep`) REFERENCES `t_dept` (`code_dept`);

--
-- Contraintes pour la table `t_dtlcode`
--
ALTER TABLE `t_dtlcode`
  ADD CONSTRAINT `t_dtlcode_ibfk_1` FOREIGN KEY (`codcde`) REFERENCES `t_entcde` (`codcde`);

--
-- Contraintes pour la table `t_dtlcode_codobj`
--
ALTER TABLE `t_dtlcode_codobj`
  ADD CONSTRAINT `t_dtlcode_codobj_ibfk_1` FOREIGN KEY (`detail_id`) REFERENCES `t_dtlcode` (`id`),
  ADD CONSTRAINT `t_dtlcode_codobj_ibfk_2` FOREIGN KEY (`objet_id`) REFERENCES `t_objet` (`codobj`);

--
-- Contraintes pour la table `t_dtlcode_idcondit`
--
ALTER TABLE `t_dtlcode_idcondit`
  ADD CONSTRAINT `t_dtlcode_idcondit_ibfk_1` FOREIGN KEY (`detail_id`) REFERENCES `t_dtlcode` (`id`),
  ADD CONSTRAINT `t_dtlcode_idcondit_ibfk_2` FOREIGN KEY (`conditionnement_id`) REFERENCES `t_conditionnement` (`idcondit`);

--
-- Contraintes pour la table `t_entcde`
--
ALTER TABLE `t_entcde`
  ADD CONSTRAINT `t_entcde_ibfk_1` FOREIGN KEY (`codcli`) REFERENCES `t_client` (`codcli`);

--
-- Contraintes pour la table `t_utilisateur_role`
--
ALTER TABLE `t_utilisateur_role`
  ADD CONSTRAINT `t_utilisateur_role_ibfk_1` FOREIGN KEY (`utilisateur_id`) REFERENCES `t_utilisateur` (`code_utilisateur`),
  ADD CONSTRAINT `t_utilisateur_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `t_role` (`codrole`);
COMMIT;