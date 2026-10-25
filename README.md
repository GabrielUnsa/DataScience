# DataScience — Análisis de datos y optimización

Material académico de ciencia de datos con Python y de investigación operativa con GLPK. Reúne una introducción práctica a pandas, apuntes de preparación y modelado de datos, y modelos matemáticos de programación lineal, por metas y entera.

Estos ejercicios prácticos fueron realizados durante el cursado de diversas materias mientras estudiaba la **Licenciatura en Análisis de Sistemas (Plan 2010)** de la **Universidad Nacional de Salta**.

**Materia:** ______________________________

## Contenido

- [Estructura](#estructura)
- [Análisis de datos con Python](#análisis-de-datos-con-python)
- [Modelos de optimización con GLPK](#modelos-de-optimización-con-glpk)
- [Preparación y uso](#preparación-y-uso)
- [Estado y validación](#estado-y-validación)
- [Licencia](#licencia)

## Estructura

```text
.
├── Python/
│   ├── 1. introduction.py
│   ├── 2. Data Wrangling.py
│   ├── 3. EDA.py
│   ├── 4. Model Development.py
│   └── 5. Model Evaluation.py
├── GLPK/
│   ├── TP1/
│   │   └── Estudio Sensibilidad/
│   ├── TP2/
│   └── TP3/
├── LICENSE
└── README.md
```

## Análisis de datos con Python

La carpeta [Python](Python/) organiza el material en cinco etapas:

| Archivo | Temas y comportamiento |
| --- | --- |
| [1. introduction.py](Python/1.%20introduction.py) | Lee un CSV mediante una URL de Google Drive y muestra tipos de columnas, estadísticas descriptivas e información del DataFrame. Es el único archivo de esta serie que ejecuta un análisis. |
| [2. Data Wrangling.py](Python/2.%20Data%20Wrangling.py) | Apuntes sobre valores ausentes, conversión de tipos, normalización, discretización y codificación de categorías. |
| [3. EDA.py](Python/3.%20EDA.py) | Estadística descriptiva, gráficos, agrupaciones, tablas dinámicas, mapas de calor, ANOVA y correlación de Pearson. |
| [4. Model Development.py](Python/4.%20Model%20Development.py) | Regresión lineal simple y múltiple, polinomios, escalado, pipelines, gráficos de diagnóstico y métricas MSE, R², MAE y RMSE. |
| [5. Model Evaluation.py](Python/5.%20Model%20Evaluation.py) | Separación de entrenamiento y prueba, validación cruzada, selección de modelos, regresión Ridge y búsqueda de hiperparámetros. |

Los archivos `2` a `5` contienen el material dentro de cadenas multilínea. Ejecutarlos directamente no realiza las operaciones descritas: para practicar hay que extraer los fragmentos, agregar sus importaciones y proporcionar los datos y variables que utilizan. Algunos ejemplos esperan columnas como `price`, `horsepower` o `engine-size`; no hay un conjunto de datos local que las suministre.

## Modelos de optimización con GLPK

Los archivos `.mod` describen variables, una función objetivo y restricciones en el lenguaje de modelado de GLPK. Los modelos completos incluyen instrucciones `solve` y `display` para resolver y mostrar resultados.

| Carpeta | Contenido |
| --- | --- |
| [GLPK/TP1](GLPK/TP1/) | Dos ejemplos de clase y trece ejercicios. Incluye maximización y minimización con restricciones de recursos, mezclas, nutrición, inversión y cobertura de períodos. `Ejercicio-5.mod` incorpora variables enteras. |
| [Estudio Sensibilidad](GLPK/TP1/Estudio%20Sensibilidad/) | Variantes de coeficientes y restricciones de los ejercicios 10 a 13 y del ejemplo de práctica. Incluye un modelo dual del ejercicio 12 y archivos `.txt` con soluciones y reportes de sensibilidad guardados. |
| [GLPK/TP2](GLPK/TP2/) | Modelos por metas con variables de desviación y penalizaciones. Los ejercicios 1 y 2 contienen objetivo, restricciones y resolución; el ejercicio 3 es un borrador con variables declaradas. |
| [GLPK/TP3](GLPK/TP3/) | Ejercicios 1, 2, 4 y 5 de programación entera y binaria, con restricciones de cobertura y relaciones entre decisiones. |

Los archivos de resultados son registros del trabajo realizado; modificar un modelo no actualiza automáticamente esos reportes.

## Preparación y uso

Los comandos siguientes se ejecutan en Bash desde la raíz de este repositorio:

```bash
git clone https://github.com/GabrielUnsa/DataScience.git
cd DataScience
```

### Python

Se necesita Python 3 y pandas para el primer script. Para experimentar con los fragmentos de los demás archivos se utilizan también NumPy, Matplotlib, Seaborn, SciPy y scikit-learn.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas numpy matplotlib seaborn scipy scikit-learn
python "Python/1. introduction.py"
```

La introducción necesita conexión a Internet y acceso al CSV indicado en su variable `url`. Si esa fuente deja de estar disponible, se debe cambiar la variable por una ruta o URL de un CSV accesible. El repositorio no incluye el archivo de datos ni versiones fijadas de las dependencias.

### GLPK

Con GLPK instalado y `glpsol` disponible en la terminal:

```bash
glpsol --model "GLPK/TP1/EjemploTeoria.mod"
```

Para guardar una solución y un reporte de sensibilidad de un modelo lineal continuo:

```bash
mkdir -p resultados
glpsol --model "GLPK/TP1/Ejercicio-10.mod" \
  --output resultados/ejercicio10-solucion.txt \
  --ranges resultados/ejercicio10-sensibilidad.txt
```

Cada modelo se resuelve de forma independiente. Los modelos con variables enteras o binarias se pueden resolver con `--model`; el reporte de sensibilidad del ejemplo corresponde al modelo lineal continuo.

## Estado y validación

Se comprobó la sintaxis de los cinco archivos Python con Python 3.13.5 y se verificó que los archivos `2` a `5` solo contienen apuntes. No se ejecutó la descarga del CSV ni el entrenamiento de modelos. GLPK no estaba instalado en el entorno de documentación, por lo que los comandos de resolución no se probaron.

El material conserva ejemplos y borradores de estudio. Los fragmentos de Python requieren revisión de sus variables y llamadas a bibliotecas antes de reutilizarlos. En GLPK, `TP2/Ejercicio-3.mod` está incompleto y algunas restricciones deben cotejarse con sus enunciados; por ejemplo, el ejercicio 7 de TP1 repite términos en las restricciones de disponibilidad de químicos. No se incluyen los enunciados originales ni pruebas automatizadas.

## Licencia

Distribuido bajo la [licencia MIT](LICENSE). Copyright © 2025 Gabriel Marmanillo.
