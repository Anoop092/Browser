from url import URL

def show(body,scheme):
    if scheme.startswith("view-source:"):
        print(body)
        return 
    inTag = False
    for ch in body:
        if  ch == "<":
            inTag = True
        elif ch == ">":
            inTag = False
        elif  not inTag:
            print(ch,end="")

def load(url):
    body,scheme = url.request()
    show(body,scheme)

if __name__ == "__main__":
    import sys
    load(URL(sys.argv[1]))