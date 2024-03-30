import socket
import sys
import argparse
from termcolor import colored

def main():
    objetivo = input('Introduce la IP a escanear: ')
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print (colored(f'El puerto {port} está abierto.', 'blue'))
        
        s.close()





if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print (colored('\nSaliendo...\n', 'red'))
        exit()