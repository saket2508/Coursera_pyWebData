import re
def parse():
    textf = open('actualData.txt','r')
    lines = textf.readlines()
    res = list()
    for line in lines:
        prs = re.findall('[0-9]+',line)
        res.extend(prs)
    res = list(map(int,res))
    print(sum(res))

if __name__== '__main__':
    parse()
