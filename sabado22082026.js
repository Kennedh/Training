/**
 * TREINO DE SÁBADO (22/08/2026) - Assincronicidade ⏳
 * Dominando Promises e async/await
 */

const bancoDeDados = {
  1: { nome: "Espada Longa", dano: 50 },
  2: { nome: "Cajado Arcano", dano: 75 }
};

// -----------------------------------------------------------------------------
// 1. CRIANDO UMA PROMISE (Simulando uma API)
// -----------------------------------------------------------------------------
export function buscarArmaNoBanco(id) {
  // TODO: Retorne uma nova Promise: return new Promise((resolve, reject) => { ... })
  // Dentro dela, use setTimeout para aguardar 1 segundo (1000ms).
  // Se o 'id' existir no bancoDeDados, chame o resolve() passando o objeto da arma.
  // Se não existir, chame o reject() passando a string "Arma não encontrada".
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const arma = bancoDeDados[id];
      if (arma) {
        resolve(arma);
      } else {
        reject("Arma não encontrada");
      }
    }, 1000);
  });
}

// -----------------------------------------------------------------------------
// 2. CONSUMINDO A PROMISE COM ASYNC/AWAIT
// -----------------------------------------------------------------------------
export async function equiparHeroi(idDaArma) {
  // TODO: Use um bloco try/catch.
  // No 'try', aguarde (await) a buscarArmaNoBanco(idDaArma).
  // Retorne uma string no formato: "Equipado: [nome da arma]"
  // No 'catch', retorne o erro que veio do reject.
  try {
    const arma = await buscarArmaNoBanco(idDaArma);
    return `Equipado: ${arma.nome}`;
  } catch (erro) {
    return erro;
  }
}

// =============================================================================
// 🧪 ÁREA DE TESTES 
// =============================================================================

async function runTests() {
  console.log("== INICIANDO TREINO DE SÁBADO ==\n");

  try {
    const arma = await buscarArmaNoBanco(1);
    console.log(arma.nome === "Espada Longa" ? "✅ PASSOU: Promise resolveu a arma" : "❌ FALHOU: Promise resolveu errado");
  } catch (e) {
    console.log("❌ FALHOU: Promise rejeitou quando devia resolver");
  }

  try {
    await buscarArmaNoBanco(99);
    console.log("❌ FALHOU: Promise resolveu quando devia rejeitar");
  } catch (e) {
    console.log(e === "Arma não encontrada" ? "✅ PASSOU: Promise rejeitou o erro correto" : "❌ FALHOU: Erro incorreto");
  }

  const sucesso = await equiparHeroi(2);
  console.log(sucesso === "Equipado: Cajado Arcano" ? "✅ PASSOU: Async/Await sucesso" : "❌ FALHOU: Async/Await sucesso");

  const falha = await equiparHeroi(99);
  console.log(falha === "Arma não encontrada" ? "✅ PASSOU: Async/Await falha (catch)" : "❌ FALHOU: Async/Await falha (catch)");
}

runTests();