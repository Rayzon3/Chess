import pygame
import engine

WIDTH = HEIGHT = 400
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ["wE", "wH", "wB", "wQ", "wK", "wP", "bE", "bH", "bB", "bQ", "bK", "bP"]
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("/Users/rahulbhardwaj/Documents/Dev/Chess/assets/" + piece + ".png"), (SQUARE_SIZE - 8, SQUARE_SIZE - 8))


def main():
    pygame.init()
    boardWindow = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    boardWindow.fill(pygame.Color("white"))
    gameState = engine.GameState()
    loadImages()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        drawGameState(boardWindow, gameState)
        clock.tick(MAX_FPS)
        pygame.display.flip()
            

def drawGameState(boardWindow, gameState):
    drawSquares(boardWindow)
    drawPieces(boardWindow, gameState.board)


def drawSquares(boardWindow):
    colors = [pygame.Color("white"), pygame.Color("dark gray")]
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            color = colors[((i + j) % 2)]
            pygame.draw.rect(boardWindow, color, pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(boardWindow, board):
    for i in range(DIMENSION):
        for j in range(DIMENSION):
            piece = board[i][j]
            if piece != "--":
                boardWindow.blit(IMAGES[piece], pygame.Rect(j * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


if __name__ == "__main__":
    main()