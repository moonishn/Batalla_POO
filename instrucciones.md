# Simulador de Combate en Python

Este proyecto implementa un sencillo simulador de combate en Python utilizando la Programación Orientada a Objetos (POO). Incluye tres clases principales: `Personaje`, `Guerrero` y `Mago`, que pueden enfrentarse en combate por turnos.


## Instrucciones para Crear el Código

### 1. Crear la Clase Base `Personaje`
- **Descripción:**
  Esta será la clase base de todos los personajes del juego. Debe manejar atributos como el nombre y la salud del personaje.

- **Tareas:**
  1. Define el método constructor para inicializar los atributos `nombre` y `salud`. El valor de salud debe ser `100`.
  2. Implementa un método `atacar(otro_personaje)`, que imprima `"El personaje ataca"`
  3. Crea un método `esta_vivo()` que devuelva `True` si la salud del personaje es mayor a 0, y `False` en caso contrario.

---

### 2. Crear la Clase `Guerrero`
- **Descripción:**
  Representa a un personaje especializado en ataques físicos con espada.

- **Tareas:**
  1. Hereda de `Personaje`.
  2. En el constructor, agrega un nuevo atributo `fuerza`, que representará el daño que causa en sus ataques. La `fuerza` del guerrero por defecto debe de ser `15`. La `salud` del guerrero por defecto debe ser `120`.
  3. Sobrescribe el método `atacar(otro_personaje)` para reducir la salud del oponente según el valor de `fuerza`.
  4. Asegúrate de que al atacar, se imprima un mensaje indicando el ataque realizado.

---

### 3. Crear la Clase `Mago`
- **Descripción:**
  Representa a un personaje que ataca usando hechizos mágicos.

- **Tareas:**
  1. Hereda de `Personaje`.
  2. En el constructor, agrega un nuevo atributo `poder_magico` para definir el daño de sus hechizos.La `salud` del mago debe ser por defecto `90`. El `poder_magico` del mago debe ser por defecto `20`.
  3. Sobrescribe el método `atacar(otro_personaje)` para reducir la salud del oponente según el valor de `poder_magico`.
  4. Asegúrate de que al atacar, se imprima un mensaje indicando el ataque realizado.

---

### 4. Implementar la Función `combate()`
- **Descripción:**
  Simula un combate entre un Guerrero y un Mago, alternando ataques hasta que uno de los dos pierda toda su salud.

- **Tareas:**
  1. Crea una instancia de `Guerrero` con un nombre personalizado.
  2. Crea una instancia de `Mago` con un nombre personalizado.
  3. Crea una variable `turno` que permita alternar entre ataques de cada personaje.
  4. Implementa un bucle que continúe ejecutándose mientras ambos personajes estén vivos.
  5. En cada turno, el personaje correspondiente debe atacar al otro.
  6. Después de cada ataque, imprime la salud actual de ambos personajes.
  7. Cuando uno de los dos personajes llegue a `0` de salud, imprime quién es el ganador del combate.

---

## Resultado Esperado

Al ejecutar el código correctamente, el programa mostrará algo similar a lo siguiente:

```sh
¡Inicia el combate!

Arthur (Guerrero) ataca a Merlin con su espada.
Salud de Arthur: 120
Salud de Merlin: 75

Merlin (Mago) lanza un hechizo a Arthur.
Salud de Arthur: 100
Salud de Merlin: 75

...
¡Arthur ha ganado el combate con X de salud restante!
```

El resultado puede variar dependiendo del flujo del combate.