from url import URL

def show(body):
    inTag = False
    for ch in body:
        if  ch == "<":
            inTag = True
        elif ch == ">":
            inTag = False
        elif  not inTag:
            print(ch,end="")

def load(url):
    body = url.request()
    show(body)

if __name__ == "__main__":
    import sys
    load(URL(sys.argv[1]))