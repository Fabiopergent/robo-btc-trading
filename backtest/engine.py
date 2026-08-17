class BacktestEngine:

    def __init__(self, initial_balance):
        """
        Inicializa o ambiente de simulação.
        """

        self.initial_balance = initial_balance
        self.balance = initial_balance
        self.position = None
        self.pending_signal = None
        self.trades = []

    def has_position(self):
        """
        Verifica se existe uma posição aberta.
        """

        return self.position is not None

    def has_pending_signal(self):
        """
        Verifica se existe um sinal aguardando
        a abertura do próximo candle.
        """

        return self.pending_signal is not None

    def set_signal(
        self,
        direction,
        quantity,
        stop_price,
        target_price
    ):
        """
        Registra um sinal para ser executado
        na abertura do próximo candle.

        direction:
            BUY
            SELL
        """

        if direction not in ["BUY", "SELL"]:
            return False

        if self.has_position():
            return False

        if self.has_pending_signal():
            return False

        self.pending_signal = {

            "direction": direction,

            "quantity": quantity,

            "stop": stop_price,

            "target": target_price
        }

        return True

    def execute_pending_signal(self, candle):
        """
        Executa o sinal pendente utilizando
        a abertura do candle atual.
        """

        if not self.has_pending_signal():
            return False

        if self.has_position():
            return False

        entry_price = candle["open"]

        signal = self.pending_signal

        self.position = {

            "entry": entry_price,

            "quantity": signal["quantity"],

            "stop": signal["stop"],

            "target": signal["target"],

            "direction": signal["direction"]
        }

        self.pending_signal = None

        return True

    def open_position(
        self,
        entry_price,
        quantity,
        stop_price,
        target_price,
        direction
    ):
        """
        Abre uma posição simulada diretamente.

        Mantida para os testes anteriores.
        """

        if self.has_position():
            return False

        if direction not in ["BUY", "SELL"]:
            return False

        self.position = {

            "entry": entry_price,

            "quantity": quantity,

            "stop": stop_price,

            "target": target_price,

            "direction": direction
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

        direction = self.position["direction"]

        if direction == "BUY":

            profit = (
                exit_price - entry_price
            ) * quantity

        else:

            profit = (
                entry_price - exit_price
            ) * quantity

        self.balance += profit

        trade = {

            "entry": entry_price,

            "exit": exit_price,

            "quantity": quantity,

            "direction": direction,

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

        direction = self.position["direction"]

        # -----------------------------------------
        # BUY
        # -----------------------------------------

        if direction == "BUY":

            if candle["low"] <= stop:

                self.close_position(
                    stop,
                    "STOP"
                )

                return

            if candle["high"] >= target:

                self.close_position(
                    target,
                    "TARGET"
                )

                return

        # -----------------------------------------
        # SELL
        # -----------------------------------------

        elif direction == "SELL":

            if candle["high"] >= stop:

                self.close_position(
                    stop,
                    "STOP"
                )

                return

            if candle["low"] <= target:

                self.close_position(
                    target,
                    "TARGET"
                )

                return

    def run(self, df):
        """
        Percorre os candles em ordem cronológica.

        Um sinal gerado anteriormente é executado
        na abertura do candle seguinte.
        """

        for index, candle in df.iterrows():

            # -----------------------------------------
            # EXECUTAR SINAL PENDENTE
            # -----------------------------------------

            self.execute_pending_signal(candle)

            # -----------------------------------------
            # PROCESSAR STOP / TARGET
            # -----------------------------------------

            self.process_candle(candle)