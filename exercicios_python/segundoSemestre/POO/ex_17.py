class Aluno():
    def __init__(self):
        self.nome = ''
        self.tempo_sem_dormir = 0

    def estudar(self, horas):
        h = horas
        self.tempo_sem_dormir += h
        return self.tempo_sem_dormir

    def dormir(self, horas):
        h = horas
        self.tempo_sem_dormir -= h
        return self.tempo_sem_dormir
