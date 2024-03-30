import socket
import sys
import argparse
from termcolor import colored


parser = argparse.ArgumentParser(description='Escaner de puertos')
parser.add_argument('-i', '--ip', required=True, help='Debes introducir una IP.')
parser = parser.parse_args()

def main():
    if parser.ip:
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            resultado = s.connect_ex((parser.ip, port))
            if resultado == 0:
                print (colored(f'El puerto {port} está abierto.', 'blue'))
            
                

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print (colored('\nSaliendo...\n', 'red'))
        exit()