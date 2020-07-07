#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: genesisthomas
"""

import sys
from setuptools import setup, find_packages
OPTIONS = {}
mainscript = 'perfecto/perfectoemailer.py'
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='perfectoemailer',
    #  version='1.0.0', #testpypi
     version='1.0.6',
     author="Genesis Thomas",
     author_email="gthomas@perforce.com",
     description="perfectoemailer is an automated emailable reporter along with AI graphs & predictions",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='GPLv3',
     keywords = ['Perfecto', 'appium', 'selenium', 'testing', 'api', 'automation'],
     url="https://github.com/genesisthomas/perfectoemailer",
     install_requires=[
            'requests','configparser','termcolor','numpy','cython','pandas','retrying','ephem','pymeeus','easydict','korean-lunar-calendar','MarkupSafe','jinja2','matplotlib', 'colorama','LunarCalendar','holidays','cmdstanpy','convertdate','openpyxl','wheel','pystan','xlrd','jinja2','tzlocal','plotly','fbprophet'
      ],
     packages=find_packages(),
     include_package_data=True,
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
         'Operating System :: OS Independent'
     ],
     entry_points={"console_scripts": ["perfectoemailer=perfecto.perfectoemailer:main"]}
 )