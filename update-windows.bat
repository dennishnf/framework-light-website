@ECHO.
git pull
@ECHO.
py "md2html-windows.py" 
@ECHO.
git add -A
git commit -m "making website"
git push -u origin master
@ECHO.
