"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import logging
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

DICT_URL = {
    "users": USERS_DATA_URL,
    "posts": POSTS_DATA_URL,
}

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
)
log = logging.getLogger(__name__)


async def get_json_data(resource: str):
    url = DICT_URL.get(resource)
    async with ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data
