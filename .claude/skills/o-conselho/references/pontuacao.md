# Pontuação

Todos os números vêm dos cartões das cadeiras. O Presidente calcula, nunca inventa. Use a última rodada que aconteceu (Rodada 3 se houve, senão Rodada 2).

## Nota das opções (o número principal)

Todo cartão dá nota de 0 a 10 a toda opção. Para cada opção:

`nota da opção = soma(peso x nota da cadeira para a opção) / soma(pesos)`, uma casa decimal.

A **opção recomendada** é a de maior nota, a não ser que uma trava abaixo a remova. Mostre a conta de cada opção numa linha, por exemplo: `B (3x6 + 2x7 + 1x8 + ...) / 22 = 6,7`.

## Faixas de veredito (sobre a nota da opção recomendada)

| Nota da opção | Veredito |
|---|---|
| 7,5 a 10 | VAI |
| 6,0 a 7,4 | VAI COM CONDIÇÕES |
| 4,5 a 5,9 | REFORMULE |
| abaixo de 4,5 | NÃO FAÇA |

Dois rótulos substituem a faixa quando servem melhor, e o relatório diz por quê:

- **ESPERE**: a opção recomendada é boa mas depende de um pré-requisito que ainda não existe (resultado de teste, caixa, contratação). ESPERE sempre nomeia o gatilho e a data que transformam em VAI, e o que acontece se o gatilho falhar.
- **NÃO FAÇA** também vale quando "não fazer" é a opção de maior nota.

## Apoio à resolução

A NOTA FINAL da Rodada 3 é o apoio de cada cadeira à minuta como escrita. Informe a média ponderada como "Apoio à resolução". Ela mede o quanto o plano do Presidente capturou a sala, não se a ideia é boa.

## Travas (aplicadas depois da faixa, e declaradas no relatório)

1. **Trava de ruína.** Qualquer cadeira que termine em `RISCO DE RUÍNA: provável` na opção recomendada limita o veredito a REFORMULE até a resolução nomear uma mitigação que essa cadeira aprovou. Uma cadeira em risco de ruína pesa mais que dez cadeiras animadas.
2. **Trava de porta de mão única.** Se a opção recomendada é porta de mão única (pela cadeira Bezos ou pela maioria) e a amplitude nela é 4 ou mais, limite a VAI COM CONDIÇÕES e torne o teste mais barato uma pré-condição.
3. **Checagem de unanimidade.** Se a opção favorita de toda cadeira é a mesma e as notas estão dentro de 1 ponto na Rodada 1, o Presidente nomeia a alternativa mais forte não defendida como ponto de discórdia na Rodada 2 e pede às cadeiras cujos pilares estão mais em risco que a defendam com força total.

## Amplitude e confiança

- `amplitude` = maior menos menor nota das cadeiras na opção recomendada.
- `confiança do conselho` = média da confiança das cadeiras x 2, arredondada, menos 1 se a amplitude for 5 ou mais. Escala de 1 a 10.
- Informe as duas. Um 7,0 com amplitude 1 é uma resposta diferente de um 7,0 com amplitude 6.

## Placar dos pilares

Uma coluna por cadeira: a NOTA DO PILAR final, que é o julgamento da cadeira sobre a opção recomendada só no seu pilar. Todo pilar com 4 ou menos ganha uma correção nomeada em "O que fazer agora", mesmo quando o veredito é VAI.

| Pilar | Dimensão |
|---|---|
| Dinheiro e capital (Buffett) | Risco e eficiência de capital |
| Estratégia e decisões (Bezos) | Encaixe estratégico e reversibilidade |
| Engenharia e primeiros princípios (Musk) | Custo, simplicidade e velocidade |
| Mentalidade, vendas e execução no Brasil (Flávio) | Disposição, venda e realidade local |
| Ofertas, preço e vendas (Hormozi) | Força da oferta e economia unitária |
| Produto e startups (Graham) | Demanda real e crescimento |
| Operações e escala (Wickman) | Prontidão operacional |
| Renda, perenidade e dividendos (Barsi) | Renda perene para o dono |
| Produto, experiência e foco (Jobs) | Qualidade da experiência e foco |
| Ambição, tecnologia e escala (Page) | Potencial 10x e escala |
| Pessoas, cultura e sociedade (Benchimol) | Sócios, cultura e cliente no centro |
