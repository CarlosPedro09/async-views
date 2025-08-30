import asyncio
# from time import sleep
# import httpx
from django.http import HttpResponse

# async def http_call_async():
#     for num in range(1, 6):
#         await asyncio.sleep(1)
#         print(num)
#     async with httpx.AsyncClient() as client:
#         r = await client.get('https://httpbin.org')
#         print(r)  


# def http_call_sync():
#     for num in range(1, 6):
#         sleep(1)
#         print(num)
#     r = httpx.get('https://httpbin.org/')  
#     print(r) 


# async def async_view(request):
#     loop = asyncio.get_event_loop()
#     loop.create_task(http_call_async())
#     return HttpResponse('Non-blocking HTTP request')            


# def sync_view(request):
#     http_call_sync()
#     return HttpResponse('Blocking HTTP request')

import asyncio
from django.http import HttpResponse

# Nova view assíncrona com contador de tempo
async def contador_view(request):
    for i in range(1, 8):
        await asyncio.sleep(1)
        print(f"Contador: {i}")  # Apenas para ver no console

    return HttpResponse("Contador assíncrono finalizado!")

