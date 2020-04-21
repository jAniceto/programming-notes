# MessagePack serializer for Python

MessagePack is an efficient binary serialization format. It lets you exchange data among multiple languages like JSON. But it's faster and smaller.

## Install

```
$ pip install msgpack
```

## Usage

```python
import msgpack
import json
import random


def msgpack_example_1():
    example_dict = {i: random.random() for i in range(10000)}

    with open('json_file.json', 'w') as f:
        json.dump(example_dict, f)
    with open('json_file.json') as f:
        back_from_json = json.load(f)

    # Saving and loading
    with open('msgpack_file.msgpack', 'wb') as f:
        # f.write(msgpack.packb(example_dict))
        f.write(msgpack.packb(example_dict, use_single_float=True))
    with open('msgpack_file.msgpack', 'rb') as f:
        back_from_msgpack = msgpack.unpackb(f.read())

    # Data integrity
    print(type(next(iter(back_from_json.keys()))))
    print(type(next(iter(back_from_msgpack.keys()))))


def msgpack_example_2():
    list_of_dicts = [{0: random.random()} for i in range(100)]
    with open('streamed.msgpack', 'wb') as f:
        for d in list_of_dicts:
            f.write(msgpack.packb(d))

    with open('streamed.msgpack', 'rb') as f:
        loaded_list_of_dicts = [item for item in msgpack.Unpacker(f)]

    print(list_of_dicts[3][0], loaded_list_of_dicts[3][0])

if __name__ == '__main__':
    # msgpack_example_1()
    msgpack_example_2()
```
