import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # Asegura acceso local

import pytest
from modulos.calculadora_impuestos import CalculadoraImpuestos
from modulos.drivers.test_driver import TestDriver  # Corrección de ruta

class TestNivelBase:
    """Nivel 1: Prueba de los módulos base individuales"""

    def setup_method(self):
        self.calc = CalculadoraImpuestos()
        self.driver = TestDriver(self.calc)

    def test_isr_salario_bajo(self):
        """Prueba ISR para salario <= 10,000"""
        salario = 8000
        resultado = self.calc.calcular_isr(salario)
        assert resultado == 400  # 5% de 8000

    def test_isr_salario_medio(self):
        """Prueba ISR para salario entre 10,001 y 20,000"""
        salario = 15000
        resultado = self.calc.calcular_isr(salario)
        assert resultado == 1500  # 10% de 15000

    def test_isr_salario_alto(self):
        """Prueba ISR para salario > 20,000"""
        salario = 30000
        resultado = self.calc.calcular_isr(salario)
        assert resultado == 4500  # 15% de 30000

    def test_seguro_social(self):
        """Prueba del cálculo de seguro social"""
        salario = 10000
        resultado = self.calc.calcular_seguro_social(salario)
        assert resultado == 625  # 6.25% de 10000
