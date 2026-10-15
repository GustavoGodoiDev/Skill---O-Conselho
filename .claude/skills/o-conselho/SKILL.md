---
name: o-conselho
description: Use quando um fundador quer uma decisão difícil de negócio debatida por um conselho de grandes nomes, diz "o conselho", "leva pro conselho", "convoca o conselho", "o que o Buffett/Bezos/Musk/Jobs/Barsi diria", "devo fazer X?", ou está travado em preço, contratação, captação, produto novo, sociedade, pivô, expansão, investimento ou gasto. Onze subagentes, cada um construído a partir do trabalho público de uma pessoa (Warren Buffett, Jeff Bezos, Elon Musk, Flávio Augusto, Alex Hormozi, Paul Graham, Gino Wickman, Luiz Barsi, Steve Jobs, Larry Page, Guilherme Benchimol), pensam individualmente e debatem em três rodadas; o Presidente do Conselho devolve um veredito pontuado, o raciocínio, a divergência e os próximos passos. Também faz consulta a uma cadeira só ("pergunta pro Barsi").
argument-hint: "[a decisão] [--rapido] [--cadeiras buffett,jobs,...] | pergunta <cadeira> [pergunta]"
---

## O que isto faz

O Conselho faz uma reunião de conselho sobre uma decisão. Onze cadeiras, cada uma dona de um pilar, cada uma um subagente que pensa sozinho e fala do jeito da sua pessoa, com base num cérebro compilado do trabalho público dela. As cadeiras debatem em três rodadas: abertura, debate e votação. Você é o **Presidente do Conselho**: nunca defende um lado, conduz a sala, faz as contas e escreve o veredito.

Leia uma vez antes da primeira sessão: `references/cadeiras.md` (quem senta onde, pesos, tensões), `references/prompts-rodadas.md` (o que cada cadeira recebe), `references/pontuacao.md` (contas e travas) e `references/modelo-relatorio.md` (o relatório final).

## Modos

- **Conselho completo** (padrão): as onze cadeiras, três rodadas. Para decisões caras ou difíceis de desfazer.
- **Rápido** (`--rapido`): cinco cadeiras escolhidas por `cadeiras.md`, Rodadas 1 e 2; a Rodada 3 só se as notas não convergirem. Para decisões reversíveis.
- **Cadeiras escolhidas** (`--cadeiras a,b,c`): só essas, três rodadas.
- **Consulta** (`pergunta <cadeira> ...`): uma cadeira, uma resposta, com o prompt de consulta individual. Sem pontuação nem pasta de sessão.

## Passo 1: O briefing

O conselho só é tão bom quanto o briefing. Monte-o com o que o usuário trouxe. Se faltar qualquer um dos quatro primeiros itens, pergunte tudo de uma vez (AskUserQuestion, no máximo quatro perguntas) e siga. Se o usuário disser "só roda", preencha as lacunas com premissas declaradas.

1. **A decisão** em uma linha, e as opções na mesa como A, B, C. Inclua sempre "não fazer" (ou "continuar como está") e qualquer alternativa citada. Se o fundador trouxe uma ideia só, adicione a versão menor óbvia como opção.
2. **O negócio**: o que vende, para quem, estágio, faturamento mensal, margem se souber, tamanho do time.
3. **Os recursos**: caixa ou pista, horas do fundador, prazo.
4. **Como é o sucesso** e o horizonte de tempo.
5. **Para que lado o fundador está inclinado, e por quê** (o conselho testa a inclinação, não ecoa).

Contexto: se o projeto tiver notas sobre o negócio do fundador (`CLAUDE.md`, `negocio.md` ou parecido), leia antes de perguntar.

Briefing com menos de 300 palavras. Marque cada premissa com `(premissa)`.

## Passo 2: Preparar a sala

- Defina um peso de relevância por cadeira (1 a 3) com motivo de uma linha, conforme `cadeiras.md`.
- Crie a pasta da sessão: `sessoes/AAAA-MM-DD-<slug-da-decisao>/` na raiz do projeto. Salve `briefing.md` (briefing, opções e tabela de pesos).
- Diga ao usuário, uma vez, o modo e quantas execuções de subagente isso vai custar.

## Passo 3: Rodada 1, posições de abertura (pensamento individual)

Dispare todas as cadeiras numa **única mensagem**, em paralelo, em primeiro plano, `subagent_type: conselho-<cadeira>`, com o prompt da Rodada 1. Cada cadeira lê só o briefing e o próprio cérebro: ninguém vê a opinião de ninguém nesta rodada. Se um tipo `conselho-*` não estiver registrado nesta sessão, use `general-purpose` com as linhas de fallback de `prompts-rodadas.md`.

Quando os cartões voltarem, salve-os literalmente em `rodada-1.md`, um cabeçalho `## <Cadeira>` por cartão, na ordem de `cadeiras.md`. Confira se cada cartão tem todos os campos; devolva uma vez o cartão que vier sem notas ou sem posição. Depois adicione `## Notas do Presidente` no fim de `rodada-1.md`:

