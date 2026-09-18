class Jogo {
  constructor(nome, genero, preco) {
    this.nome = nome;
    this.genero = genero; // Ex: 'RPG', 'Ação', 'Corrida'
    this.preco = preco;
  }
}

class LojaRetro {
  constructor() {
    this.catalogo = [];
  }

  adicionarJogo(jogo) {
    this.catalogo.push(jogo);
  }

  // ==========================================
  // DESAFIO 1: filter e map (Lembre do encadeamento!)
  // ==========================================
  obterNomesPorGenero(generoBuscado) {
    // TODO:
    // 1. Filtre os jogos que tenham o gênero igual ao 'generoBuscado'.
    // 2. Mapeie para retornar APENAS os nomes desses jogos.
    return this.catalogo
      .filter(jogo => jogo.genero === generoBuscado)
      .map(jogo => jogo.nome);
  }

  // ==========================================
  // DESAFIO 2: reduce
  // ==========================================
  calcularValorDoEstoque() {
    // TODO:
    // 1. Some o 'preco' de todos os jogos no catálogo e retorne o total.
    return this.catalogo.reduce(
      (total, jogo) => total + jogo.preco,
      0
    );
  }
}

// ---------------------------------------------------------
// 🧪 ÁREA DE TESTES
// ---------------------------------------------------------
const minhaLoja = new LojaRetro();
minhaLoja.adicionarJogo(new Jogo("Super Mario World", "Ação", 120));
minhaLoja.adicionarJogo(new Jogo("Zelda: A Link to the Past", "RPG", 150));
minhaLoja.adicionarJogo(new Jogo("Top Gear", "Corrida", 90));
minhaLoja.adicionarJogo(new Jogo("Chrono Trigger", "RPG", 200));

// Descomente as linhas abaixo para testar quando terminar:
console.log("Jogos de RPG:", minhaLoja.obterNomesPorGenero("RPG"));
// Esperado: [ 'Zelda: A Link to the Past', 'Chrono Trigger' ]

console.log("Valor total do estoque:", minhaLoja.calcularValorDoEstoque());
// Esperado: 560