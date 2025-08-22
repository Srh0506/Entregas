class NumeroBinario:
    def __init__(self, valor):
        # Validación de número binario
        if not all(c in '01' for c in valor):  # Verifica que solo contenga 0s y 1s
            raise ValueError(f"El valor '{valor}' no es un número binario válido.")
        self.valor = valor
    
    def sumar(self, otro_numero):
        # Implementación de suma para binarios (esta es solo una estructura, debes agregar lógica real)
        pass

    def restar(self, otro_numero):
        # Implementación de resta para binarios
        pass
