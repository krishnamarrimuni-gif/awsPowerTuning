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

        response = table.get_item(Key={'id': person_id})
        item = response.get('Item')

        if not item:
            return {
                'statusCode': 404,
                'headers': cors_headers(),
                'body': json.dumps({'message': 'Person not found'})
            }

        return {
            'statusCode': 200,
            'headers': cors_headers(),
            'body': json.dumps(item)
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
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
