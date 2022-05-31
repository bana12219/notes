#!/usr/bin/bash
n=0 
command=$1
# este es como sys.argv[1], para acceder al primer commandline
# se mantiene reintentando hasta que command sea 0, que significa status de exito
while $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1)) #va incrementando para esperar mas tiempo entre intentos
    echo "Retry #$n"
done;
