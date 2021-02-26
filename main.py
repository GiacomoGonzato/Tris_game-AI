from utils.gioco_tris import game_tris
import sys

if __name__ == "__main__":
    giocare = 'y'
    while True:
        if giocare == 'y':
            gioco = game_tris(5)
            gioco.play()
            giocare = input("La faccimo un'altra partita? [Y/N] ").lower()
        else:
            sys.exit()
