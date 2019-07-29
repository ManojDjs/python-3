#for random calling of fucntion
import asyncio
import time
import requests
start_time = time.time()
async def say_after(i):
    print(f'im runnig {i}')
    d = requests.get('https://test.jobiak.ai:8443/getKeyWordsBasedOnTitle?jobTitle=/'+str(i))
    await asyncio.sleep(0.01)
    print(f'im done {i}')
    print(d.json())
    return d.json()
async def desc(i):
    print(f'im runnig {i}')
    d = requests.get('https://test.jobiak.ai:8443/getKeyWordsBasedOnTitle?jobTitle=/' + str(i))
    await asyncio.sleep(0.01)
    print(f'im done {i}')
    print(d.json())
    return d.json()
async def main():
        task=[]
        # for i in range(0,5):
        #         task.append(say_after(i))
        # print(task)
        #await asyncio.gather(*task)
        await asyncio.gather(say_after(200))
        await asyncio.gather(desc(2))
        await asyncio.gather(say_after(300))
l=asyncio.get_event_loop()
l.run_until_complete(main())
print("--- %s seconds ---" % (time.time() - start_time))
#print((t2-t1))