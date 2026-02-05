aws_permissions
-----
## Descripcion
 >  Herramienta en Python (boto3) para **enumerar permisos en una cuenta de AWS** a partir de un usuario IAM  

Lista para cada política asociada:
- Nombre de la política
- ARN
- Permisos (acciones) asociados a la política
    
Esta información permite **auditar permisos**, apoyar revisiones de **mínimo privilegio** y **detectar posibles vectores de escalación de privilegios**.

## Casos de uso (Security)
- Revisión de permisos efectivos de usuarios IAM
- Auditorías internas / cumplimiento (IAM Access Review)
- Identificación de políticas demasiado permisivas (`*`, `iam:*`, `sts:*`, etc.)
- Apoyo a hardening y reducción de privilegios
    
------

## Requisitos
- AWS CLI instalado y configurado  
  https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- Python 3.x
- Boto3
  ```bash
  pip install boto3

## Uso de la herramienta

Configurar credenciales en el perfil por defecto de AWS CLI (o exportar variables de entorno).

Nota: Usa credenciales con permisos de lectura IAM (ej. iam:List*, iam:Get*) para minimizar riesgo.

## Instalación

git clone https://github.com/passwdd/aws.git

cd aws

## Uso

python aws_permissions.py
	
La herramienta solicitará el nombre del usuario IAM con el cual se realizara la validación:
	
Introduce el nombre del usuario de AWS: privesc

En este punto la herramienta analizar los permisos IAM y genera un reporte con los hallazgos mas relevantes

Salida (ejemplo)

Ejemplo de salida esperada:

PolicyName: <NOMBRE>

PolicyArn: <ARN>

Actions: <LISTA_DE_ACCIONES>

![](https://raw.githubusercontent.com/passwdd/aws/main/images/Enum_AWS.png)

Con esta informacion se pueden validar los posibles vectores de escalacion de privilegios

## Buenas prácticas / Aviso

Esta herramienta está pensada para uso autorizado en entornos propios o con permiso explícito.
No se recomienda ejecutarla con credenciales de alto privilegio; use el principio de mínimo privilegio.

---
FeedBack

Pull requests y forks son bienvenidos.
