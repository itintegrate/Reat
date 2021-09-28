import asyncio
import re

import aiohttp
import aiomysql
from pyquery import PyQuery

start_url = "https://indemand.com.au" 

async def fetch(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as resp:
      print("url states {}".format(resp.status))
      print(await resp.text())


if __name__ == "__main__":
  loop2 = asyncio.get_event_loop()
  task = []
  task.append(fetch(start_url))
  print(fetch(start_url)) 
  loop2.run_until_complete(asyncio.wait(task)) 