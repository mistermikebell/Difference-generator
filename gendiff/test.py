import json

file1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

file2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}

nihao = json.load(open('file1.json'))
print(nihao)
