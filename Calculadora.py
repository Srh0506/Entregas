# Clase padre
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def convertir_decimal(self):
        pass

    def sumar(self, otro):
        resultado_decimal = self.convertir_decimal() + otro.convertir_decimal()
        return NumeroDecimal(resultado_decimal)

    def restar(self, otro):
        resultado_decimal = self.convertir_decimal() - otro.convertir_decimal()
        return NumeroDecimal(resultado_decimal)


# Clases hijas
class NumeroDecimal(Numero):
    def convertir_decimal(self):
        return int(self.valor)


class HexaDecimal(Numero):
    def convertir_decimal(self):
        return int(self.valor, 16)


class NumeroBinario(Numero):
    def convertir_decimal(self):
        return int(self.valor, 2)


class NumeroOctal(Numero):
    def convertir_decimal(self):
        return int(self.valor, 8)


class NumeroRomano(Numero):
    valores_romanos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def convertir_decimal(self):
        total = 0
        anterior = 0
        for simbolo in reversed(self.valor.upper()):
            valor = self.valores_romanos[simbolo]
            if valor < anterior:
                total -= valor
            else:
                total += valor
            anterior = valor
        return total


# Función para crear las litas 
def crear_numero(tipo, valor):
    clases = {
        "decimal": NumeroDecimal,
        "binario": NumeroBinario,
        "hexadecimal": HexaDecimal,
        "octal": NumeroOctal,
        "romano": NumeroRomano
    }
    return clases[tipo.lower()](valor)


print("Tipos disponibles: decimal, binario, hexadecimal, octal, romano")

tipo1 = input("Ingrese el tipo del primer número: ")
valor1 = input("Ingrese el valor: ")
numero1 = crear_numero(tipo1, valor1)

tipo2 = input("Ingrese el tipo del segundo número: ")
valor2 = input("Ingrese el valor: ")
numero2 = crear_numero(tipo2, valor2)

operacion = input("¿Qué operación quieres hacer, sumar o restar?: ")

if operacion.lower() == "sumar":
    resultado = numero1.sumar(numero2)
elif operacion.lower() == "restar":
    resultado = numero1.restar(numero2)
else:
    print("Operación no válida")
    exit()

print(f"Resultado en decimal: {resultado.valor}")
 
        
    