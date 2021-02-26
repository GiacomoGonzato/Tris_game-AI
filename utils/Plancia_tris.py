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
        # Vince O -----> -1
        # Pareggio ---->  0
        # In corso ---->  2

        for i in range(3):
            a = self.get_plancia[i][0]
            b = self.get_plancia[i][1]
            c = self.get_plancia[i][2]

            if a == 'X' and a == b and a == c:
                return 1
            elif a == 'O' and a == b and a == c:
                return -1
        for i in range(3):
            a = self.get_plancia[0][i]
            b = self.get_plancia[1][i]
            c = self.get_plancia[2][i]

            if a == 'X' and a == b and a == c:
                return 1
            elif a == 'O' and a == b and a == c:
                return -1

        a = self.get_plancia[0][0]
        b = self.get_plancia[1][1]
        c = self.get_plancia[2][2]
        d = self.get_plancia[0][2]
        e = self.get_plancia[2][0]

        if a == 'X' and a == b and a == c:
            return 1
        elif a == 'O' and a == b and a == c:
            return -1
        elif d == 'X' and d == b and d == e:
            return 1
        elif d == 'O' and d == b and d == e:
            return -1
        else:
            pareggio = True
            for i in range(3):
                for j in range(3):
                    if self.get_plancia[i][j] == '':
                        pareggio = False
            if pareggio == True:
                return 0
            else:
                return 2
