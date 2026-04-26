# BB84 Simulator

Simulador educativo del protocolo de criptografía cuántica BB84 usando Python.

Este proyecto muestra cómo Fotoncio y Bitberto pueden generar una clave compartida usando bases aleatorias, mientras Evetron intenta espiar la comunicación.

## Personajes

- **Fotoncio**: emisor de los bits.
- **Bitberto**: receptor que mide los bits.
- **Evetron**: espía que intenta interceptar la comunicación.

## ¿Qué simula?

El programa simula una versión sencilla del protocolo BB84:

1. Fotoncio genera bits aleatorios.
2. Fotoncio elige bases aleatorias: `Z` o `X`.
3. Bitberto también elige bases aleatorias.
4. Evetron puede intentar espiar.
5. Solo se conservan los bits donde Fotoncio y Bitberto usaron la misma base.
6. Esos bits forman una clave compartida.
7. Si hay errores, se detecta posible espionaje.

## ¿Por qué es importante?

BB84 demuestra una idea central de la criptografía cuántica:

> Si alguien intenta medir la información cuántica, puede alterar los resultados y ser detectado.

Este simulador no usa fotones reales, pero ayuda a entender la lógica del protocolo.

## Cómo ejecutar el programa

Necesitas tener Python instalado.

Ejecuta:

```bash
python main.py
```
También puedes copiar el código y probarlo en Google Colab.

## Ejemplo de uso

Elige tu rol:
1. Ser Fotoncio
2. Ser Bitberto
3. Ser Evetron

¿Cuántos bits quieres simular? Ejemplo 10, 20, 50: 20

El programa mostrará:

- Bases usadas por Fotoncio
- Bases usadas por Bitberto
- Clave compartida
- Errores detectados
- Si Evetron fue detectado o no

## Conceptos usados

- Criptografía cuántica  
- Protocolo BB84  
- Bits  
- Bases de medición  
- Clave compartida  
- Detección de espionaje  
- Simulación con números aleatorios  

---

## ⚠️ Limitaciones

Este proyecto es una simulación educativa.

No implementa criptografía cuántica real ni usa hardware cuántico.  
Su objetivo es explicar el funcionamiento básico de BB84 de forma sencilla.

---

## 👨‍💻 Autor

Creado por **giiiacomobl** como proyecto educativo de programación y criptografía cuántica.
