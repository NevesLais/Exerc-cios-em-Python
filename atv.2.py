nbaPontosPorJogo = 200
brasileiraoGolsPorJogo = 2.53

nbaPontosPorMinuto = nbaPontosPorJogo / 48
print("pontos nba por minuto "+str(nbaPontosPorMinuto))
nbaPontosPorJogoEquivalentes = nbaPontosPorMinuto * 96
print("pontos por jogo equivalentes "+str(nbaPontosPorJogoEquivalentes))

pontos_mais = nbaPontosPorJogoEquivalentes - brasileiraoGolsPorJogo
print("pontos a mais equivalentes na nba "+str(pontos_mais))'''


nbaPontosPorJogo = 200
brasileiraoGolsPorJogo = 2.53

nbaPontosPorMinuto = nbaPontosPorJogo / 48
pontos_mais = (nbaPontosPorMinuto * 96) - brasileiraoGolsPorJogo

print("pontos a mais equivalentes na nba "+str(pontos_mais))
