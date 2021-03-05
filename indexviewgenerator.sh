#!/bin/bash

echo "Enter App Name :   "
read dic

cd $dic

printf "\n" >>views.py
printf "\n" >>views.py
printf "\n" >>views.py

printf "def index(request):" >>views.py

printf "\n" >>views.py

printf "  template = '' " >>views.py

printf "\n" >>views.py

printf "  context = {}" >>views.py

printf "\n" >>views.py

printf "  return render(request, template, context)" >>views.py
