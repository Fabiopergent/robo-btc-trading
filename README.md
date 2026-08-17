# robo-btc-trading
criação de robo para cripto que opere de forma autonoma.


ROBO BTC TRADING — REGRAS E ESTRUTURA DO PROJETO
1. OBJETIVO DO ROBÔ

Criar um robô de trading para operar BTC inicialmente em simulação/backtest, utilizando as regras de Price Action e gerenciamento de risco estudadas no curso.

Capital planejado para futura operação real:

R$ 100,00

A operação real somente será considerada depois de:

Desenvolvimento completo.
Testes unitários.
Backtests.
Simulações.
Avaliação dos resultados.
Teste em ambiente real/simulado da Binance.
Validação da estratégia.

O robô não deve operar dinheiro real durante a fase de desenvolvimento.

2. FILOSOFIA PRINCIPAL

O robô deve ser conservador.

Prioridades:

Preservar capital.
Evitar entradas sem confirmação.
Não operar em lateralização.
Não tentar prever o mercado.
Seguir regras objetivas.
Respeitar Stop Loss.
Buscar relação risco/retorno mínima de 1:3.
Não realizar operações por emoção ou impulso.

Regra principal:

Se o setup não estiver confirmado, o robô NÃO entra.

3. TIMEFRAME

Timeframe inicialmente utilizado:

30 minutos

O timeframe poderá ser alterado futuramente através do config.py, sem alterar a lógica principal do robô.

4. FLUXO PRINCIPAL DO ROBÔ

O raciocínio do robô deverá seguir esta sequência:

CANDLES
   ↓
PIVÔS
   ↓
ESTRUTURA
   ↓
TENDÊNCIA
   ↓
SUPORTE / RESISTÊNCIA
   ↓
ROMPIMENTO
   ↓
RETESTE
   ↓
PRICE ACTION
   ↓
VOLUME
   ↓
SETUP
   ↓
GERENCIAMENTO DE RISCO
   ↓
ENTRADA
   ↓
STOP LOSS
   ↓
TAKE PROFIT

Nenhuma etapa deve ser ignorada.

5. PIVÔ — 3 CANDLES

Foi escolhido o sistema de pivô de 3 candles.

O candle central é comparado com o candle anterior e posterior.

Pivot High

O candle central precisa possuir máxima maior que as máximas dos dois candles vizinhos.

High anterior < High central > High posterior
Pivot Low

O candle central precisa possuir mínima menor que as mínimas dos dois candles vizinhos.

Low anterior > Low central < Low posterior
Pivô ambíguo

Se o mesmo candle for simultaneamente:

PIVOT HIGH
+
PIVOT LOW

será classificado como:

AMBIGUOUS

e não deverá ser utilizado para construir a estrutura.

Motivo:

Quando o contexto não está claro, o robô não deve forçar uma interpretação.

6. ESTRUTURA DE MERCADO

A estrutura utiliza:

HH = Higher High
HL = Higher Low
LH = Lower High
LL = Lower Low
HH

Novo topo maior que o topo anterior.

High atual > High anterior
LH

Novo topo menor que o topo anterior.

High atual < High anterior
HL

Novo fundo maior que o fundo anterior.

Low atual > Low anterior
LL

Novo fundo menor que o fundo anterior.

Low atual < Low anterior
7. IDENTIFICAÇÃO DA TENDÊNCIA

A tendência não será determinada simplesmente porque existe um HH ou HL isolado.

Será necessária confirmação estrutural.

Tendência de alta

Sequência:

HH
HL
HH
HL

Resultado:

UPTREND

Interpretação:

Topos ascendentes
+
Fundos ascendentes
Tendência de baixa

Sequência:

LL
LH
LL
LH

Resultado:

DOWNTREND

Interpretação:

Fundos descendentes
+
Topos descendentes
Estrutura insuficiente

Quando não houver informações suficientes:

UNKNOWN

O robô não deve operar.

Lateralização

Quando a sequência não confirmar uma tendência:

SIDEWAYS

Regra:

SIDEWAYS = NÃO OPERAR.

