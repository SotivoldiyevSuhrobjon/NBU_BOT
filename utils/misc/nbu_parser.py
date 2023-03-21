import aiohttp


async def get_currency():
    url = "https://nbu.uz/exchange-rates/json/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()