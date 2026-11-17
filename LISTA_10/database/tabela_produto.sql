CREATE TABLE IF NOT EXISTS produtos(
    codigo TEXT PRIMARY KEY,
    descricao TEXT NOT NULL
        CHECK (length(trim(descricao)) BETWEEN 1 AND 40),
    preco_unitario REAL NOT NULL
        CHECK (preco_unitario >= 0)
);