8. DIREÇÃO DAS OPERAÇÕES

A tendência determina o lado em que o robô pode procurar oportunidades.

UPTREND
UPTREND
   ↓
PROCURAR COMPRA
DOWNTREND
DOWNTREND
   ↓
PROCURAR VENDA
SIDEWAYS
SIDEWAYS
   ↓
NÃO OPERAR

O robô não deve operar contra a tendência principal.

9. SUPORTE E RESISTÊNCIA

Os pivôs serão utilizados como base para encontrar regiões.

Pivot High

Pode formar:

RESISTANCE
Pivot Low

Pode formar:

SUPPORT

Não trabalharemos inicialmente com uma linha exata.

Serão utilizadas zonas de preço.

Exemplo:

RESISTANCE


109.67 ───────── 110.33

A tolerância da região será definida através do:

config.py

pela variável:

ZONE_TOLERANCE
10. AGRUPAMENTO DE REGIÕES

Regiões do mesmo tipo que estejam sobrepostas ou suficientemente próximas poderão ser agrupadas.

Exemplo:

Resistance 100.00
Resistance 100.10
Resistance 100.20

Pode ser transformado em:

RESISTANCE
100.00 ───────── 100.20

Objetivo:

Evitar que o robô trate vários pivôs muito próximos como várias resistências independentes.

11. ROMPIMENTO

O rompimento será tratado como uma etapa própria.

O robô não deverá considerar simplesmente:

Preço passou da resistência
=
COMPRA

Isso pode ser um falso rompimento.

O fluxo será:

RESISTÊNCIA
     ↓
PREÇO ROMPE
     ↓
CONFIRMAR ROMPIMENTO
     ↓
AGUARDAR RETESTE
     ↓
CONFIRMAÇÃO

Somente depois disso o setup poderá continuar.

12. RETESTE

O reteste será diferente do rompimento.

Rompimento

O preço supera uma região importante.

Reteste

Depois do rompimento, o preço retorna para testar a região rompida.

Exemplo:

ANTES:


RESISTÊNCIA
──────────────


Preço
  ↑
  │
  │

Depois:

ROMPIMENTO
──────────────
      ↑
      │ preço rompe

Depois:

       preço
         ↓
──────────────
   RETESTE

A antiga resistência pode passar a funcionar como suporte.

13. FALSO ROMPIMENTO

O robô deverá evitar entradas baseadas somente em um rompimento momentâneo.

Exemplo:

RESISTÊNCIA
──────────────
      ↑
      │
      │ falso rompimento
      ↓
──────────────

Se não houver confirmação adequada:

NÃO ENTRAR
14. PRICE ACTION

Depois da estrutura, tendência, região e rompimento/reteste, o robô poderá utilizar Price Action como confirmação.

Padrões estudados:

Martelo
Martelo invertido
Engolfo
Doji
Estrela da manhã
Estrela da noite
Harami
Inside Bar
Outside Bar

Importante:

Um candle isolado nunca deverá gerar uma entrada sozinho.

O contexto é obrigatório.

15. VOLUME

O volume será utilizado como confirmação.

Não será utilizado sozinho para gerar entrada.

Exemplo:

Rompimento
+
aumento de volume
+
reteste
+
Price Action
=
maior qualidade do setup

Volume baixo durante um rompimento poderá aumentar a suspeita de falso rompimento.

16. SETUP

O setup deverá combinar várias condições.

Exemplo de compra:

UPTREND
   +
SUPORTE/RESISTÊNCIA relevante
   +
ROMPIMENTO
   +
RETESTE
   +
CONFIRMAÇÃO PRICE ACTION
   +
VOLUME
   +
RISCO/RETORNO adequado
   =
COMPRA

Se qualquer condição obrigatória não for satisfeita:

NÃO ENTRAR
17. GERENCIAMENTO DE RISCO

Capital inicial planejado:

R$ 100,00

O robô deverá calcular automaticamente o tamanho da posição.

Não será permitido simplesmente utilizar todo o saldo em uma operação.

O risco deverá ser controlado através de:

Position Size
Stop Loss
Take Profit
Risk/Reward
18. STOP LOSS

