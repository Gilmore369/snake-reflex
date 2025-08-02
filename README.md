# Snake Reflex

Este repositorio contiene una versión retro del juego de la serpiente (Snake) construida
con **Reflex**.  La implementación combina Python para el backend con un
front‑end en HTML, CSS y JavaScript que emula el aspecto de los teléfonos Nokia
clásicos: fondo negro, gráficos en verde lima y controles sencillos con las
flechas del teclado.  La serpiente se desplaza en una cuadrícula de 20×20
casillas, come manzanas que aparecen aleatoriamente y aumenta su longitud y
puntuación.

## Instalación

Siga estos pasos para preparar el entorno de desarrollo y ejecutar el juego
localmente:

1. **Clonar el repositorio y crear un entorno virtual**

   ```bash
   git clone https://github.com/Gilmore369/snake-reflex.git
   cd snake-reflex
   python -m venv venv
   source venv/bin/activate  # En Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

   El archivo `requirements.txt` incluye la dependencia de `reflex==0.3.10`.

2. **Ejecutar la aplicación**

   Una vez instaladas las dependencias puede lanzar el servidor de desarrollo
   utilizando el módulo de Reflex.  Esto arrancará la aplicación en el puerto
   3000 y no abrirá el navegador automáticamente (según la configuración de
   `rxconfig.py`).

   ```bash
   python -m reflex run
   ```

   Abra su navegador en [http://localhost:3000](http://localhost:3000) para
   disfrutar del juego.

## Cómo jugar

* Utilice las flechas del teclado para mover la serpiente (arriba, abajo,
  izquierda, derecha).
* Seleccione el nivel de dificultad (`Easy`, `Medium`, `Hard`) en el menú
  desplegable.  Cada nivel ajusta la velocidad de movimiento.
* La puntuación (Score) muestra cuántas manzanas ha comido la serpiente.
* El juego termina (Game Over) si la serpiente colisiona con una pared o con
  su propio cuerpo.  Puede reiniciar el juego tras finalizar.

## Pruebas unitarias

La carpeta `tests/` contiene pruebas unitarias escritas con **PyTest** que
validan la lógica principal del juego implementada en
`snake_reflex/snake_game_logic.py`.  Para ejecutarlas:

```bash
pip install pytest
pytest
```

Las pruebas comprueban que:

* Las manzanas se generan en celdas libres y nunca sobre la serpiente.
* Las colisiones con las paredes y con el propio cuerpo se detectan
  correctamente.
* La serpiente crece y aumenta su puntuación al comer una manzana.

## Despliegue

Puede automatizar el despliegue de la aplicación a servicios como Vercel o
Railway mediante scripts de automatización o flujos de trabajo de GitHub
Actions.  Un ejemplo sencillo sería definir un objetivo `deploy` en un archivo
`Makefile` o un flujo de GitHub Actions que compile los assets y publique el
sitio tras cada `merge` a la rama `main`.

## Licencia

Este proyecto se proporciona bajo los términos de la licencia MIT.
