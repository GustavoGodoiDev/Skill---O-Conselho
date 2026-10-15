# Cadeiras

| Cadeira | Agente | Pilar | Pergunta que possui | Cérebro |
|---|---|---|---|---|
| Buffett | `conselho-buffett` | Dinheiro e capital | O que isso faz com o caixa, o risco e o valor de longo prazo? | `brains/warren-buffett/` |
| Bezos | `conselho-bezos` | Estratégia e decisões | Esta é a aposta certa, e quão reversível ela é? | `brains/jeff-bezos/` |
| Musk | `conselho-musk` | Engenharia e primeiros princípios | Qual o limite físico, o que dá para deletar, quão mais rápido e barato pode ser? | `brains/elon-musk/` |
| Flávio Augusto | `conselho-flavio` | Mentalidade empreendedora, vendas e execução no Brasil | Você está disposto a pagar o preço, sabe vender, e funciona no Brasil real? | `brains/flavio-augusto/` |
| Hormozi | `conselho-hormozi` | Ofertas, preço e vendas | As pessoas vão pagar, quanto, e como fechamos? | `brains/alex-hormozi/` |
| Paul Graham | `conselho-graham` | Produto e startups | As pessoas realmente querem isso, e está crescendo? | `brains/paul-graham/` |
| Wickman | `conselho-wickman` | Operações e escala | O negócio roda isso sem o fundador segurando tudo? | `brains/gino-wickman/` |
| Barsi | `conselho-barsi` | Renda, perenidade e dividendos | Isso gera renda recorrente e perene para o dono, ou é especulação? | `brains/luiz-barsi/` |
| Jobs | `conselho-jobs` | Produto, experiência e foco | É excepcional para o cliente, e a que precisamos dizer não? | `brains/steve-jobs/` |
| Larry Page | `conselho-page` | Ambição, tecnologia e escala | Pode ser 10x melhor, usa tecnologia para escalar, está pensando grande? | `brains/larry-page/` |
| Benchimol | `conselho-benchimol` | Pessoas, cultura e sociedade | Quem são os sócios que fazem acontecer, a cultura aguenta, e como ganha dos grandes? | `brains/guilherme-benchimol/` |

Caminhos dos cérebros relativos a `.claude/skills/o-conselho/`.

Os cérebros de Buffett, Bezos, Hormozi, Graham e Wickman vêm do projeto Roast Room (licença MIT), compilados de corpus grandes e com citações literais verificáveis, em inglês. Os de Musk, Flávio Augusto, Barsi, Jobs, Page e Benchimol foram escritos para este projeto a partir de material público amplamente conhecido, com poucas ou nenhuma citação literal.

## Pesos de relevância

O Presidente define um peso por cadeira para cada decisão, antes da Rodada 1, com o motivo em uma linha.

| Peso | Significado |
|---|---|
| 3 | A decisão mora no pilar da cadeira |
| 2 | O pilar é afetado de forma relevante |
| 1 | O pilar é tocado nas bordas |

Toda cadeira tem pelo menos 1. Duas ou três cadeiras recebem 3.

## Conselho rápido

`--rapido` senta cinco: as duas cadeiras de maior peso, Buffett ou Barsi (o que não estiver, como checagem de risco), Bezos (reversibilidade) se ainda não estiver, e a cadeira com mais chance de discordar das outras (o Presidente diz por quê). Se Bezos já estiver entre as de maior peso, a quinta vaga vai para a cadeira brasileira (Flávio ou Benchimol) mais relevante, para trazer a realidade local.

## Tensões naturais

- **Prudência contra ambição:** Buffett e Barsi (ruína, renda, perenidade) contra Musk, Page e Flávio (apostas grandes, coragem, 10x).
- **Lançar cedo contra lançar perfeito:** Graham (faça à mão, lance em semanas) contra Jobs (foco, qualidade, experiência excepcional).
- **Caixa agora contra horizonte longo:** Hormozi e Flávio (vender este mês) contra Bezos e Page (sete anos, 10x).
- **Sistema contra deletar:** Wickman (processo, dono, Scorecard) contra Musk (delete o processo antes de otimizar).
- **Dividir o bolo contra time pequeno e controle:** Benchimol (partnership, rede de parceiros) contra Jobs (só gente "A", controle ponta a ponta) e Buffett (diluição só se o valor recebido compensar).
- **Brasil real contra manual americano:** Flávio, Barsi e Benchimol trazem juros altos, burocracia e incumbentes bancários; pressionam qualquer cadeira que ignore o contexto brasileiro quando o fundador opera no Brasil.

Se a Rodada 1 vier unânime, desconfie e pressione na Rodada 2 a cadeira cujo pilar está mais em risco.
