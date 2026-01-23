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
    await t1()
    await t2()

asyncio.run(main())

# ye piece of code sirf async ka use kar raha hai , real cuncurrency yha nhi hai. mtla hai ki many task
# manage nahi ho rhe sirf non blocking sleep ka use ho rha hai but us sleep mein koi aur kaam nhi 
# ho raha hai.
