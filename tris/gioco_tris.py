from Plancia_tris import plancia

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

        tavolo = plancia(self.lato)
        tavolo.stampa_plancia()
        contatore = 0
        while tavolo.check_vittoria() == -1:
            if contatore % 2 == 0:
                flag = True
                while flag:
                    inserire = input(
                        'Inserisci coordinata (riga,colonna) giocare (X): ')
                    inserire = str_to_tupla(inserire)
                    if inserire[0] in {1, 2, 3} and inserire[1] in {1, 2, 3} and tavolo.get_plancia[inserire[0] - 1][inserire[1] - 1] == '':
                        flag = False
                tavolo.posiziona(inserire, 'X')
            else:
                flag = True
                while flag:
                    inserire = input(
                        'Inserisci coordinata (riga,colonna) giocare (O): ')
                    inserire = str_to_tupla(inserire)
                    if inserire[0] in {1, 2, 3} and inserire[1] in {1, 2, 3} and tavolo.get_plancia[inserire[0] - 1][inserire[1] - 1] == '':
                        flag = False
                tavolo.posiziona(inserire, 'O')
            contatore += 1
            tavolo.stampa_plancia()
        if tavolo.check_vittoria() == 0:
            print('Pareggio')
        elif tavolo.check_vittoria() == 1:
            print('Ha vinto il giocatore delle X')
        elif tavolo.check_vittoria() == 2:
            print('Ha vinto il giocatore delle O')
        print('\n')