import asyncio

async def test():
    print("X")

async def main():
    print("A")
    await test()    # test() coroutine object banata hai await execute karta hai.
    print("B")

asyncio.run(main())