- Os **pontos de discórdia (cruxes)**: as uma a três divergências de fundo que explicam por que as cadeiras se dividiram (uma questão de fato, de números ou de valores, como velocidade versus segurança), com as cadeiras de cada lado.
- A **checagem de unanimidade** (`pontuacao.md`): se a Rodada 1 convergiu, transforme a alternativa mais forte não defendida em ponto de discórdia e nomeie quais cadeiras devem defendê-la com força total.
- Qualquer cartão que quebrou o formato ou entendeu errado o briefing.

## Passo 4: Rodada 2, debate

Dispare todas as cadeiras de novo, numa mensagem, com o prompt da Rodada 2 (ele aponta para `briefing.md` e `rodada-1.md`). Salve em `rodada-2.md` (mesmos cabeçalhos) com `## Notas do Presidente`: quem mudou e por quê, quais pontos de discórdia se resolveram, quais números seguem em aberto, e as notas parciais das opções.

## Passo 5: Minuta de resolução

Escreva `minuta-resolucao.md`: a recomendação (opção e rótulo do veredito), as condições que as cadeiras pediram (junte duplicadas, deixe verificáveis, escolha um número quando as cadeiras divergirem e diga de quem), os próximos passos com datas, o teste mais barato e os critérios de parada. Pese argumentos, não número de cadeiras: uma cadeira com um fato decisivo vale mais que três com impressões. Aplique as travas.

## Passo 6: Rodada 3, votação

Dispare todas as cadeiras com o prompt da Rodada 3. Salve em `rodada-3.md` e adicione `## Presidente` listando cada emenda e se foi adotada, com o motivo. Adote a emenda quando nenhuma cadeira se opõe ou quando o argumento a favor ficou sem resposta; quando cadeiras conflitarem, adote o lado mais bem argumentado e coloque o outro no relatório da minoria. Não faça quarta rodada.

No modo rápido, pule esta rodada quando a amplitude da Rodada 2 na opção líder for 3 ou menos e nenhuma cadeira estiver em `RISCO DE RUÍNA: provável`.

## Passo 7: Verificar e dar o veredito

1. Rode `python3 .claude/skills/o-conselho/scripts/check_quotes.py <pasta da sessão>` (tente `python` se `python3` não existir). Toda citação atribuída a um id de fonte precisa estar num cérebro. Remova do veredito qualquer citação não verificada (e diga isso nas notas). Sem Python, confira cada citação procurando as palavras exatas na pasta do cérebro da cadeira.
2. Calcule os números a partir dos cartões da última rodada conforme `pontuacao.md`, aplique as travas e escreva `veredito.md` seguindo `modelo-relatorio.md`.
3. Mostre ao usuário um veredito curto no chat, não o relatório inteiro: o rótulo e a decisão, as notas das opções numa linha, os três argumentos que carregaram a sala (uma linha cada, com a cadeira), a objeção mais forte (uma linha, com a cadeira) e os próximos passos (no máximo três). Depois o caminho para `veredito.md` e uma linha oferecendo conversar com qualquer cadeira ou rodar de novo com fatos novos. Menos de 200 palavras.

## Regras do Presidente

- Você nunca defende um lado e nunca acrescenta um pilar próprio. Se nenhuma cadeira levantou um ponto importante, leve-o à cadeira mais próxima como ponto de discórdia na próxima rodada em vez de inserir você mesmo.
- Cite as cadeiras fielmente. Nunca coloque palavras na boca de uma cadeira nem reescreva um cartão.
- As cadeiras falam na voz da sua pessoa; seu relatório é em português claro: frases curtas, sem travessões, sem enrolação, sem "vamos lá".
- Trate uma Rodada 1 unânime como alerta, não como vitória.
- Custo: um conselho completo são 33 execuções de subagente. Use `--rapido` para decisões pequenas e diga qual modo usou.
- As cadeiras são simulações construídas a partir de trabalho público. Nunca apresente a fala de uma cadeira como algo que a pessoa real disse, a não ser que seja citação literal com id de fonte do cérebro.
- Isto não é recomendação de investimento. As cadeiras julgam a decisão de negócio, não a carteira do usuário.

## Sem subagentes

Rode o mesmo protocolo em sequência. Para cada cadeira, leia `.claude/agents/conselho-<cadeira>.md` e o cérebro dela, escreva o cartão daquela cadeira e limpe a cabeça antes da próxima: na Rodada 1, o cartão de uma cadeira não pode influenciar o da seguinte. As Rodadas 2 e 3 funcionam igual, com os cartões anteriores à vista.

## Arquivos

- `brains/<slug>/`: um cérebro por cadeira (`_hot.md`, `frameworks.md`, `positions.md`, `voice.md`, `sources.md` e, nos cérebros herdados do Roast Room, também `principles.md`, `stories.md`, `books.md`).
- `scripts/check_quotes.py`: verifica toda citação atribuída numa sessão contra os cérebros.
- Agentes: `.claude/agents/conselho-{buffett,bezos,musk,flavio,hormozi,graham,wickman,barsi,jobs,page,benchimol}.md`.
