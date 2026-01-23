# Step 0️⃣ — Fake Fetch (no internet yet)
import time
import asyncio


def sync_fetch():
    """
    This is sync fetch(takes more time.)
    """
    time.sleep(1)
    return f"data from {url}"

async def async_fetch():
    asyncio.sleep(1)
    return f"date from {url}"