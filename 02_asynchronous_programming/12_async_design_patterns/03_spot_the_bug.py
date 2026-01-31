async def dashboard():
    data = []
    for api in apis:
        data.append(await call_api(api))
    return data
