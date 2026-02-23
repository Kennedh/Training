"""
Você deve criar uma classe ou um conjunto de funções que simule o comportamento de abas de um navegador. O objetivo é
gerenciar para qual URL o usuário vai quando clica em "Voltar" ou "Avançar".

Requisitos:
Visitar página: Adiciona uma nova URL ao histórico. Quando uma nova página é visitada, o histórico de "Avançar" deve
ser limpo.

Voltar (Back): Move o usuário para a página anterior.

Avançar (Forward): Move o usuário para a página que estava à frente (se ele tiver voltado anteriormente).
"""

class Navegador:
    def __init__(self):
        self.historico = []
        self.futuro = []
        self.pagina_atual = []

    def visitar(self, url):
        if self.pagina_atual:
            self.historico.append(self.pagina_atual)
        self.pagina_atual = url
        print(f"Pagina Atual: {self.pagina_atual}")
        self.futuro.clear()

    def voltar(self):
        if not self.historico:
            print("Você não acessou nenhuma pagina antes dessa!")
        else:
            self.futuro.append(self.pagina_atual)
            self.pagina_atual = self.historico.pop()
            print(f"Pagina Atual: {self.pagina_atual}")

    def avancar(self):
        if not self.futuro:
            print("Não tem pagina para avançar")
        else:
            self.historico.append(self.pagina_atual)
            self.pagina_atual = self.futuro.pop()
            print(f"Pagina Atual: {self.pagina_atual}")


# Teste

nav = Navegador()
nav.visitar("google.com")
nav.visitar("python.org")
nav.voltar() #Retorna para "google.com"
nav.avancar() # Retorna para "python.org"