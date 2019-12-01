#!/usr/bin/python3

import os
import sys
import socket
from termcolor import colored


def retBanner(host, port):
    try:
        socket.setdefaulttimeout(2)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        banner = sock.recv(1024)

        return banner
    except:
        return


def checkVuln(banner, filename):
    f = open(filename, "r")

    for line in f.readlines():
        if line.strip('\n') in banner.decode("utf-8"):
            print(f"[*] Server is vulnerable to: " + banner.decode("utf-8").strip('\n'))


def main():

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] File doesn't exists...! Aborting.")
            exit(0)

        if not os.access(filename, os.R_OK):
            print("[-] Access Denied...! File is not accessible!")
            exit(1)
    else:
        print("Usage: " + sys.argv[0] + " <vuln filename>")

    host = str(input(colored("[*] Enter the IP: ", 'blue')))
    p = int(input(colored('[*] Enter the port upper bound: ', 'blue')))

    for port in range(1,p+1):
        banner = retBanner(host, port)

        if banner:
            print(f"[+] {host}:{port} ->   " + banner.decode("utf-8"))
            checkVuln(banner, filename)


main()
