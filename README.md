# IA TAREA2 CONECTA4

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/Care99/ia-tarea2-conecta4)](https://github.com/Care99/conecta4/releases)

## Acerca de

Tarea 2 de Inteligencia Artificial

## Descripcion

2- Conecta4: El tablero normalmente es una matriz de 6 filas x 7 columnas, cada columna actúa como
una pila de fichas, cada jugador en su turno escoge una columna para apilar una ficha. El objetivo es
conectar 4 fichas del mismo jugador en vertical, horizontal o diagonal, antes que el oponente. Función
de evaluación posible: F(Jugador) = Suma ponderada de Cantidad de i fichas del jugador en línea y libre
(no trancado en por lo menos un extremo), donde i puede tomar: 3, 2, 1 y las ponderaciones para 3 en
línea debería ser mayor e ir disminuyendo para 2 y 1. Finalmente la evaluación calcular como: F(propia)
– F(adversario)
