#1) encryption
aws kms encrypt --key-id <alias/tutorial> #key de KMS 
-- plintext fileb://sampleSecretFile.txt --outpt text 
--query CiphertextBlob 
--region eu-west-2 > ExampleSecretFileEncrypted.base64 #archivo donde se guarda el texto cifrado
#base 64 decode for linux or Mac OS
#binario de a llave
cat ExampleSecretFileEncrypted.base64 | base64 --decode > ExampleSecretFileEncrypted

#base64 decode for windows 
certutil -decode .\ExampleSecretFileEncrypted.base64.\ExampeEncryptedFile

#2) decryption
aws kms decrypt --ciphertext-blob fileb://ExampleSecretFileEncrypted --output text --query plintext > ExampleFileDecripted.base64 --region eu-west-2

#base64 decode for Linus or Mac OS
cat ExampleFileDecripted.base64 | base64 --decode > ExamleFileDecrypted.txt