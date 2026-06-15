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

        body = event.get('body')
        if isinstance(body, str):
            body = json.loads(body)
        elif body is None:
            body = event

        table.update_item(
            Key={'id': person_id},
            UpdateExpression='SET #n=:n, experience=:e, certifications=:c, git_repo=:g',
            ExpressionAttributeNames={'#n': 'name'},
            ExpressionAttributeValues={
                ':n': body.get('name', ''),
                ':e': body.get('experience', ''),
                ':c': body.get('certifications', ''),
                ':g': body.get('git_repo', '')
            }
        )

        return {
            'statusCode': 200,
            'headers': cors_headers(),
            'body': json.dumps({'message': 'Person updated successfully'})
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
        'Access-Control-Allow-Methods': 'PUT',
        'Access-Control-Allow-Headers': 'Content-Type,X-Api-Key'
    }
