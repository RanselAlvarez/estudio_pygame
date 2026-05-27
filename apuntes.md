* `pygame.init()` → Prepara los módulos internos (gráficos, entrada, audio, fuentes).
* `pygame.display.set_mode((ancho, alto))` → Crea la ventana donde dibujaremos.
* **El ****bucle principal** (`while corriendo:`) → Es el corazón de todo programa visual. Sin él, el programa termina en milisegundos.
* `pygame.event.get()` → Lee lo que hace el usuario (teclas, clics, cerrar ventana).
* `pygame.display.flip()` → Refresca la pantalla para mostrar los cambios acumulados.
* `pygame.quit()` → Cierra los recursos correctamente al final.


# --- DETECCIÓN DE COLISIÓN ---

distancia = math.hypot(x - enemigo_x, y - enemigo_y)

if distancia < radio + enemigo_radio:
