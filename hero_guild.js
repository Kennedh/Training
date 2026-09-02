class Prato {
  constructor(nome, categoria, preco) {
    this.nome = nome;
    this.categoria = categoria; // Ex: 'Entrada', 'Prato Principal', 'Sobremesa'
    this.preco = preco;
  }
}

class Cardapio {
  constructor() {
    this.pratos = []; // Array que guarda os objetos da classe Prato
  }

  adicionarPrato(prato) {
    this.pratos.push(prato);
  }

  // DESAFIO 1: Combinar filter e map (Tente encadear!)
  obterNomesPorCategoria(categoriaBuscada) {
    // 1. Filtre os pratos que pertencem à 'categoriaBuscada'
    // 2. Mapeie para retornar APENAS os nomes desses pratos
    const pratosFiltrados = this.pratos.filter(prato => prato.categoria === categoriaBuscada);
    return pratosFiltrados.map(pratos => pratos.nome);
  }

  // DESAFIO 2: Usar o reduce
  calcularCustoDoMenuCompleto() {
    // 1. Some o 'preco' de todos os pratos no cardápio e retorne o valor total
    return this.pratos.reduce((acc,item) => acc + item.preco,0)
  }
}

// Criando nossos pratos e o cardápio para testar:
const meuCardapio = new Cardapio();
meuCardapio.adicionarPrato(new Prato("Salada Caesar", "Entrada", 25));
meuCardapio.adicionarPrato(new Prato("Bife Ancho", "Prato Principal", 85));
meuCardapio.adicionarPrato(new Prato("Pudim", "Sobremesa", 15));
meuCardapio.adicionarPrato(new Prato("Lasanha", "Prato Principal", 55));

console.log(meuCardapio.obterNomesPorCategoria("Prato Principal"));
console.log(meuCardapio.calcularCustoDoMenuCompleto());