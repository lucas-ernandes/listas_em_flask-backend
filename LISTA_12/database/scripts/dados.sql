CREATE TABLE IF NOT EXISTS departamentos(
    numero      INTEGER PRIMARY KEY,
    descricao   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS professor(
    matricula   INTEGER PRIMARY KEY,
    nome   TEXT NOT NULL,
    titulacao TEXT NOT NULL CHECK(
        titulacao IN ('Doutor', 'Mestre', 'Especialista')
    )
);