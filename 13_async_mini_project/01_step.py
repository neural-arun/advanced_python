import time

def sync_fetch():
    time.sleep(1)

def sync_main(urls):
    start = time.time()
    results = []

    for url in urls:
        results.append(sync_fetch(url))

    print("Sync time:", time.time() - start)
    return results
