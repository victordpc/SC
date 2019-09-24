#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import xmlrpclib
import xmlrpc
import http.client


def main():
    # Accedemos a Odoo
    login()



def login():
    # common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
    common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
    res =common.version()
    #{
    #    "server_version": "8.0",
    #    "server_version_info": [8, 0, 0, "final", 0],
    #    "server_serie": "8.0",
    #    "protocol_version": 1,
    #}
    print(res)



if __name__ == '__main__':
    # info = xmlrpclib.ServerProxy('https://demo.odoo.com/start').start()
    info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
    url, db, username, password = \
        info['host'], info['biopressman'], info['vpino@ucm.es'], info['123456']

    main()

    print('Fin')