Toda operação deverá possuir Stop Loss definido antes da entrada.

Nunca entrar primeiro para depois decidir onde colocar o stop.

O Stop deverá ser calculado de acordo com a estrutura/setup.

19. TAKE PROFIT

Toda operação deverá possuir alvo definido.

Regra inicial:

Risco : Retorno
1 : 3

Exemplo:

Risco = R$ 1


Alvo = R$ 3

Não entrar se o setup não apresentar relação mínima adequada, salvo se posteriormente decidirmos alterar essa regra conscientemente.

20. POSIÇÃO

Regra definida:

Se já existe posição:
    procurar oportunidade de saída/gerenciamento


Se não existe posição:
    procurar nova oportunidade

O robô não deverá abrir várias operações simultâneas sem uma regra específica para isso.

Inicialmente:

uma posição por vez.

21. SIMULAÇÃO / BACKTEST

Antes de operar dinheiro real:

Código
 ↓
Teste unitário
 ↓
Backtest
 ↓
Simulação
 ↓
Paper Trading
 ↓
Avaliação
 ↓
Somente então
 ↓
Operação real

O primeiro objetivo não é ganhar dinheiro.

O primeiro objetivo é descobrir se:

o robô executa corretamente as regras que definimos.

22. ESTRUTURA ATUAL DO PROJETO
robo-btc-trading/
│
├── main.py
├── config.py
├── requirements.txt
│
├── strategy/
│   ├── __init__.py
│   ├── pivots.py
│   ├── trend.py
│   ├── support_resistance.py
│   ├── breakout.py
│   ├── retest.py
│   ├── price_action.py
│   ├── volume.py
│   └── setup.py
│
├── risk/
│   ├── __init__.py
│   ├── position_size.py
│   ├── stop_loss.py
│   └── take_profit.py
│
├── backtest/
│   ├── __init__.py
│   ├── engine.py
│   └── statistics.py
│
├── database/
│   ├── __init__.py
│   └── database.py
│
└── reports/
    ├── __init__.py
    └── charts.py
23. RESPONSABILIDADE DE CADA ARQUIVO
main.py

Orquestra o robô.

Recebe dados
↓
chama as estratégias
↓
toma decisão
config.py

Parâmetros configuráveis.

Exemplos:

TIMEFRAME
ZONE_TOLERANCE
RISCO
RISK/REWARD
strategy/pivots.py

Identificação dos pivôs.

PIVOT_HIGH
PIVOT_LOW
AMBIGUOUS
strategy/structure.py

Transforma pivôs em:

HH
HL
LH
LL
strategy/trend.py

Determina:

UPTREND
DOWNTREND
SIDEWAYS
UNKNOWN
strategy/support_resistance.py

Cria:

SUPPORT
RESISTANCE

e agrupa regiões próximas.

strategy/breakout.py

Responsável por identificar e validar rompimentos.

Próxima etapa do desenvolvimento.

strategy/retest.py

Verificará se o preço voltou para testar a região rompida.

strategy/price_action.py

Identificará padrões de candles.

strategy/volume.py

Analisará volume e suas confirmações.

strategy/setup.py

Juntará as condições e determinará:

SETUP VALID

ou:

SETUP INVALID
risk/position_size.py

Calcula quanto comprar/vender de acordo com o risco permitido.

risk/stop_loss.py

Calcula o Stop Loss.

risk/take_profit.py

Calcula o alvo.

backtest/engine.py

Simula as operações historicamente.

backtest/statistics.py

Calcula resultados como:

Número de operações
Win Rate
Loss Rate
Lucro
Prejuízo
Profit Factor
Drawdown
Risco/Retorno
database/database.py

Armazena dados das operações.

reports/charts.py

Gera gráficos e relatórios do desempenho.

24. ESTADO ATUAL DO ROBÔ

Até agora temos:

Pivô 3 candles             ✅
Pivô ambíguo               ✅
HH / HL / LH / LL          ✅
Estrutura                  ✅
Detecção de tendência      ✅
UPTREND                    ✅
DOWNTREND                  ✅
SIDEWAYS                   ✅
Suporte                    ✅
Resistência                ✅
Zonas de preço             ✅
Agrupamento de zonas       ✅

