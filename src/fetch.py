"""
Proprietary License

Copyright 2024 Bueezi™
All Rights Reserved.

This software is licensed under the Proprietary License. Unauthorized copying, modification, distribution, or use
of this software is strictly prohibited. For full license details, see the LICENSE file in this repository.
"""

import asyncio, aiohttp, time

time_list = []
current_time = None
last_status = ""

async def Fetch(url, cookie=None, proxy=None):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, cookies={'.ROBLOSECURITY': cookie}, proxy=proxy, timeout=15) as response:
                return await response.json(), await IsError(response.status, url)
        except asyncio.TimeoutError:
            print("Request timed out.")
            return 0, 1
        except (aiohttp.ClientHttpProxyError, aiohttp.ClientConnectionError):
            print("Proxy Error")
            return 0, 1
        except aiohttp.ContentTypeError:
            print("Content Type Error")
            return 0, 1
            

async def IsError(status, API):
    API = 2 if "v2" in API else 1
    if status == 200:
        print(f"{last_status}")
        time_list.append(current_time)
        return 0
    elif status == 429:
        print(f"{last_status}, R on V{str(API)}")
        if API ==2: 
            await asyncio.sleep(1)
    else:
        print(f"{last_status}, U : {status} on V{str(API)}")
    return 1

async def Status():
    global current_time, last_status
    while 1:
        current_time = int(time.time())
        for _ in time_list:
            if _+60 < current_time:
                time_list.remove(_)
        await asyncio.sleep(0.25)
        last_status = f"Checks : {len(time_list)/10}K/m"