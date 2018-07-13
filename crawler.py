#!/usr/bin/python3
#

import re
from requests import get
from bs4 import BeautifulSoup as bs

r = get('http://trend.caipiao.163.com/dlt/?beginPeriod=07001&endPeriod=18076')
soup = bs(r.text,'html.parser')
data = soup.findAll('tr')
one=data[4].findAll('td')

#构造两个数据集
ball_data = []    #用于存储中奖球的数据
record_data = []  #用于存储未中奖次数的数据


for i in range(1,len(data)-13):#遍历数据，最后13个不是数据
	onedata = data[i].findAll('td')
	oneline = []
	oneline_2  = []
	oneline.append(int(onedata[0].text))   #存储中奖球数一行
	oneline_2.append(int(onedata[0].text)) #存储历史记录
	for j in range(2,len(onedata)):
		if onedata[j].attrs['class'][0]==('ball_red'):
			oneline.append(int(onedata[j].text))
			oneline_2.append(int(0))
			continue
		elif onedata[j].attrs['class'][0]==('ball_brown'):
			oneline.append(int(onedata[j].text))
			oneline_2.append(int(0))
			continue
		elif onedata[j].attrs['class'][0]==('ball_blue'):
			oneline.append(int(onedata[j].text))
			oneline_2.append(int(0))
			continue
		elif onedata[j].text=='':
			continue
		oneline_2.append(int(onedata[j].text))
	ball_data.append(oneline)
	record_data.append(oneline_2)

for k in record_data:
	print(k)
	print(len(k))
