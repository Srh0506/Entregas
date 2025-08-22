class HexaDecimal:
    def __init__(self, valor):
        # Validación de número hexadecimal
        try:
            int(valor, 16)  # Si no es un valor hexadecimal válido, lanzará ValueError
            self.valor = valor
        except ValueError:
            raise ValueError(f"El valor '{valor}' no es un número hexadecimal válido.")
    
    def sumar(self, otro_numero):
        # Implementación de suma para hexadecimales
        pass

    def restar(self, otro_numero):
        # Implementación de resta para hexadecimales
        pass
