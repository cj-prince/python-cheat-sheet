#! python3
# pw.py - store user password app 

PassWord = {
  'email': 'hyrheifht4598niuy0ko09iop',
  'website': '1223tydffurbretee',
  'blog': '766885944',
  'flog': 'gytrfu'
}

import sys
if len(sys.argv) < 3:
  print('Bad request')
  sys.exit()

account = sys.argv[1]

import pyperclip
