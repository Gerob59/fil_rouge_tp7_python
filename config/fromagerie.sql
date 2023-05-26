-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 26 mai 2023 à 16:58
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `fromagerie`
--
CREATE DATABASE IF NOT EXISTS `fromagerie` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `fromagerie`;

-- --------------------------------------------------------

--
-- Structure de la table `t_client`
--

DROP TABLE IF EXISTS `t_client`;
CREATE TABLE `t_client` (
  `codcli` int(11) NOT NULL,
  `genrecli` varchar(8) DEFAULT NULL,
  `nomcli` varchar(40) DEFAULT NULL,
  `prenomcli` varchar(30) DEFAULT NULL,
  `adresse1cli` varchar(50) DEFAULT NULL,
  `adresse2cli` varchar(50) DEFAULT NULL,
  `adresse3cli` varchar(50) DEFAULT NULL,
  `villecli_id` int(11) DEFAULT NULL,
  `telcli` varchar(10) DEFAULT NULL,
  `emailcli` varchar(255) DEFAULT NULL,
  `portcli` varchar(10) DEFAULT NULL,
  `newsletter` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_communes`
--

DROP TABLE IF EXISTS `t_communes`;
CREATE TABLE `t_communes` (
  `id` int(11) NOT NULL,
  `dep` varchar(2) DEFAULT NULL,
  `cp` varchar(5) DEFAULT NULL,
  `ville` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_conditionnement`
--

DROP TABLE IF EXISTS `t_conditionnement`;
CREATE TABLE `t_conditionnement` (
  `idcondit` int(11) NOT NULL,
  `libcondit` varchar(50) DEFAULT NULL,
  `poidscondit` int(11) DEFAULT NULL,
  `prixcond` decimal(10,0) DEFAULT NULL,
  `ordreimp` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dept`
--

DROP TABLE IF EXISTS `t_dept`;
CREATE TABLE `t_dept` (
  `code_dept` varchar(2) NOT NULL,
  `nom_dept` varchar(50) DEFAULT NULL,
  `ordre_aff_dept` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dtlcode`
--

DROP TABLE IF EXISTS `t_dtlcode`;
CREATE TABLE `t_dtlcode` (
  `id` int(11) NOT NULL,
  `codcde` int(11) DEFAULT NULL,
  `qte` int(11) DEFAULT NULL,
  `colis` int(11) DEFAULT NULL,
  `commentaire` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_dtlcode_codobj`
--

DROP TABLE IF EXISTS `t_dtlcode_codobj`;
CREATE TABLE `t_dtlcode_codobj` (
  `id` int(11) NOT NULL,
  `detail_id` int(11) DEFAULT NULL,
  `objet_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_enseigne`
--

DROP TABLE IF EXISTS `t_enseigne`;
CREATE TABLE `t_enseigne` (
  `id_enseigne` int(11) NOT NULL,
  `lb_enseigne` varchar(50) DEFAULT NULL,
  `ville_enseigne` varchar(50) DEFAULT NULL,
  `dept_enseigne` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_entcde`
--

DROP TABLE IF EXISTS `t_entcde`;
CREATE TABLE `t_entcde` (
  `codcde` int(11) NOT NULL,
  `datcde` date DEFAULT NULL,
  `codcli` int(11) DEFAULT NULL,
  `timbrecli` float DEFAULT NULL,
  `timbrecde` float DEFAULT NULL,
  `nbcolis` int(11) DEFAULT NULL,
  `cheqcli` float DEFAULT NULL,
  `idcondit` int(11) DEFAULT NULL,
  `cdeComt` varchar(255) DEFAULT NULL,
  `barchive` int(11) DEFAULT NULL,
  `bstock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_objet`
--

DROP TABLE IF EXISTS `t_objet`;
CREATE TABLE `t_objet` (
  `codobj` int(11) NOT NULL,
  `libobj` varchar(50) DEFAULT NULL,
  `tailleobj` varchar(50) DEFAULT NULL,
  `puobj` decimal(10,0) DEFAULT NULL,
  `poidsobj` decimal(10,0) DEFAULT NULL,
  `indispobj` int(11) DEFAULT NULL,
  `o_imp` int(11) DEFAULT NULL,
  `o_aff` int(11) DEFAULT NULL,
  `o_cartp` int(11) DEFAULT NULL,
  `points` int(11) DEFAULT NULL,
  `o_ordre_aff` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_poids`
--

DROP TABLE IF EXISTS `t_poids`;
CREATE TABLE `t_poids` (
  `id` int(11) NOT NULL,
  `valmin` decimal(10,0) DEFAULT NULL,
  `valtimbre` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_poidsv`
--

DROP TABLE IF EXISTS `t_poidsv`;
CREATE TABLE `t_poidsv` (
  `id` int(11) NOT NULL,
  `valmin` decimal(10,0) DEFAULT NULL,
  `valtimbre` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_rel_cond`
--

DROP TABLE IF EXISTS `t_rel_cond`;
CREATE TABLE `t_rel_cond` (
  `idrelcond` int(11) NOT NULL,
  `qteobjdeb` int(11) DEFAULT NULL,
  `qteobjfin` int(11) DEFAULT NULL,
  `codobj` int(11) DEFAULT NULL,
  `codcond` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_role`
--

DROP TABLE IF EXISTS `t_role`;
CREATE TABLE `t_role` (
  `codrole` int(11) NOT NULL,
  `librole` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_utilisateur`
--

DROP TABLE IF EXISTS `t_utilisateur`;
CREATE TABLE `t_utilisateur` (
  `code_utilisateur` int(11) NOT NULL,
  `nom_utilisateur` varchar(50) DEFAULT NULL,
  `prenom_utilisateur` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `couleur_fond_utilisateur` int(11) DEFAULT NULL,
  `date_insc_utilisateur` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `t_utilisateur_role`
--

DROP TABLE IF EXISTS `t_utilisateur_role`;
CREATE TABLE `t_utilisateur_role` (
  `id` int(11) NOT NULL,
  `utilisateur_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `t_client`
--
ALTER TABLE `t_client`
  ADD PRIMARY KEY (`codcli`),
  ADD KEY `villecli_id` (`villecli_id`),
  ADD KEY `ix_t_client_nomcli` (`nomcli`);

--
-- Index pour la table `t_communes`
--
ALTER TABLE `t_communes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `commune_index` (`dep`,`cp`,`ville`);

--
-- Index pour la table `t_conditionnement`
--
ALTER TABLE `t_conditionnement`
  ADD PRIMARY KEY (`idcondit`);

--
-- Index pour la table `t_dept`
--
ALTER TABLE `t_dept`
  ADD PRIMARY KEY (`code_dept`);

--
-- Index pour la table `t_dtlcode`
--
ALTER TABLE `t_dtlcode`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_t_dtlcode_codcde` (`codcde`);

--
-- Index pour la table `t_dtlcode_codobj`
--
ALTER TABLE `t_dtlcode_codobj`
  ADD PRIMARY KEY (`id`),
  ADD KEY `detail_id` (`detail_id`),
  ADD KEY `objet_id` (`objet_id`);

--
-- Index pour la table `t_enseigne`
--
ALTER TABLE `t_enseigne`
  ADD PRIMARY KEY (`id_enseigne`);

--
-- Index pour la table `t_entcde`
--
ALTER TABLE `t_entcde`
  ADD PRIMARY KEY (`codcde`),
  ADD KEY `codcli` (`codcli`),
  ADD KEY `commmande_index` (`cdeComt`,`codcli`);

--
-- Index pour la table `t_objet`
--
ALTER TABLE `t_objet`
  ADD PRIMARY KEY (`codobj`);

--
-- Index pour la table `t_poids`
--
ALTER TABLE `t_poids`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `t_poidsv`
--
ALTER TABLE `t_poidsv`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `t_rel_cond`
--
ALTER TABLE `t_rel_cond`
  ADD PRIMARY KEY (`idrelcond`),
  ADD KEY `codobj` (`codobj`),
  ADD KEY `codcond` (`codcond`),
  ADD KEY `ix_t_rel_cond_idrelcond` (`idrelcond`);

--
-- Index pour la table `t_role`
--
ALTER TABLE `t_role`
  ADD PRIMARY KEY (`codrole`);

--
-- Index pour la table `t_utilisateur`
--
ALTER TABLE `t_utilisateur`
  ADD PRIMARY KEY (`code_utilisateur`);

--
-- Index pour la table `t_utilisateur_role`
--
ALTER TABLE `t_utilisateur_role`
  ADD PRIMARY KEY (`id`),
  ADD KEY `utilisateur_id` (`utilisateur_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `t_client`
--
ALTER TABLE `t_client`
  MODIFY `codcli` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_communes`
--
ALTER TABLE `t_communes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_conditionnement`
--
ALTER TABLE `t_conditionnement`
  MODIFY `idcondit` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dtlcode`
--
ALTER TABLE `t_dtlcode`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_dtlcode_codobj`
--
ALTER TABLE `t_dtlcode_codobj`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_enseigne`
--
ALTER TABLE `t_enseigne`
  MODIFY `id_enseigne` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_entcde`
--
ALTER TABLE `t_entcde`
  MODIFY `codcde` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_objet`
--
ALTER TABLE `t_objet`
  MODIFY `codobj` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_poids`
--
ALTER TABLE `t_poids`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_poidsv`
--
ALTER TABLE `t_poidsv`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_rel_cond`
--
ALTER TABLE `t_rel_cond`
  MODIFY `idrelcond` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_role`
--
ALTER TABLE `t_role`
  MODIFY `codrole` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_utilisateur`
--
ALTER TABLE `t_utilisateur`
  MODIFY `code_utilisateur` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `t_utilisateur_role`
--
ALTER TABLE `t_utilisateur_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

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
-- Contraintes pour la table `t_entcde`
--
ALTER TABLE `t_entcde`
  ADD CONSTRAINT `t_entcde_ibfk_1` FOREIGN KEY (`codcli`) REFERENCES `t_client` (`codcli`);

--
-- Contraintes pour la table `t_rel_cond`
--
ALTER TABLE `t_rel_cond`
  ADD CONSTRAINT `t_rel_cond_ibfk_1` FOREIGN KEY (`codobj`) REFERENCES `t_objet` (`codobj`),
  ADD CONSTRAINT `t_rel_cond_ibfk_2` FOREIGN KEY (`codcond`) REFERENCES `t_conditionnement` (`idcondit`);

--
-- Contraintes pour la table `t_utilisateur_role`
--
ALTER TABLE `t_utilisateur_role`
  ADD CONSTRAINT `t_utilisateur_role_ibfk_1` FOREIGN KEY (`utilisateur_id`) REFERENCES `t_utilisateur` (`code_utilisateur`),
  ADD CONSTRAINT `t_utilisateur_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `t_role` (`codrole`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
