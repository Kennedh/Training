/**
 * TREINO DE SÁBADO: DESESTRUTURAÇÃO, REST E SPREAD
 * Preencha o corpo das funções abaixo.
 */

// -----------------------------------------------------------------------------
// 1. Array Destructuring + Rest
// -----------------------------------------------------------------------------
export function separarProtagonista(personagens) {
  // TODO: Use a desestruturação de array e o Rest (...rest) para extrair o 
  // primeiro personagem (o protagonista) e agrupar o restante do time.
  // Retorne um array no formato: [protagonista, restoDoTime]
    const [protagonista, ...restoDoTime] = personagens;
    return [protagonista, [...restoDoTime]];
}

// -----------------------------------------------------------------------------
// 2. Array Spread
// -----------------------------------------------------------------------------
export function montarSetupGamer(pecasAtuais, novasPecas) {
  // TODO: Use o operador Spread (...) para juntar as peças que você já tem
  // com as peças do seu novo upgrade em uma única lista.
  // Retorne um único array com todas as peças.
    let res = [...pecasAtuais, ...novasPecas];
    return res;
}

// -----------------------------------------------------------------------------
// 3. Object Destructuring + Rest
// -----------------------------------------------------------------------------
export function separarNomePet(tarefaPet) {
  // TODO: O objeto 'tarefaPet' possui a propriedade 'nome'.
  // Use a desestruturação de objeto e o Rest para extrair APENAS o 'nome' 
  // e guardar o restante dos detalhes da tarefa em uma variável separada.
  // IMPORTANTE: Retorne um ARRAY no formato: [nome, restoDaTarefa]
    let {nome, ...restoDaTarefa} = tarefaPet;
    return [nome, restoDaTarefa];
}

// -----------------------------------------------------------------------------
// 4. Object Spread (Atenção à ordem!)
// -----------------------------------------------------------------------------
export function atualizarStatusJogo(statusBase, buffs) {
  // TODO: Use o operador Spread para mesclar o objeto 'statusBase' com o objeto 'buffs'.
  // DICA: Se a mesma propriedade existir nos dois objetos (como "dano"), 
  // o objeto que for espalhado por último vai sobrescrever o valor do primeiro.
  // Retorne o objeto unificado, garantindo que os buffs sobrescrevam a base.
    const statusAtualizado = {
    ...statusBase,
    ...buffs
  };
  
  return statusAtualizado;
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

  console.log("== INICIANDO TESTES DE SÁBADO ==\n");

  // Testes 1
  assert("separarProtagonista - time do anime", 
    separarProtagonista(["Naruto", "Sasuke", "Sakura", "Kakashi"]), 
    ["Naruto", ["Sasuke", "Sakura", "Kakashi"]]
  );

  // Testes 2
  assert("montarSetupGamer - upgrade com RTX e Ryzen", 
    montarSetupGamer(["Gabinete", "Fonte", "SSD"], ["RTX 5060", "Ryzen 9000"]), 
    ["Gabinete", "Fonte", "SSD", "RTX 5060", "Ryzen 9000"]
  );

  // Testes 3
  assert("separarNomePet - hora do passeio", 
    separarNomePet({ nome: "Pandora", acao: "Passear no parque", duracao: "40 minutos", coleira: "Vermelha" }), 
    ["Pandora", { acao: "Passear no parque", duracao: "40 minutos", coleira: "Vermelha" }]
  );

  // Testes 4
  assert("atualizarStatusJogo - aplicando buffs no personagem", 
    atualizarStatusJogo({ classe: "Guerreiro", vida: 100, dano: 15 }, { dano: 30, armadura: 50 }), 
    { classe: "Guerreiro", vida: 100, dano: 30, armadura: 50 }
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

// Executa os testes automaticamente
runTests();