-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 14/05/2025 às 02:10
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

-- Configurações iniciais do SQL
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: farmacia_sa
--

-- --------------------------------------------------------

-- Tabela de Administradores
CREATE TABLE adm (
  idADM int(11) NOT NULL,
  nome text DEFAULT NULL,
  email text DEFAULT NULL,
  CPF text DEFAULT NULL,
  senha text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

-- Tabela de Clientes (ATUALIZADA com email, telefone e cpf)
CREATE TABLE cliente (
  idcliente int(11) NOT NULL,
  nome text DEFAULT NULL,
  senha text DEFAULT NULL,
  email text DEFAULT NULL,
  telefone text DEFAULT NULL,
  cpf text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

-- Tabela de Fornecedores
CREATE TABLE fornecedor (
  idfornecedor int(11) NOT NULL,
  nome_Empresa text DEFAULT NULL,
  email text DEFAULT NULL,
  telefone text DEFAULT NULL,
  produto text DEFAULT NULL,
  transporte text DEFAULT NULL,
  inicio_contrato text DEFAULT NULL,
  final_contrato text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

-- Tabela de Funcionários
CREATE TABLE funcionario (
  idfuncionario int(11) NOT NULL,
  nome text DEFAULT NULL,
  cpf text DEFAULT NULL,
  email text DEFAULT NULL,
  telefone text DEFAULT NULL,
  funcao text DEFAULT NULL,
  quantidade_vendas text DEFAULT NULL,
  salario text DEFAULT NULL,
  inicio_contrato text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

-- Tabela de Produtos
CREATE TABLE produto (
  idproduto int(11) NOT NULL,
  nome_produto text DEFAULT NULL,
  tipo text DEFAULT NULL,
  quantidade_enviada text DEFAULT NULL,
  tempo_de_validade text DEFAULT NULL,
  data_de_fabricacao text DEFAULT NULL,
  lote text DEFAULT NULL,
  fornecedor text DEFAULT NULL,
  quantidade_em_estoque text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

-- Índices Primários
ALTER TABLE adm
  ADD PRIMARY KEY (idADM);

ALTER TABLE cliente
  ADD PRIMARY KEY (idcliente);

ALTER TABLE fornecedor
  ADD PRIMARY KEY (idfornecedor);

ALTER TABLE funcionario
  ADD PRIMARY KEY (idfuncionario);

ALTER TABLE produto
  ADD PRIMARY KEY (idproduto);

-- --------------------------------------------------------

-- Configurações AUTO_INCREMENT
ALTER TABLE adm
  MODIFY idADM int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE cliente
  MODIFY idcliente int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE fornecedor
  MODIFY idfornecedor int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE funcionario
  MODIFY idfuncionario int(11) NOT NULL AUTO_INCREMENT;

ALTER TABLE produto
  MODIFY idproduto int(11) NOT NULL AUTO_INCREMENT;

-- Finaliza a transação
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
