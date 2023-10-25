@echo off
@title MySQL Setup

call pip install -r requirements.txt -U
cls
py setup_mysql.py
@pause