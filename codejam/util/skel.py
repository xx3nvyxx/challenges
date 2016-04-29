#!/usr/bin/env python
"""Create Skeleton files for Google Code Jam problems"""

from builtins import input
from datetime import date
from os import makedirs,path,sep
import errno

def main():
    root = input('What is the root of the source tree? [..]: ') or ".."
    year = input('What year was the problem released? [' + str(date.today().year) + ']: ' ) or str(date.today().year)
    ctst = input('What is the name of the contest this problem is a part of? ')
    lttr = input('What index letter is associated with this problem? [A]: ') or "A"
    name = input('What is the name of this problem? ')
    filePath = sep.join([root, year, ctst, lttr])
    machineName = name.replace(' ', '')
    fileName = machineName + '.py'
    confirm = input('Create the file "' + filePath + sep + fileName + '"? [Y/n]: ') or "Y"
    if confirm.upper() != "Y":
        print("Quitting...")
        return
    try:
        makedirs(filePath)
    except OSError as exc:
        if exc.errno == errno.EEXIST and path.isdir(filePath):
            pass
        else:
            raise

    with open(filePath + sep + fileName, 'w') as f:
        f.write('#!/user/bin/env python\n')
        f.write('"""Google Code Jam ' + year + ': Problem ' + lttr + '. ' + name + '"""\n')
        f.write('\n')
        f.write('from builtins import input\n')
        f.write('\n')
        f.write('def main():\n')

        T = input('What variable should hold the number of test cases? [T]: ') or "T"
        Tmin = input('What is the minimum number of test cases? [1]: ') or "1"
        Tmax = input('What is the maximum number of test cases? [100]: ') or "100"
        f.write('    ' + T + ' = int(input())\n')
        f.write('    if ' + T + ' < ' + Tmin + ' or ' + T + ' > ' + Tmax + ':\n')
        f.write('        raise RuntimeError("' + T +' is not within the valid range")\n')
        f.write('    for i in range(' + T + '):\n')

        I = input('What variable(s) should hold the input(s)? [I]: ') or "I"
        if I.find(',') != -1:
            f.write('        ' + I + ' = input().split()\n')
        else:
            f.write('        ' + I + ' = input()\n')
            
        f.write('    r = ' + machineName + '(' + I + ')\n')
        f.write('    print("Case #" + str(i + 1) + ": " + r)\n')
        f.write('\n')

        f.write('def ' + machineName + '(' + I + '):\n')
        f.write('    pass\n')
        f.write('\n')
        
        f.write('if __name__=="__main__":\n')
        f.write('    main()\n')
    return

if __name__=="__main__":
    main()
