#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
  return 'Moe Flask приложение в контейнере Docker.'
 
if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')

=======

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Мое Flask приложение в контейнере Docker.'

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
>>>>>>> 76ec82df18452ecf29d80cda593eb0839f0e4217
