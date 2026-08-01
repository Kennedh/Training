/**
 * TREINO DE SEXTA: DESESTRUTURAÇÃO, REST E SPREAD
 * Preencha o corpo das funções abaixo.
 */

// -----------------------------------------------------------------------------
// 1. Array Destructuring + Rest
// -----------------------------------------------------------------------------
export function separarConvidados(lista) {
  // TODO: Use a desestruturação de array e o Rest (...rest) para extrair o 
  // primeiro nome (o VIP) e agrupar o restante da galera.
  // Retorne um array no formato: [vip, restoDaGalera]
  const [vip, ...restoDaGalera] = lista;
  return [vip, restoDaGalera];
}

// -----------------------------------------------------------------------------
// 2. Array Spread
// -----------------------------------------------------------------------------
export function juntarPlaylists(classicas, novas) {
  // TODO: Use o operador Spread (...) para juntar as duas listas de músicas 
  // (strings) em uma só.
  // Retorne um único array com todas as músicas.
  return [...classicas, ...novas];
}

// -----------------------------------------------------------------------------
// 3. Object Destructuring + Rest
// -----------------------------------------------------------------------------
export function separarTempoEntrega(pedido) {
  // TODO: O objeto 'pedido' possui várias propriedades, incluindo 'tempoEstimado'.
  // Use a desestruturação de objeto e o Rest para extrair APENAS o 'tempoEstimado' 
  // e guardar o resto em uma variável separada.
  // IMPORTANTE: Retorne um ARRAY no formato: [tempoEstimado, restoDoPedido]
  const { tempoEstimado, ...restoDoPedido } = pedido;
  return [tempoEstimado, restoDoPedido];
}

// -----------------------------------------------------------------------------
// 4. Object Spread
// -----------------------------------------------------------------------------
export function adicionarExtrasPedido(pedidoBase, extras) {
  // TODO: Use o operador Spread para mesclar o objeto 'pedidoBase' com o objeto 'extras'.
  // Retorne um único objeto contendo as informações dos dois.
  return { ...pedidoBase, ...extras };
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

  console.log("== INICIANDO TESTES DA RESENHA ==\n");

  // Testes 1
  assert("separarConvidados - lista normal", 
    separarConvidados(["Kennedh", "João", "Maria"]), 
    ["Kennedh", ["João", "Maria"]]
  );

  // Testes 2
  assert("juntarPlaylists - unindo rock clássico e novo", 
    juntarPlaylists(["Avenged Sevenfold", "Disturbed"], ["Three Days Grace"]), 
    ["Avenged Sevenfold", "Disturbed", "Three Days Grace"]
  );

  // Testes 3
  assert("separarTempoEntrega - isolando o tempo do Brutal Burguer", 
    separarTempoEntrega({ restaurante: "Brutal Burguer", lanche: "Duplo Bacon", tempoEstimado: "45 mins", taxa: 5.00 }), 
    ["45 mins", { restaurante: "Brutal Burguer", lanche: "Duplo Bacon", taxa: 5.00 }]
  );

  // Testes 4
  assert("adicionarExtrasPedido - juntando os objetos", 
    adicionarExtrasPedido({ lanche: "X-Salada" }, { bebida: "Refrigerante", batata: true }), 
    { lanche: "X-Salada", bebida: "Refrigerante", batata: true }
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

// Executa os testes automaticamente
runTests();
