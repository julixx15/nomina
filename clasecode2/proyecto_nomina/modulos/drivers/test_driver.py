# pytest: skip-file

class TestDriver:
    """Driver para ejecutar pruebas unitarias en módulos base"""

    def __init__(self, modulo):
        self.modulo = modulo
        self.resultados = []

    def ejecutar_prueba_unitaria(self, metodo, parametros, esperado):
        """Ejecuta prueba de un método del módulo"""
        resultado = getattr(self.modulo, metodo)(*parametros)
        exito = abs(resultado - esperado) < 0.01  # Tolerancia

        self.resultados.append({
            'metodo': metodo,
            'parametros': parametros,
            'resultado': resultado,
            'esperado': esperado,
            'exito': exito
        })

        assert exito, f"Fallo en {metodo}: {resultado} != {esperado}"
        return f"✓ {metodo}({parametros}) = {resultado} OK"
