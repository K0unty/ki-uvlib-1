# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
# ]
# ///

import requests as rq

def main() -> None:
    print("bootyChocolate")
    ban()
    

def ban() -> None:
    rez = rq.get("https://snips.sh/f/SuUcj6kw21?r=1")
    print(rez.text)
    


if __name__ == "__main__":
    main()
