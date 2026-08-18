/**
 * TREINO DE SEGUNDA (17/08/2026)
 * A Santíssima Trindade: .map(), .filter() e .reduce()
 */

// -----------------------------------------------------------------------------
// 1. .map() -> TRANSFORMAÇÃO (Formatando Tickets de Suporte)
// O .map() passa por cada item do array e devolve um NOVO array com os itens modificados.
// -----------------------------------------------------------------------------
export function formatarTicketsERP(chamados) {
  // TODO: 'chamados' é um array de objetos: { id: 1042, cliente: "Fazenda Sol", erro: "Falha no SQL" }
  // Use o .map() para transformar cada objeto em uma string formatada.
  // Retorne um novo array de strings no formato: "[TICKET 1042] Fazenda Sol: Falha no SQL"
  return chamados.map(({ id, cliente, erro }) => `[TICKET ${id}] ${cliente}: ${erro}`);
}

// -----------------------------------------------------------------------------
// 2. .filter() -> FILTRAGEM (Limpando o Inventário do Fishing Frenzy)
// O .filter() devolve um NOVO array apenas com os itens que passarem no teste (retornarem true).
// -----------------------------------------------------------------------------
export function filtrarLootValioso(pescaria) {
  // TODO: 'pescaria' é um array de objetos: { item: "Sardinha", tipo: "Peixe" } ou { item: "Bota", tipo: "Lixo" }
  // Use o .filter() para criar um novo array apenas com os itens onde o 'tipo' seja DIFERENTE (!==) de "Lixo".
  // Retorne o novo array filtrado.
  return pescaria.filter(item => item.tipo !== "Lixo");
}

// -----------------------------------------------------------------------------
// 3. .reduce() -> ACUMULAÇÃO (Calculando as Horas do 365 Days of Code)
// O .reduce() pega um array e "esmaga" ele até virar um único valor (uma soma, por exemplo).
// Sintaxe básica: array.reduce((acumulador, itemAtual) => acumulador + itemAtual.valor, 0)
// -----------------------------------------------------------------------------
export function calcularTempoDeEstudo(sessoes) {
  // TODO: 'sessoes' é um array de objetos: { dia: "Segunda", minutos: 45 }
  // Use o .reduce() para somar todos os 'minutos' das sessões.
  // Não esqueça de passar o 0 no final do reduce como valor inicial do acumulador!
  // Retorne o total de minutos.
  return sessoes.reduce((acumulador, { minutos }) => acumulador + minutos, 0);

}

// -----------------------------------------------------------------------------
// 4. O COMBO FATAL: .filter() + .map() (Analisando Logs do SYS-PULSE)
// Você pode encadear esses métodos! array.filter(...).map(...)
// -----------------------------------------------------------------------------
export function extrairProcessosCriticos(processos) {
  // TODO: 'processos' é um array: { nome: "VSCode", usoCPU: 15 }, { nome: "Chrome", usoCPU: 85 }
  // 1. Use o .filter() para pegar APENAS os processos com 'usoCPU' maior que 80.
  // 2. Logo em seguida, emende um .map() para pegar apenas o 'nome' desses processos filtrados.
  // Retorne o array final contendo apenas os nomes dos processos que estão fritando o PC.
  return processos
    .filter(({ usoCPU }) => usoCPU > 80)
    .map(({ nome }) => nome);
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

  console.log("== INICIANDO TREINO DE SEGUNDA ==\n");

  // Testes 1: map
  const ticketsRaw = [
    { id: 1042, cliente: "Fazenda Sol", erro: "Falha no SQL" },
    { id: 1043, cliente: "AgroTech", erro: "Timeout no Progress" }
  ];
  assert("formatarTicketsERP - transformando objetos em strings", 
    formatarTicketsERP(ticketsRaw), 
    ["[TICKET 1042] Fazenda Sol: Falha no SQL", "[TICKET 1043] AgroTech: Timeout no Progress"]
  );

  // Testes 2: filter
  const inventario = [
    { item: "Sardinha", tipo: "Peixe" },
    { item: "Bota Furada", tipo: "Lixo" },
    { item: "Tubarão", tipo: "Peixe" },
    { item: "Lata Velha", tipo: "Lixo" }
  ];
  assert("filtrarLootValioso - removendo o lixo", 
    filtrarLootValioso(inventario), 
    [{ item: "Sardinha", tipo: "Peixe" }, { item: "Tubarão", tipo: "Peixe" }]
  );

  // Testes 3: reduce
  const rotinaEstudos = [
    { dia: "Duolingo", minutos: 5 },
    { dia: "Exercism", minutos: 40 },
    { dia: "Leitura de Docs", minutos: 15 }
  ];
  assert("calcularTempoDeEstudo - somando todos os minutos", 
    calcularTempoDeEstudo(rotinaEstudos), 
    60
  );

  // Testes 4: combo
  const monitoramento = [
    { nome: "Sistema", usoCPU: 5 },
    { nome: "Node.js", usoCPU: 12 },
    { nome: "Compilador Rust", usoCPU: 95 },
    { nome: "Discord", usoCPU: 2 },
    { nome: "Jogo AAA pesado", usoCPU: 88 }
  ];
  assert("extrairProcessosCriticos - filtrando e mapeando", 
    extrairProcessosCriticos(monitoramento), 
    ["Compilador Rust", "Jogo AAA pesado"]
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();