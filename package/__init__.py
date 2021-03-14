# suppose here write is a method for my image api the api takes in a text and writes it on an image and returns it
  
import aiohttp
from io import BytesIO


class Client:
    def __init__(self):
        self.headers = {"User-Agent": "Base Api"}
        self.session = aiohttp.ClientSession(headers=self.headers)
        self.base_url = "URL TO YOUR API"

# Example method your api will have        
    async def Write(self, text: str):
        url = self.base_url + "Link to the api page EG" + text # EG = www.google.com/hello (hello part =EG)
        async with self.session.get(url) as response:
            image_bytes = await response.read()

            buffer = io.BytesIO(image_bytes)
            buffer.seek(0)

        return buffer

    async def close(self):
        await self.session.close()
