import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PersonDetails')

def lambda_handler(event, context):
    try:
        body = event.get('body')
        if isinstance(body, str):
            body = json.loads(body)
        elif body is None:
            body = event

        table.put_item(Item={
            'id': body['id'],
            'name': body.get('name', ''),
            'experience': body.get('experience', ''),
            'certifications': body.get('certifications', ''),
            'git_repo': body.get('git_repo', '')
        })

        return {
            'statusCode': 201,
            'headers': cors_headers(),
            'body': json.dumps({'message': 'Person created successfully'})
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
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type,X-Api-Key'
    }
