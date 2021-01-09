#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2017-09-24 14:53
# @Author    : modm
'''
you can start the server by uwsgi
like gunicorn -w 4 ScrapyKeeper.uwsgi:app
'''
import warnings
warnings.filterwarnings("ignore", message="Importing flask.ext.restful") 

from ScrapyKeeper.app import app, initialize

initialize()
