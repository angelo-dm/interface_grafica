CREATE DATABASE IF NOT EXISTS cadastro;
USE cadastro;

CREATE TABLE IF NOT EXISTS visitantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    documento VARCHAR(12),
    motivo VARCHAR(255),
    data_visita DATE
);