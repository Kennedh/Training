class Missao {
  constructor(nome, dificuldade, recompensa, status) {
    this.nome = nome;
    this.dificuldade = dificuldade; // Ex: 'Fácil', 'Média', 'Difícil'
    this.recompensa = recompensa; // Valor em moedas galácticas
    this.status = status; // 'Pendente' ou 'Concluída'
  }
}

class NaveExploradora {
  constructor(nome) {
    this.nome = nome;
    this.missoes = []; // Array de objetos da classe Missao
  }

  adicionarMissao(missao) {
    this.missoes.push(missao);
  }

  // DESAFIO 1: filter, map e encadeamento
  obterNomesDasMissoesConcluidasDificeis() {
    // 1. Filtre as missões que tenham status "Concluída" E dificuldade "Difícil".
    // 2. Mapeie para retornar apenas o 'nome' da missão.
    // Dica: Tente usar desestruturação nos parâmetros!
    
    return 
  }

  // DESAFIO 2: filter e reduce
  calcularTotalDeRecompensasPendentes() {
     // 1. Filtre as missões com status 'Pendente'.
     // 2. Use o reduce para somar a 'recompensa' de todas elas e retorne o total.
  }

  // DESAFIO 3: Async/Await, try/catch, e throw
  async transmitirRelatorio(apiExterna) {
    // 1. Se o array this.missoes estiver vazio (length === 0), lance um erro: throw new Error("Sem missões")
    // 2. Use um try/catch.
    // 3. No try, aguarde (await) a promessa: apiExterna.enviar(this.missoes) e retorne o resultado.
    // 4. No catch, retorne a mensagem de erro capturada.
  }
}

// ---------------------------------------------------------
// 🧪 ÁREA DE TESTES (Não precisa alterar)
// ---------------------------------------------------------
const minhaNave = new NaveExploradora("Apollo");
minhaNave.adicionarMissao(new Missao("Mapear Marte", "Média", 500, "Concluída"));
minhaNave.adicionarMissao(new Missao("Resgate em Júpiter", "Difícil", 2000, "Concluída"));
minhaNave.adicionarMissao(new Missao("Coletar Minérios", "Fácil", 300, "Pendente"));
minhaNave.adicionarMissao(new Missao("Explorar Buraco Negro", "Difícil", 5000, "Pendente"));

console.log("Desafio 1:", minhaNave.obterNomesDasMissoesConcluidasDificeis()); 
// Esperado: [ 'Resgate em Júpiter' ]

console.log("Desafio 2:", minhaNave.calcularTotalDeRecompensasPendentes()); 
// Esperado: 5300 (300 + 5000)

// Simulador de API para o Desafio 3
const apiSimulada = {
  enviar: async (dados) => "Relatório transmitido com sucesso!"
};
minhaNave.transmitirRelatorio(apiSimulada).then(console.log);
// Esperado: "Relatório transmitido com sucesso!"