Ainda falta:

Rompimento                 ✅
Reteste                    ✅
Price Action               ✅⏳
Volume                     ✅
Setup final                ✅
Position Size              ✅
Stop Loss                  ✅
Take Profit                ✅
Integração do risco        ✅
Backtest Engine            ✅
Estatísticas               ✅
Backtest completo          ⏳
Simulação                  ⏳
Integração Binance         ⏳




🔒 Protocolo de desenvolvimento do robô
1. Antes de mexer em qualquer arquivo existente

Você me manda o conteúdo atual do arquivo.

Por exemplo:

breakout.py está assim:

...

Eu primeiro verifico:

o que já existe;
quais funções já foram criadas;
quais outras partes do robô dependem delas;
se a nova função realmente está faltando;
se precisamos adicionar, alterar ou simplesmente não mexer.

Não vou assumir que o arquivo está vazio.

2. Não vamos refazer módulos já concluídos

Por exemplo, neste momento:

pivots.py              🔒
structure.py           🔒
trend.py               🔒
support_resistance.py  🔒

Eles já estão funcionando.

Se precisarmos utilizá-los, vamos chamá-los, e não recriar suas funções dentro de outro arquivo.

Por exemplo:

breakout.py
      ↓
usa support_resistance.py
      ↓
usa trend.py

Não vamos copiar a lógica de suporte/resistência para breakout.py.

3. Controle de progresso

Vamos manter exatamente esta lista:

ROBO BTC — CHECKLIST DE DESENVOLVIMENTO


[✅] Pivô 3 candles
[✅] Pivô ambíguo
[✅] HH / HL / LH / LL
[✅] Estrutura
[✅] Tendência
[✅] UPTREND
[✅] DOWNTREND
[✅] SIDEWAYS
[✅] Suporte
[✅] Resistência
[✅] Zonas de preço
[✅] Agrupamento de zonas


[ ] Rompimento
[ ] Reteste
[ ] Price Action
[ ] Volume
[ ] Setup final
[ ] Position Size
[ ] Stop Loss
[ ] Take Profit
[ ] Integração do risco
[ ] Backtest completo
[ ] Estatísticas
[ ] Simulação
[ ] Integração Binance

E só mudamos [ ] para [✅] quando aquela etapa estiver realmente testada e concluída.

4. Quando uma etapa terminar

Vou avisar explicitamente:

🟢 ETAPA CONCLUÍDA — ROMPIMENTO

E vou informar:

Arquivo:
strategy/breakout.py


Status:
✅ Implementado
✅ Testado
✅ Integrado

Aí você atualiza seu arquivo .txt.

Assim seu documento externo vira uma espécie de backup da arquitetura e das regras do projeto.

5. Se encontrarmos um problema em uma etapa antiga

Também não vamos simplesmente alterar o código antigo sem avisar.

Por exemplo, se estivermos no retest.py e descobrirmos que breakout.py precisa de uma pequena alteração:

eu vou dizer:

⚠️ Precisamos voltar ao breakout.py por causa de X.

E explicarei:

Arquivo afetado:
breakout.py


Motivo:
...


Alteração:
...


Impacto:
...

Assim você sabe exatamente o que mudou.

6. E existe uma regra ainda mais importante

Quando chegarmos ao momento de integrar tudo, não vamos confiar somente nos testes individuais.

Vamos testar a cadeia inteira:

BTC CANDLES
     ↓
PIVOTS
     ↓
STRUCTURE
     ↓
TREND
     ↓
SUPPORT/RESISTANCE
     ↓
BREAKOUT
     ↓
RETEST
     ↓
PRICE ACTION
     ↓
VOLUME
     ↓
SETUP
     ↓
RISK
     ↓
ENTRY
     ↓
STOP
     ↓
TARGET
     ↓
BACKTEST

Porque uma coisa é:

cada módulo funciona sozinho ✅

Outra é:

todos os módulos funcionam juntos ✅

Precisamos dos dois.