/**
 * TREINO DE SEXTA (21/08/2026) - REVISÃO DA SEMANA ⚔️
 * Desestruturação, map, filter, reduce, Closures e Callbacks!
 */

// -----------------------------------------------------------------------------
// 1. O COMBO DE ARRAYS E DESESTRUTURAÇÃO (Taverna do Aventureiro)
// -----------------------------------------------------------------------------
export function calcularXpFinal(missoes) {
  // TODO: 'missoes' é um array de objetos, ex: { nome: "Cace o Orc", status: "Concluida", xp: 150 }
  // 1. Filtre APENAS as missões com status "Concluida" (tente desestruturar o status!).
  // 2. Mapeie para extrair apenas a propriedade 'xp' (desestruture o xp!).
  // 3. Reduza para somar e retornar o XP total ganho.
  return missoes
    .filter(({ status }) => status === "Concluida")
    .map(({ xp }) => xp)
    .reduce((total, xp) => total + xp, 0);
}

// -----------------------------------------------------------------------------
// 2. CLOSURES E CALLBACKS (Sistema de Level Up)
// -----------------------------------------------------------------------------
export function criarVerificadorDeNivel(xpMeta, callbackSubiuNivel) {
  // TODO: Retorne uma função (closure) que recebe um número (xpAtual).
  // Essa função interna deve:
  // 1. Checar se xpAtual é maior ou igual a xpMeta.
  // 2. Se for, chamar a função callbackSubiuNivel() (sem passar parâmetros).
  // 3. Retornar o valor de xpAtual, independente se subiu de nível ou não.
  return function(xpAtual) {
    if (xpAtual >= xpMeta) {
      callbackSubiuNivel();
    }
    return xpAtual;
  };
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

  console.log("== INICIANDO REVISÃO DE SEXTA ==\n");

  // Testes 1: Combo de Arrays
  const diarioDeMissoes = [
    { nome: "Entregar poção", status: "Concluida", xp: 50 },
    { nome: "Derrotar o Dragão", status: "Em Andamento", xp: 5000 },
    { nome: "Achar o anel", status: "Falha", xp: 0 },
    { nome: "Limpar o porão", status: "Concluida", xp: 120 }
  ];
  
  assert("calcularXpFinal - filtrando, mapeando e somando XP", 
    calcularXpFinal(diarioDeMissoes), 
    170 // 50 + 120
  );

  // Testes 2: Closures e Callbacks
  let levelUpDisparado = false;
  function avisarLevelUp() {
    levelUpDisparado = true;
  }
  
  const checarNivel = criarVerificadorDeNivel(1000, avisarLevelUp);

  assert("criarVerificadorDeNivel - não atinge a meta", 
    checarNivel(800), 
    800
  );
  assert("criarVerificadorDeNivel - callback não foi chamado antes da hora", 
    levelUpDisparado, 
    false
  );
  
  assert("criarVerificadorDeNivel - atinge a meta", 
    checarNivel(1050), 
    1050
  );
  assert("criarVerificadorDeNivel - callback foi chamado com sucesso", 
    levelUpDisparado, 
    true
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();