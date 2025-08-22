class NumeroOctal:
    def __init__(self, valor):
        # Validación de número octal
        try:
            int(valor, 8)  # Verifica que sea un valor octal válido
            self.valor = valor
        except ValueError:
            raise ValueError(f"El valor '{valor}' no es un número octal válido.")
    
    def sumar(self, otro_numero):
        # Implementación de suma para octales
        pass

    def restar(self, otro_numero):
        # Implementación de resta para octales
        pass
