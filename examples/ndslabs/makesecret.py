#!/usr/bin/env python
import os
import yaml
import sys
import subprocess


def main(argv):
    certname = argv[1]
    cname = certname+".crt"
    kname = certname+".key"
    subprocess.call(['openssl', 'req', '-new', '-newkey', 'rsa:2048', '-days', '365', '-nodes', '-x509', '-keyout', kname, '-out', cname])
    with open(cname) as f:
        clines = f.readlines()
    with open(kname) as f:
        klines = f.readlines()
    # Cat the lines into one
    kdata = ''
    cdata ='' 
    klines[0]=''
    clines[0]=''
    klines[len(klines)-1] = ''
    clines[len(clines)-1] = ''
    for l in klines:
        print l
        kdata = kdata + l.rstrip('\n')
    for l in clines:
        cdata = cdata + l.rstrip('\n')
    print 'cdata:', cdata
    print 'kdata:', kdata


    #
    # write the yaml
    #
    k8yml = {
        'apiVersion': 'v1', 
        'kind': 'Secret', 
        'metadata':  {
            'name':  certname+'-secret' },
        'type': 'Opaque',
        'data': {
            'tls.crt': cdata,
            'tls.key': kdata },
        }
    with open(certname+'-secret.yml', 'w') as yaml_file:
        yaml_file.write( yaml.dump(k8yml, default_flow_style=False))

if __name__ == "__main__":
    main(sys.argv)
