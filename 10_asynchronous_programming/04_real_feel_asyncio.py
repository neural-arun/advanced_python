import asyncio

async def task():
    print('start')
    await asyncio.sleep(2)  # await hi pause and run karta hai so i have to await before asyncio.sleep()
    print('end')

async def main():
    print("before")
    await task()
    print("after")

asyncio.run(main())