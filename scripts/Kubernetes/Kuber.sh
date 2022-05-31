#Kubernetes
#on prem installation
# 1 instalar docker para las aplicaciones
	# en todos los nodos
	apt-get update
	apt-get install -y docker.io
	
	
# 2 Kubeadm, kubectl, kubelet
	#para todos los nodos, incluido el master
	#prerequisito, https
	apt-get update && apt-get install -y apt-transport-https
	#descargar la llave, probablemente debas installar curl antes
	#apt install curl
	curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add-
	# agregar sources a sources list
	cta <<EOF >/etc/apt/sources.list.d/kubernetes.list
	deb http://apt.kubernetes.io/ kubernetes-xenial.main
	EOF
	apt-get update
	#install kubelet
	apt-get install -y kubelet kubeadm kubectl
	
# 3 initialize del master
	# se deben especificar algunos parametros previamente
		#escoger la ed que se va a usar
		
		#plug network plugin
		--pod-network-cdir=192.168.0.0/16
		#configurar la ip estática hay 2 formas
			#esta no perdura
			--apiserver-advertise-address=<ip-address>
		#entonces queda kubeadmin init --pod-network-cdir=192.168.0.0/16 --apiserver-advertise-address=192.168.56.2
			#esta si perdura
			
# 4 configurar la red
# 5 join the node
