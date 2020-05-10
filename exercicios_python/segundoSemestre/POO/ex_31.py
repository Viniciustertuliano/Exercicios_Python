class Disciplina:
    def __init__(self, nome):
        self.nome = nome


class Pessoa:
    def __init__(self, nome, endereco, fone, cpf):
        self.nome = nome
        self.endereco = endereco
        self.fone = fone
        self.cpf = cpf


class Aluno(Pessoa):
    def __init__(self, nome, endereco, fone, cpf):
        super().__init__(nome, endereco, fone, cpf)
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Funcionario(Pessoa):
    def __init__(self, nome, endereco, fone, cpf, salario):
        super().__init__(nome, endereco, fone, cpf)
        self.salario = salario


class Professor(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, titulacao):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.titulacao = titulacao
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Tecnico(Funcionario):
    def __init__(self, nome, endereco, fone, cpf, salario, cargo):
        super().__init__(nome, endereco, fone, cpf, salario)
        self.cargo = cargo


disc = Disciplina("Programação")
prof = Professor("Joao", "rua...", "11999999", "9999999", 2000, "mestrado")

alu = Aluno("Maria", "rua...", "1188888", "555555")
tec = Tecnico("Pedro", "rua...", "11333333", "8787887", 1500, "Tecnico")

alu.incluir_disciplina(disc)
prof.incluir_disciplina(disc)
