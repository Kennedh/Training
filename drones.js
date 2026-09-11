class Pacote {
  constructor(id, destino, peso, status = 'Pendente') {
    this.id = id;
    this.destino = destino;
    this.peso = peso;
    this.status = status; // Pode ser 'Pendente' ou 'Entregue'
  }
}

class CentralDeDrones {
  constructor() {
    this.pacotes = []; // Guarda os objetos da classe Pacote
  }

  receberPacote(pacote) {
    this.pacotes.push(pacote);
  }

  // ==========================================
  // DESAFIO 1: filter e map
  // ==========================================
  obterDestinosLevesPendentes(pesoMaximo) {
    // 1. Filtre os pacotes que tenham status 'Pendente' E cujo peso seja menor ou igual ao pesoMaximo.
    // 2. Mapeie para retornar APENAS o 'destino' desses pacotes.
    return this.pacotes
      .filter(pacote => pacote.status === 'Pendente' && pacote.peso <= pesoMaximo)
      .map(pacote => pacote.destino);
  }

  // ==========================================
  // DESAFIO 2: Criando uma Promise
  // ==========================================
  vooDoDrone(pacote) {
    // 1. Retorne uma nova Promise: return new Promise((resolve, reject) => { ... })
    // 2. Dentro dela, use o setTimeout para esperar 1500ms (1.5 segundos).
    // 3. Quando o tempo acabar, mude o status do pacote para 'Entregue'.
    // 4. Chame o resolve() passando uma mensagem: `Pacote ${pacote.id} entregue!`
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        pacote.status = 'Entregue';
        resolve(`Pacote ${pacote.id} entregue!`);
      }, 1500);
    });
  }

  // ==========================================
  // DESAFIO 3: Consumindo com Async/Await e Try/Catch
  // ==========================================
  async despachar(idPacote) {
    // 1. Use o método .find() para achar o pacote com o id correspondente na lista this.pacotes.
    // 2. Se o pacote não existir, lance um erro (throw new Error("Pacote não encontrado")).
    // 3. Se o pacote já estiver com status 'Entregue', lance um erro (throw new Error("Pacote já foi entregue")).
    // 4. Abra um bloco try/catch.
    // 5. No try, use o await para esperar a função this.vooDoDrone(pacote) e retorne o resultado.
    // 6. No catch, retorne a mensagem do erro (erro.message).
    const pacote = this.pacotes.find(p => p.id === idPacote);

    if (!pacote) {
      throw new Error("Pacote não encontrado");
    }

    if (pacote.status === 'Entregue') {
      throw new Error("Pacote já foi entregue");
    }

    try {
      const resultado = await this.vooDoDrone(pacote);
      return resultado;
    } catch (erro) {
      return erro.message;
    }
  }
}

// ---------------------------------------------------------
// 🧪 ÁREA DE TESTES (Não precisa alterar)
// ---------------------------------------------------------
async function rodarTestes() {
  console.log("🛸 INICIANDO SISTEMA DE DRONES...\n");
  
  const central = new CentralDeDrones();
  central.receberPacote(new Pacote("P01", "Rua A", 2));
  central.receberPacote(new Pacote("P02", "Avenida B", 5, "Entregue"));
  central.receberPacote(new Pacote("P03", "Praça C", 1.5));
  central.receberPacote(new Pacote("P04", "Beco D", 8));

  console.log("📦 DESAFIO 1 (Destinos Leves e Pendentes, max 3kg):");
  console.log(central.obterDestinosLevesPendentes(3)); 
  // Esperado: [ 'Rua A', 'Praça C' ]

  console.log("\n🚀 DESAFIO 3 (Despachando P01 - aguarde 1.5s):");
  const resultado1 = await central.despachar("P01");
  console.log(resultado1); 
  // Esperado: "Pacote P01 entregue!"

  console.log("\n⚠️ DESAFIO 3 (Tentando despachar P02 que já foi entregue):");
  try {
    const resultado2 = await central.despachar("P02");
    console.log(resultado2);
  } catch (e) {
    console.log(e.message); 
    // Esperado: "Pacote já foi entregue"
  }
}

rodarTestes();