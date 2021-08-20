from bot_client_pasha import run

from multiprocessing import Process

tokens = ['1697352371:AAF7wMrG7_mmOCmpfA6_4JzlxJ9WujuAnZU', '1964670988:AAFaHLy14k0x5JKRZ_9L3M0hR9c3vbyBguc']


def proc(token):
    p = Process(target=run, args=(token,))
    p.start()
    return p


# procs = []
if __name__ == '__main__':
    proc(tokens[0])
    proc(tokens[1])
    proc('1162664199:AAEJkIOBBSKU_FoUCVjC1qpreUKLeL1Ky8s')