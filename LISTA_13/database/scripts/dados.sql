-- Cria a tabela 'usuarios' se ela não existir
CREATE TABLE IF NOT  EXISTS usuarios (
    id_usuario   INTEGER PRIMARY KEY,
    -- nome: não deixar vazio e nome unico
    username    TEXT NOT NULL UNIQUE CHECK(length(username) > 0),
    -- senha
    password    TEXT NOT NULL
);

-- Cria a tabela "post" se não existe e faz relação com id da tabela usuarios
CREATE TABLE IF NOT  EXISTS post (
    id_post     INTEGER PRIMARY KEY,
    titulo      TEXT NOT NULL,
    conteudo    TEXT NOT NULL,
    id_usuario  INTEGER NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);