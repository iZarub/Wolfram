'''
API для получения точных выражений для интегралов от 
быстроосцеллирующих функций.

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

import requests


app = FastAPI()

@app.get("/simpson")
async def get_solution(u: str, response_class=HTMLResponse):
    url = "https://www.wolframcloud.com/obj/33502dc5-72eb-4e7f-a835-b02275748653?u=" + str(u)
    ans = requests.get(url).json()
    if ans["Success"] == True:
        return True, ans["Result"]
    if ans["Success"] == False:
        return False, ans["Messages"]

