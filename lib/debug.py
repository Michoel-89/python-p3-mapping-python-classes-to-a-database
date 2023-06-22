#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    hello = Song("Hello", "25")
    hello.save()

    despacito = Song("Despacito", "Vida")
    despacito.save()

    hello.id
    
    despacito.id
    import ipdb; ipdb.set_trace()
