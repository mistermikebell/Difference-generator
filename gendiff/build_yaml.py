import json
import yaml

with open('../tests/fixtures/file2b.yaml', 'w') as f:
    yaml.dump(json.load(open('../tests/fixtures/file2b.json')), f, allow_unicode=True)


print(gen_diff('../tests/fixtures/file1b.json', '../tests/fixtures/file2b.json', stylish))
