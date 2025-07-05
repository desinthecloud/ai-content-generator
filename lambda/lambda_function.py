import boto3
import json

def lambda_handler(event, context):
    try:
        body = event.get('body')
        if isinstance(body, str):
            body = json.loads(body)
        elif body is None:
            body = {}

        prompt = body.get("prompt", "Write a short blog post about AI.")

        client = boto3.client("bedrock-runtime", region_name="us-east-1")

        # Claude 2.1 prompt structure
        full_prompt = f"\n\nHuman: {prompt}\n\nAssistant:"

        payload = {
            "prompt": full_prompt,
            "max_tokens_to_sample": 300,
            "temperature": 0.7,
            "stop_sequences": ["\n\nHuman:"]
        }

        response = client.invoke_model(
            modelId="anthropic.claude-v2:1",
            body=json.dumps(payload),
            contentType="application/json",
            accept="application/json"
        )

        result = json.loads(response["body"].read())

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'response': result.get('completion')})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

