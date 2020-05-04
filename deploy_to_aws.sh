#!/bin/bash
pip3 install requests -t ./package --upgrade
cd package
zip -r ${OLDPWD}/function.zip .
cd ..
zip -g function.zip lambda_function.py
aws lambda update-function-code --function-name PostToAdaFruitIO --zip-file fileb://function.zip
