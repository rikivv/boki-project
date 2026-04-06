import requests


url = "http://127.0.0.1:8080/v1/chat/completions"

data = {
    "model": "local-model",
    "messages": [
        {"role": "user", "content": "Explain recursion in simple terms"}
    ],
    #"max_tokens": 100,
}

request = requests.post(url, json=data)

request_response = request.json()

print(request_response["choices"][0]["message"]["content"])
print()
print(request_response["timings"])