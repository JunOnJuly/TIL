import requests

nextUrl = 'alpha'
answer = [
    'hellossafy',
    'dfs',
    'ssafycial',
    'protocol',
    'json',
    'singleton',
    'cookie',
    'redis',
    'mvvm',
    'pandas',
    'bluetooth',
    'fittymon',
    'memoization',
    'ioc',
    'docker',
    'dfs',
    'bloom',
    'a',
    'quick',
    'Kubernetes'
]

for i in range(len(answer)):
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "nickname": "서울6반성지훈",
        "yourAnswer": f"{answer[i]}"
    }
    url = f'http://13.125.222.176/quiz/{nextUrl}'
    r = requests.post(url, headers=headers, json=data).json()
    nextUrl = r['nextUrl']
    print(r)
