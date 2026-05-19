# Sistema de Clasificación de Textos

Proyecto desarrollado en Python para implementar la fase 3 del caso práctico, tomando como base el diagrama de clases UML del sistema de clasificación e intercambio de textos.

En esta fase se fortaleció el modelo orientado a objetos mediante la implementación de abstracción y polimorfismo, permitiendo una estructura más flexible, reutilizable y escalable para la clasificación de materiales de lectura.

## Conceptos aplicados

- Clases
- Objetos
- Encapsulamiento
- Herencia
- Abstracción
- Polimorfismo
- Relaciones entre clases

## Implementación de Abstracción

La clase `ReadingMaterial` fue convertida en una clase abstracta, definiendo comportamientos generales que deben ser implementados por todas las clases derivadas.

Se agregaron los siguientes métodos abstractos:

- `getMaterialType()`
- `classifyMaterial()`
- `showDetails()`

Esto permite establecer una estructura común para todos los materiales de lectura del sistema.

## Implementación de Polimorfismo

Las clases hijas:

- `LiteratureBook`
- `ScientificBook`
- `Magazine`
- `Comic`
- `ResearchArticle`

sobrescriben los métodos abstractos de `ReadingMaterial`, permitiendo que cada tipo de material responda de forma diferente utilizando la misma interfaz común.

El polimorfismo se demuestra en `main.py`, recorriendo distintos objetos de tipo `ReadingMaterial` y ejecutando los mismos métodos con comportamientos específicos para cada subclase.

## Diagrama de Clases

A continuación se muestra el diagrama de clases actualizado del sistema:

![Class Diagram](diagrams/class-diagram.png)

## Estructura del proyecto

- `diagrams/class-diagram.puml`: Código del diagrama en PlantUML
- `diagrams/class-diagram.png`: Imagen del diagrama
- `models/`: Clases del sistema
- `main.py`: Ejecución y demostración del sistema

## Tecnologías utilizadas

- Python
- UML (Lenguaje Unificado de Modelado)
- PlantUML

## Características del sistema

- Registro de usuarios
- Gestión de materiales de lectura
- Préstamo y devolución de materiales
- Intercambio de textos
- Clasificación de materiales
- Estadísticas de lectura
- Demostración de abstracción y polimorfismo

## Notas

El sistema representa una solución orientada a objetos para la gestión e intercambio de materiales de lectura, aplicando los principales pilares de la Programación Orientada a Objetos (POO).

La arquitectura fue diseñada siguiendo buenas prácticas de modularidad, reutilización de código y separación de responsabilidades.

## Autor

Trabajo académico - Unidad 3
