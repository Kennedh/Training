/**
 * TREINO LEVE DE QUARTA (12/08/2026)
 * (Revisão relax: Destructuring, Rest, Spread, ?. , ?? e Dicionários)
 */

// -----------------------------------------------------------------------------
// 1. Destructuring + Rest (Aquele commit diário)
// -----------------------------------------------------------------------------
export function registrarProgressoDiario(registro) {
  // TODO: O objeto 'registro' possui { dia, foco, horas, streak }.
  // Extraia 'foco' e 'streak' usando desestruturação.
  // Guarde o resto no operador Rest chamado 'detalhes'.
  // Retorne um array no formato: [`Foco: ${foco}, Streak: ${streak}`, detalhes]
  const {foco, streak, ...detalhes} = registro;
  return [`Foco: ${foco}, Streak: ${streak}`, detalhes]
}

// -----------------------------------------------------------------------------
// 2. Spread (Expandindo horizontes)
// -----------------------------------------------------------------------------
export function expandirEstudos(idiomasAtuais, idiomasNovos) {
  // TODO: Use o Spread Operator (...) para juntar as listas 'idiomasAtuais' e 'idiomasNovos'.
  // Adicione a linguagem "Rust" no FINAL da nova lista.
  // Retorne o novo array.
  return [...idiomasAtuais, ...idiomasNovos, "Rust"]
}

// -----------------------------------------------------------------------------
// 3. Optional Chaining (?.) e Nullish Coalescing (??)
// -----------------------------------------------------------------------------
export function analisarFeiticeiroJujutsu(feiticeiro) {
  // TODO: Retorne o grau da expansão de domínio do personagem.
  // O caminho no objeto deveria ser: feiticeiro.dominio.grau
  // Use o Encadeamento Opcional (?.) para tentar acessar 'grau' sem quebrar o código.
  // Se o resultado for undefined/null, use a Coalescência Nula (??) para retornar "Sem Domínio".
  return feiticeiro?.dominio?.grau ?? "Sem Domínio"
}

// -----------------------------------------------------------------------------
// 4. Dicionários + Loops (Farmando no Fishing Frenzy)
// -----------------------------------------------------------------------------
const PRECOS_PEIXES = {
  'Sardinha': 2,
  'Peixe_Espada': 15,
  'Tubarao_Branco': 100
};

export function calcularLucroFishingFrenzy(pescados) {
  // TODO: 'pescados' é um array de strings, ex: ['Sardinha', 'Peixe_Espada'].
  // Use for...of para iterar sobre a lista de 'pescados'.
  // Some o valor usando o dicionário PRECOS_PEIXES (use || 0 caso pesque uma bota ou algo que não tem preço).
  // Retorne o total.
  let totalLucro = 0;
  for(const peixe of pescados){
    totalLucro += PRECOS_PEIXES[peixe] || 0;
  }
  return totalLucro;
}


// =============================================================================
// 🧪 ÁREA DE TESTES
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

  console.log("== INICIANDO TREINO LEVE DE QUARTA ==\n");

  // Testes 1
  assert("registrarProgressoDiario - extraindo foco e streak", 
    registrarProgressoDiario({ dia: 247, foco: "Loops", horas: 2, streak: 247 }), 
    ["Foco: Loops, Streak: 247", { dia: 247, horas: 2 }]
  );

  // Testes 2
  assert("expandirEstudos - unindo listas e adicionando Rust", 
    expandirEstudos(["Inglês", "JavaScript"], ["Python"]), 
    ["Inglês", "JavaScript", "Python", "Rust"]
  );

  // Testes 3
  assert("analisarFeiticeiroJujutsu - com domínio", 
    analisarFeiticeiroJujutsu({ nome: "Gojo Satoru", dominio: { nome: "Muryo Kusho", grau: "Especial" } }), 
    "Especial"
  );
  assert("analisarFeiticeiroJujutsu - sem domínio", 
    analisarFeiticeiroJujutsu({ nome: "Yuji Itadori" }), 
    "Sem Domínio"
  );

  // Testes 4
  assert("calcularLucroFishingFrenzy - somando peixes conhecidos e desconhecidos", 
    calcularLucroFishingFrenzy(['Sardinha', 'Tubarao_Branco', 'Bota_Velha', 'Sardinha']), 
    104 // (2 + 100 + 0 + 2)
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();