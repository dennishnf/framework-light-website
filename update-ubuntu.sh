#!/bin/bash

#update
git pull;

#create html files
python md2html-ubuntu.py

#upload
git add -A;
git commit -m "making website";
git push -u origin master;


