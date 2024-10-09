import requests as rq


def bo1() -> None:
    rez = rq.get("https://snips.sh/f/SuUcj6kw21?r=1")
    print(rez.text)
