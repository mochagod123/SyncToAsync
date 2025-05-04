import asyncio
from functools import partial
import requests
from deep_translator import GoogleTranslator

class SyncToAsync():
    def __init__(self):
        pass

    async def run(self, function, *args, **kwargs):
        loop = asyncio.get_event_loop()
        info = await loop.run_in_executor(None, partial(function, *args, **kwargs))
        return info

class AsyncRequests():
    def __init__(self):
        self.async_converter = SyncToAsync()

    async def get(self, url: str, headers: dict = None, params: dict = None, data: dict = None, cookies: dict = None, json: dict = None):
        return await self.async_converter.run(requests.get, url, headers=headers, params=params, data=data, cookies=cookies, json=json)
    
    async def post(self, url: str, headers: dict = None, params: dict = None, data: dict = None, cookies: dict = None, json: dict = None):
        return await self.async_converter.run(requests.post, url, headers=headers, params=params, data=data, cookies=cookies, json=json)
    
    async def put(self, url: str, headers: dict = None, params: dict = None, data: dict = None, cookies: dict = None, json: dict = None):
        return await self.async_converter.run(requests.put, url, headers=headers, params=params, data=data, cookies=cookies, json=json)
    
    async def delete(self, url: str, headers: dict = None, params: dict = None, data: dict = None, cookies: dict = None, json: dict = None):
        return await self.async_converter.run(requests.delete, url, headers=headers, params=params, data=data, cookies=cookies, json=json)
    
class AsyncTranslate():
    def __init__(self):
        self.async_converter = SyncToAsync()

    async def translate(self, text: str, source: str = "auto", target: str = "en"):
        tra = await self.async_converter.run(GoogleTranslator, source=source, target=target)
        return await self.async_converter.run(tra.translate, text)