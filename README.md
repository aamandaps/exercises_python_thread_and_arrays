## Exercícios:
<p>1) Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id
como parâmetro e imprima no console o texto “Thread #” + id. Antes de imprimir o valor, deve-
se fazer um sleep de 0.5 segundos.</p>

<p>2) Fazer uma aplicação que, na main, inicialize uma variável id, inteira e inicialize 5 variáveis
inteiras para valores, crie um vetor de parâmetros, com o id como primeiro parâmetro e um
vetor com os 5 valores recebidos. As variáveis que recebem os valores devem receber, cada
uma delas, um valor aleatório de 1 a 100. Esses parâmetros devem ser preenchidos para 3
chamadas de Threads. Faça 3 chamadas de Threads, passando os parâmetros e, cada Thread,
deve calcular a soma de cada linha (Cada iteração do laço, para a soma deve ser seguido por
um sleep de 0.2 segundos), ao final, deve-se imprimir a identificação da linha e o resultado da
soma.</p>

<p>3) Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1
sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância
máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o
tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para
cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu.
Assim que o sapo percorrer a distância máxima, a Thread deve apresentar que o sapo chegou.
</p>

<p>4) No Sistema Operacional Linux, o comando para realizar uma operação de ping com 10
iterações é ping -4 -c 10 <servidor> e no Sistema Operacional Windows, o comando para a
mesma função é ping -4 -n 10 <servidor>. Fazer uma aplicação Python que rode 3 Threads,
sendo que a Thread deve identificar o SO para rodar o comando certo, fazendo operação de
ping para os servidores UOL (www.uol.com.br), Terra (www.terra.com.br) e Google
(www.google.com.br). Cada thread deve ler a saída do ping imprimindo, a cada iteração, o
nome do servidor (usar fixo: UOL, Terra ou Google) e o tempo daquela iteração. Ao fim, deve-
se exibir o nome do servidor (usar fixo: UOL, Terra ou Google) e o tempo médio obtido pela
operação. Outros Sistemas Operacionais devem ser descartados.
