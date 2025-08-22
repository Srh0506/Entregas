class Numero:
    def __init__(self, valor):
        self.valor = valor

    def convertir_decimal(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase.")

    def sumar(self, otro):
        resultado_decimal = self.convertir_decimal() + otro.convertir_decimal()
        return resultado_decimal

    def restar(self, otro):
        resultado_decimal = self.convertir_decimal() - otro.convertir_decimal()
        return resultado_decimal
