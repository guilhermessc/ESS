#bin/bash

# to modify this file change these variables
KEY_FILE=private.pem
RND_KEY_FILE=rnd_pub_key
ENCRYPTED_FILE=encrypted.data
PARTIAL_DECRYPTED_FILE=partial_decrypted.data
FILE=un_encrypted.data
PASSWORD=key

# decrypt
openssl rsautl -decrypt -inkey $KEY_FILE -passin file:$PASSWORD -in $ENCRYPTED_FILE -out $PARTIAL_DECRYPTED_FILE
openssl enc -d -aes-256-cbc -kfile $RND_KEY_FILE -in $PARTIAL_DECRYPTED_FILE -out $FILE

# results
cat $FILE

# clean up
rm $PARTIAL_DECRYPTED_FILE $ENCRYPTED_FILE
