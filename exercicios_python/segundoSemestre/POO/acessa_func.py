import ex_16

func = ex_16.Funcionario()
func.nome = input('Digite seu nome ')
func.salario = int(input('Digite seu salario '))
poc = float(input('Digite a porcentaem de almento salarial '))
func.aumenta_salario(poc)
