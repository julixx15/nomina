class CalculadoraBonos:
    """Calcula bonos para empleados"""

    def calcular_bonos(self, empleado):
        # Simula cálculo de bono por antigüedad y rendimiento
        antiguedad = empleado.get('antiguedad', 0)
        rendimiento = empleado.get('rendimiento', 0)

        bono = 0
        if antiguedad > 5:
            bono += 1000
        if rendimiento >= 90:
            bono += 500
        return bono
