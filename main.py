import asyncio
import aiohttp
import time
import json

url = "https://jsonplaceholder.typicode.com/posts/"

# it is much faster than other methods we used before. it needs averagely 0.5 seconds to terminate the task.
# while multitasking and thread pools needed more than 1 second. it is not much big of a deal but as the data
# size increases this will have a lot of meaning.


async def fetch_post(session, post_id):
    """Asynchronously fetch a post given its ID and return the JSON response."""
    async with session.get(url + str(post_id)) as response:
        return await response.json()


async def fetch_all_posts():
    """Asynchronously fetch all posts and return the data.
    This is a main function to handle the event loop and asynchronous tasks."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_post(session, i) for i in range(1, 78)]
        return await asyncio.gather(*tasks)


start_time = time.time()

# I am running an Event loop
posts_async = asyncio.run(fetch_all_posts())

# Saving the posts to a json file
with open('async_posts.json', 'w') as f:
    json.dump(posts_async, f, indent=4)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.5f} seconds")
