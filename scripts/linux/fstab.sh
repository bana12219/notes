#comprobar que funcione

#!/bin/bash
fstab=/etc/fstab

if [[ $(grep -q "poky-disc" "$fstab") ]]
# forgiving me for being a bit of over-rigorous, 
#you might want to change this matching word, as below, 
#'poky-disc' merely a comment, not exactly a config line, so
then
    echo "#poky-disc" >> /etc/fstab
    echo "/dev/sdb1 /media/poky ext4 defaults 0 2" >> /etc/fstab
else
    echo "Entry in fstab exists."
fi



grep -q 'init-poky' /etc/fstab || 
printf '# init-poky\n/dev/sdb1    /media/poky    ext4    defaults    0    2\n' >> /etc/fstab
