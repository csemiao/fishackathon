#!/bin/bash

FILE=$PWD/settings.py
echo $FILE

if [ -L $FILE ]
then
    echo 'Existing symlink found, removing it...'
    rm $FILE
fi


echo 'Creating symlink for settings.py...'
{
 pushd .
 cd ..
 cd ./fishackathon2016
 SETTINGS_PATH=$PWD/settings.py
 popd
} &> /dev/null
ln -s $SETTINGS_PATH $PWD/settings.py

echo 'Setting up database...'
cd ..
python manage.py makemigrations
python manage.py migrate

echo 'Done...'
