import asyncio

async def t1():
    print("T1 Start")
    await asyncio.sleep(1)
    print("T1 End")

async def t2():
    print("T2 Start")
    await asyncio.sleep(1)
    print("t2 End")

async def main():
    await asyncio.gather(t1(),t2())

asyncio.run(main())

# ab yaha pahle t1 start hoga aur sleep pr chala jayega phir turant hi t2 start hoga (as another task.)
# Output: T1 start, t2 start, t1 end, t2 end.
# Total time  approx 1 sec not 2 sec.