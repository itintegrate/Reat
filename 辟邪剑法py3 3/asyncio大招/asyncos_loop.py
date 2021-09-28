# -*- coding: utf-8 -*-
# @Author: jinpengwu
# @Date:   2020-03-06 08:44:10
# @Last Modified by:   jinpengwu
# @Last Modified time: 2020-03-10 09:05:25


import asyncio
import time
from functools import partial
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")    
    return url

def callback(url, future):
    print(url)
    print("send email to bobby")    


#可以拿return值2法-1
async def main():
    tasks = []
    for url in range(200):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks.append(asyncio.ensure_future(get_html(url)))# 先把它变成furtur 撞到 tasks里面
    for task in asyncio.as_completed(tasks): #再用 as_complate调出
        result = await task #一定要要用 await去拿
        print(result)

if __name__ == "__main__":
#只能传值，拿不了值  
    start_time = time.time()
    loop2 = asyncio.get_event_loop() #1 先开事件循环
    tasks1 = []
    tasks2 = []
    for url in range(2):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks1.append(get_html(url)) 
    for url in range(2):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        tasks2.append(get_html(url)) 
    #loop2.run_until_complete(asyncio.gather(*tasks1,*tasks2)) # gather来合并
    loop2.run_until_complete(asyncio.wait(tasks1)) 
    print(time.time() - start_time)

# #可以拿return值1法
#     loop2 = asyncio.get_event_loop()
#     tasks = []
#     for url in range(20):
#         url = "http://shop.projectsedu.com/goods/{}/".format(url)
#         tasks.append(asyncio.ensure_future(get_html(url)))
#     loop2.run_until_complete(asyncio.wait(tasks))
#     for each in tasks:
#       print(each.result())  

    # #可以拿return值2法-2
    # loop2 = asyncio.get_event_loop()
    # loop2.run_until_complete(main())