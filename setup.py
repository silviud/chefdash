#!/usr/bin/env python
from setuptools import setup

setup(
	name = 'chefdash',
	version = '0.1.0',
	author = 'Sidebolt Studios',
	author_email = 'contact@sidebolt.com',
	scripts = ['bin/chefdashd.py',],
	packages = [
		'chefdash',
	],
	package_data = {
		'chefdash': ['static/*.png', 'static/*.ico', 'static/*.css', 'static/*.js', 'templates/*.html'],
	},
	url = 'http://github.com/sidebolt/chefdash/',
	description = 'Chef Dash'
)
