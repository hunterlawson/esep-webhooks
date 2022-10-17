import requests

def lambda_handler(event, context):
    issue_url = event.get('issue').get('html_url')
    request_url = '[REDACTED]'
    request_text = f'Issue created: {issue_url}'
    request_payload = {
        'text': request_text
    }
    response = requests.post(request_url, data=request_payload)
    return response.text