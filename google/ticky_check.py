#!/usr/bin/env python3
import re
import operator
import os
def clasifiying_log_lines(filename):
    '''recibe el nombre del logfile, lee cada línea y clasifica por tipo de error
    el numero de repeticiones y por usuario la cantidad de mensajes ERROR e INFO
    '''
    errors_counter= dict()
    per_user=dict()
    with open(filename) as log_file:
        pattern=r'.*ticky: (INFO|ERROR) (.*) \((.+)\)$'
        for line in log_file.readlines():
            result = re.search(pattern, line)
            print(line, result.groups())
            message_type=result[1]
            message_info=result[2]
            username =result[3]
            if message_type =="ERROR":
                errors_counter[message_info]=errors_counter.get(message_info,0)+1
            per_user_count= per_user.get(username,dict(INFO=0,ERROR=0))
            per_user_count[message_type]=per_user_count.get(message_type)+1
            per_user[username]=per_user_count
    log_file.close()
    sorted_errors=sorted(errors_counter.items(),key=operator.itemgetter(1),reverse=True)
    sorted_users=sorted(per_user.items(),key=operator.itemgetter(0))
    return sorted_errors,sorted_users

def writting_file(header,per_user,fileoutput):
    with open(fileoutput,"w") as output:
        output.write("{},{},{}\n".format(str(header[0]),str(header[1]),str(header[2])))    
        #for lines in per_user:
        for keys,values in per_user:
            output.write("{},{},{}\n".format(str(keys),str(values[header[1]]), str(values[header[2]])))
    output.close()
def writting_error_file(header,error,fileoutput):
    with open(fileoutput,"w") as output:
        output.write("{},{}\n".format(header[0],header[1]))
        for keys,values in error:
            output.write("{},{}\n".format(keys,values))
    output.close()

if __name__=="__main__":
    error_header=["Error", "Count"]
    user_header=["Username", "INFO", "ERROR"]
    path="/media/an-b3z/Windows/files/files/linux/data/"
    filename=os.path.join("syslog.log")
    error_file=os.path.join("error_message.csv")
    user_file=os.path.join("user_statistics.csv")
    error,per_user=clasifiying_log_lines(filename)
    #writting_file(user_header,per_user,user_file)
    #writting_error_file(error_header,error,error_file)
