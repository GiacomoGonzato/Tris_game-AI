from utils.Plancia_tris import plancia


def check_mosse_possibili(board):
    posti_vuoti = []
    for i in range(3):
        for j in range(3):
            if board.get_plancia[i][j] == '':
                posti_vuoti.append((i+1, j+1))
    return posti_vuoti


def valore_mossa(board, contatore):
    tavolo = plancia()
    tavolo.get_plancia = [[board.get_plancia[i][j]
                           for i in range(3)] for j in range(3)]
    if tavolo.check_vittoria() == 1:
        return tavolo.check_vittoria()
    elif tavolo.check_vittoria() == -1:
        return tavolo.check_vittoria()
    elif tavolo.check_vittoria() == 0:
        return tavolo.check_vittoria()

    valori = []
    for mossa in check_mosse_possibili(tavolo):
        banco_prova = plancia()
        banco_prova.get_plancia = [[board.get_plancia[i][j]
                                    for i in range(3)] for j in range(3)]
        if contatore % 2 == 0:
            if 1 in valori:
                break
            banco_prova.posiziona(mossa, 'X')
        else:
            if -1 in valori:
                break
            banco_prova.posiziona(mossa, 'O')
        valori.append(valore_mossa(banco_prova, contatore + 1))
        del banco_prova
    if contatore % 2 == 0:
        return max(valori)
    else:
        return min(valori)


def scegli_mossa_ai(board, contatore):
    if contatore % 2 == 0:
        valore = -100
        simbolo = 'X'
    else:
        valore = 100
        simbolo = 'O'
    for mossa in check_mosse_possibili(board):
        banco_prova = plancia()
        banco_prova.get_plancia = [[board.get_plancia[i][j]
                                    for j in range(3)] for i in range(3)]
        banco_prova.posiziona(mossa, simbolo)
        move_power = valore_mossa(banco_prova, contatore + 1)
        if contatore % 2 == 0:
            if valore < move_power:
                mossa_futura = mossa
        else:
            if valore > move_power:
                mossa_futura = mossa
        valore = move_power
    return mossa_futura
