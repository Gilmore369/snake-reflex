# Primero parcheamos sys.exception para que no rompa Reflex en Py3.10+
import sys, traceback
sys.exception = lambda: traceback.format_exc()

import reflex as rx

def index():
    # Inyectamos el iframe como HTML crudo
    html = (
        '<iframe '
        'src="/snake/index.html" '
        'width="420px" '
        'height="480px" '
        'style="border:none;" '
        '></iframe>'
    )
    return rx.center(
        # rx.html() renderiza HTML crudo vía dangerouslySetInnerHTML
        rx.html(
            dangerously_set_inner_html={"__html": html}
        ),
        height="100vh",
        background_color="black",
    )

# Creamos la app y añadimos la página en la ruta raíz "/"
app = rx.App()
app.add_page(index, route="/", title="Snake Reflex")
