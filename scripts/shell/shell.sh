echo $PATH
  123  echo $OLDPWD
  124  ls
  125  find aws
  126  find aws*
  127  find . aws*
  #ver variables
    var path
  131  env PATH
  132  echo PATH
  133  echo ${PATH}
  134  echo ${JAVA_HOME}
  153  sudo su
  155  sudo visudo
  #consultar o mostrar un archivo
  183  cat /var/log/messages
  184  cd /var/log
  #buscar Jafar en el archivo, me devuelve la línea
  195  grep Jafar employees.txt
  196  grep -Jafar- employees.txt
  197  grep "Jafar" employees.txt
  198  grep -n "Jafar" employees.txt
  199  grep -no "Jafar" employees.txt
  200  grep -no "Jafar" *
  201  grep -l "Jafar" *
  202  grep -h "Jafar" *
  #hace split de la linea tomando como separador " " y devuelve las columnas solicitadas
  203  cut -d " " -f 3 employees.txt
  204  cut -d " " -f 3,5,6 employees.txt
  205  cut -d " " -f 3,4,5 employees.txt
  206  cut -d " " -f 2,3,5 employees.txt
  207  cut -d " " -f5 var employees.txt

#awk da formato a las líneas, del input  toma las columnas pedidas y les da formato

  210  awk -F '[ ]' '{print $2 $3 likes to $5}' employees.txt 
  211  awk -F '[ ]' '{print $2\t $3\t likes to $5}' employees.txt 
  212  awk -F '[ ]' '{echo $2 $3 likes to $5}' employees.txt 
  213  awk -F '[ ]' '{print $2 $3 likes to $5}' employees.txt 
  214  awk -F '[ ]' '{echo $2 $3 likes to $5}' employees.txt 
  215  awk -F '[ ]' '{print $2" " $3" likes to "$5}' employees.txt 
  216  awk -F '[ ]' '{printf"$%.2f\n"$4 }' employees.txt 
  217  awk -F '[ ]' '{printf"$%.2f\n" "${4}" }' employees.txt 
  218  awk -F '[ ]' '{printf"$%.2f\n" "$4" }' employees.txt 
  219  awk -F '[ ]' '{printf"%f\n" "$4" }' employees.txt 
  220  awk -F '[ ]' '{print"%f\n" "$4" }' employees.txt 
  221  awk -F '[ ]' '{print "$4" }' employees.txt 
  222  awk -F '[ ]' '{print $4 }' employees.txt 
  223  awk -F '[ ]' '{printf("%f" $4) }' employees.txt 
  224  awk  '{printf("%f\n" $4) }' employees.txt 
  
  234  tput cols
  235  printf "${tput cols}"
  236  printf "(${tput cols})"
  237  var columnas = tput cols
  238  columnas = tput cols
  239  columnas=tput cols
  240  columnas=$(tput cols)
  241  echo columnas
  242  echo $columnas
  243  echo $(tput cols)
  244  printf "$(tput cols)"
  245  clear
  246  printf "%$(tput cols)s" "-"
  247  printf "%30s" "-"
  248  printf "%$(tput cols)s" "-" | tr " " "-"
  249  printf "%.2f" "3"
  250  printf "%.2f" "3000000000"
  251  var=4
  252  printf "%.2f" "${var}"
  253  var=45000000000000
  254  printf "%.2f" "${var}"
  255  printf "$%.2f" "${var}"
  256  man awk
  257  awk '{print $2" "$3" likes to "$5}' employees.txt
  258  awk '{print "$2 $3 likes to $5"}' employees.txt
  259  awk '{print $2" "$3" likes to "$5}' employees.txt
  260  awk '{printf "%.2f" "3000000000"}' employees.txt
  261  awk '{printf "%s" "$2"}' employees.txt
  262  awk '{printf "%s" "${2}"}' employees.txt
  263  awk '{printf "%s" "$(2)"}' employees.txt
  264  awk '{printf "%s", "$(2)"}' employees.txt
  265  awk '{printf "%s", "${2}"}' employees.txt
  266  awk '{printf "%s", ${2}}' employees.txt
  267  awk '{printf  ${2}}' employees.txt
  268  awk '{printf  $2}' employees.txt
  269  cat employees.txt
  270  awk '{printf "%s\n"  $2}' employees.txt
  271  awk '{printf "%s\n",  $2}' employees.txt
  272  awk '{printf  ${2}"\n"}' employees.txt
  273  awk '{printf  ${2}}' employees.txt
  274  awk '{printf  $2}' employees.txt
  275  awk '{printf  $2\n}' employees.txt
  276  awk '{printf  $2"\n"}' employees.txt
  277  awk '{print $2"\n"}' employees.txt
  278  awk '{printf "%s .\n",  $2}' employees.txt
  279  awk '{printf "$%s \n",  $4}' employees.txt
  280  awk '{printf "$%f \n",  $4}' employees.txt
  281  awk '{printf "$%.2f \n",  $4}' employees.txt
  282  awk '{printf "%.2f" "3000000000"}' employees.txt
  283  awk '{printf "%.2f", "3000000000"}' employees.txt
  284  ls
  285  sed "p" commands
  286  sed "2-$p" commands
  287  sed "2,$p" commands
  288  sed -n "2,$p" commands
  289  sed -n '2,$p' commands
  290  sed '2,$p' commands
  291  sed -n '2,$p' commands
  292  sed -1 '2,$p' commands
  293  sed -n '2,$p' commands
  294  sed -i '2,$p' commands
  295  cat commands
  296  sed -i '2,$d' commands
  297  cat commands
  298  sed '2,$d' commands
  299  cat commands
  300  sed '/*/unix/g' demo.txt
  301  sed 's/*/unix/g' demo.txt
  302  sed -i 's/unix/linux/' demo.txt
  310  sed -i -l 1 's/unix/linux/' demo.txt
  311  cat demo.txt
  312  sed -i -l1 's/linux/unix/' demo.txt
  322  awk '{print $2" " $3" likes to "$5}' employees.txt
  323  cat demo.txt
  324  sed -i '1 s/linux/unix/' demo.txt
  325  cat demo.txt
  326  sed -i 's/^linux/unix/' demo.txt
  327  cat demo.txt
  328  sed -i 's/^unix/linux/' demo.txt
  329  cat demo.txt
  330  sed -i 's/^linux/unix/' demo.txt
  331  sed -i 's/[a-zA-Z]*/linux/' demo.txt
  332  cat demo.txt
  333  sed -i 's/[a-zA-Z]*/linux/g' demo.txt
  334  cat demo.txt
  335  sed -i 's/[a-zA-Z]*/linux/g' demo.txt
  336  cat demo.txt
  337  cut -d " " demo.txt | tr "[a-zA-Z]*" "unix"
  338  cat demo.txt | tr "[a-zA-Z]*" "unix"
  
  411  emacs employees.txt
  
  
  414  env > /Desktop/variables.txt
  415  touch /Desktop/env.txt
  416  touch /home/an-b3z/Desktop/env.txt
  417  env > /home/an-b3z/Desktop/env.txt
  418  cat /home/an-b3z/Desktop/env.txt
  419  cut -d "=" -f 1 /home/an-b3z/Desktop/env.txt > /home/an-b3z/Desktop/env2.txt
  
  498  cat /etc/network/interfaces
  499  man interfaces
  500  map ip
  501  man ip
  502  man ip-addres
  503  man ip -addres
  510  grep Nigar employees.txt | cut -d" " -f2,3,5 | sort | tr " " ", " | column -t
  511  grep Nigar employees.txt | cut -d" " -f2,3,5 | echo "$0 $1 likes to $2"
  512  echo "$0 $1 likes to $2"| cut -d" " -f2,3,5 |
  513  echo "$0 $1 likes to $2"| cut -d" " -f2,3,5 employees.txt
  514  echo "$0 $1 likes to $2"| cut -d" " -f2,3,5 employees.txt|echo "$0 $1 likes to $2"
  515  echo "$0 $1 likes to $2"| cut -d" " -f2,3,5 employees.txt|echo "$2 $3 likes to $5"
  516  cut -d" " -f2,3,5 employees.txt|echo "$2 $3 likes to $5"
  
  
