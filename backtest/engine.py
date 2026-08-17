class BacktestEngine:

    def __init__(self, initial_balance):
        """
        Inicializa o ambiente de simulação.
        """

        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.position = None
        self.trades = []

    def has_position(self):
        """
        Verifica se existe uma posição aberta.
        """

        return self.position is not None

    def open_position(
        self,
        entry_price,
        quantity,
        stop_price,
        target_price
    ):
        """
        Abre uma posição simulada.
        """

        if self.has_position():
            return False

        self.position = {

            "entry": entry_price,

            "quantity": quantity,

            "stop": stop_price,

            "target": target_price
        }

        return True

    def close_position(
        self,
        exit_price,
        reason
    ):
        """
        Fecha a posição e registra o resultado.
        """

        if not self.has_position():
            return False

        entry_price = self.position["entry"]

        quantity = self.position["quantity"]

        profit = (
            exit_price - entry_price
        ) * quantity

        self.balance += profit

        trade = {

            "entry": entry_price,

            "exit": exit_price,

            "quantity": quantity,

            "profit": profit,

            "reason": reason
        }

        self.trades.append(trade)

        self.position = None

        return True

    def process_candle(self, candle):
        """
        Verifica se o candle atingiu stop ou alvo
        da posição aberta.
        """

        if not self.has_position():
            return

        stop = self.position["stop"]

        target = self.position["target"]

        # -----------------------------------------
        # STOP
        # -----------------------------------------

        if candle["low"] <= stop:

            self.close_position(
                stop,
                "STOP"
            )

            return

        # -----------------------------------------
        # ALVO
        # -----------------------------------------

        if candle["high"] >= target:

            self.close_position(
                target,
                "TARGET"
            )

            return
        
    def run(self, df):
        """
        Percorre os candles em ordem cronológica
        e processa cada candle.
        """

        for index, candle in df.iterrows():

            self.process_candle(candle)    