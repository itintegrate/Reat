from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
import concurrent.futures
import time

def get_html(times):
  time.sleep(times)
  print("get page {} successful".format(times))
  return times

urls = [3,2,4]


#with 用法

with ThreadPoolExecutor(3) as executor:
  all_task = [executor.submit(get_html, (url)) for url in urls]
  for future in as_completed(all_task):
    data = future.result()
    print("get data {}".format(data)) 



# 正常的用法

# executor = ThreadPoolExecutor(max_workers=2)
# all_task = [executor.submit(get_html, (url)) for url in urls]

# wait 等全部做完或者第一个做完回到主线程
# wait(all_task, return_when = FIRST_COMPLETED)
# print("main")


#这个是全面的方法
# all_task = [executor.submit(get_html, (url)) for url in urls]
# for future in as_completed(all_task):
#   data = future.result()
#   print("get data {}".format(data)) 

# 这个是快速的方法 
# for data in executor.map(get_html, urls):
#   print("get data {}".format(data))