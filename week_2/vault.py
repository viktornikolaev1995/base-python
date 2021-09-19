import os, json, tempfile, argparse

storage_path = os.path.join(tempfile.gettempdir(), 'storage690.data')
# print(storage_path)

def write(data):
    with open(storage_path, "w") as f:
        return json.dump(data, f)
def read():
    with open(storage_path, "r") as f:
        return json.load(f)


if os.path.isfile(storage_path):
    parser = argparse.ArgumentParser(description="Key-value vault")
    parser.add_argument('--key', help="Enter some text")
    parser.add_argument('--val', help="Enter some text")

    parsers = parser.parse_args()
    print(parsers)

    if parsers.key and parsers.val:
        d = read()
        if parsers.key in d.keys() and not isinstance(d[parsers.key],list):
            d[parsers.key] = [d[parsers.key]]
            d[parsers.key].append(parsers.val)
        elif parsers.key in d.keys() and len(d[parsers.key]) >= 2:
            d[parsers.key].append(parsers.val)
        elif parsers.key not in d.keys():
            d.update({parsers.key: parsers.val})
            write(d)
    elif parsers.key:
        d = read()
        if parsers.key in d.keys() and isinstance(d[parsers.key], list):
            print(', '.join(d[parsers.key]))
        elif parsers.key in d.keys() and not isinstance(d[parsers.key], list):
            print(''.join(d[parsers.key]))
        elif parsers.key not in d.keys():
            d.update({parsers.key: None})
            write(d)
            print(d.get(parsers.key))

# elif not os.path.isfile(storage_path):
#     if parsers.key and not parsers.val:
#         print(None)
#     else:
#         with open(storage_path, "w") as f:
#             json.dump({}, f)
else:
    try:
        with open(storage_path, "w") as f:
            json.dump({},f)
    except:
        raise Exception(f"{storage_path} is not valid")




with open(storage_path, "r") as f:
    d = json.load(f)
    ke = "5"
    va = 300
    if ke in d.keys():
        d[ke] = [d[ke]]
        d[ke].append(va)
        with open(storage_path,"w") as f:
            json.dump(d,f)
