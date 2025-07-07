from pathlib import Path

p1 = Path('path to file here') #i.e /test/test.txt given you have a folder named test
print(type(p1))

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('New File')
else:
    print("That file already exists.")