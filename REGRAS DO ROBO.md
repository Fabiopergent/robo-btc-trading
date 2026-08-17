🤖 ROBÔ BTC — REGRAS OFICIAIS
1. Objetivo

Criar um robô para operar BTC, inicialmente em simulação/backtest, seguindo o setup que estudamos no curso.

Capital planejado para o futuro teste real:

R$ 100,00

A operação real só acontecerá depois de:

Desenvolvimento
↓
Testes
↓
Backtest
↓
Simulação
↓
Paper Trading
↓
Validação
↓
Teste real com capital pequeno
2. Filosofia do robô

O robô deve ser seletivo e conservador.

Regras principais:
Não entrar sem confirmação.
Não operar por impulso.
Não tentar prever o mercado.
Não operar lateralização.
Não operar contra a tendência.
Sempre definir Stop Loss.
Sempre definir Take Profit.
Buscar inicialmente Risco/Retorno mínimo de 1:3.
Uma posição por vez inicialmente.
Se o setup não estiver completo → não operar.
Regra-mestra:

O robô não procura uma operação. Ele procura condições que justifiquem uma operação.

3. Fluxo geral

O cérebro do robô seguirá esta sequência:

DADOS BTC
   ↓
PIVÔ 3 CANDLES
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

A ordem é importante.

4. Pivô de 3 candles

Utilizaremos o sistema de 3 candles.

Pivot High

O candle central possui máxima maior que os candles vizinhos:

High anterior < High central > High posterior
Pivot Low

O candle central possui mínima menor:

Low anterior > Low central < Low posterior
Pivô ambíguo

Se o candle puder ser interpretado simultaneamente como:

Pivot High
+
Pivot Low

não devemos utilizá-lo para criar estrutura.

5. Estrutura do mercado

Os pivôs serão classificados como:

HH = Higher High
HL = Higher Low
LH = Lower High
LL = Lower Low
HH

Topo maior que o topo anterior.

LH

Topo menor que o topo anterior.

HL

Fundo maior que o fundo anterior.

LL

Fundo menor que o fundo anterior.

6. Tendência
🟢 Alta

Estrutura:

HH
HL
HH
HL

Resultado:

UPTREND

O robô procura COMPRA.

🔴 Baixa

Estrutura:

LL
LH
LL
LH

Resultado:

DOWNTREND

O robô procura VENDA.

🟡 Lateralização

Quando a estrutura não confirma tendência:

SIDEWAYS
Regra:

Não operar.

⚪ Estrutura insuficiente
UNKNOWN
Regra:

Não operar.

7. Direção das operações
UPTREND
UPTREND
   ↓
procurar COMPRA
DOWNTREND
DOWNTREND
   ↓
procurar VENDA
SIDEWAYS
SIDEWAYS
   ↓
NÃO OPERAR
8. Suporte e resistência

Os pivôs servem como base para encontrar regiões.

Pivot High
→ RESISTÊNCIA
Pivot Low
→ SUPORTE

Não trabalharemos inicialmente com uma linha exata.

Exemplo:

RESISTÊNCIA


109.67 ───────── 110.33

É uma região, não um preço único.

9. Agrupamento de regiões

Se várias regiões próximas forem do mesmo tipo, elas podem ser agrupadas.

Exemplo:

Resistance 100
Resistance 100.10
Resistance 100.20

Pode virar:

RESISTANCE
100.00 ───────── 100.20

Isso evita que o robô enxergue três resistências diferentes quando, na prática, existe uma única região.

10. Rompimento

O rompimento não gera entrada automaticamente.

Primeiro:

RESISTÊNCIA
     ↓
Preço rompe
     ↓
fechamento confirma
     ↓
volume confirma

Para resistência:

close > região superior

Para suporte:

close < região inferior

O rompimento deverá ser validado para reduzir falsos rompimentos.

11. Volume

O volume será utilizado como confirmação, não como sinal isolado.

A ideia atual é comparar o volume do candle com uma média dos candles anteriores.

Exemplo:

Volume médio = 1.000
Volume atual = 1.800

Se o multiplicador configurado exigir, por exemplo, 1,5×:

1.000 × 1,5 = 1.500

Então:

1.800 > 1.500

Volume confirmado.

⚠️ Essa lógica já existe parcialmente no breakout.py, mas ainda vamos validar e posteriormente organizar melhor o módulo volume.py.

12. Reteste

Depois do rompimento, o robô não entra imediatamente.

Ele aguarda o preço voltar para testar a região.

Exemplo:

RESISTÊNCIA
──────────────
       ↑
       │ rompimento
       │
       ↓
       RETESTE
