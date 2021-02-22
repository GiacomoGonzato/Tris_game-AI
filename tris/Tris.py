class plancia():
    def __init__(self, lato=6):
        self.lato = lato*2
        self.get_plancia = [['' for i in range(3)] for j in range(3)]

    def stampa_plancia(self):
        def quadrato(simbolo=''):
            square = [['  ' for j in range(self.lato)]
                      for i in range(self.lato)]
            if simbolo == 'X' or simbolo == 'x':
                for i in range(self.lato):
                    square[i][i] = 'XX'
                    square[i][self.lato - 1 - i] = 'XX'
            elif simbolo == 'O' or simbolo == 'o' or simbolo == '0':
                for i in range(self.lato):
                    for j in range(self.lato):
                        if (i - (self.lato - 1)/2)**2 + (j - (self.lato - 1)/2)**2 <= (self.lato // 2-1)**2:
                            square[i][j] = 'OO'
            return square

        def unire_matrici(mat1, mat2):
            for riga in range(len(mat2)):
                mat1[riga].extend(mat2[riga])

        def stampa_riga(lista):
            print('-'*self.lato*6 + '-'*4)
            riga = [['|'] for i in range(self.lato)]
            for simbolo in lista:
                unire_matrici(riga, quadrato(simbolo))
                unire_matrici(riga, [['|'] for i in range(self.lato)])
            for y in range(len(riga)):
                linea = ''
                for x in range(len(riga[0])):
                    linea += riga[y][x]
                print(linea)

        for linea in self.get_plancia:
            stampa_riga(linea)
        print('-'*self.lato*6 + '-'*4)

    def posiziona(self, coordinata, simbolo):
        self.get_plancia[coordinata[0] - 1][coordinata[1] - 1] = simbolo

    def check_vittoria(self):
        # Vince X ----->  1
        # Vince O ----->  2
        # Pareggio ---->  0
        # In corso ----> -1
        for i in range(3):
            if self.get_plancia[i][0] == 'X' and self.get_plancia[i][0] == self.get_plancia[i][1] and self.get_plancia[i][0] == self.get_plancia[i][2]:
                return 1
            elif self.get_plancia[i][0] == 'O' and self.get_plancia[i][0] == self.get_plancia[i][1] and self.get_plancia[i][0] == self.get_plancia[i][2]:
                return 2
        for i in range(3):
            if self.get_plancia[0][i] == 'X' and self.get_plancia[0][i] == self.get_plancia[1][i] and self.get_plancia[0][i] == self.get_plancia[2][i]:
                return 1
            elif self.get_plancia[0][i] == 'O' and self.get_plancia[0][i] == self.get_plancia[1][i] and self.get_plancia[0][i] == self.get_plancia[2][i]:
                return 2
        if self.get_plancia[0][0] == 'X' and self.get_plancia[0][0] == self.get_plancia[1][1] and self.get_plancia[0][0] == self.get_plancia[2][2]:
            return 1
        elif self.get_plancia[0][0] == 'O' and self.get_plancia[0][0] == self.get_plancia[1][1] and self.get_plancia[0][0] == self.get_plancia[2][2]:
            return 2
        elif self.get_plancia[0][2] == 'X' and self.get_plancia[0][2] == self.get_plancia[1][1] and self.get_plancia[0][2] == self.get_plancia[2][0]:
            return 1
        elif self.get_plancia[0][2] == 'O' and self.get_plancia[0][2] == self.get_plancia[1][1] and self.get_plancia[0][2] == self.get_plancia[2][0]:
            return 2
        else:
            pareggio = True
            for i in range(3):
                for j in range(3):
                    if self.get_plancia[i][j] == '':
                        pareggio = False
            if pareggio == True:
                return 0
            else:
                return -1


class gioco_tris():
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


a = gioco_tris(5)
a.play()
