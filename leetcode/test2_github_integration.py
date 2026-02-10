import requests
#URL config
url =  "https://api.github.com/repos/openai/openai-ruby/pulls"
#making GET request
response = requests.get(url)
#validating respons is success/failue
if response.status_code == 200:
    #converting response to json
    pull_data=response.json()
    #listing pull request with required info - User, Pull request title
    for data in range(len(pull_data)):
        print(f"User: {pull_data[data]["user"]["login"]} , Pull Request Title: {pull_data[data]["title"]}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")