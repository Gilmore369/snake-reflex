import reflex as rx

config = rx.Config(
    app_name="snake_reflex",
    # Dónde está tu carpeta de archivos estáticos (public por defecto)
    static_assets="public",
    # Puerto, navegador, etc.
    port=3000,
    open_browser=False,
)
