import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PersonDetails')

def lambda_handler(event, context):
    try:
        path_params = event.get('pathParameters') or {}
        person_id = path_params.get('id')

        if not person_id:
            return {
                'statusCode': 400,
                'headers': cors_headers(),
                'body': json.dumps({'message': 'Missing id parameter'})
            }

        table.delete_item(Key={'id': person_id})

        return {
            'statusCode': 200,
            'headers': cors_headers(),
            'body': json.dumps({'message': 'Person deleted successfully'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': cors_headers(),
            'body': json.dumps({'error': str(e)})
        }

def cors_headers():
    return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'DELETE',
        'Access-Control-Allow-Headers': 'Content-Type,X-Api-Key'
    }
