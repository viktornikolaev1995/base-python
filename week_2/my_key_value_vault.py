import os, json, tempfile, argparse

parser = argparse.ArgumentParser(description="Key-value vault")
parser.add_argument('--key', help="Enter some text")
parser.add_argument('--val', help="Enter some text")

parsers = parser.parse_args()
# print(parsers)
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# print(storage_path)

def write(data):
    with open(storage_path, "w") as f:
        return json.dump(data, f)
def read():
    with open(storage_path, "r") as f:
        return json.load(f)

if parsers.key and parsers.val and not os.path.isfile(storage_path):
    with open(storage_path, "w") as f:
        json.dump({parsers.key: parsers.val},f)

elif parsers.key and parsers.val and os.path.isfile(storage_path):
    d = read()
    if parsers.key in d.keys() and not isinstance(d[parsers.key],list):
        d[parsers.key] = [d[parsers.key]]
        d[parsers.key].append(parsers.val)
    elif parsers.key in d.keys() and len(d[parsers.key]) >= 2:
        d[parsers.key].append(parsers.val)
    elif parsers.key not in d.keys():
        d.update({parsers.key: parsers.val})
    write(d)

elif parsers.key and os.path.isfile(storage_path):
    d = read()
    if parsers.key in d.keys() and isinstance(d[parsers.key], list):
        print(', '.join(d[parsers.key]))
    elif parsers.key in d.keys() and not isinstance(d[parsers.key], list):
        print(''.join(d[parsers.key]))
    elif parsers.key not in d.keys():
        d.update({parsers.key: None})
        write(d)
        print(d.get(parsers.key))

elif parsers.key and not os.path.isfile(storage_path):
    print(None)


# with open(storage_path, "r") as f:
#     print(json.load(f))




