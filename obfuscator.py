import os
import base64
from sys import argv

offsetclay = 10
clay = '__clay_clay' * 100

def obfuscate(content):
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{clay} = ""\n'
    for _ in range(int(len(b64_content) / offsetclay) + 1):
        _str = ''
        for char in b64_content[index:index + offsetclay]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{clay} += "{_str}"\n'
        index += offsetclay
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({clay}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    return code

def main():
    print('###########################')
    print('#                         #')
    print('#    Simple Obfuscator    #')
    print('#         by clay         #')
    print('#                         #')
    print('###########################')

    try:
        path = argv[1]
        if not os.path.exists(path):
            print('[-] file not found')
            exit()

        if not os.path.isfile(path) or not path.endswith('.py'):
            print('[-] invalid file')
            exit()
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            file_content = file.read()

        content = obfuscate(file_content)

        with open(f'{path.split(".")[0]} (obfuscated).py', 'w') as file:
            file.write(content)

        print('[+] script has been obfuscated')
    except:
        print(f'usage: py {argv[0]} <file>')

if __name__ == '__main__':
    main()
