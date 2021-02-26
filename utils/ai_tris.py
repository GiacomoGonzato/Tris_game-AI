from utils.Plancia_tris import plancia
from math import *


def check_mosse_possibili(board):
    posti_vuoti = []
    for i in range(3):
        for j in range(3):
            if board.get_plancia[i][j] == '':
                posti_vuoti.append((i+1, j+1))
    return posti_vuoti


def valore_mossa(board, contatore, alpha=- inf, beta=inf):
    tavolo = plancia()
    tavolo.get_plancia = [[board.get_plancia[i][j]
                           for i in range(3)] for j in range(3)]

    check_win = tavolo.check_vittoria()
    if check_win == 1:
        return check_win
    elif check_win == -1:
        return check_win
    elif check_win == 0:
        return check_win

    if contatore % 2 == 0:
        valore = - inf
        for mossa in check_mosse_possibili(tavolo):
            banco_prova = plancia()
            banco_prova.get_plancia = [[board.get_plancia[i][j]
                                        for i in range(3)] for j in range(3)]
            banco_prova.posiziona(mossa, 'X')
            valore = max(valore, valore_mossa(
                banco_prova, contatore + 1, alpha, beta))
            del banco_prova
            alpha = max(alpha, valore)
            if beta <= alpha:
                break
        return valore
    else:
        valore = inf
        for mossa in check_mosse_possibili(tavolo):
            banco_prova = plancia()
            banco_prova.get_plancia = [[board.get_plancia[i][j]
                                        for i in range(3)] for j in range(3)]
            banco_prova.posiziona(mossa, 'O')
            valore = min(valore, valore_mossa(
                banco_prova, contatore + 1, alpha, beta))
            del banco_prova
            beta = min(beta, valore)
            if beta <= alpha:
                break
        return valore


def scegli_mossa_ai(board, contatore):
    if contatore % 2 == 0:
        valore = - inf
        for mossa in check_mosse_possibili(board):
            banco_prova = plancia()
            banco_prova.get_plancia = [[board.get_plancia[i][j]
                                        for j in range(3)] for i in range(3)]
            banco_prova.posiziona(mossa, 'X')
            move_power = valore_mossa(banco_prova, contatore + 1)
            if valore < move_power:
                mossa_futura = mossa
            valore = move_power
        return mossa_futura
    else:
        valore = inf
        for mossa in check_mosse_possibili(board):
            banco_prova = plancia()
            banco_prova.get_plancia = [[board.get_plancia[i][j]
                                        for j in range(3)] for i in range(3)]
            banco_prova.posiziona(mossa, 'O')
            move_power = valore_mossa(banco_prova, contatore + 1)
            if valore > move_power:
                mossa_futura = mossa
            valore = move_power
        return mossa_futura
