import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3 + json"}
response = requests.get(url=url, headers=headers)
print(response.status_code)
response_dict = response.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete result: {not response_dict['incomplete_results']}")

repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected message about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']} ")
    print(f"Description: {repo_dict['description']}")
