# O Conselho

Leve uma decisão difícil de negócio e onze conselheiros simulados pensam sozinhos, debatem entre si e devolvem um veredito pontuado. Roda no Claude Code: cada conselheiro é um subagente com seu próprio "cérebro", e o Claude Code é o Presidente do Conselho, que conduz as rodadas, faz as contas e escreve o veredito.

Inspirado em [roast-room](https://github.com/nateherkai/roast-room) (MIT).

| Cadeira | Pilar | A pergunta que ela possui |
|---|---|---|
| Warren Buffett | Dinheiro e capital | O que isso faz com o caixa, o risco e o valor de longo prazo? |
| Jeff Bezos | Estratégia e decisões | Esta é a aposta certa, e quão reversível ela é? |
| Elon Musk | Engenharia e primeiros princípios | Qual o limite físico, o que dá para deletar, quão mais rápido e barato? |
| Flávio Augusto | Mentalidade, vendas e execução no Brasil | Você paga o preço, sabe vender, e funciona no Brasil real? |
| Alex Hormozi | Ofertas, preço e vendas | As pessoas vão pagar, quanto, e como fechamos? |
| Paul Graham | Produto e startups | As pessoas realmente querem isso, e está crescendo? |
| Gino Wickman | Operações e escala | O negócio roda isso sem o fundador segurando tudo? |
| Luiz Barsi | Renda, perenidade e dividendos | Isso gera renda perene para o dono, ou é especulação? |
| Steve Jobs | Produto, experiência e foco | É excepcional para o cliente, e a que dizemos não? |
| Larry Page | Ambição, tecnologia e escala | Pode ser 10x, escala com tecnologia, está pensando grande? |
| Guilherme Benchimol | Pessoas, cultura e sociedade | Quem são os sócios, a cultura aguenta, como ganha dos grandes? |

## Como usar

Abra o Claude Code nesta pasta (`claude`) e digite:

```
/o-conselho Tenho uma agência de marketing que fatura R$ 80 mil/mês com 12 clientes,
margem de 30%, 6 pessoas no time e R$ 150 mil em caixa. Devo (A) lançar um curso online,
(B) contratar um segundo vendedor, ou (C) continuar como está? Sucesso é R$ 150 mil/mês
em 12 meses. Estou inclinado ao curso porque escala sem gente.
```

O que colocar na pergunta:

- **A decisão** em uma linha e **as opções** (duas ou três; "continuar como está" conta).
- **Seus números**: faturamento, margem, caixa, tamanho do time.
- **Seus limites**: prazo, horas, orçamento.
- **Como é o sucesso**, e até quando.
- **Para que lado você está inclinado**, e por quê. O conselho testa a inclinação em vez de concordar.

Faltou algo? O Presidente pergunta antes de começar.

Outros modos:

- `/o-conselho --rapido ...` senta cinco conselheiros por duas rodadas. Para decisões menores e reversíveis.
- `/o-conselho --cadeiras barsi,buffett,jobs ...` senta só quem você escolher.
- `/o-conselho pergunta musk ...` uma resposta de um conselheiro só.

## Como funciona

1. **Briefing.** O Presidente monta um briefing curto com opções A, B, C e define o peso (1 a 3) de cada cadeira para essa decisão.
2. **Rodada 1, pensamento individual.** As onze cadeiras rodam em paralelo, cada uma lendo só o briefing e o próprio cérebro. Ninguém vê a opinião de ninguém.
3. **Rodada 2, debate.** Cada cadeira lê todas as aberturas e os pontos de discórdia, rebate, concede e pode mudar de posição.
4. **Rodada 3, votação** de uma minuta de resolução, com emendas.
5. **Veredito.** Notas ponderadas por opção, travas de ruína e de porta de mão única, relatório da minoria, condições, próximos passos. Salvo em `sessoes/<data>-<decisao>/veredito.md`.

Custo: o conselho completo são 33 execuções de subagente e consome bastante do seu plano. Use `--rapido` para decisões pequenas.

## O que tem dentro

| Caminho | O quê |
|---|---|
| `.claude/skills/o-conselho/SKILL.md` | O protocolo do Presidente |
| `.claude/skills/o-conselho/references/` | Cadeiras e pesos, prompts das rodadas, pontuação, modelo de relatório |
| `.claude/skills/o-conselho/brains/` | Um cérebro por conselheiro |
| `.claude/skills/o-conselho/scripts/check_quotes.py` | Confere se toda citação existe no cérebro |
| `.claude/agents/conselho-*.md` | Os onze subagentes |
| `sessoes/` | Suas sessões (fora do git) |

## Sobre os conselheiros

São simulações construídas a partir do trabalho público de cada pessoa. Não são as pessoas, não falam por elas, e nenhuma delas é afiliada ou endossa este projeto. Não é recomendação de investimento.

- Os cérebros de **Buffett, Bezos, Hormozi, Paul Graham e Wickman** vêm do roast-room (MIT, AI Automation Society; ver `THIRD_PARTY_LICENSE_roast-room.txt`), compilados de corpus grandes, em inglês, com citações literais e fontes.
- Os cérebros de **Musk, Flávio Augusto, Barsi, Jobs, Larry Page e Benchimol** foram escritos para este projeto a partir de material público amplamente conhecido (livros, palestras, entrevistas), listado em cada `sources.md`. Têm poucas citações literais (Musk, Jobs, Page) ou nenhuma (Flávio, Barsi, Benchimol); o resto é paráfrase. Vale enriquecê-los com transcrições reais para ganhar fidelidade.
