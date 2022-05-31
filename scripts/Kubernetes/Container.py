Container
     2 estados
        rest-> el contenedor es un archivo en disco
               llamado container image o container repository
        running-> al iniciar el contenedor, el Container Engine, lo desempaca (files y metadata)
                y le da el control al kernel de linux
                iniciar un contenedor es similar a iniciar un kernel de linux y 
                requiere hacer una llamada al api del kernel linux 
                ésta llamada inicia una extra aislada y monta una copia de los archivos en la imagen
    Una vez corriendo el contenedor es un proceso más de linux.
    El proceso de levantar un contenedor como el formato de imagen en disco, son definidos y gobernados
    por estándares

    
Image
    Hay diferentes formatos de imagen:
        Docker
        Appc
        LXD
    La industria se rige bajo Open Container Initiative que define 
    Container Image Format Specification que define el formato en disco así como la metadata
        como hw arquitecture y operating system.
    Algunos Container Engines son:
        Docker
        Cri-O
        Railcar
        RKT
Container Image
Registry
Repository
Tag 
Base Image
Platform Image
Layer





