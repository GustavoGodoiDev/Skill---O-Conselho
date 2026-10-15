# Prompts das rodadas

Cole estes prompts em cada chamada de Agent. Troque as partes entre colchetes. As cadeiras leem o briefing e as rodadas anteriores na pasta da sessão, então os cartões ficam literais sem precisar colar em todo prompt.

Tipo de agente: `conselho-<cadeira>`. Se esse tipo não estiver registrado nesta sessão (arquivos de agente carregam no início da sessão), use `general-purpose` e coloque estas linhas primeiro: `Leia .claude/agents/conselho-<cadeira>.md e siga como suas instruções durante toda esta tarefa. Só leia arquivos; não escreva nada.`

Caminhos nos prompts são relativos à raiz do projeto; informe a raiz absoluta uma vez no topo de cada prompt.

**Opções.** Quando o briefing lista opções (A, B, C, incluindo "não fazer"), todo cartão dá nota a toda opção. Quando é uma decisão de sim ou não, as opções são "fazer como proposto" e "não fazer".

**Nota do pilar.** A nota da cadeira para a opção que ela recomenda, julgada só pelo seu pilar.

---

## Rodada 1: posição de abertura

```
O CONSELHO, RODADA 1 DE 3: POSIÇÃO DE ABERTURA

Raiz do projeto: [caminho absoluto]. Você ocupa a cadeira [CADEIRA] ([pilar]). Leia o _hot.md do seu cérebro e depois no máximo três arquivos do cérebro que sirvam a esta decisão (frameworks.md e positions.md costumam ser os certos).

Leia o briefing: [pasta da sessão]/briefing.md

Pense sozinho: você não sabe o que as outras cadeiras acham e não tenta adivinhar.

Seu peso nesta decisão: [p]/3 ([motivo em uma linha]).

Responda na voz da sua cadeira, em português do Brasil, texto simples, menos de 350 palavras, exatamente neste formato:

CADEIRA: [CADEIRA] ([pilar])
POSIÇÃO: Sim forte | Sim | Sim com condições | Não | Não forte   (sobre a opção que você recomenda)
NOTAS DAS OPÇÕES: [A] n/10 · [B] n/10 · [C] n/10   (o quanto você apoia cada opção)
NOTA DO PILAR: n/10   ([dimensão]: a opção que você recomenda, julgada só pelo seu pilar)
CONFIANÇA: n/5
RISCO DE RUÍNA: nenhum | possível | provável   (perda irreversível que pode afundar a empresa ou o fundador, na opção que você recomenda)
PORTA: mão única | mão dupla   (quão reversível é a opção que você recomenda?)

A DECISÃO: uma frase, nomeando a opção ou uma variação.
POR QUÊ:
1. argumento, nomeando o framework ou princípio usado e o id da fonte, ex.: (Equação de Valor, S014)
2. ...
3. ...
O RISCO QUE EU VEJO: a maior coisa que pode dar errado.
O QUE ME FARIA MUDAR DE IDEIA: um fato ou número concreto.
O QUE EU FARIA ESTA SEMANA: uma ação.
PERGUNTA PARA O FUNDADOR: a pergunta que você faria antes de assinar.

Regras: argumente primeiro pelo seu pilar. Use os números reais do briefing e diga quais está assumindo quando faltarem. Coloque entre aspas só frases literais do seu cérebro, com o id da fonte. Não fique em cima do muro; o Presidente equilibra o conselho, você traz sua lente com força total.
```

---

## Rodada 2: debate

```
O CONSELHO, RODADA 2 DE 3: DEBATE

Raiz do projeto: [caminho absoluto]. Você ocupa a cadeira [CADEIRA]. Leia o _hot.md do seu cérebro de novo e qualquer arquivo do cérebro que precise para responder aos outros (no máximo três).

Leia: [pasta da sessão]/briefing.md e [pasta da sessão]/rodada-1.md (o cartão de cada cadeira e os pontos de discórdia do Presidente).

OS PONTOS DE DISCÓRDIA QUE O PRESIDENTE VÊ
1. [ponto]: [cadeiras de cada lado]. [Se esta cadeira está num lado, nomeie o argumento que ela precisa responder.]
2. ...

Responda na voz da sua cadeira, em português do Brasil, menos de 300 palavras, exatamente neste formato:

CADEIRA: [CADEIRA]
DISCORDO MAIS DE: [cadeira]. O argumento dela em uma linha, depois sua réplica usando seus frameworks.
EU CONCEDO: o ponto mais forte que outra cadeira fez contra você, e o que ele muda. "Nada" só se você souber dizer por que o melhor ponto dela falha.
SOBRE OS PONTOS DE DISCÓRDIA: sua resposta a cada um, uma ou duas linhas.
POSIÇÃO: ...
NOTAS DAS OPÇÕES: [A] n/10 · [B] n/10 · [C] n/10
NOTA DO PILAR: n/10
CONFIANÇA: n/5
RISCO DE RUÍNA: nenhum | possível | provável
MUDEI: não | sim, de X para Y, porque ...
MINHAS CONDIÇÕES PARA O SIM: até três, concretas e verificáveis (um número, uma data, um resultado de teste).

Regras: enfrente os argumentos reais que estão na mesa. Só mude por um argumento melhor, nunca para agradar. Se todos concordam com você, ache a parte mais fraca do seu caso e diga.
```

---

## Rodada 3: votação

```
O CONSELHO, RODADA 3 DE 3: VOTAÇÃO DA MINUTA

Raiz do projeto: [caminho absoluto]. Você ocupa a cadeira [CADEIRA]. Você já argumentou em duas rodadas; leia só o seu _hot.md se precisar.

Leia: [pasta da sessão]/briefing.md, a sua seção de [pasta da sessão]/rodada-2.md, e [pasta da sessão]/minuta-resolucao.md.

Responda na voz da sua cadeira, em português do Brasil, menos de 150 palavras, exatamente neste formato:

CADEIRA: [CADEIRA]
VOTO: Aprovo | Aprovo com emenda | Divirjo
NOTAS DAS OPÇÕES: [A] n/10 · [B] n/10 · [C] n/10   (considerando as condições da resolução)
NOTA FINAL: n/10   (seu apoio à minuta como está escrita)
NOTA FINAL DO PILAR: n/10
EMENDA OU DIVERGÊNCIA: uma ou duas frases (o que mudar, ou por que diverge). Em branco se aprovar.
UMA LINHA PARA O FUNDADOR: a coisa do seu pilar que ele não pode esquecer.
```

---

## Consulta individual

```
O CONSELHO, CONSULTA INDIVIDUAL

Raiz do projeto: [caminho absoluto]. Você ocupa a cadeira [CADEIRA]. Leia o _hot.md do seu cérebro e depois no máximo quatro arquivos do cérebro que sirvam à pergunta.

A PERGUNTA
[pergunta, mais qualquer contexto]

Responda na voz da sua cadeira, em primeira pessoa, em português do Brasil, menos de 500 palavras: sua decisão, seu raciocínio com frameworks nomeados e ids de fonte, o que você faria esta semana e a pergunta que você faria de volta. Não narre a pessoa em terceira pessoa. Termine com "Fontes:" e os ids usados.
```
