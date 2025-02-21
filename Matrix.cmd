@echo off
tilte Matrix
color 0a
mode 1000
goto Greeting

:Greeting
cls
echo Hello Neo.
pause
cls
goto Matrix

:Matrix
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
PING 1.1.1.1 -n 1 -w 0.4 >NUL
goto Matrix