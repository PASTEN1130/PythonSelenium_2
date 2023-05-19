import pytest

# Crear la clase CuentaBancaria
class test_CuentaBancaria:
    def __init__(self, numero_cuenta: int, titular_cuenta: str, saldo: float):
        self.__numero_cuenta = numero_cuenta
        self.__titular_cuenta = titular_cuenta
        self.__saldo = saldo

    def setup_method(self):
        print("*" * 80)
        print(f"METHOD SETUP ")
        print("*" * 80)

    def setup_method(self):
        self.cuenta = CuentaBancaria("Luis", 100)

    def test_depositar(self, dinero: float):
        self.__saldo += dinero
        print("Se han depositado $", dinero, "en la cuenta.")

    def test_retirar(self, dinero: float):
        if self.__saldo >= dinero:
            self.__saldo -= dinero
            print("Se han retirado $", dinero, "de la cuenta.")
        else:
            print("No hay suficiente saldo en la cuenta para realizar el retiro.")

    def test_consultar_saldo(self):
        print("El saldo actual de la cuenta es: $", self.__saldo)



