from utils.Plancia_tris import plancia
from utils.ai_tris import scegli_mossa_ai


class game_tris():
    def __init__(self, lato=6):
        self.lato = lato
        print('IL GIOCO INIZIA')

    def play(self):
        def str_to_tupla(stringa):
            num = list()
            for i in stringa:
                if ord(i) >= 49 and ord(i) <= 51:
                    num.append(int(i))
            if len(num) != 2:
                return (9, 9)
            else:
                return tuple(num)

        computer = 'entra nel loop'
        while computer not in {'Y', 'y', 'N', 'n'}:
            computer = input('Vuoi giocare contro il computer? [Y/N]')
        if computer in {'Y', 'y'}:
            segno = 'entra nel loop'
            while segno not in {'X', 'x', 'O', 'o', '0'}:
                segno = input('Con che segno vuoi giocare? ')

        tavolo = plancia(self.lato)
        tavolo.stampa_plancia()
        contatore = 0
        while tavolo.check_vittoria() == 2:
            if contatore % 2 == 0:
                flag = True
                while flag:
                    if computer in {'N', 'n'} or (computer in {'Y', 'y'} and segno in {'X', 'x'}):
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
                    if computer in {'N', 'n'} or (computer in {'Y', 'y'} and segno in {'O', 'o', '0'}):
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
        if tavolo.check_vittoria() == 0:
            print('Pareggio')
        elif tavolo.check_vittoria() == 1:
            print('Ha vinto il giocatore delle X')
        elif tavolo.check_vittoria() == -1:
            print('Ha vinto il giocatore delle O')
        print('\n')
