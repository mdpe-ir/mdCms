#!/bin/bash

echo "Enter App Name :   "
read dic

cd $dic



printf "from django.urls import path" >> urls.py

printf "\n" >> urls.py

printf "from .views import *" >> urls.py

printf "\n" >> urls.py

printf "app_name = '"$dic"' " >> urls.py

printf "\n" >> urls.py 

printf "urlpatterns = [ " >> urls.py

printf "\n" >> urls.py 

printf " path('', index, name='home')," >> urls.py

printf "\n" >> urls.py 

printf "]" >> urls.py

printf "\n" >> urls.py 





