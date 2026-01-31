import asyncio

async def get_profile():
    pass

async def get_results():
    pass

async def get_payments():
    pass

async def main():
    tasks = [
        get_profile(),
        get_results(),
        get_payments()
    ]
    profile, result, payments = await asyncio.gather(*tasks)

asyncio.run(main())
