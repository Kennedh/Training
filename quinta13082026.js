/**
 * TREINO DE QUINTA (13/08/2026)
 * O Teste: Destructuring, Rest, Spread, ?., ?? e Dicionários
 */

// -----------------------------------------------------------------------------
// 1. Destructuring + Rest (Rock in Rio)
// -----------------------------------------------------------------------------
export function organizarIngressoRiR(ingresso) {
  // TODO: O objeto 'ingresso' possui { dia, palco, bandaPrincipal, vip, valor }.
  // Extraia 'bandaPrincipal' e 'palco' usando desestruturação.
  // Guarde o resto no operador Rest chamado 'outrosDados'.
  // Retorne um array no formato exato: [`Ver a banda ${bandaPrincipal} no ${palco}`, outrosDados]
  const {bandaPrincipal, palco, ...outrosDados} = ingresso
  return [`Ver a banda ${bandaPrincipal} no ${palco}`, outrosDados]
}

// -----------------------------------------------------------------------------
// 2. Spread Operator (Consolidando Logs do SYS-PULSE)
// -----------------------------------------------------------------------------
export function consolidarLogs(logsAntigos, logsNovos) {
  // TODO: Use o Spread Operator (...) para juntar os arrays 'logsAntigos' e 'logsNovos'.
  // Adicione a string "INICIO_DO_MONITORAMENTO" na PRIMEIRA posição da nova lista.
  // Retorne o novo array completo.
  return ["INICIO_DO_MONITORAMENTO", ...logsAntigos, ...logsNovos]
}

// -----------------------------------------------------------------------------
// 3. Optional Chaining (?.) e Nullish Coalescing (??) (Petshop da Pandora)
// -----------------------------------------------------------------------------
export function verificarBanhoTosa(cachorro) {
  // TODO: Retorne o status do banho do pet.
  // O caminho no objeto deveria ser: cachorro.agendamento.status
  // Use o Encadeamento Opcional (?.) para evitar erros se o cachorro não tiver um agendamento marcado.
  // Se for nulo ou indefinido, use a Coalescência Nula (??) para retornar a string "Sem agendamento".
  return cachorro?.agendamento?.status ?? "Sem agendamento"
}

// -----------------------------------------------------------------------------
// 4. Dicionários + Loops (Calculando XP no Duolingo)
// -----------------------------------------------------------------------------
const XP_POR_TIPO = {
  'Ingles_Basico': 10,
  'Matematica_Rapida': 15,
  'Desafio_Ofensiva': 25
};

export function calcularXpDiario(licoesFeitas) {
  // TODO: 'licoesFeitas' é um array de strings, ex: ['Ingles_Basico', 'Desafio_Ofensiva'].
  // Use for...of para iterar sobre a lista.
  // Some o XP usando o dicionário XP_POR_TIPO (use o fallback || 0 caso faça uma lição nova não mapeada).
  // Retorne o XP total ganho nos seus 5 minutos de estudo.
  let total = 0
  for(const licao of licoesFeitas){
    total += XP_POR_TIPO[licao] || 0
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

  console.log("== INICIANDO TREINO DE QUINTA ==\n");

  // Testes 1
  assert("organizarIngressoRiR - extraindo show principal", 
    organizarIngressoRiR({ dia: "Sexta", palco: "Palco Mundo", bandaPrincipal: "Avenged Sevenfold", vip: true, valor: 800 }), 
    ["Ver a banda Avenged Sevenfold no Palco Mundo", { dia: "Sexta", vip: true, valor: 800 }]
  );

  // Testes 2
  assert("consolidarLogs - unindo registros e adicionando flag inicial", 
    consolidarLogs(["CPU_80%", "RAM_60%"], ["CPU_85%", "TEMP_70C"]), 
    ["INICIO_DO_MONITORAMENTO", "CPU_80%", "RAM_60%", "CPU_85%", "TEMP_70C"]
  );

  // Testes 3
  assert("verificarBanhoTosa - pet com agendamento", 
    verificarBanhoTosa({ nome: "Pandora", raca: "Shih Tzu", agendamento: { dia: "Sábado", status: "Confirmado" } }), 
    "Confirmado"
  );
  assert("verificarBanhoTosa - pet sem agendamento", 
    verificarBanhoTosa({ nome: "Pandora", raca: "Shih Tzu" }), 
    "Sem agendamento"
  );

  // Testes 4
  assert("calcularXpDiario - somando XP de lições", 
    calcularXpDiario(['Ingles_Basico', 'Matematica_Rapida', 'Historia_Antiga', 'Desafio_Ofensiva']), 
    50 // (10 + 15 + 0 + 25)
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();