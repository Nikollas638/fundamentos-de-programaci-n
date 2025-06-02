import pygame
import random

pygame.init()

# Constantes
ANCHO_VENTANA = 300
ALTO_VENTANA = 600
TAM_CUADRO = 30
COLUMNAS = ANCHO_VENTANA // TAM_CUADRO
FILAS = ALTO_VENTANA // TAM_CUADRO

# Colores
NEGRO = (0, 0, 0)
GRIS = (50, 50, 50)
COLORES = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (0, 255, 255),
    (255, 0, 255),
    (255, 165, 0),
]

FIGURAS = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
]

class Pieza:
    def __init__(self, x, y, figura):
        self.x = x
        self.y = y
        self.figura = figura
        self.color = random.choice(COLORES)

    def rotar(self):
        self.figura = [list(fila) for fila in zip(*self.figura[::-1])]

def crear_tablero():
    return [[NEGRO for _ in range(COLUMNAS)] for _ in range(FILAS)]

def colision(tablero, pieza):
    for i, fila in enumerate(pieza.figura):
        for j, celda in enumerate(fila):
            if celda:
                nueva_x = pieza.x + j
                nueva_y = pieza.y + i
                if (
                    nueva_x < 0 or nueva_x >= COLUMNAS or
                    nueva_y >= FILAS or
                    (nueva_y >= 0 and tablero[nueva_y][nueva_x] != NEGRO)
                ):
                    return True
    return False

def fijar_pieza(tablero, pieza):
    for i, fila in enumerate(pieza.figura):
        for j, celda in enumerate(fila):
            if celda:
                tablero[pieza.y + i][pieza.x + j] = pieza.color

def eliminar_filas(tablero):
    nuevas_filas = [fila for fila in tablero if any(c == NEGRO for c in fila)]
    cantidad_eliminadas = FILAS - len(nuevas_filas)
    while len(nuevas_filas) < FILAS:
        nuevas_filas.insert(0, [NEGRO for _ in range(COLUMNAS)])
    return nuevas_filas, cantidad_eliminadas

def dibujar_tablero(pantalla, tablero, pieza, fuente, nivel):
    pantalla.fill(NEGRO)

    for y in range(FILAS):
        for x in range(COLUMNAS):
            pygame.draw.rect(
                pantalla,
                tablero[y][x],
                (x * TAM_CUADRO, y * TAM_CUADRO, TAM_CUADRO, TAM_CUADRO),
                0
            )
            pygame.draw.rect(
                pantalla,
                GRIS,
                (x * TAM_CUADRO, y * TAM_CUADRO, TAM_CUADRO, TAM_CUADRO),
                1
            )

    for i, fila in enumerate(pieza.figura):
        for j, celda in enumerate(fila):
            if celda:
                rect = pygame.Rect(
                    (pieza.x + j) * TAM_CUADRO,
                    (pieza.y + i) * TAM_CUADRO,
                    TAM_CUADRO,
                    TAM_CUADRO
                )
                pygame.draw.rect(pantalla, pieza.color, rect, 0)
                pygame.draw.rect(pantalla, GRIS, rect, 1)

    texto_nivel = fuente.render(f'Nivel: {nivel}', True, (255, 255, 255))
    pantalla.blit(texto_nivel, (10, 10))

    pygame.display.flip()

def main():
    pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tetris")
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Arial", 20)

    tablero = crear_tablero()
    pieza = Pieza(COLUMNAS // 2 - 1, 0, random.choice(FIGURAS))
    velocidad = 15
    contador = 0
    nivel = 1
    lineas_totales = 0
    corriendo = True

    while corriendo:
        reloj.tick(30)
        contador += 1

        if contador >= velocidad:
            contador = 0
            pieza.y += 1
            if colision(tablero, pieza):
                pieza.y -= 1
                fijar_pieza(tablero, pieza)
                tablero, eliminadas = eliminar_filas(tablero)
                lineas_totales += eliminadas
                if lineas_totales >= nivel * 3:
                    nivel += 1
                    if velocidad > 2:
                        velocidad -= 1
                pieza = Pieza(COLUMNAS // 2 - 1, 0, random.choice(FIGURAS))
                if colision(tablero, pieza):
                    print("Game Over")
                    corriendo = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    pieza.x -= 1
                    if colision(tablero, pieza):
                        pieza.x += 1
                elif evento.key == pygame.K_RIGHT:
                    pieza.x += 1
                    if colision(tablero, pieza):
                        pieza.x -= 1
                elif evento.key == pygame.K_DOWN:
                    pieza.y += 1
                    if colision(tablero, pieza):
                        pieza.y -= 1
                elif evento.key == pygame.K_SPACE:
                    while not colision(tablero, pieza):
                        pieza.y += 1
                    pieza.y -= 1
                    fijar_pieza(tablero, pieza)
                    tablero, eliminadas = eliminar_filas(tablero)
                    lineas_totales += eliminadas
                    if lineas_totales >= nivel * 3:
                        nivel += 1
                        if velocidad > 2:
                            velocidad -= 4
                    pieza = Pieza(COLUMNAS // 2 - 1, 0, random.choice(FIGURAS))
                    if colision(tablero, pieza):
                        print("Game Over")
                        corriendo = False
                elif evento.key == pygame.K_UP:
                    pieza.rotar()
                    if colision(tablero, pieza):
                        for _ in range(3):
                            pieza.rotar()

        dibujar_tablero(pantalla, tablero, pieza, fuente, nivel)

    pygame.quit()

if __name__ == "__main__":
    main()
