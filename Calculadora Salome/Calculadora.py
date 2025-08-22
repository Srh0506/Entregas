from Numeroedecimal import NumeroDecimal
from Numerobinario import NumeroBinario
from Numerohexadecimal import HexaDecimal
from Numerooctal import NumeroOctal
from Numeroromano import NumeroRomano

def crear_numero(tipo, valor):
    clases = {
        "decimal": NumeroDecimal,
        "binario": NumeroBinario,
        "hexadecimal": HexaDecimal,
        "octal": NumeroOctal,
        "romano": NumeroRomano
    }
    tipo = tipo.lower()
    if tipo not in clases:
        raise ValueError(f"Tipo no válido. Tipos permitidos: {', '.join(clases.keys())}")
    return clases[tipo](valor)

def pedir_dato(mensaje, opciones_validas=None):
    while True:
        dato = input(mensaje).strip().lower()
        if opciones_validas and dato not in opciones_validas:
            print(f"Opción inválida. Opciones válidas: {', '.join(opciones_validas)}")
        else:
            return dato

def main():
    print("Tipos disponibles: decimal, binario, hexadecimal, octal, romano")
    
    try:
        tipo1 = pedir_dato("Ingrese el tipo del primer número: ", ["decimal", "binario", "hexadecimal", "octal", "romano"])
        valor1 = input("Ingrese el valor: ")
        numero1 = crear_numero(tipo1, valor1)

        tipo2 = pedir_dato("Ingrese el tipo del segundo número: ", ["decimal", "binario", "hexadecimal", "octal", "romano"])
        valor2 = input("Ingrese el valor: ")
        numero2 = crear_numero(tipo2, valor2)

        operacion = pedir_dato("¿Qué operación quieres hacer, sumar o restar?: ", ["sumar", "restar"])

        if operacion == "sumar":
            resultado = numero1.sumar(numero2)
        else:
            resultado = numero1.restar(numero2)

        print(f"Resultado en decimal: {resultado}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()

