/**
 * TREINO COMPLETO DE SÁBADO (15/08/2026)
 * O Boss Final: Arquitetura e Integração de Funções
 */

// -----------------------------------------------------------------------------
// 1. Preparar o Herói (Destructuring, Rest, ?. e ??)
// -----------------------------------------------------------------------------
export function prepararHeroi(heroi) {
  // TODO: O objeto 'heroi' possui { nome, nivel, vida, mana, equipamentos }.
  // 1. Extraia 'nome' e 'nivel'. 
  // 2. Guarde 'vida' e 'mana' no operador Rest chamado 'statusBase'.
  // 3. Acesse o nome da arma usando o caminho: heroi.equipamentos.arma.nome
  // 4. Use ?. e ?? para que, se não houver arma equipada, o valor seja "Punhos Nus".
  // 5. Retorne um NOVO objeto no formato: { nome, nivel, arma, statusBase }
  const { nome, nivel, vida, mana, equipamentos } = heroi;
  const { statusBase } = { statusBase: { vida, mana } };
  const arma = equipamentos?.arma?.nome ?? "Punhos Nus";
  return { nome, nivel, arma, statusBase: { vida, mana } };
}

// -----------------------------------------------------------------------------
// 2. Mesclar Inventário (Spread Operator)
// -----------------------------------------------------------------------------
export function coletarLoot(mochilaAtual, itensDropados) {
  // TODO: Use Spread (...) para unir os arrays 'mochilaAtual' e 'itensDropados'.
  // Adicione a string "Chave do Chefe" na PRIMEIRA posição do novo array.
  // Retorne o novo array.
  return ["Chave do Chefe", ...mochilaAtual, ...itensDropados];
}

// -----------------------------------------------------------------------------
// 3. Calculadora de Dano (Dicionários + for...of)
// -----------------------------------------------------------------------------
const TABELA_HABILIDADES = {
  'Ataque_Basico': 20,
  'Golpe_Pesado': 50,
  'Raio_Arcano': 120
};

export function calcularDanoTotal(habilidadesUsadas) {
  // TODO: 'habilidadesUsadas' é um array de strings, ex: ['Ataque_Basico', 'Errou_Alvo'].
  // Use for...of para iterar sobre a lista.
  // Some o dano usando o dicionário TABELA_HABILIDADES (use || 0 para habilidades que falharam ou não existem).
  // Retorne o dano total causado no turno.
  let danoTotal = 0;
  for (const habilidade of habilidadesUsadas) {
    danoTotal += TABELA_HABILIDADES[habilidade] || 0;
  }
  return danoTotal;
}

// -----------------------------------------------------------------------------
// 4. A INTEGRAÇÃO FINAL (O Boss)
// -----------------------------------------------------------------------------
export function processarFimDeFase(dadosDaFase) {
  // TODO: 'dadosDaFase' é um objeto enorme com { heroi, mochila, loot, combos }.
  // Você não precisa reescrever a lógica! Chame as funções que você acabou de criar:
  // 1. Passe dadosDaFase.heroi para prepararHeroi().
  // 2. Passe dadosDaFase.mochila e dadosDaFase.loot para coletarLoot().
  // 3. Passe dadosDaFase.combos para calcularDanoTotal().
  // 
  // Retorne um objeto organizando tudo isso:
  // {
  //   perfil: <resultado da função prepararHeroi>,
  //   inventarioFinal: <resultado da função coletarLoot>,
  //   danoCausado: <resultado da função calcularDanoTotal>
  // }
  return {
    perfil: prepararHeroi(dadosDaFase.heroi),
    inventarioFinal: coletarLoot(dadosDaFase.mochila, dadosDaFase.loot),
    danoCausado: calcularDanoTotal(dadosDaFase.combos)
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

  console.log("== INICIANDO BOSS DE SÁBADO ==\n");

  // Testes 1
  assert("prepararHeroi - herói com equipamento completo", 
    prepararHeroi({ nome: "Arthur", nivel: 40, vida: 1000, mana: 300, equipamentos: { arma: { nome: "Excalibur" } } }), 
    { nome: "Arthur", nivel: 40, arma: "Excalibur", statusBase: { vida: 1000, mana: 300 } }
  );
  assert("prepararHeroi - herói sem arma (fallback)", 
    prepararHeroi({ nome: "Monge", nivel: 15, vida: 400, mana: 50 }), 
    { nome: "Monge", nivel: 15, arma: "Punhos Nus", statusBase: { vida: 400, mana: 50 } }
  );

  // Testes 2
  assert("coletarLoot - unindo mochila e drops", 
    coletarLoot(["Poção Média"], ["Ouro", "Anel de Prata"]), 
    ["Chave do Chefe", "Poção Média", "Ouro", "Anel de Prata"]
  );

  // Testes 3
  assert("calcularDanoTotal - somando combos válidos e inválidos", 
    calcularDanoTotal(['Ataque_Basico', 'Errou_Alvo', 'Raio_Arcano', 'Ataque_Basico']), 
    160 // (20 + 0 + 120 + 20)
  );

  // Testes 4
  const dados = {
    heroi: { nome: "Kael", nivel: 99, vida: 9999, mana: 9999, equipamentos: { arma: { nome: "Cajado do Vazio" } } },
    mochila: ["Elixir"],
    loot: ["Capa Arcana"],
    combos: ["Raio_Arcano", "Raio_Arcano", "Bloqueado"]
  };

  assert("processarFimDeFase - integrando todas as funções", 
    processarFimDeFase(dados), 
    {
      perfil: { nome: "Kael", nivel: 99, arma: "Cajado do Vazio", statusBase: { vida: 9999, mana: 9999 } },
      inventarioFinal: ["Chave do Chefe", "Elixir", "Capa Arcana"],
      danoCausado: 240
    }
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();