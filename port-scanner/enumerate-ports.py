import socket
from threading import Thread, Semaphore


screenLock = Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('garbage-data\r\n'.encode())
        results = connSkt.recv(100)

        screenLock.acquire()
        print('[+] {}/tcp open'.format(tgtPort))
        print('[+] {}\n'.format(results.decode()))
    except:
        screenLock.acquire()
        print('[-] {}/tcp closed\n'.format(tgtPort))
    finally:
        screenLock.release()
        connSkt.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve {}: Unknown host".format(tgtHost))
        return

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+] Scan Results for: {}\n'.format(tgtName[0]))
    except:
        print('\n[+] Scan Results for: {}\n'.format(tgtIP))

    socket.setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
