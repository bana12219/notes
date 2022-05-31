#kube ctl
curl -o kubectl https://amazon-eks ...

chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin
curl -o aws-iam-authenticator https://amazon ...

chmod +x ./aws-iam-authenticator
sudo mv ./aws-iam-authenticator /usr/local/bin

aws-iam-authenticator help

#required eks cluster rol
#Cloudformation EKS stack
#vpc
#subnets
#routetables

aws eks create-cluster 
  --name demo-cluster 
  --region us-east-2 
  --role-arn arn:aws:iam::accountnumber:role/EKSROLENAME 
  --resources-vpc-config subnetId 
  securityGoups

#revisar el status del cluster
aws eks --region us-east-2 describe-cluster --name demo-cluster-eks --query cluster.status
"ACTIVE"
 
 #actualizar la configuración del cluster con el arn del cluster en aws

 aws eks --region us-east-2 update-kubeconfig --name demo-cluster-eks 

get svc
#consultar los nodos workers que estan ligados al master node  
kubectl get nodes

#agregar worker nodes
    #authenticacion
    curl -o aws-auth-cm.yaml https://s3 template authentication cm.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles:
    - rolearn: <ARN of instance role(no instance profile)>
      username: system:node:{{EC2PrivateDNSName}}
      groups:
        - system:bootstrappers
        - system:nodes


aws-auth-cm.yml

kubectl apply -f aws-auth-cm.yml
#configmap/aws-auth unchanged

kubectl get nodes

kubectl create deployment --image=nginx nginx-app

kubectl get deployments

kubectl expose deployment nginx-app --port=80 --name=nginx-http --type loadbalancer

kubectl get services
