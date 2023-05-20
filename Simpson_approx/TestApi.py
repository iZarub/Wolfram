import requests


def get_integral(f: str, llim: str, rlim: str):
    url = f"https://www.wolframcloud.com/obj/03ded825-704c-46f2-bb2a-5e4f4e7d3b50?f={f}&llim={llim}&rlim={rlim}"
    ans = requests.get(url).json()
    if ans["Success"] == True:
        return True, ans["Result"]
    if ans["Success"] == False:
        return False, ans["Messages"]