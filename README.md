# 🧪 Proyecto de Pruebas Bottom Up — Sistema de Nómina

## 🎯 Objetivo

Este proyecto tiene como finalidad aplicar **pruebas de integración Bottom Up** en un sistema de nómina. Iniciamos validando los módulos base de manera unitaria, y luego los integramos progresivamente hasta construir y probar el sistema completo.

---

## 🧰 Tecnologías y Requisitos

- ✅ Python 3.8+
- ✅ Pytest
- ✅ Pytest-cov (para generar reportes de cobertura)
- ✅ Editor recomendado: VS Code
- ✅ Calculadora básica para verificar manualmente los cálculos

---

## 🧱 Estructura del Proyecto

proyecto_nomina/
├── modulos/
│ ├── init.py
│ ├── calculadora_impuestos.py # Módulo base: ISR y seguro
│ ├── calculadora_bonos.py # (No implementado en esta etapa)
│ ├── calculadora_deducciones.py # (No implementado en esta etapa)
│ └── drivers/
│ ├── init.py
│ └── test_driver.py # Driver para pruebas modulares
│
├── nomina_sistema.py # Sistema principal (nivel superior)
├── test_bottom_up.py # Pruebas unitarias Bottom Up
└── htmlcov/ # Carpeta generada para reportes de cobertura

yaml
Copiar código

---

## 🧪 Fases de Pruebas Bottom Up

### ✅ 1. Pruebas de Nivel Inferior (Unidad)

El archivo `test_bottom_up.py` contiene pruebas unitarias para el módulo base `CalculadoraImpuestos`, verificando:

- Cálculo de ISR según tres tramos salariales
- Cálculo del Seguro Social (6.25%)

```python
def test_isr_salario_bajo():
    salario = 8000
    resultado = self.calc.calcular_isr(salario)
    assert resultado == 400  # 5%

def test_seguro_social():
    salario = 10000
    resultado = self.calc.calcular_seguro_social(salario)
    assert resultado == 625  # 6.25%
✅ 2. Driver de Pruebas
El archivo modulos/drivers/test_driver.py actúa como driver, que ejecuta pruebas automáticas a métodos individuales con tolerancia mínima de error.

python
Copiar código
driver.ejecutar_prueba_unitaria(
    metodo="calcular_isr",
    parametros=(15000,),
    esperado=1500
)
⚠️ Este archivo no es una prueba de Pytest, por lo que contiene # pytest: skip-file al inicio para evitar advertencias.

🚀 Cómo Ejecutar las Pruebas
1. Instala dependencias (si no lo hiciste):
bash
Copiar código
python -m pip install pytest pytest-cov
2. Ejecutar pruebas unitarias
bash
Copiar código
python -m pytest test_bottom_up.py -v
3. Ejecutar pruebas con reporte de cobertura
bash
Copiar código
python -m pytest test_bottom_up.py --cov=modulos --cov-report=html
4. Ver el reporte de cobertura
Abre el archivo generado:

text
Copiar código
htmlcov/index.html
Este te muestra gráficamente qué líneas de código fueron ejecutadas durante las pruebas.

📊 Resultados Esperados
Al ejecutar correctamente las pruebas, deberías ver algo como esto:

markdown
Copiar código
test_bottom_up.py ....                    [100%]

---------- coverage: platform win32 ----------
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
modulos/calculadora_impuestos.py         12      0   100%
---------------------------------------------------------
TOTAL                                    12      0   100%

Coverage HTML written to dir htmlcov
✅ Todas las pruebas pasan
✅ Cobertura del 100%
✅ Reporte generado correctamente

✅ Estado Actual del Proyecto
 Módulo de impuestos implementado y probado

 Driver de pruebas funcional

 Pruebas unitarias con pytest

 Cobertura con pytest-cov

 Módulos de bonos y deducciones (pendientes)

 Pruebas de integración del sistema completo

🧠 Notas Finales
Este enfoque Bottom Up garantiza que cada parte del sistema esté validada antes de ser integrada.

Puedes seguir expandiendo el proyecto agregando nuevos módulos y pruebas por niveles.

Recuerda mantener los módulos pequeños, reutilizables y testeables.
