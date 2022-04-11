import nmap
import optparse
import os


def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)

    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print(' [*] {} tcp/{} {}'.format(tgtHost, tgtPort, state))


def main():
    parser = optparse.OptionParser(
        'usage {} -H <target host> -p <target port>'.format(
            os.path.basename(__file__))
    )

    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target port[s] separated by commas')

    (options, _) = parser.parse_args()

    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) or (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)

    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)


if __name__ == '__main__':
    main()
