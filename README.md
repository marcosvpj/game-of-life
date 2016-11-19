##Game of Life

[![Code Health](https://landscape.io/github/marcosvpj/game-of-life/master/landscape.svg?style=flat-square)](https://landscape.io/github/marcosvpj/game-of-life/master)


![Game of life](/game-of-life-crop.gif)

##Descrição

Este "jogo" é na realidade um jogo sem jogador, o que quer dizer que sua evolução é determinada pelo seu estado inicial, não necessitando de nenhuma entrada de jogadores humanos. 
Cada célula tem oito "vizinhos", que são as células adjacentes, incluindo as diagonais. Cada célula pode estar em dois estados: "viva" ou "morta".
O estado do tabuleiro evolui e se modifica em pequenas passagens de tempo. Os estados de todas as células em um instante são considerados para calcular o estado de todas as células no instante seguinte. 
Todas as células são atualizadas simultaneamente. As transições dependem apenas do número de vizinhos vivos.

##Regras

As regras são simples e elegantes:

Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.

É importante entender que todos os nascimentos e mortes ocorrem simultaneamente. Juntos eles constituem uma geração ou, como podemos chamá-los, um "instante" na história da vida completa da configuração inicial.



[https://pt.wikipedia.org/wiki/Jogo_da_vida](https://pt.wikipedia.org/wiki/Jogo_da_vida)