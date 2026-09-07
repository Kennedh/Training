class Heroi {
  constructor(nome, vocacao, nivel) {
    this.nome = nome;
    this.vocacao = vocacao; // Ex: 'Mago', 'Guerreiro', 'Arqueiro'
    this.nivel = nivel;
  }
}

class Guilda {
  constructor() {
    this.membros = []; // Um array que vai guardar os objetos da classe Heroi
  }

  recrutar(heroi) {
    this.membros.push(heroi);
  }

  // DESAFIO 1: Combinar filter e map
  obterNomesPorVocacao(vocacaoBuscada) {
    // Aqui nós queremos:
    // 1. Filtrar os membros que têm a mesma vocação que a 'vocacaoBuscada'
    // 2. Mapear esse resultado para devolver APENAS os nomes desses heróis
    const res = this.membros.filter(membro => membro.vocacao === vocacaoBuscada)
    return res.map(resultado => resultado.nome)
  }

  // DESAFIO 2: Usar o reduce
  calcularPoderTotal() {
    // Aqui nós queremos:
    // 1. Somar o 'nivel' de todos os membros da guilda e retornar o total
    return this.membros.reduce((acc, item) => acc + item.nivel, 0);
  }
}

// Criando nossos heróis e a guilda para testar depois:
const guilda = new Guilda();
guilda.recrutar(new Heroi("Gandalf", "Mago", 100));
guilda.recrutar(new Heroi("Aragorn", "Guerreiro", 85));
guilda.recrutar(new Heroi("Merlin", "Mago", 120));

console.log(guilda.calcularPoderTotal())
console.log(guilda.obterNomesPorVocacao("Mago"))