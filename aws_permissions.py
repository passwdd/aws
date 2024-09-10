import boto3
from collections import defaultdict

# Inicializar el cliente de IAM
iam_client = boto3.client('iam')

# Función para obtener las políticas adjuntas a un usuario
def get_attached_policies(user_name):
    attached_policies = []
    try:
        # Obtener políticas directamente adjuntas al usuario
        user_policies = iam_client.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
        for policy in user_policies:
            attached_policies.append((policy['PolicyArn'], policy['PolicyName']))

        # Obtener políticas asociadas a los grupos del usuario
        groups = iam_client.list_groups_for_user(UserName=user_name)['Groups']
        for group in groups:
            group_policies = iam_client.list_attached_group_policies(GroupName=group['GroupName'])['AttachedPolicies']
            for policy in group_policies:
                attached_policies.append((policy['PolicyArn'], policy['PolicyName']))

    except Exception as e:
        print(f"Error obteniendo políticas: {e}")
    
    return attached_policies

# Función para obtener las acciones permitidas en una política
def get_policy_permissions(policy_arn):
    permissions = set()
    try:
        policy_version = iam_client.get_policy(PolicyArn=policy_arn)['Policy']['DefaultVersionId']
        policy_document = iam_client.get_policy_version(PolicyArn=policy_arn, VersionId=policy_version)['PolicyVersion']['Document']

        # Verificar las acciones permitidas
        for statement in policy_document['Statement']:
            if statement['Effect'] == 'Allow':
                actions = statement.get('Action', [])
                if isinstance(actions, str):
                    actions = [actions]
                permissions.update(actions)
    except Exception as e:
        print(f"Error al obtener permisos para la política {policy_arn}: {e}")

    return permissions

# Función para categorizar los permisos por servicio
def categorize_permissions_by_service(permissions):
    categorized_permissions = defaultdict(set)
    for permission in permissions:
        # Dividir el permiso por ':' para identificar el servicio (el primer elemento antes de ':')
        service = permission.split(':')[0]
        categorized_permissions[service].add(permission)
    
    return categorized_permissions

# Función principal para identificar todos los permisos de un usuario
def get_all_permissions(user_name):
    attached_policies = get_attached_policies(user_name)
    all_permissions = set()

    if not attached_policies:
        print(f"No se encontraron políticas para el usuario {user_name}")
        return

    print(f"\nPermisos para el usuario {user_name}:")

    # Recorrer todas las políticas adjuntas y obtener los permisos
    for policy_arn, policy_name in attached_policies:
        print(f"\nPolítica: {policy_name} (ARN: {policy_arn})")
        permissions = get_policy_permissions(policy_arn)
        all_permissions.update(permissions)

        # Categorizar los permisos por servicio
        categorized_permissions = categorize_permissions_by_service(permissions)

        # Mostrar permisos organizados por servicio
        for service, permissions in categorized_permissions.items():
            print(f"\nPermisos para {service}:\n")
            for permission in permissions:
                print(f"  - {permission}")

# Ejecutar script
if __name__ == "__main__":
    user_name = input("\nIntroduce el nombre del usuario de AWS: ")
    get_all_permissions(user_name)

