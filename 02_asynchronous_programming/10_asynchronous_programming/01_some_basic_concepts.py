import asyncio
async def work():
    print("Start")
    await asyncio.sleep(1)
    print("Middle")
    await asyncio.sleep(1)
    print("End")

async def main():
    await work()

asyncio.run(main())

# this fuction can be paused and resumed via await and event loop.

#asyncio.run(work())  # this runs this function at the top level of python this creates a event loop.

