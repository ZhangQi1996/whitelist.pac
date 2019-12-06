#!/bash/bin/python
import json
import re
import os

def read_json(file_name='whitelist.pac'):

    with open(file=file_name, mode='r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace("\n", "")
    ret = re.compile("white_domains.*};").search(text).group().strip().lstrip("white_domains = ")\
        .rstrip(';').replace(",}", '}')
    return json.loads(ret)

def get_data(json_data: dict):
    domains = []
    for k in json_data.keys():
        for kk in json_data[k].keys():
            domains.append(kk)
    return domains

def yield_user_rule_file(domains: list, dir_path='.'):
    dir_path = dir_path.strip().rstrip(os.sep).rstrip('/') + os.sep + 'user-rule.txt'
    with open(file=dir_path, mode='w', encoding='utf-8') as f:
        f.write('''! Put user rules line by line in this file.
! See https://adblockplus.org/en/filter-cheatsheet\n
''')
        for d in domains:
            if d.strip() == '':
                continue
            f.write('@@*.%s.*\n' % d)




if __name__ == '__main__':
    json_ = read_json()
    domains = get_data(json_)
    yield_user_rule_file(domains)