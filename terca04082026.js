/**
 * TREINO DE TERÇA: CONSOLIDAÇÃO DE FUNDAMENTOS
 * (Destructuring, Rest, Spread, forEach e for...of em arrays de objetos)
 */

// -----------------------------------------------------------------------------
// 1. Object Destructuring + Rest (Lidando com strings)
// -----------------------------------------------------------------------------
export function organizarSuplementos(pote) {
  // TODO: O objeto 'pote' possui { produto, sabor, peso, fabricante, validade }.
  // Extraia 'produto' e 'sabor' usando desestruturação.
  // Guarde o restante no operador Rest.
  // Retorne um array contendo uma string formatada na primeira posição e o resto na segunda: 
  // Exemplo do retorno: [`${produto} de ${sabor}`, restoDoPote]
  
  const { produto, sabor, ...restoDoPote } = pote;
  return [`${produto} de ${sabor}`, restoDoPote];
}

// -----------------------------------------------------------------------------
// 2. Array Spread (Adicionando itens extras)
// -----------------------------------------------------------------------------
export function montarPlaylist(classicos, metal) {
  // TODO: Use o Spread Operator (...) para juntar os arrays 'classicos' e 'metal'.
  // Desafio extra: Adicione a banda "Tool" no final dessa nova lista, no mesmo return.
  // Retorne o novo array completo.

  return [...classicos, ...metal, "Tool"];
}

// -----------------------------------------------------------------------------
// 3. Iteração com .forEach (Soma condicional)
// -----------------------------------------------------------------------------
export function calcularTempoPasseioPandora(atividadesDiarias) {
  // TODO: 'atividadesDiarias' é um array de objetos, ex: { acao: "Passeio", duracaoMinutos: 30 }
  // Use o .forEach() para iterar sobre o array.
  // Some a 'duracaoMinutos' APENAS quando a 'acao' for estritamente igual a "Passeio".
  // Retorne o tempo total em minutos.
  
  let tempoTotal = 0;
  
  atividadesDiarias.forEach(atividade => {
    if (atividade.acao === "Passeio") {
      tempoTotal += atividade.duracaoMinutos;
    }
  });
  
  return tempoTotal;
}

// -----------------------------------------------------------------------------
// 4. Iteração com for...of (Lógica com propriedades de objetos)
// -----------------------------------------------------------------------------
export function classificarEpisodiosNaruto(episodios, buscarCanon) {
  // TODO: 'episodios' é um array de objetos, ex: { numero: 1, filler: false }
  // 'buscarCanon' é um booleano (true ou false).
  // Use um loop 'for...of' para percorrer os 'episodios'.
  // Se 'buscarCanon' for true, conte os episódios que NÃO são filler (filler === false).
  // Se 'buscarCanon' for false, conte os episódios que SÃO filler (filler === true).
  // Retorne a contagem final. 
  // Dica: Tente usar aquela mesma estrutura elegante de IF que você fez na segunda-feira!

  let contagem = 0;
  
  for (const episodio of episodios) {
    if (buscarCanon) {
      // Conta episódios canônicos (não filler)
      if (episodio.filler === false) {
        contagem++;
      }
    } else {
      // Conta episódios filler
      if (episodio.filler === true) {
        contagem++;
      }
    }
  }
  
  return contagem;
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

  console.log("== INICIANDO TESTES DE TERÇA ==\n");

  // Testes 1
  assert("organizarSuplementos - extraindo info do whey", 
    organizarSuplementos({ produto: "Whey Protein Isolado", sabor: "Chocolate", peso: "900g", validade: "2027" }), 
    ["Whey Protein Isolado de Chocolate", { peso: "900g", validade: "2027" }]
  );

  // Testes 2
  assert("montarPlaylist - unindo rock e adicionando Tool no final", 
    montarPlaylist(["Nickelback"], ["Disturbed", "Avenged Sevenfold"]), 
    ["Nickelback", "Disturbed", "Avenged Sevenfold", "Tool"]
  );

  // Testes 3
  assert("calcularTempoPasseioPandora - somando apenas os passeios", 
    calcularTempoPasseioPandora([
      { acao: "Dormir", duracaoMinutos: 120 },
      { acao: "Passeio", duracaoMinutos: 25 },
      { acao: "Comer", duracaoMinutos: 10 },
      { acao: "Passeio", duracaoMinutos: 20 }
    ]), 
    45
  );

  // Testes 4
  const listaEpisodios = [
    { numero: 135, filler: false },
    { numero: 136, filler: true },
    { numero: 137, filler: true },
    { numero: 138, filler: false }
  ];

  assert("classificarEpisodiosNaruto - contando episódios canônicos", 
    classificarEpisodiosNaruto(listaEpisodios, true), 
    2
  );

  assert("classificarEpisodiosNaruto - contando episódios fillers", 
    classificarEpisodiosNaruto(listaEpisodios, false), 
    2
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

// Executa os testes automaticamente
runTests();