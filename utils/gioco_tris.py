from utils.plancia_tris import plancia
from utils.ai_tris import scegli_mossa_ai
import ast


def str_to_tupla(stringa):
    num = list()
    for i in stringa:
        if ord(i) >= 49 and ord(i) <= 51:
            num.append(int(i))
    if len(num) != 2:
        return (9, 9)
    else:
        return tuple(num)


class game_tris():
    def __init__(self, lato=6):
        self.lato = lato
        print('IL GIOCO INIZIA')

    def play(self):
        computer = 'entra nel loop'
        while computer not in {'y', 'n'}:
            computer = input('Vuoi giocare contro il computer? [Y/N]').lower()

        if computer == 'y':
            segno = 'entra nel loop'
            while segno not in {'x', 'o', '0'}:
                segno = input('Con che segno vuoi giocare? ').lower()

        tavolo = plancia(self.lato)
        tavolo.stampa_plancia()

        contatore = 0

        check = tavolo.check_vittoria()
        while check == 2:
            if contatore % 2 == 0:
                flag = True

                while flag:
                    if computer == 'n' or (computer == 'y' and segno == 'x'):
                        inserire = input(
                            'Inserisci coordinata (riga,colonna) giocare (X): ')
                        inserire = str_to_tupla(inserire)

                    else:
                        inserire = scegli_mossa_ai(tavolo, contatore)

                    if inserire[0] in {1, 2, 3} and inserire[1] in {1, 2, 3} and tavolo.get_plancia[inserire[0] - 1][inserire[1] - 1] == '':
                        flag = False

                tavolo.posiziona(inserire, 'X')

            else:
                flag = True
                while flag:
                    if computer == 'n' or (computer == 'y' and segno in {'o', '0'}):
                        inserire = input(
                            'Inserisci coordinata (riga,colonna) giocare (O): ')
                        inserire = str_to_tupla(inserire)

                    else:
                        inserire = scegli_mossa_ai(tavolo, contatore)

                    if inserire[0] in {1, 2, 3} and inserire[1] in {1, 2, 3} and tavolo.get_plancia[inserire[0] - 1][inserire[1] - 1] == '':
                        flag = False

                tavolo.posiziona(inserire, 'O')

            contatore += 1
            tavolo.stampa_plancia()

            if contatore >= 4:
                check = tavolo.check_vittoria()

        if check == 0:
            print('Pareggio')
        elif check == 1:
            print('Ha vinto il giocatore delle X')
        elif check == -1:
            print('Ha vinto il giocatore delle O')
        print('\n')
