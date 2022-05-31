#!/bin/bash
for file in *.py; do
#"$file" las comillas permiten incluir aquellos archivos que contengan espacios en el nombre
    name=$(basename "$file" .py)
    echo mv "$file" "$name.html"
done