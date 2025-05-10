CREATE TABLE usuarios (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nome, email) VALUES
  ('João Silva', 'joao@exemplo.com'),
  ('Maria Souza', 'maria@exemplo.com'),
  ('Carlos Pereira', 'carlos@exemplo.com');
