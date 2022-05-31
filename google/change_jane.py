#!/usr/bin/env python3
import sys
import subprocess
def change_name(old_name_file):
    print("mensaje")
    #validar que el archivo no esté vacío
    old_name="jane"
    new_name="jdoe"
    new_line=""
    with open(old_name_file) as file_names:
        for line in file_names.readlines():
            line=line.strip()
            new_line=line.replace(old_name,new_name)
            #en log
            print("line: {} replaced with:{}".format(line,new_line)) 
            #en archivo
            result=subprocess.run(["mv",line,new_line], capture_output=True)
            print(result.returncode)
            print(result.stdout)
            print(result.stderr)
    file_names.close()

if __name__=="__main__":    
    old_name_file=sys.argv[1]
    change_name(old_name_file)
    sys.exit(0)stream 


    stream.read()
    me dice el numero de bytes de datos

    class MultiStream:
    def read(self, n: int) -> List[int]:
        ...

    def add(self, stream: Stream) -> None:
        ...

    def remove(self, stream: Stream) -> None: