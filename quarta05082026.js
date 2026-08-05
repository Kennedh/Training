/**
 * TREINO DE QUARTA: PREPARAÇÃO PARA O EXERCISM
 * (Destructuring, Rest, Spread, forEach e for...of com cálculos)
 */

// -----------------------------------------------------------------------------
// 1. Object Destructuring + Rest
// -----------------------------------------------------------------------------
export function registrarCommit(commit) {
  // TODO: O objeto 'commit' possui { repo, dia, mensagem, arquivosAlterados, linguagem }.
  // Extraia 'repo' e 'dia' usando desestruturação.
  // Guarde o restante no operador Rest chamado 'detalhes'.
  // Retorne um array no formato: [`Dia ${dia} no repo ${repo}`, detalhes]
  
  const { repo, dia, ...detalhes } = commit;
  return [`Dia ${dia} no repo ${repo}`, detalhes];
}

// -----------------------------------------------------------------------------
// 2. Array Spread (Adicionando no início)
// -----------------------------------------------------------------------------
export function maratonaHarryPotter(filmesAntigos, filmesNovos) {
  // TODO: Use o Spread Operator (...) para juntar 'filmesAntigos' e 'filmesNovos'.
  // Desafio: Diferente de ontem, adicione o filme "A Ordem da Fênix" no INÍCIO da nova lista.
  // Retorne o novo array completo.

  return ["A Ordem da Fênix", ...filmesAntigos, ...filmesNovos];
}

// -----------------------------------------------------------------------------
// 3. Iteração com .forEach (Cálculo de Volume)
// -----------------------------------------------------------------------------
export function calcularVolumeLegPress(series) {
  // TODO: 'series' é um array de objetos, ex: { repeticoes: 10, peso: 200 }
  // Use o .forEach() para iterar sobre as séries.
  // O "volume total" de um exercício é a soma de (repetições * peso) de cada série.
  // Calcule e retorne o volume total levantado em todo o exercício.
  
  let volumeTotal = 0;
  
  series.forEach(serie => {
    volumeTotal += serie.repeticoes * serie.peso;
  });
  
  return volumeTotal;
}

// -----------------------------------------------------------------------------
// 4. Iteração com for...of (Análise de Monitoramento)
// -----------------------------------------------------------------------------
export function monitorarSysPulse(leituras, focarCpu) {
  // TODO: 'leituras' é um array de objetos, ex: { cpu: 85, ram: 60 }
  // 'focarCpu' é um booleano.
  // Use um loop 'for...of'.
  // Se 'focarCpu' for true, conte quantas vezes a CPU passou de 80% (cpu > 80).
  // Se 'focarCpu' for false, conte quantas vezes a RAM passou de 70% (ram > 70).
  // Retorne a contagem final.
  // Desafio Ouro: Tente usar aquela lógica de uma linha só (OU e E) que vimos ontem!

  let contador = 0;
  
  for (const leitura of leituras) {
    if (focarCpu && leitura.cpu > 80) contador++;
    if (!focarCpu && leitura.ram > 70) contador++;
  }
  
  return contador;
}