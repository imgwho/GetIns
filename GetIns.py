# -*- coding: utf-8 -*-
import urllib2
import re

response = urllib2.urlopen('https://www.instagram.com/p/BG-zLnvOSoJ/')
html = response.read()  
#print html


#re.findall(pattern, string[, flags])搜索string，以列表形式返回全部能匹配的子串。
# catch = re.compile(r'"display_url": (.+?\.jpg)')
# urls = re.findall(catch,html)
# for i, url in enumerate(urls):
# print urls

#re.search(pattern, string[, flags])match()函数只检测re是不是在string的
#开始位置匹配，search()会扫描整个string查找匹配，match（）只有在0位置匹
#配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回None。
catch = re.compile(r'"display_url": (.+?\.jpg)')
urls = re.search(catch,html)
temp = urls.group()
end = re.sub(r'"display_url": "',"",temp)
print end

response = urllib2.urlopen(end)  
pic = response.read()  
with open('1.jpg','wb') as f:
    f.write(pic)
