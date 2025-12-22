"""
Você deve criar um sistema que gerencia a ordem de atendimento de pacientes em um pronto-socorro.

Regras:
Cada paciente é uma tupla ou dicionário contendo nome e gravidade (onde 1 é leve e 5 é emergência).

Pacientes com gravidade maior devem ser atendidos primeiro.

Se dois pacientes tiverem a mesma gravidade, o critério de desempate é a ordem de chegada (quem chegou antes é atendido antes).

Exemplo de Entrada e Saída:
Chegadas: 1. ("João", 2) 2. ("Maria", 5) 3. ("José", 2)

Ordem de Atendimento (Saída):

Maria (Gravidade 5)

João (Gravidade 2, chegou primeiro que José)

José (Gravidade 2)
"""

fila_hospital = []

def adicionar_paciente(nome, gravidade):
    pass

def atender_proximo():
    if not fila_hospital:
        return "Nenhum paciente na fila."
    pass

# Teste
adicionar_paciente("Tiago", 2)
adicionar_paciente("Ana", 4)
adicionar_paciente("Beto", 4)
adicionar_paciente("Carlos", 1)

print(atender_proximo()) # Deve ser Ana
print(atender_proximo()) # Deve ser Beto (mesma prioridade, mas chegou depois)