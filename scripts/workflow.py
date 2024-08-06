import requests
import os

def trigger_workflow():
    repo_owner = 'mrgouveia'
    repo_name = 'python-workflow-dispatch'
    workflow_name = 'dispatch.yml'
    token = os.getenv('GITHUB_TOKEN')  # Set your token here
    inputs = {
        'repo_name': 'repo_name_here',  # Customize input parameters if required
        'owner': 'the_owner_here'
    }

    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{workflow_name}/dispatches'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'ref': 'main',  # Specify the branch
        'inputs': inputs
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 204:
        print(f"Workflow '{workflow_name}' triggered successfully!")
    else:
        print(f"Error triggering workflow: {response.status_code} - {response.text}")

if __name__ == '__main__':
    trigger_workflow()
