class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historial = []  # Para almacenar el historial de transacciones

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor que cero.")
        self.saldo += cantidad
        self.historial.append(f"Depositado: {cantidad:.2f} euros")
        return self.saldo
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError("No tienes suficientes fondos para retirar esa cantidad.")
        self.saldo -= cantidad
        self.historial.append(f"Retirado: {cantidad:.2f} euros")
        return self.saldo
    
    def ver_historial(self):
        if not self.historial:
            return "No hay transacciones registradas."
        return "\n".join(self.historial)
    
    def __str__(self):
        return f"Cuenta de {self.titular} con un saldo de {self.saldo:.2f} euros"
    
def simular_cuenta_bancaria():
    titular = input("Ingresa el nombre del titular de la cuenta: ")
    
    while True:
        try:
            saldo_inicial = float(input("Ingresa el saldo inicial de la cuenta: "))
            if saldo_inicial < 0:
                raise ValueError("El saldo inicial no puede ser negativo.")
            break
        except ValueError as e:
            print("Error:", e)

    cuenta = CuentaBancaria(titular, saldo_inicial)
    
    while True:
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Ver saldo")
        print("4. Ver historial de transacciones")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            try:
                cantidad = float(input("Ingresa la cantidad a depositar: "))
                print(f"Se ha depositado {cantidad:.2f} euros en la cuenta de {cuenta.titular}. Saldo actual: {cuenta.depositar(cantidad):.2f} euros.")
            except ValueError as e:
                print("Error:", e)
        elif opcion == "2":
            try:
                cantidad = float(input("Ingresa la cantidad a retirar: "))
                print(f"Se han retirado {cantidad:.2f} euros de la cuenta de {cuenta.titular}. Saldo actual: {cuenta.retirar(cantidad):.2f} euros.")
            except ValueError as e:
                print("Error:", e)
        elif opcion == "3":
            print(cuenta)
        elif opcion == "4":
            print("Historial de transacciones:")
            print(cuenta.ver_historial())
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    simular_cuenta_bancaria()