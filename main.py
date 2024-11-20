"""
Proprietary License

Copyright 2024 Bueezi™
All Rights Reserved.

This software is licensed under the Proprietary License. Unauthorized copying, modification, distribution, or use
of this software is strictly prohibited. For full license details, see the LICENSE file in this repository.
"""

import asyncio, random, json
from src.fetch import Fetch, Status
from src.webhook import Send_Webhook
from src.get_cookie import Get_Cookie

config = None
with open("config.json", "r") as f:
    config = json.load(f)
closed_list = None
with open("src/closed.txt", "r") as f:
    closed_list = f.readlines()
    closed_list = [int(_.replace("\n", "")) for _ in closed_list]

def Get_IDs():
    IDs = str([random.randint(32_000_000, 35_230_749) for _ in range(100)])
    return IDs.replace(" ", "")[:-1][1:]

def AddClosed(ID):
    closed_list.append(ID)
    with open("src/closed.txt", "a") as f:
        f.write(str(ID)+ "\n")

async def Thread(n):
    await asyncio.sleep(n/4) # gradually increase the amount of active threads
    proxy = "http://127.0.0.1:"+str(9080+n)
    while 1:
        url = f"https://groups.roblox.com/v2/groups?groupIds={Get_IDs()}"
        data, error = await Fetch(url, Get_Cookie(), proxy)
        if error: continue
        for group in data["data"]:
            if group["owner"] is None:
                if group["id"] not in closed_list:
                    if config["make_closed_list_mode"]: 
                        AddClosed(group["id"])
                    data, error = await Fetch(f"https://groups.roblox.com/v1/groups/{group['id']}", Get_Cookie(), proxy)
                    #data, error = await Fetch(f"https://groups.roblox.com/v1/groups/{group['id']}") # Use this one one's Closed.txt done making
                    if error: continue
                    if "isLocked" not in data and data["publicEntryAllowed"] == True:
                        print(f"True Ownerless found : {str(group['id'])}")
                        message = f"<@{config["discord_userID"]}> https://www.roblox.com/groups/{str(group['id'])}"
                        await Send_Webhook(config["webhook_url"] ,message)
                        with open("src/logs.txt", "a") as f:
                            f.write(f"Found Ownerless group : {str(group["id"])}")
                    elif not config["make_closed_list_mode"]:
                        AddClosed(group["id"])

async def main():
    tasks = [asyncio.create_task(Thread(_)) for _ in range(config["thread_amount"])]
    tasks.append(asyncio.create_task(Status()))
    await asyncio.gather(*tasks)

asyncio.run(main())