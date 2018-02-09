#!/usr/bin/python

import re, urllib2, os

while True:

    while True:

        print('\n Please enter the url you would like to check:')
        userURL = raw_input()

        if userURL.startswith('http'):
            print '\n    Enter url without http, e.g. www.'
            continue
        elif userURL == '':
            continue
        else:
            break

    request = urllib2.Request('http://' + userURL)
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0')
    response = urllib2.urlopen(request)
    html = response.read()
    coinSearch = re.findall('coin-hive.com|coinhive|CoinHive|var miner|miner.start|monero-miner', html)


    print '\n Your External ip: '
    os.system('curl ipinfo.io/ip')

    print '\n Website Response code: '
    print str(response.getcode())

    print '\n Scan Results: '
    if len(coinSearch) == 0:
      print 'nothing found \n'
    else:
      print 'Possible crypto mining found! \n'
      print "Keywords found: " + '\n * ' + '\n * '.join(set(coinSearch))

    inp = raw_input('\n Would you like to scan another url? (y/n): ')
    if(inp == "y" or inp == "Y"):
      continue
    else:
      print '\n Ciao!\n'
      break
