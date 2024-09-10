#aws_permissions
-----
## Descripcion
 >  Este script realiza la enumeracion de todos los permisos de una cuenta de AWS, lista el nombre de la politica, ARN y los permisos asociados a la politica
    
    Nota: se deben configurar las credenciales del usuario en el perfil por defecto de aws CLI que se desea enumerar
    
------
##Requisitos

aws clic

- https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Libreria de python boto3

pip install boto3 / pip3 install boto3


## Uso de la herramienta
    
	git clone https://github.com/passwdd/aws.git
	cd aws
	python aws_permissions.py
	
	En este punto solicitara el usuario
	
	Introduce el nombre del usuario de AWS: privesc
    

![](https://raw.githubusercontent.com/passwdd/aws/main/images/Enum_AWS.png)

Con esta informacion se pueden validar los posibles vectores de escalacion de privilegios

---
##FeedBack

Pueden hacer un fork para mejorar la herramienta.
