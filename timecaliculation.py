import requests
import time
import asyncio
start_time = time.time()
async def say_after(i):
    print(f'im runnig {i}')
    d = requests.get('https://test.jobiak.ai:8443/getKeyWordsBasedOnTitle?jobTitle=/' + str(i))
    time.sleep(0.000001)
    print(f'im done {i}')
    print(d.json())
    return d.json()
async def main():
    await say_after(3)
    await say_after(10)
asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))