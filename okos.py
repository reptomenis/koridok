def köridő(sor):
    '''Bedobjuk a köridőt string-ként (00:00:00), és visszatér másodpercekkel integer-ként.'''
    perc = int(sor[4][3:5])
    sec  = int(sor[4][6:])
    return perc*60 + sec