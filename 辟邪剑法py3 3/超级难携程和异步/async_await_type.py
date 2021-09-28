import time
import types

final_result = {}
#不传值的情况下 用 async 和 await 就好了
#如果传值的情况下 要用 type装饰器
@types.coroutine
def t_main(key):
    total = 0
    nums = []
    while True:
        x = yield
        print(key+"销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums

async def middle(key):
  final_result[key] = await t_main(key)
  print(key+"销量统计完成！！.")




def main():
    data_sets = {
        "bobby牌面膜1": [1200, 1500, 3000],
        "bobby牌手机2": [28,55,98,108 ],
        "bobby牌大衣3": [280,560,778,70],
        "bobby牌面膜4": [1200, 1500, 3000],
        "bobby牌手机5": [28,55,98,108 ],
        "bobby牌大衣6": [280,560,778,70],
        "bobby牌面膜7": [1200, 1500, 3000],
        "bobby牌手机8": [28,55,98,108 ],
        "bobby牌大衣9": [280,560,778,70],
        "bobby牌面膜0": [1200, 1500, 3000],
        "bobby牌手机10": [28,55,98,108 ],
        "bobby牌大衣11": [280,560,778,70],
        "bobby牌面膜12": [1200, 1500, 3000],
        "bobby牌手机13": [28,55,98,108 ],
        "bobby牌大衣14": [280,560,778,70],
        "bobby牌面膜15": [1200, 1500, 3000],
        "bobby牌手机16": [28,55,98,108 ],
        "bobby牌大衣17": [280,560,778,70],
        "bobby牌面膜18": [1200, 1500, 3000],
        "bobby牌手机19": [28,55,98,108 ],
        "bobby牌大衣20": [280,560,778,70],
        "bobby牌面膜21": [1200, 1500, 3000],
        "bobby牌手机22": [28,55,98,108 ],
        "bobby牌大衣23": [280,560,778,70],
        "bobby牌面膜24": [1200, 1500, 3000],
        "bobby牌手机25": [28,55,98,108 ],
        "bobby牌大衣26": [280,560,778,70],
        "bobby牌面膜27": [1200, 1500, 3000],
        "bobby牌手机28": [28,55,98,108 ],
        "bobby牌大衣29": [280,560,778,70],
        "bobby牌面膜30": [1200, 1500, 3000],
        "bobby牌手机31": [28,55,98,108 ],
        "bobby牌大衣32": [280,560,778,70],
        "bobby牌面膜33": [1200, 1500, 3000],
        "bobby牌手机34": [28,55,98,108 ],
        "bobby牌大衣35": [280,560,778,70],
        "bobby牌面膜36": [1200, 1500, 3000],
        "bobby牌手机37": [28,55,98,108 ],
        "bobby牌大衣38": [280,560,778,70],
        "bobby牌面膜39": [1200, 1500, 3000],
        "bobby牌手机40": [28,55,98,108 ],
  


    }
    for key, data_set in data_sets.items():
          print("start key:", key)
          m = middle(key)
          try:
            m.send(None)
          except StopIteration:
            pass
          for value in data_set:
              m.send(value)   # 给协程传递每一组的值
          try:
            m.send(None)
          except StopIteration:
            pass
    print("final_result:", final_result)


                




if __name__ == "__main__":
  # tt = middle("testing")
  # try:
  #   tt.send(None)
  # except StopIteration:
  #   pass
  start_time = time.time()  
  main()
  print(time.time()-start_time)
