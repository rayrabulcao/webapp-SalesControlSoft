CREATE SCHEMA [bs]
GO

CREATE TABLE bs.Etapa (
  id INT IDENTITY(1,1) PRIMARY KEY,
  descricao VARCHAR(100) NOT NULL UNIQUE,
  status BIT NULL DEFAULT 0
);

CREATE TABLE bs.Instrucao (
  id INT IDENTITY (1,1) PRIMARY KEY,
  id_etapa INT,
  id_codigo_bios INT,
  posicao INT,
  descricao VARCHAR(100),
  FOREIGN KEY (id_etapa) REFERENCES bs.Etapa (id),
  FOREIGN KEY (id_codigo_bios) REFERENCES dbo.Codigo_BIOS (id)
);

CREATE TABLE bs.Configuracao (
  id INT IDENTITY (1,1) PRIMARY KEY,
  id_placa_mae INT,
  id_etapa INT,
  id_codigo_bios INT,
  descricao_instrucao VARCHAR(100),
  feedback_por varchar(2),
  sensor_de INT,
  sensor_ate INT,
  tempo FLOAT,
  posicao INT,
  bloqueado BIT NULL DEFAULT 0,
  tipo INT,
  color INT,
  FOREIGN KEY (id_placa_mae) REFERENCES dbo.Placa_Mae (id),
  FOREIGN KEY (id_etapa) REFERENCES bs.Etapa (id),
  FOREIGN KEY (id_codigo_bios) REFERENCES dbo.Codigo_BIOS (id)
);

CREATE TABLE bs.Comando (
  id INT IDENTITY (1,1) PRIMARY KEY,
  id_configuracao INT,
  nome_tecla VARCHAR (50),
  codigo_tecla VARCHAR(50),
  posicao INT,
  FOREIGN KEY (id_configuracao) REFERENCES bs.Configuracao (id) on DELETE CASCADE
);

CREATE TABLE bs.Configuracao_op (
  id INT IDENTITY (1,1) PRIMARY KEY,
  id_placa_mae INT,
  id_etapa INT,
  id_codigo_bios INT,
  op varchar(200),
  descricao_instrucao VARCHAR(100),
  feedback_por varchar(2),
  sensor_de INT,
  sensor_ate INT,
  tempo FLOAT,
  posicao INT,
  bloqueado BIT NULL DEFAULT 0,
  tipo INT,
  color INT,
  FOREIGN KEY (id_placa_mae) REFERENCES dbo.Placa_Mae (id),
  FOREIGN KEY (id_etapa) REFERENCES bs.Etapa (id),
  FOREIGN KEY (id_codigo_bios) REFERENCES dbo.Codigo_BIOS (id)
);

CREATE TABLE bs.Comando_op (
  id INT IDENTITY (1,1) PRIMARY KEY,
  id_configuracao_op INT,
  nome_tecla VARCHAR (50),
  codigo_tecla VARCHAR(50),
  posicao INT,
  FOREIGN KEY (id_configuracao_op) REFERENCES bs.Configuracao_op (id) on DELETE CASCADE
);

CREATE TABLE bs.usuario (
  id INT IDENTITY (1,1) PRIMARY KEY,
  nome VARCHAR(30),
  login VARCHAR(20),
  password VARCHAR(20),
  admin BIT NULL DEFAULT 0,
);

ALTER SCHEMA bs TRANSFER dbo.Comando;