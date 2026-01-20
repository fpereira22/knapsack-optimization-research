# Optimización Combinatoria: Resolución del Problema de la Mochila (Knapsack Problem)

[![DOI](https://img.shields.io/badge/DOI-10.60483%2FUNAB%2FVTK92P-blue)](https://doi.org/10.60483/UNAB/VTK92P)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--3994--8936-green)](https://orcid.org/0009-0005-3994-8936)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Language: Julia](https://img.shields.io/badge/Language-Julia-9558B2?logo=julia)](https://julialang.org/)

## 📝 Descripción del Proyecto
Este repositorio contiene el entorno experimental desarrollado para mi tesis de investigación sobre el **Problema de la Mochila**. El objetivo principal es contrastar la lógica secuencial tradicional con la potencia del paralelismo moderno en la resolución de problemas de optimización combinatoria.

El proyecto ofrece una comparativa robusta entre diferentes estrategias algorítmicas (fuerza bruta, programación dinámica y algoritmos voraces), evaluando el equilibrio entre la exactitud matemática y la eficiencia computacional de alto rendimiento.

## 🛠️ Tecnologías y Herramientas
* **Julia:** Implementaciones principales (secuencial y paralelo).
* **C:** Benchmarks de rendimiento para evaluación de bajo nivel.
* **AMPL:** Modelos matemáticos exactos para validación de resultados.
* **Python:** Procesamiento de datos y visualización de análisis comparativos.

## 🔬 Metodología Algorítmica
El laboratorio digital explora tres enfoques fundamentales:
1.  **Fuerza Bruta:** Análisis de complejidad en instancias pequeñas.
2.  **Programación Dinámica:** Optimización de memoria y tiempo.
3.  **Algoritmos Voraces (Greedy):** Eficiencia en instancias masivas de datos.

## 📂 Estructura del Repositorio
* `/src`: Código fuente en Julia (paralelismo y secuencial).
* `/benchmarks`: Pruebas de rendimiento implementadas en C.
* `/models`: Definiciones exactas en lenguaje AMPL.
* `/analysis`: Scripts de Python y notebooks para visualización de resultados.
* `/data`: Instancias del problema utilizadas en los experimentos.

## 🎓 Citación
Si utilizas este código o los datos en tu investigación, por favor cítalo de la siguiente manera:

> Gatica, G. (2026). *Optimización Combinatoria: Resolución del Problema de la Mochila*. Repositorio de GitHub. DOI: 10.60483/UNAB/VTK92P

---
**Investigador:** [Gustav Gatica](https://orcid.org/0009-0005-3994-8936)
