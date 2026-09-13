class Lanche {
  constructor(nome, preco, tempoPreparo) {
    this.nome = nome;
    this.preco = preco;
    this.tempoPreparo = tempoPreparo; // Tempo em milissegundos
  }
}

class Lanchonete {
  
  // ==========================================
  // DESAFIO 1: reduce
  // ==========================================
  calcularTotal(lanches) {
    // TODO: 'lanches' é um array de objetos da classe Lanche.
    // Use o .reduce() para somar o 'preco' de todos eles e retorne o valor total.
    //return this.lanches.preco.reduce((total,preco) => total + preco,0)
    return lanches.reduce((acc,lanches) => acc + lanches.preco,0)
  }

  // ==========================================
  // DESAFIO 2: Criando a Promise Dinâmica
  // ==========================================
  prepararLanche(lanche) {
    // TODO: Retorne uma nova Promise.
    // Use o setTimeout, mas o tempo de espera deve ser o 'lanche.tempoPreparo'.
    // Quando o tempo acabar, chame o resolve() com a string: `${lanche.nome} pronto!`
  }

  // ==========================================
  // DESAFIO 3: async/await e Promise.all
  // ==========================================
  async entregarPedido(cliente, lanches) {
    // 1. Se o array 'lanches' estiver vazio, lance um erro: throw new Error("Pedido vazio!")
    // 2. Abra um bloco try/catch.
    // 3. No try:
    //    - Crie um array de promessas usando o .map() para passar cada lanche do array na função this.prepararLanche(lanche).
    //    - Use o await com o Promise.all() para aguardar todas as promessas terminarem juntas.
    //    - Pegue o total usando this.calcularTotal(lanches).
    //    - Retorne a string: `Pedido de ${cliente} finalizado! Total: R$ ${total}`
    // 4. No catch: retorne a mensagem de erro.
  }
}

// ---------------------------------------------------------
// 🧪 ÁREA DE TESTES
// ---------------------------------------------------------
async function rodarTestes() {
  console.log("🍔 ABRINDO A LANCHONETE...\n");
  const lanchonete = new Lanchonete();

  const pedidoMesa1 = [
    new Lanche("Hambúrguer Clássico", 25, 2000), // Demora 2 segundos
    new Lanche("Batata Frita", 15, 1000),        // Demora 1 segundo
    new Lanche("Refrigerante", 8, 500)           // Demora 0.5 segundo
  ];

  console.log("Calculando total da Mesa 1...");
  console.log("Total esperado: 48 | Total calculado:", lanchonete.calcularTotal(pedidoMesa1));

  console.log("\nPreparando pedido da Mesa 1 (Aguarde ~2 segundos)...");
  const resultado = await lanchonete.entregarPedido("Maria", pedidoMesa1);
  console.log(resultado);
  // Esperado: "Pedido de Maria finalizado! Total: R$ 48"

  console.log("\n⚠️ Tentando pedido vazio:");
  try {
    const erro = await lanchonete.entregarPedido("João", []);
    console.log(erro);
  } catch(e) {
    console.log(e.message);
  }
}

rodarTestes();