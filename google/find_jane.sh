#!/bin/bash
#crear el archivo de jane
#test que el archivo no tenga nada escrito
if test -e /media/an-b3z/Windows/files/files/linux/data/oldFiles.txt;
then
    echo "el archivo oldFiles.txt ya existe, será sobrescrito"
fi
> /media/an-b3z/Windows/files/files/linux/data/oldFiles.txt
#buscar las lineas del archivo list.txt con los filenames jane, y guardarlo en una variable files
grep " jane " /media/an-b3z/Windows/files/files/linux/data/list.txt | cut -d ' ' -f 3 | while read -r filename ; do
    echo "Matched name:  $filename"
    #si el archivo existe
    if test -e $filename;
    then 
        #files=$files" "$filename
        echo "File exists"; 
        echo $filename>> /media/an-b3z/Windows/files/files/linux/data/oldFiles.txt
    else echo "File doesn't exist"; 
    fi
done
