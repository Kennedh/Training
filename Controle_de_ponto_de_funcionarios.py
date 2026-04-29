"""
📌 Sistema de Controle de Ponto dos Funcionários
Sistema inteligente para registro de ponto com múltiplas entradas/saídas
"""

from datetime import date, datetime, timedelta
import time
import os


class ControlePonto:
    def __init__(self):
        self.pontos = []
        self.nome_funcionario = ""
        self.data_atual = date.today()
        self.status_atual = "fora"  # "dentro" ou "fora"
        
    def limpar_tela(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exibir_cabecalho(self):
        """Exibe cabeçalho do sistema"""
        self.limpar_tela()
        print("=" * 50)
        print("🏢 SISTEMA DE CONTROLE DE PONTO".center(50))
        print("=" * 50)
        if self.nome_funcionario:
            print(f"👤 Funcionário: {self.nome_funcionario}")
            print(f"📅 Data: {self.data_atual.strftime('%d/%m/%Y')}")
            print(f"🔵 Status: {'🟢 Trabalhando' if self.status_atual == 'dentro' else '⚪ Fora do expediente'}")
        print("=" * 50)
    
    def configurar_funcionario(self):
        """Solicita o nome do funcionário"""
        self.exibir_cabecalho()
        print("\n📝 PRIMEIRO ACESSO - CONFIGURAÇÃO\n")
        self.nome_funcionario = input("Nome do funcionário: ").strip().title()
        
        while not self.nome_funcionario:
            print("❌ Nome não pode estar vazio!")
            self.nome_funcionario = input("Nome do funcionário: ").strip().title()
        
        print(f"\n✅ Bem-vindo(a), {self.nome_funcionario}!")
        time.sleep(1.5)
    
    def registrar_entrada(self):
        """Registra entrada do funcionário"""
        if not self.nome_funcionario:
            self.configurar_funcionario()
        
        self.exibir_cabecalho()
        
        if self.status_atual == "dentro":
            print("\n❌ Você já está registrado como 'dentro'!")
            print("💡 Primeiro registre a saída antes de uma nova entrada.")
            time.sleep(2)
            return
        
        hora_atual = datetime.now()
        self.pontos.append({
            'tipo': 'entrada',
            'hora': hora_atual,
            'data': hora_atual.date()
        })
        
        self.status_atual = "dentro"
        
        print(f"\n✅ ENTRADA REGISTRADA COM SUCESSO!")
        print(f"🕐 Horário: {hora_atual.strftime('%H:%M:%S')}")
        
        # Verifica se é horário de almoço ou normal
        if 11 <= hora_atual.hour < 14:
            print("🍽️  Registro de entrada após almoço")
        elif hora_atual.hour < 8:
            print("🌅 Entrada antecipada")
        elif hora_atual.hour > 9:
            print("⚠️  Atenção: Entrada após horário normal")
        
        time.sleep(2)
    
    def registrar_saida(self):
        """Registra saída do funcionário"""
        if not self.pontos:
            self.exibir_cabecalho()
            print("\n❌ Não há registros de entrada para hoje!")
            print("💡 Registre uma entrada primeiro.")
            time.sleep(2)
            return
        
        if self.status_atual == "fora":
            self.exibir_cabecalho()
            print("\n❌ Você já está registrado como 'fora'!")
            print("💡 Primeiro registre a entrada antes de uma nova saída.")
            time.sleep(2)
            return
        
        hora_atual = datetime.now()
        self.pontos.append({
            'tipo': 'saida',
            'hora': hora_atual,
            'data': hora_atual.date()
        })
        
        self.status_atual = "fora"
        
        self.exibir_cabecalho()
        print(f"\n✅ SAÍDA REGISTRADA COM SUCESSO!")
        print(f"🕐 Horário: {hora_atual.strftime('%H:%M:%S')}")
        
        # Calcula tempo da última jornada
        if len(self.pontos) >= 2:
            ultima_entrada = None
            for p in reversed(self.pontos[:-1]):
                if p['tipo'] == 'entrada':
                    ultima_entrada = p['hora']
                    break
            
            if ultima_entrada:
                duracao = hora_atual - ultima_entrada
                print(f"⏱️  Duração desta jornada: {str(duracao).split('.')[0]}")
        
        time.sleep(2)
    
    def calcular_horas_trabalhadas(self):
        """Calcula o total de horas trabalhadas"""
        total_horas = timedelta()
        entrada = None
        
        for ponto in self.pontos:
            if ponto['tipo'] == 'entrada':
                entrada = ponto['hora']
            elif ponto['tipo'] == 'saida' and entrada:
                total_horas += ponto['hora'] - entrada
                entrada = None
        
        return total_horas
    
    def exibir_resumo_dia(self):
        """Exibe resumo detalhado do dia"""
        self.exibir_cabecalho()
        
        if not self.pontos:
            print("\n📊 Nenhum registro de ponto para hoje!")
            time.sleep(2)
            return
        
        print("\n📊 RESUMO DO DIA\n")
        print("📋 Registros detalhados:")
        print("-" * 50)
        
        for i, ponto in enumerate(self.pontos, 1):
            icone = "🟢" if ponto['tipo'] == 'entrada' else "🔴"
            print(f"{icone} {i:02d}. {ponto['tipo'].upper():8} - {ponto['hora'].strftime('%H:%M:%S')}")
        
        print("-" * 50)
        
        # Cálculo de horas
        total_horas = self.calcular_horas_trabalhadas()
        
        print(f"\n⏱️  TOTAL DE HORAS TRABALHADAS: {str(total_horas).split('.')[0]}")
        
        # Informações adicionais
        num_registros = len(self.pontos)
        if num_registros % 2 != 0:
            print("\n⚠️  Atenção: Número ímpar de registros. Pode haver registros pendentes!")
        
        if total_horas > timedelta(hours=8):
            horas_extras = total_horas - timedelta(hours=8)
            print(f"🕐 Horas extras: +{str(horas_extras).split('.')[0]}")
        elif total_horas < timedelta(hours=8) and num_registros >= 2:
            horas_faltantes = timedelta(hours=8) - total_horas
            print(f"⏰ Horas faltantes: -{str(horas_faltantes).split('.')[0]}")
        
        # Status atual
        print(f"\n📌 Status atual: {'🟢 Trabalhando' if self.status_atual == 'dentro' else '⚪ Fora do expediente'}")
        
        input("\nPressione ENTER para continuar...")
    
    def menu_principal(self):
        """Menu principal do sistema"""
        if not self.nome_funcionario:
            self.configurar_funcionario()
        
        while True:
            self.exibir_cabecalho()
            
            print("\n📋 MENU PRINCIPAL")
            print("=" * 50)
            print("[1] 🟢 Registrar Entrada")
            print("[2] 🔴 Registrar Saída")
            print("[3] 📊 Exibir Resumo do Dia")
            print("[4] 🧹 Limpar Registros do Dia")
            print("[5] 👤 Trocar Funcionário")
            print("[6] 🚪 Sair")
            print("=" * 50)
            
            opcao = input("\n👉 Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.registrar_entrada()
            elif opcao == "2":
                self.registrar_saida()
            elif opcao == "3":
                self.exibir_resumo_dia()
            elif opcao == "4":
                self.limpar_registros()
            elif opcao == "5":
                self.trocar_funcionario()
            elif opcao == "6":
                self.sair()
                break
            else:
                print("\n❌ Opção inválida! Tente novamente.")
                time.sleep(1)
    
    def limpar_registros(self):
        """Limpa todos os registros do dia"""
        self.exibir_cabecalho()
        print("\n⚠️  TEM CERTEZA QUE DESEJA LIMPAR TODOS OS REGISTROS?")
        confirmacao = input("Digite 'SIM' para confirmar: ").strip().upper()
        
        if confirmacao == "SIM":
            self.pontos = []
            self.status_atual = "fora"
            print("\n✅ Registros limpos com sucesso!")
        else:
            print("\n❌ Operação cancelada.")
        
        time.sleep(1.5)
    
    def trocar_funcionario(self):
        """Troca o funcionário atual"""
        self.exibir_cabecalho()
        print("\n👥 TROCAR FUNCIONÁRIO\n")
        
        if self.pontos:
            print("⚠️  Existem registros não finalizados!")
            resposta = input("Deseja continuar mesmo assim? (S/N): ").strip().upper()
            if resposta != 'S':
                print("\n❌ Troca cancelada.")
                time.sleep(1)
                return
        
        self.nome_funcionario = ""
        self.pontos = []
        self.status_atual = "fora"
        self.configurar_funcionario()
    
    def sair(self):
        """Finaliza o sistema"""
        self.exibir_cabecalho()
        
        if self.pontos and self.status_atual == "dentro":
            print("\n⚠️  ATENÇÃO: Você está com a entrada registrada!")
            print("Recomenda-se registrar a saída antes de encerrar.")
            resposta = input("\nDeseja registrar saída agora? (S/N): ").strip().upper()
            
            if resposta == 'S':
                self.registrar_saida()
        
        print(f"\n👋 Até logo, {self.nome_funcionario}!")
        print("Sistema encerrado.")
        time.sleep(1)


if __name__ == "__main__":
    sistema = ControlePonto()
    sistema.menu_principal()