class CalculadoraDeducciones:
    """Calcula deducciones adicionales (a futuro)"""

    def calcular_deducciones(self, empleado):
        # Ejemplo: deducciones por préstamos, etc.
        return empleado.get('deducciones_extra', 0)
