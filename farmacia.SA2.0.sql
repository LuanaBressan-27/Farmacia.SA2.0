-- phpMyAdmin SQL Dumpk,m
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 13/03/2025 às 23:43
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `farmacia_sa2`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `adm`
--

CREATE TABLE `adm` (
  `idADM` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `CPF` text DEFAULT NULL,
  `senha` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `idfornecedor` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `produto` text DEFAULT NULL,
  `transporte` text DEFAULT NULL,
  `inicio_contrato` text DEFAULT NULL,
  `final_contrato` text DEFAULT NULL,
  `cidade` text DEFAULT NULL,
  `estado` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `idfuncionario` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `data_de_nascimento` text DEFAULT NULL,
  `data_de_contrato` text DEFAULT NULL,
  `telefone` text DEFAULT NULL,
  `cidade` text DEFAULT NULL,
  `estado` text DEFAULT NULL,
  `bairro` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

CREATE TABLE `produto` (
  `idproduto` int(11) NOT NULL,
  `produto` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `fornecedor` text DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `validade` text DEFAULT NULL,
  `quantidade` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE `usuario` (
  `idusuario` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `senha` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `adm`
--
ALTER TABLE `adm`
  ADD PRIMARY KEY (`idADM`);

--
-- Índices de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  ADD PRIMARY KEY (`idfornecedor`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`idfuncionario`);

--
-- Índices de tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`idproduto`);

--
-- Índices de tabela `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idusuario`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `adm`
--
ALTER TABLE `adm`
  MODIFY `idADM` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  MODIFY `idfornecedor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `idfuncionario` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `idproduto` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
