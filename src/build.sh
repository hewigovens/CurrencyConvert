#!/bin/bash

APP=CurrencyConvert
FILES="Config.plist currency.py currency_yuan.png settings_local.py"

EXT_FOLDER="$APP.popclipext"
EXT_FILENAME="$APP.popclipextz"

rm -rf $EXT_FOLDER $EXT_FILENAME
mkdir -p $EXT_FOLDER
for file in $FILES; do
    cp $file $EXT_FOLDER
done

zip -r $EXT_FILENAME $EXT_FOLDER

cp -Rf $EXT_FILENAME ../build

rm -rf $EXT_FOLDER $EXT_FILENAME

open ../build/$EXT_FILENAME