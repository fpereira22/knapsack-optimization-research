# Optimización Combinatoria: Resolución del Problema de la Mochila (Knapsack Problem)
# Datos de Réplica: Análisis de Técnicas de Resolución para el Knapsack Problem

[![DOI](https://img.shields.io/badge/DOI-10.60483%2FUNAB%2FVTK92P-blue)](https://doi.org/10.60483/UNAB/VTK92P)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--3994--8936-green)](https://orcid.org/0009-0005-3994-8936)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Julia](https://img.shields.io/badge/Language-Julia-9558B2?logo=julia)](https://julialang.org/)

Este repositorio consolida el ecosistema de investigación desarrollado para la tesis sobre el **Problema de la Mochila (Knapsack Problem)**. Aquí encontrarás un entorno experimental diseñado para explorar el equilibrio entre la exactitud matemática y la eficiencia computacional de alto rendimiento.

El proyecto contrasta la lógica secuencial tradicional con la potencia del paralelismo moderno utilizando **Julia**, validado contra benchmarks estándar de la industria en **C** y modelos exactos en **AMPL**.

---

## 📂 Estructura del Repositorio

A continuación se detalla el contenido de cada módulo de investigación:

### `Julia/` (El Núcleo del Estudio)
Implementación principal de los algoritmos con enfoque en la medición del impacto real del paralelismo:
* **Algoritmos:** Fuerza Bruta, Programación Dinámica y Greedy.
* **Paradigmas:** Versiones `Sequential` y `Parallel` (optimizada para hilos múltiples).
* **Objetivo:** Demostrar ganancias de velocidad en instancias complejas.

### `Benchmarks/` (Validación Rigurosa)
Código fuente en **C** utilizado como línea base (*baseline*) para validar resultados. Incluye generadores y soluciones de referencia:
* **Códigos:** `combo.c`, `minknap.c`, `genhard.c`.
* **Propósito:** Comparación con estándares académicos internacionales.

### `AMPL/` (Modelado Matemático)
Formulación algebraica exacta del problema:
* **Archivos:** `knapsack.mod` y archivos `.dat` asociados.
* **Uso:** Resolución exacta mediante solvers comerciales/académicos.

### `Datasets/` (Banco de Pruebas)
Colección de instancias estandarizadas (Pisinger) para el consumo de los algoritmos:
* **Escala:** Desde problemas pequeños ($n=100$) hasta desafíos masivos ($n=20.000$).
* **Formatos:** `.csv` y `.dat`.

### `Python/` (Análisis de Resultados)
Ciencia de datos aplicada a la interpretación de métricas:
* **Archivo:** `Knapsack_problem_by_Felipe_Pereira.ipynb`
* **Contenido:** Notebook con análisis exploratorio, generación de gráficas y conclusiones estadísticas.

---

## 🎓 Autoría y Créditos
* **Autor Principal:** [Felipe Pereira](https://orcid.org/0009-0005-3994-8936)
* **Profesor Guía:** Dr. Gustavo Gatica
* **Institución:** Universidad Andrés Bello (UNAB)
* **DOI del Proyecto:** [10.60483/UNAB/VTK92P](https://doi.org/10.60483/UNAB/VTK92P)

Si utilizas este material, por favor cita el trabajo original utilizando el identificador DOI proporcionado.

## 🚀 Guía de Inicio Rápido

### Requisitos Previos
* **Julia 1.x**
* **GCC/Clang** (para benchmarks en C)
* **Python 3.8+** (Jupyter, Pandas, Matplotlib)
* **AMPL** (opcional)

@thesis{Pereira_Knapsack_Tesis_2026,
  author = {Pereira, Felipe},
  title = {Análisis de Técnicas de Resolución para el Knapsack Problem},
  school = {Universidad Andrés Bello},
  type = {Tesis de Grado},
  year = {2026},
  doi = {10.60483/UNAB/VTK92P},
  url = {https://github.com/fpereira22/Knapsack-Problem-Tesis},
  note = {Profesor Guía: Dr. Gustav Gatica}
}

