import urllib.request
import json
ID= "vcbxDLrbaQqfrpIpBSua"
PW = "BXnZKHurrx"
def sendReq(url):
    try:
        req = urllib.request.Request(url)
        req.add_header("X-Naver-Client-Id",ID)
        req.add_header("X-Naver-Client-Secret",PW)
        res = urllib.request.urlopen(req)
        rescode = res.getcode()
    except:
        exception(404)
    if(rescode==200):
        res_content = json.loads(res.read().decode('utf-8'))['items']
        return res_content
    else:
        return rescode

def exception(rescode):
    if rescode==500:
        raise Exception('API 서버에서 뭔가 문제가 발생했습니다.')
    if rescode==404:
        raise Exception('요청 URL이 잘못되었습니다.')
    if rescode==429:
        raise Exception('검색 한도를 초과하였습니다. 몇시간 대기하였다가 다시 시도해주세요.')

    
def blog(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/blog?query={search_string}&display={display}&start={start}&sort=sim"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def news(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/news?query={search_string}&display={display}&start={start}&sort=sim"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def book(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/book?query={search_string}&display={display}&start={start}&sort=sim"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def encyc(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/encyc?query={search_string}&display={display}&start={start}"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def movie(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/movie?query={search_string}&display={display}&start={start}"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def cafe(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/cafearticle?query={search_string}&display={display}&start={start}&sort=sim"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def kin(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/kin?query={search_string}&display={display}&start={start}&sort=sim"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def image(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/image?query={search_string}&display={display}&start={start}&sort=sim"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def shop(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/shop?query={search_string}&display={display}&start={start}&sort=sim"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def doc(search_string, display=10, start=1):
    search_string = urllib.parse.quote(search_string)
    url = f"https://openapi.naver.com/v1/search/doc?query={search_string}&display={display}&start={start}"
    res_content = sendReq(url)
    if(type(res_content)==list):
        return res_content
    else:
        exception(res_content)

def find_everything(search_string, display=10, start=1):
    ret = {'blog':blog(search_string,display=display,start=start),
    'news':news(search_string,display=display,start=start),
    'book':book(search_string,display=display,start=start),
    'encyc':encyc(search_string,display=display,start=start),
    'movie':movie(search_string,display=display,start=start),
    'cafe':cafe(search_string,display=display,start=start),
    'kin':kin(search_string,display=display,start=start),
    'image':image(search_string,display=display,start=start),
    'doc':doc(search_string,display=display,start=start)}
    return ret

