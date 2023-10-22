from pathlib import Path
import os,re,shutil

p = Path.cwd()

# List = list(os.walk(p/'files'))[0]
# for name in List:  
path = p/'files'
spams = []
regex = re.compile(r'^spam(\d\d\d).txt$')
files = os.listdir(path)
for file in files:
    if (mo := re.search(regex,file)) != None:
        spams.append(int(f'{mo.group(1)}'))
# print(spams)
lenth = len(spams)

new = ['{:03}'.format(i) for i in spams]
old = ['{:03}'.format(i+1) for i in range(lenth)]
index = 0
for num in new:
    
    shutil.move(p/'files'/f'spam{num}.txt',p/'files'/f'spam{old[index]}.txt')
    index+=1
