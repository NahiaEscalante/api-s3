import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Nombre del bucket
    bucket_name = event['body']['bucket_name']
    
    try:
        # Crear el bucket sin especificar la región (esto funcionará solo en us-east-1)
        s3.create_bucket(Bucket=bucket_name)

        # Deshabilitar restricciones de acceso público
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )
        
    
        return {
            'statusCode': 200,
            'body': f'Bucket {bucket_name} creado exitosamente.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error al crear el bucket: {str(e)}'
        }
