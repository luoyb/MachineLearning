__author__ = 'luoyb'


import re
file = open('/Users/luoyb/Documents/rwy/code/commit-log.txt')
lines = file.readlines()
pat = re.compile('^r')
m_lines = [line for line in lines if pat.match(line)]
pat = re.compile('^re')
m2_lines = [line for line in m_lines if not pat.match(line)]
# w_file = open('/Users/luoyb/Documents/rwy/code/commit-log-m.txt','w')
#w_file.writelines(m2_lines)
dict = {'luoyb':1,'huangzw':2,'zhuanghb':3,'chenyj':4,'hongyb':5,'caizh':6,'zouyh':7,'linyb':8,'zhuozy':9,'yuxh':10,'chenlf':11,'huangrh':12,'chiqz':13,'chensf':14,'zhangjd':15,'lincy':16,'sujc':17,'chenly':18,'fupq':19}
final_lines = []
for line in m2_lines :
    try :
        words = line.strip().split('|')
        final_line = [dict[words[1].strip()],int(words[2].strip().split()[1].split(':')[0]),1]
      #  final_line = dict[words[1].strip()]+'\t'+words[2].strip().split()[1].split(':')[0]+'\t'+'1'+'\r\n'
        #print final_line
        final_lines.append(final_line)
    except :
        print 'error data : %s' %  line


data = []
for pLine in final_lines :
    for line in data :
        if line[0] == pLine[0] and line[1] == pLine[1] :
            line[2] += 1
            break
    else : data.append(pLine)

def find(data,name,hour) :
    for x in data :
        if x[0] == name and x[1] == hour :
            return True
    return False

for x in range(1,20) :
    for y in range(24) :
        if not find(data,x,y) :
            data.append([x,y,0])

amount = [0] * 20
for i in range(1,20) :
    for record in data :
        if record[0]  == i :
            amount[i] += record[2]

print amount

data = sorted(data, cmp=lambda x,y:cmp(x[1],y[1]))

w_file = open('/Users/luoyb/Documents/rwy/code/commit-log-f.txt','w')
for line in data :
     w_file.write(str(line[0])+'\t'+str(line[1])+'\t'+str(line[2])+'\r\n')
w_file.close()

from numpy import *

# file = open('/Users/luoyb/Documents/rwy/code/commit-log-f.txt')
# data = array([line.strip().split('\t') for line in file.readlines()])

data = array(data)
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12,6))
plt.subplot(111)
plt.xlabel('hour')
plt.ylabel('frequency')

# dict = {'luoyb':1,'huangzw':2,'zhuanghb':3,'chenyj':4,'hongyb':5,'caizh':6,'zouyh':7,'linyb':8,'zhuozy':9,'yuxh':10,'chenlf':11,'huangrh':12,'chiqz':13,'chensf':14,'zhangjd':15,'lincy':16,'sujc':17,'chenly':18,'fupq':19}
for i in range(6,7) :
    # *100/amount[i]
    plt.plot(data[nonzero(data[:,0] == i)[0],1],data[nonzero(data[:,0] == i)[0],2],linewidth=2.0)
    # plt.scatter(data[nonzero(data[:,0] == i)[0],1],data[nonzero(data[:,0] == i)[0],2]*100/amount[i],linewidth=1.0)
plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(data[:,1],data[:,2],30,data[:,0]*15)
# plt.show()
