import pygame
import sys

pygame.init()


width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Gato")

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

black = (0, 0, 0)
white = (255, 255, 255)

def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, black, (0, i * height / 3), (width, i * height / 3), 2)

    for i in range(1, 3):
        pygame.draw.line(screen, black, (i * width / 3, 0), (i * width / 3, height), 2)

    font = pygame.font.SysFont(None, 60)
    for i in range(3):
        for j in range(3):
            cell_value = board[i][j]
            text = font.render(cell_value, True, black)
            text_rect = text.get_rect(center=(j * width / 3 + width / 6, i * height / 3 + height / 6))
            screen.blit(text, text_rect)

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            return True

    if board[0][0] == board[1][1] == board[2][2] != '':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        return True

    return False

def main():
    turn = 'X'
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                row = int(pos[1] // (height / 3))
                col = int(pos[0] // (width / 3))

                if board[row][col] == '':
                    board[row][col] = turn

                    if check_winner():
                        print(f'¡Jugador {turn} gana!')
                        game_over = True
                    elif all(board[i][j] != '' for i in range(3) for j in range(3)):
                        print('¡Empate!')
                        game_over = True
                    else:
                        turn = 'O' if turn == 'X' else 'X'

        screen.fill(white)
        draw_board()
        pygame.display.flip()

if __name__ == "__main__":
    main()