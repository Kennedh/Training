class Filme {
  constructor(titulo, genero, duracaoEmMinutos) {
    this.titulo = titulo;
    this.genero = genero; 
    this.duracao = duracaoEmMinutos;
  }
}

class Maratona {
  constructor() {
    this.filmes = [];
  }

  adicionarFilme(filme) {
    this.filmes.push(filme);
  }

  // ==========================================
  // DESAFIO 1: filter e map
  // ==========================================
  obterTitulosPorGenero(generoBuscado) {
    // TODO:
    // 1. Filtre os filmes que tenham o gênero igual ao 'generoBuscado'.
    // 2. Mapeie para retornar APENAS os títulos desses filmes.
    return this.filmes.filter(filme => filme.genero === generoBuscado).map(filme => filme.titulo)
  }

  // ==========================================
  // DESAFIO 2: reduce
  // ==========================================
  calcularTempoTotal() {
    // TODO:
    // 1. Some a 'duracao' de todos os filmes na lista e retorne o total.
    return this.filmes.reduce((total, filme) => total + filme.duracao,0)
  }
  // ==========================================
  // DESAFIO 3: find
  // ==========================================
  buscarFilmePorTitulo(tituloBuscado) {
    // TODO:
    // Use o .find() na lista de filmes para encontrar e retornar o objeto do filme 
    // que tenha o 'titulo' exatamente igual ao 'tituloBuscado'.
    return this.filmes.find((filme) => filme.titulo === tituloBuscado)
  }
  // ==========================================
  // DESAFIO 4: some
  // ==========================================
  temFilmeLongo(tempoMinimo) {
    // TODO:
    // Use o .some() para verificar se existe ALGUM filme na lista
    // que tenha a 'duracao' maior ou igual ao 'tempoMinimo'. 
    // Ele já vai retornar true ou false automaticamente!
    return this.filmes.some(filme => filme.duracao >= tempoMinimo)
  }
  // ==========================================
  // DESAFIO 5: every
  // ==========================================
  todosSaoCurtos(tempoMaximo) {
    // TODO:
    // Use o .every() para verificar se TODOS os filmes na lista
    // têm a 'duracao' menor ou igual ao 'tempoMaximo'.
    return this.filmes.every(filme => filme.duracao <= tempoMaximo)
  }
  // ==========================================
  // DESAFIO 6: O "Combo" 
  // ==========================================
  calcularTempoPorGenero(generoBuscado) {
    // TODO:
    // 1. Isole apenas os filmes que correspondam ao 'generoBuscado'.
    // 2. Some a duração de todos os filmes que sobraram nessa lista filtrada.
    // Dica: Você pode encadear dois métodos que já usou antes!
    return this.filmes.filter(filme => filme.genero === generoBuscado).reduce((total, filme) => total + filme.duracao,0)
  }
}

// ---------------------------------------------------------
// 🧪 ÁREA DE TESTES
// ---------------------------------------------------------
const minhaMaratona = new Maratona();
minhaMaratona.adicionarFilme(new Filme("Senhor dos Anéis", "Fantasia", 180));
minhaMaratona.adicionarFilme(new Filme("Matrix", "Ficção Científica", 136));
minhaMaratona.adicionarFilme(new Filme("O Hobbit", "Fantasia", 169));
minhaMaratona.adicionarFilme(new Filme("Shrek", "Animação", 90));

console.log("Filmes de Fantasia:", minhaMaratona.obterTitulosPorGenero("Fantasia"));
// Esperado: [ 'Senhor dos Anéis', 'O Hobbit' ]

console.log("Tempo total da maratona (minutos):", minhaMaratona.calcularTempoTotal());
// Esperado: 575

console.log(minhaMaratona.buscarFilmePorTitulo("Shrek"))
// Esperado: { titulo: 'Shrek', genero: 'Animação', duracao: 90 }

console.log(minhaMaratona.temFilmeLongo(150))
// Esperado: True

console.log(minhaMaratona.todosSaoCurtos(200))
// Esperado: True

console.log(minhaMaratona.todosSaoCurtos(150))
// Esperado: False

console.log("Tempo total de Fantasia:", minhaMaratona.calcularTempoPorGenero("Fantasia"));
// Esperado: 349 (pois Senhor dos Anéis tem 180 e O Hobbit tem 169)