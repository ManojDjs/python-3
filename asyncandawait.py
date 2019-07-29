import asyncio
import time,jsonify,json
import requests
async def lis(x,no):
    ele=[]
    print('i took control ', no)
    for i in range(0,x):
        print(i)
        ele.append(i)
       #time.sleep(0.1)
    await asyncio.sleep(0.0001)
    print('i took rest ',no)
    return(ele)
async def fl():
    d=requests.get('http://localhost:5000/data')
    print(d.json())
    return d.json()
async def main():
    for i in range(0,10):
        t1=time.time()
        print(l.is_running())
        #r=l.create_task(lis(200,6))
        r2=l.create_task((fl()))
        r3=l.create_task((fl()))
        await asyncio.wait([
            r2,r3
        ])
        t2=time.time()
        print((t2-t1)*1000)
# Python 3.7+
l=asyncio.get_event_loop()
print(l.is_running())
l.run_until_complete(main())
print('retuerned result')
print(l.is_running())
ip=['18.237.125.77','34.211.228.200','34.217.118.241',
'34.214.219.21',
'34.214.248.78',
'52.34.218.226',
'54.69.178.45',
'54.185.99.156',
'54.214.95.24',
'54.245.25.127']