'''
API для получения точных выражений для интегралов от 
быстроосцеллирующих функций. Запускается из консоли,
можно ставить на внешний сервер.

Вообще можно не использовать, а делать реквест чисто с облака 
Вольфрама, но для дальнейшего развития и создания собственных
приложений будет необходимо.

Используется CloudDeploy[] в Wolfram Mathematica 13.1.

Вычисления происходят на облаке Вольфрама - есть некоторые ограничения
на скорость вычисления и их количество.

ВАЖНО: не запускать вычисления просто так и по много раз - у меня
не останется места на облаке. Фиксится покупкой подписки.
'''


from fastapi import FastAPI, Path, Form, File, UploadFile
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

from typing import Optional
import requests


app = FastAPI()

@app.get("/integrate")
async def get_integral(f: str, llim: str, rlim: str, response_class=HTMLResponse):
    url = f"https://www.wolframcloud.com/obj/b1ac109a-0322-4245-97d8-5a0eae714f26?f={f}&llim={llim}&rlim={rlim}"
    ans = requests.get(url).json()
    if ans["Success"] == True:
        return True, ans["Result"]
    if ans["Success"] == False:
        return False, ans["Messages"]



'''
В дальнейшем возможно дописать аппроксимацию функции рядом Тейлора и
считать интеграл еще одним способом
'''

@app.get("/series")
async def get_series(f: str, deg : Optional[int] = 4, response_class=HTMLResponse):
    url = "https://www.wolframcloud.com/obj/74f9b69b-610c-4f6c-868e-d413f4414a48?f={f}&deg={deg}"
    ans = requests.get(url).json()
    if ans["Success"] == True:
        return True, ans["Result"]
    if ans["Success"] == False:
        return False, ans["Messages"]