──────────────

A antiga resistência pode passar a funcionar como suporte.

13. Price Action

O Price Action será utilizado como confirmação do setup.

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
Regra importante:

Nenhum candle isolado gera entrada.

O candle precisa estar dentro do contexto correto.

14. Falso rompimento

Um simples pavio ultrapassando a região não será suficiente.

Exemplo:

        │
        │ pavio
────────┼──────── resistência
        │
        │

Se não houver confirmação:

NÃO ENTRAR
15. Setup de COMPRA

A ideia geral será:

UPTREND
   ↓
região relevante
   ↓
rompimento
   ↓
volume
   ↓
reteste
   ↓
Price Action favorável
   ↓
confirmação
   ↓
Risco/Retorno adequado
   ↓
COMPRA
16. Setup de VENDA
DOWNTREND
   ↓
região relevante
   ↓
rompimento
   ↓
volume
   ↓
reteste
   ↓
Price Action favorável
   ↓
confirmação
   ↓
Risco/Retorno adequado
   ↓
VENDA
17. Lateralização

Essa é uma das regras que você definiu especificamente:

SIDEWAYS
     ↓
NÃO OPERAR

Mesmo que apareça um possível rompimento, o robô deverá aguardar uma estrutura que confirme o movimento antes de começar a procurar operações.

18. Gerenciamento de risco

Capital planejado:

R$ 100

O robô não deve simplesmente colocar os R$100 inteiros em uma operação sem controle.

Teremos módulos separados para:

Position Size
Stop Loss
Take Profit
19. Stop Loss

Toda operação precisa ter Stop Loss.

O stop será definido antes da entrada.

Não será permitido:

ENTRAR
↓
depois decidir o stop

O correto:

SETUP
↓
entrada
↓
STOP definido
↓
alvo definido
↓
executar
20. Take Profit

O alvo será definido antes da operação.

Regra inicial:

RISCO : RETORNO


1 : 3

Exemplo:

Entrada = 100
Stop    = 97


Risco = 3


Alvo mínimo:
100 + 9 = 109
21. Posição

Inicialmente:

1 posição por vez

Se já estiver comprado:

não abrir outra compra

Se não houver posição:

procurar setup

A regra que você definiu anteriormente também será preservada:

Se houver ativo/posição, o robô deve administrar essa posição; se não houver posição, procurar uma nova entrada conforme a tendência.

22. Backtest

O backtest deverá simular:

Candle
↓
decisão
↓
entrada
↓
Stop/Alvo
↓
resultado

Sem utilizar informações futuras para tomar decisões passadas.

Esse ponto será extremamente importante para evitar um backtest enganoso.

23. O que já está implementado
[✅] Pivô 3 candles
[✅] Estrutura HH/HL/LH/LL
[✅] Tendência
[✅] UPTREND
[✅] DOWNTREND
[✅] SIDEWAYS
[✅] Suporte
[✅] Resistência
[✅] Zonas
[✅] Agrupamento de zonas
[🟡] Rompimento — código existe, estamos testando
24. O que ainda falta
[ ] Finalizar/testar Rompimento
[ ] Reteste
[ ] Price Action
[ ] Módulo de Volume
[ ] Setup final
[ ] Position Size
[ ] Stop Loss
[ ] Take Profit
[ ] Integração do gerenciamento de risco
[ ] Backtest completo
[ ] Estatísticas
[ ] Simulação
[ ] Integração Binance
25. Estrutura dos arquivos
robo-btc-trading/
│
├── main.py
├── config.py
├── requirements.txt
│
├── strategy/
│   ├── __init__.py
│   ├── pivots.py
│   ├── structure.py
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
🔐 Regra de desenvolvimento

E essa é importante para nossa continuidade:

Não vamos recriar um arquivo que já possui código.

Quando formos trabalhar em um arquivo que já existe, você me manda o conteúdo atual e eu verifico primeiro:

O que já existe?
       ↓
O que funciona?
       ↓
O que falta?
       ↓
O que precisa ser alterado?
       ↓
Só então modificamos.

Assim conseguimos manter o projeto modular e evitar que uma etapa apague ou duplique outra.

Estado atual: estamos no breakout.py, e o próximo objetivo é testar a implementação que você já possui antes de modificá-la.


📋 Regra adicionada ao projeto
ENTRADA NO BACKTEST


O setup é avaliado após o fechamento do candle.


Se houver sinal BUY ou SELL,
o sinal fica pendente.


A posição é aberta na abertura
do candle seguinte.


O preço de entrada será o
preço de abertura do próximo candle.