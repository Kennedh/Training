/**
 * TREINO DE QUINTA (27/08/2026) - A Guilda dos Aventureiros 🏰
 * Classes, Herança e Manipulação Avançada de Objetos
 */

// -----------------------------------------------------------------------------
// 1. CLASSES E CONSTRUTORES
// -----------------------------------------------------------------------------
export class Aventureiro {
  // TODO: 
  // 1. Crie um 'constructor' que receba 'nome' e 'raca', e salve-os no 'this'.
  // 2. Crie um método chamado 'saudar()' que retorne a string: "Olá, sou [nome], um [raca]!"
  constructor(nome, raca) {
    this.nome = nome;
    this.raca = raca;
  }

  saudar() {
    return `Olá, sou ${this.nome}, um ${this.raca}!`;
  }
}

// -----------------------------------------------------------------------------
// 2. HERANÇA (extends e super)
// -----------------------------------------------------------------------------
export class Guerreiro extends Aventureiro {
  // TODO: 'Guerreiro' herda de 'Aventureiro'.
  // 1. Crie um 'constructor' que receba 'nome', 'raca' e 'arma'.
  // 2. Use o 'super()' para passar 'nome' e 'raca' para a classe pai.
  // 3. Salve a 'arma' no 'this'.
  // 4. Crie um método 'atacar()' que retorne a string: "[nome] atacou com [arma]!"
  constructor(nome, raca, arma) {
    super(nome, raca);
    this.arma = arma;
  }

  atacar() {
    return `${this.nome} atacou com ${this.arma}!`;
  }
}

// -----------------------------------------------------------------------------
// 3. MANIPULAÇÃO AVANÇADA DE OBJETOS (Object.values)
// -----------------------------------------------------------------------------
export function calcularPoderDaGuilda(membros) {
  // TODO: 'membros' é um objeto literal, ex: { "Arthur": 10, "Kael": 15, "Elara": 20 }
  // 1. Use Object.values(membros) para transformar o objeto em um array apenas com os níveis: [10, 15, 20].
  // 2. Use o .reduce() (que você dominou na segunda-feira!) para somar e retornar esse poder total.
  const niveis = Object.values(membros);
  return niveis.reduce((total, nivel) => total + nivel, 0);
}


// =============================================================================
// 🧪 ÁREA DE TESTES (NÃO PRECISA ALTERAR NADA DAQUI PARA BAIXO)
// =============================================================================

function runTests() {
  let passados = 0;
  let falhados = 0;

  function assert(nome, recebido, esperado) {
    const recStr = JSON.stringify(recebido);
    const espStr = JSON.stringify(esperado);
    if (recStr === espStr) {
      console.log(`✅ PASSOU: ${nome}`);
      passados++;
    } else {
      console.log(`❌ FALHOU: ${nome}`);
      console.log(`   Esperado: ${espStr}`);
      console.log(`   Recebido: ${recStr}`);
      falhados++;
    }
  }

  console.log("== INICIANDO TREINO DE QUINTA ==\n");

  // Testes 1: Classes
  const heroi = new Aventureiro("Gimli", "Anão");
  assert("Classe Aventureiro - Propriedades", { nome: heroi.nome, raca: heroi.raca }, { nome: "Gimli", raca: "Anão" });
  assert("Classe Aventureiro - Método saudar", heroi.saudar(), "Olá, sou Gimli, um Anão!");

  // Testes 2: Herança
  const cavaleiro = new Guerreiro("Arthur", "Humano", "Excalibur");
  assert("Classe Guerreiro - Herança de propriedades", cavaleiro.raca, "Humano");
  assert("Classe Guerreiro - Método herdado", cavaleiro.saudar(), "Olá, sou Arthur, um Humano!");
  assert("Classe Guerreiro - Método próprio", cavaleiro.atacar(), "Arthur atacou com Excalibur!");

  // Testes 3: Object.values
  const guilda = {
    "Ragnar": 30,
    "Lagertha": 25,
    "Floki": 20
  };
  assert("calcularPoderDaGuilda - Somando valores de um objeto", calcularPoderDaGuilda(guilda), 75);

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();