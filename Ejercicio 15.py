'''Ejercicio 15. Clase UsuarioBanco :
Explicación del ejercicio:
Descripción:
Crea la clase
UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si
tiene o no cuenta corriente. Proporciona métodos para realizar operaciones
como retirar dinero, transferir dinero desde otro usuario y agregar dinero al
saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente
mediante True y False .
2. Implementar el método retirar_dinero para retirar dinero del saldo del
usuario. Lanzará un error en caso de no poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia
desde otro usuario al usuario actual. Lanzará un error en caso de no poder
hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del
usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo
inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Alicia".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia"'''


class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Fondos insuficientes para realizar esta operación.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError("Fondos insuficientes en el usuario remitente para realizar la transferencia.")
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)

usuario1.agregar_dinero(20)
usuario1.transferir_dinero(usuario2, 80)
usuario1.retirar_dinero(50)

print(f"{usuario1.nombre} - Saldo: {usuario1.saldo}")
print(f"{usuario2.nombre} - Saldo: {usuario2.saldo}")
