#bin/bash

# to modify this file change these variables
KEYS_FILE=private.pem
PASSWORD_FILE=key
PUBLIC_KEY_FILE=public.pem

openssl genrsa -out $KEYS_FILE -aes256 -passout file:$PASSWORD_FILE 1024
openssl rsa -aes256 -passin file:$PASSWORD_FILE -inform PEM -outform PEM -pubout -in $KEYS_FILE -out $PUBLIC_KEY_FILE