import json

def writeJSON_File(p: str, d: dict):
    try:
        with open(p, 'w+', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=4)
        return True
    except:
        return False

def readJsonFile(p):
    try:
        return json.loads(readFile(p))
    except:
        return None

def readFile(p):
    try:
        f = open(p, "r", encoding='utf-8')
        data = f.read()
        f.close()
        return data
    except:
        return None