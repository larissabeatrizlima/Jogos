# General
Um jogo de dados onde cada jogadorem sua vez, tem três chances de arremessar os dados. Na primeira, joga os cinco dados; na segunda, conforme o resultado obtido, pode voltar a arremessar de um a cinco dados, mantendo os demais sobre a mesa, ou aceitar o resultado, dando a jogada por encerrada; na terceira, da mesma forma, pode arremessar de um a cinco dados (mesmo os que ele tenha mantido sobre a mesa entre o primeiro e o segundo arremesso) ou aceitar o resultado.

O resultado obtido ao final da jogada deve ser classificado, pelo próprio jogador, como uma das 13 possíveis combinações. De acordo com os dados obtidos na jogada, as combinações fornecem diferentes pontuações:

**Jogada de 1:** É marcada a soma de todos os dados de valor 1 (por exemplo: 1-1-1-4-5 vale 3 pontos);
**Jogadas de 2, 3, 4, 5 e 6:** correspondentes à jogada de 1 para os demais números (por exemplo: 3-3-4-4-5 vale 6 pontos se for considerada uma jogada de 3, ou 8 pontos se for considerada uma jogada de 4, ou ainda 5 pontos se for uma jogada de 5);
**Trinca:** Caso hajam três dados de mesmo valor na jogada, são marcados 30 pontos;
**Quadra:** Caso hajam quatro dados de mesmo valor na jogada, são marcados 40 pontos;
**Full house:** Caso hajam três dados de mesmo valor e os outros dois também tenham o mesmo valor, são marcados 50 pontos;
**Sequência alta:** Caso hajam entre os dados da jogada todos os valores 2, 3, 4, 5 e 6, são marcados 25 pontos;
**Sequência baixa:** Caso hajam entre os dados da jogada todos os valores 1, 2, 3, 4 e 5, são marcados 25 pontos;
**General:** Caso os cinco dados tenham o mesmo valor, são marcados 60 pontos;

Ao fim de todas as jogadas, é obrigatório escolher uma das combinações para marcar a pontuação. É possível escolher marcar 0 pontos em uma combinação, caso a jogada não cumpra os requisitos de pontuação.
Uma vez que uma combinação seja escolhida, ela não poderá mais ser escolhida por aquele jogador.

O jogo acaba quando os jogadores estiverem a cartela toda preenchida. Vence aquele que pontuar mais.

Regras retirado de:  http://lugardagente.blogspot.com/p/general.html


### Principais Bibliotecas:
* Pygame: `pip install pygame`
