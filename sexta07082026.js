/**
 * TREINO DE SEXTA: O DESAFIO CYBERPUNK
 * (Destructuring, Rest, Spread, for...of, ?. e ??)
 */

// -----------------------------------------------------------------------------
// 1. Optional Chaining (?.) e Nullish Coalescing (??)
// -----------------------------------------------------------------------------
export function verificarCyberware(personagem) {
  // TODO: Retorne o modelo do implante ocular do personagem.
  // O caminho no objeto deveria ser: personagem.implantes.olhos.modelo
  // Porém, o personagem pode não ter a chave 'implantes' ou a chave 'olhos'.
  // Use o Encadeamento Opcional (?.) para tentar acessar o modelo sem quebrar o código.
  // Se o resultado for undefined/null, use a Coalescência Nula (??) para retornar a string "Kiroshi Padrão".
    return personagem.implantes?.olhos.modelo ?? "Kiroshi Padrão"
}

// -----------------------------------------------------------------------------
// 2. Destructuring + Rest + ??
// -----------------------------------------------------------------------------
export function processarContrato(contrato) {
  // TODO: O objeto tem { alvo, recompensa, local, risco }.
  // 1. Extraia 'alvo' e 'recompensa' usando desestruturação.
  // 2. Guarde o resto no operador Rest chamado 'detalhes'.
  // 3. Se a 'recompensa' extraída for nula ou indefinida, atribua o valor 500 (use o ?? para isso em uma nova variável, ou retorne direto).
  // Retorne um array: [alvo, recompensaFinal, detalhes]
    const {alvo, recompensa, ...detalhes} = contrato;
    const recompensaFinal = recompensa ?? 500;
    return [alvo, recompensaFinal, detalhes];
}

// -----------------------------------------------------------------------------
// 3. Array Spread
// -----------------------------------------------------------------------------
export function atualizarArsenal(armasBase, armasSaqueadas) {
  // TODO: Use Spread (...) para juntar as duas listas.
  // Adicione a arma "Mantis Blades" no INÍCIO da lista unificada.
  // Retorne o novo array.
    return ["Mantis Blades" ,...armasBase, ...armasSaqueadas]
}

// -----------------------------------------------------------------------------
// 4. Iteração com for...of + ?. e ??
// -----------------------------------------------------------------------------
export function calcularLucroMissoes(missoes) {
  // TODO: 'missoes' é um array de objetos. Ex: { id: 1, pagamento: { creditos: 1500 } }
  // Use for...of para somar os 'creditos' de todas as missões.
  // ATENÇÃO: Algumas missões falharam e não têm a propriedade 'pagamento', ou 'creditos' está vazio.
  // Use ?. para tentar acessar os creditos, e use ?? 0 para somar zero caso não exista pagamento.
  // Retorne o total.
    let total = 0;
    for (const objeto of missoes){
      total += objeto?.pagamento?.creditos ?? 0;
    }
    return total;
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

  console.log("== INICIANDO TESTES DE QUINTA ==\n");

  // Testes 1
  assert("verificarCyberware - personagem com implantes completos", 
    verificarCyberware({ nome: "V", implantes: { olhos: { modelo: "Kiroshi Mk.3" } } }), 
    "Kiroshi Mk.3"
  );
  assert("verificarCyberware - personagem sem implantes", 
    verificarCyberware({ nome: "Jackie" }), 
    "Kiroshi Padrão"
  );

  // Testes 2
  assert("processarContrato - contrato com recompensa definida", 
    processarContrato({ alvo: "Placide", recompensa: 12000, local: "Pacifica", risco: "Alto" }), 
    ["Placide", 12000, { local: "Pacifica", risco: "Alto" }]
  );
  assert("processarContrato - contrato sem recompensa (aplicando fallback)", 
    processarContrato({ alvo: "Scavenger", recompensa: null, local: "Beco", risco: "Baixo" }), 
    ["Scavenger", 500, { local: "Beco", risco: "Baixo" }]
  );

  // Testes 3
  assert("atualizarArsenal - unindo armas e adicionando no início", 
    atualizarArsenal(["Pistola Lexington"], ["Escopeta Carnage", "Rifle Copperhead"]), 
    ["Mantis Blades", "Pistola Lexington", "Escopeta Carnage", "Rifle Copperhead"]
  );

  // Testes 4
  const missoesExecutadas = [
    { id: 1, pagamento: { creditos: 2000 } },
    { id: 2 }, // Missão falhou, sem pagamento
    { id: 3, pagamento: { creditos: 3500 } },
    { id: 4, pagamento: null } // Calote
  ];

  assert("calcularLucroMissoes - somando créditos com segurança", 
    calcularLucroMissoes(missoesExecutadas), 
    5500
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();