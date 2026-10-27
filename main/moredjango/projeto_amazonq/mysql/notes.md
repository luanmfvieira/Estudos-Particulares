#Comando realizados durante a criação do projeto


-- Criação do database e table funcionarios

create database loroantech

create table funcionarios(
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    cargo VARCHAR(50),
    salario FLOAT,
    descricao TEXT,
    data_nascimento DATE,
    data_admissao DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('ativo', 'afastado', 'desligado') DEFAULT 'ativo');


INSERT INTO funcionarios (nome, email, telefone, cargo, salario, descricao, data_nascimento, data_admissao, status)
VALUES

-- Diretor Executivo

('Luan Miguel de Freitas Vieira', 'luanmiguel.contato@loroantech.com', '+55 11 94902-2272',
 'Diretor Executivo (CEO)', 20000, 'Fundador e Diretor Executivo da LoroanTech',
 '2000-02-28', '2020-04-03', 'ativo')


-- Desenvolvedores Front-End

('Ana Souza','ana.souza@loroantech.com','+5511999999991','Desenvolvedor Front-End Júnior','3500','Responsável por manutenção e ajustes básicos no front','1999-05-12','2025-01-10','ativo'),
('Carlos Mendes','carlos.mendes@loroantech.com','+5511999999992','Desenvolvedor Front-End Pleno','6500','Desenvolvimento de interfaces responsivas e integrações','1995-08-21','2025-01-10','ativo'),
('Fernanda Lima','fernanda.lima@loroantech.com','+5511999999993','Desenvolvedor Front-End Sênior','11000','Líder técnico do time de front-end','1990-11-03','2025-01-10','ativo'),


-- Desenvolvedores Back-End

('Rafael Torres','rafael.torres@loroantech.com','+5511999999994','Desenvolvedor Back-End Júnior','3800','Auxilia em rotinas simples do servidor e banco de dados','2001-07-18','2025-01-10','ativo'),
('Juliana Castro','juliana.castro@loroantech.com','+5511999999995','Desenvolvedor Back-End Pleno','7000','Implementa APIs e integrações de sistemas','1994-03-27','2025-01-10','ativo'),
('Marcos Silva','marcos.silva@loroantech.com','+5511999999996','Desenvolvedor Back-End Sênior','12000','Arquiteto de soluções e responsável por escalabilidade','1988-09-14','2025-01-10','ativo'),


-- Cargos essenciais 

('Patrícia Gomes','patricia.gomes@loroantech.com','+5511999999997','Analista de QA','6000','Responsável por testes e qualidade de software','1993-02-05','2025-01-10','ativo'),
('Rodrigo Alves','rodrigo.alves@loroantech.com','+5511999999998','UX/UI Designer','7000','Criação de interfaces intuitivas e experiência do usuário','1996-12-20','2025-01-10','ativo'),
('Beatriz Fernandes','beatriz.fernandes@loroantech.com','+5511999999999','Tech Recruiter','5500','Responsável por recrutamento e seleção de talentos de TI','1992-06-30','2025-01-10','ativo'),
('Tiago Oliveira','tiago.oliveira@loroantech.com','+5511999999980','Gerente de Projetos','9000','Coordenação de times e cronogramas de entrega','1989-04-11','2025-01-10','ativo');
