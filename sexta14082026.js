/**
 * TREINO DE SEXTA: O SEXTOU! 🍔🎮
 * Fechando a semana com Destructuring, Rest, Spread, ?., ?? e Dicionários
 */

// -----------------------------------------------------------------------------
// 1. Destructuring + Rest (Preparando o Setup)
// -----------------------------------------------------------------------------
export function prepararSetupSexta(setup) {
  // TODO: O objeto 'setup' possui { jogo, bebida, monitor, teclado, mouse }.
  // Extraia 'jogo' e 'bebida' usando desestruturação.
  // Guarde o resto no operador Rest chamado 'perifericos'.
  // Retorne um array no formato exato: [`Sextou com ${jogo} e ${bebida}`, perifericos]
  const {jogo, bebida, ...perifericos} = setup
  return [`Sextou com ${jogo} e ${bebida}`, perifericos]
}

// -----------------------------------------------------------------------------
// 2. Spread Operator (Roteiro do Fim de Semana)
// -----------------------------------------------------------------------------
export function organizarFimDeSemana(rolesSexta, rolesSabado) {
  // TODO: Use o Spread Operator (...) para juntar os arrays 'rolesSexta' e 'rolesSabado'.
  // Adicione a string "Descansar com a Pandora" no FINAL da nova lista.
  // Retorne o novo array completo.
  return [...rolesSexta, ...rolesSabado, "Descansar com a Pandora"]
}

// -----------------------------------------------------------------------------
// 3. Optional Chaining (?.) e Nullish Coalescing (??) (Voltando pra casa)
// -----------------------------------------------------------------------------
export function checarCarona(viagem) {
  // TODO: Retorne a categoria da corrida de aplicativo.
  // O caminho no objeto deveria ser: viagem.aplicativo.categoria
  // Use o Encadeamento Opcional (?.) para evitar erros se o app estiver fora do ar ou sem viagem.
  // Se for nulo ou indefinido, use a Coalescência Nula (??) para retornar a string "Ir a pé".
  return viagem?.aplicativo?.categoria ?? "Ir a pé"
}

// -----------------------------------------------------------------------------
// 4. Dicionários + Loops (Calculando o Gasto do Rolê)
// -----------------------------------------------------------------------------
const TABELA_PRECOS_SEXTA = {
  'Brutal_Burguer': 45,
  'GNC_Cinemas': 35,
  'Uber_X': 15,
  'Pipoca': 20
};

export function calcularGastoSextou(despesas) {
  // TODO: 'despesas' é um array de strings, ex: ['Brutal_Burguer', 'Uber_X'].
  // Use for...of para iterar sobre a lista.
  // Some o valor usando o dicionário TABELA_PRECOS_SEXTA (use o fallback || 0 para imprevistos).
  // Retorne o custo total da noite.
  let total = 0
  for(const despesa of despesas){
    total += TABELA_PRECOS_SEXTA[despesa] || 0
  }
  return total
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

  console.log("== INICIANDO TREINO DE SEXTA ==\n");

  // Testes 1
  assert("prepararSetupSexta - separando o que importa", 
    prepararSetupSexta({ jogo: "Apeiron", bebida: "Café", monitor: "144hz", teclado: "Mecânico", mouse: "Gamer" }), 
    ["Sextou com Apeiron e Café", { monitor: "144hz", teclado: "Mecânico", mouse: "Gamer" }]
  );

  // Testes 2
  assert("organizarFimDeSemana - unindo os rolês", 
    organizarFimDeSemana(["Godó Pizza"], ["Praia em Balneário Esplanada"]), 
    ["Godó Pizza", "Praia em Balneário Esplanada", "Descansar com a Pandora"]
  );

  // Testes 3
  assert("checarCarona - com uber chamado", 
    checarCarona({ destino: "Casa", aplicativo: { nome: "Uber", categoria: "Uber One" } }), 
    "Uber One"
  );
  assert("checarCarona - sem bateria no celular", 
    checarCarona({ destino: "Casa" }), 
    "Ir a pé"
  );

  // Testes 4
  assert("calcularGastoSextou - somando lanche, cinema e transporte", 
    calcularGastoSextou(['Uber_X', 'GNC_Cinemas', 'Pipoca', 'Brutal_Burguer', 'Uber_X', 'Flanelinha']), 
    130 // (15 + 35 + 20 + 45 + 15 + 0)
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();