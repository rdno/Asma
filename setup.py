#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import os

def get_icons():
    ls = []
    for i in glob.glob("icons/*x*"):
        ls.append(("share/icons/hicolor/"+os.path.split(i)[1]+"/apps",
                   glob.glob(i+"/*.png")))
    return ls
data_files = [
    ("share/applications", ["data/asma.desktop"])
]
data_files.extend(get_icons())
print data_files
from setuptools import setup

setup(name="asma",
      version="0.2",
      package_dir={"":"src"},
      packages = ["asma", "asma.addons"],
      scripts = ["src/asma.py"],
      description= "All System MAnagers",
      author="Rıdvan Örsvuran",
      author_email="flasherdn@gmail.com",
      data_files=data_files
)
