#bin/bash

# to modify this file change these variables
KEY_FILE=public.pem
RND_KEY_FILE=rnd_pub_key
FILE=not_encrypted.data
ENCRYPTED_FILE=partial_encrypted.data
FINAL_ENCRYPTED_FILE=encrypted.data

# Initial data
echo 'Initial data:'
cat $FILE
echo

# encrypt
openssl enc -aes-256-cbc -kfile $RND_KEY_FILE -in $FILE -out $ENCRYPTED_FILE
openssl rsautl -encrypt -inkey $KEY_FILE -pubin -in $ENCRYPTED_FILE -out $FINAL_ENCRYPTED_FILE

# results
echo 'Encrypted data:'
cat $FINAL_ENCRYPTED_FILE
echo

# clean up
rm $ENCRYPTED_FILE