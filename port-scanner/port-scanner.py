#!/usr/bin/python3

import optparse
import os
# from . import enumerate-ports
enumerate_ports = __import__('enumerate-ports')


def main():
    parser = optparse.OptionParser(
        'usage {} -H <target host> -p <target port>'.format(os.path.basename(__file__)))

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

    enumerate_ports.portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
