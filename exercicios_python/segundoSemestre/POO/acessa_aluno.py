import ex_17

aluno1 = ex_17.Aluno()
aluno1.nome = "Luizinho"
aluno1.estudar(3)
aluno1.dormir(2)
aluno1.estudar(4)
aluno1.dormir(2)
print('O aluno', aluno1.nome, 'está a',
      aluno1.tempo_sem_dormir, 'horas sem dormir')
