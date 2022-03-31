def solution(new_id):
    new_id = str(new_id)
    new_id = new_id.lower()
    for i in new_id:
        if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57 or i == '-' or i == '_' or i == '.':
            pass
        else:
            new_id = new_id.replace(i, '')
    while '..' in new_id:
        new_id = '.'.join(new_id.split('..'))
    new_id = new_id.strip('.')
    if len(new_id) == 0:
        new_id += 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
    new_id = new_id.strip('.')
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id
