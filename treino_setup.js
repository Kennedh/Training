/**
 * TREINO: MONTANDO O SETUP DOS SONHOS
 * (Dicionários, Rest, Spread e loops)
 */

// Tabela de preços das peças principais
const PRECOS_PECAS = {
  'Ryzen_9000': 3500,
  'RTX_5060': 2500,
  'Placa_Mae_B650': 1200
};

// Tabela de preços dos adicionais
const PRECOS_ADICIONAIS = {
  'Fans_RGB_iCUE': 300,
  'Garantia_Estendida': 200,
  'Cabo_Sleeved': 150
};

/**
 * 1. Calcula o valor de uma peça somado aos seus adicionais
 * 
 * @param {string} peca O nome da peça base
 * @param {string[]} adicionais Lista de adicionais (ex: RGB, Garantia)
 * @returns {number} O preço total desta peça com os adicionais
 */
export function calcularPrecoPeca(peca, ...adicionais) {
  let total = PRECOS_PECAS[peca] || 0;
  
  for (const adicional of adicionais) {
    total += PRECOS_ADICIONAIS[adicional] || 0;
  }
  
  return total;
}

/**
 * 2. Calcula o orçamento total do carrinho de compras do PC
 * 
 * @param {Object[]} carrinho Lista de objetos, ex: [{ peca: 'RTX_5060', adicionais: ['Fans_RGB_iCUE'] }]
 * @returns {number} O preço total do PC
 */
export function calcularOrcamentoPC(carrinho) {
  let totalOrcamento = 0;
  
  // Iteramos sobre cada item do carrinho
  for (const item of carrinho) {
    totalOrcamento += calcularPrecoPeca(item.peca, ...item.adicionais);
  }

  return totalOrcamento;
}

// =============================================================================
// 🧪 ÁREA DE TESTES 
// =============================================================================

function runTests() {
  let passados = 0;
  let falhados = 0;

  function assert(nome, recebido, esperado) {
    if (recebido === esperado) {
      console.log(`✅ PASSOU: ${nome}`);
      passados++;
    } else {
      console.log(`❌ FALHOU: ${nome}`);
      console.log(`   Esperado: ${esperado}`);
      console.log(`   Recebido: ${recebido}`);
      falhados++;
    }
  }

  console.log("== INICIANDO TESTES DO SETUP ==\n");

  // Testes 1
  assert("calcularPrecoPeca - Peça pura, sem adicionais", 
    calcularPrecoPeca('Ryzen_9000'), 
    3500
  );
  
  assert("calcularPrecoPeca - Peça com vários adicionais", 
    calcularPrecoPeca('RTX_5060', 'Garantia_Estendida', 'Cabo_Sleeved'), 
    2850 // (2500 + 200 + 150)
  );

  // Testes 2
  const meuCarrinho = [
    { peca: 'Placa_Mae_B650', adicionais: [] }, // 1200
    { peca: 'Ryzen_9000', adicionais: ['Garantia_Estendida'] }, // 3500 + 200 = 3700
    { peca: 'RTX_5060', adicionais: ['Fans_RGB_iCUE', 'Cabo_Sleeved'] } // 2500 + 300 + 150 = 2950
  ];

  assert("calcularOrcamentoPC - Total do carrinho com spread", 
    calcularOrcamentoPC(meuCarrinho), 
    7850 // (1200 + 3700 + 2950)
  );

  console.log(`\n== RESULTADO: ${passados} PASSARAM, ${falhados} FALHARAM ==`);
}

runTests();