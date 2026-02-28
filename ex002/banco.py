import sqlite3

def criar_conexao():
    conn = sqlite3.connect("loja.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def criar_tabelas(conn):
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Produto (
        id TEXT PRIMARY KEY,
        categoria TEXT NOT NULL,
        nome TEXT NOT NULL,
        quantidade_estoque INTEGER NOT NULL,
        valor REAL NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Vendas (
        id TEXT PRIMARY KEY,
        cliente_id TEXT NOT NULL,
        data TEXT NOT NULL,
        forma_pagamento TEXT NOT NULL,
        status TEXT,
        valor_total REAL,
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
    );

    CREATE TABLE IF NOT EXISTS Itens_Venda (
        id TEXT PRIMARY KEY,
        venda_id TEXT NOT NULL,
        produto_id TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor_unitario REAL NOT NULL,
        FOREIGN KEY (venda_id) REFERENCES Vendas(id),
        FOREIGN KEY (produto_id) REFERENCES Produto(id)
    );
    """)

    conn.commit()
