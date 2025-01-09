import socket
import ssl
class URL:
    def __init__(self,url):
        self.scheme , url = url.split("://",1)
        assert self.scheme in ["http","https"]
        if self.scheme == "http":
            self.port = 80
        elif self.port == "https":
            self.port = 443
        if "/" not in url:
            url = '/' + url
        self.host , url = url.split("/",1)
        if ":" in self.host:
            self.host , self.port = self.host.split(":",1)
            self.port = int(self.port)
        self.path = '/'+ url
    def request(self):
        '''This function help us to establish the connection between client and server and send the request to server'''
        # creating socket
        soc = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP
        )
        # establishing the connection
        soc.connect((self.host,self.port))
        if self.scheme == "https":
            ctx = ssl.create_default_context()
            soc = ctx.wrap_socket(soc,server_hostname=self.host)
        # creating a request
        request = f"GET {self.path} HTTP/1.0\r\n"
        request += f"Host: {self.host}\r\n"
        request += "\r\n"
        # we need to send request in the binary form so we are using encode
        soc.send(request.encode("utf8"))
        # soc.makefile return file object were it contains every bytes recived from server
        response = soc.makefile('r',encoding="utf8",newline="\r\n")
        statusline = response.readline()
        version, status ,explanation = statusline.split(" ", 2)
        response_header = {}
        while True:
            line = response.readline()
            if line == "\r\n":
                break
            header,value = line.split(":",1)
            response_header[header.lower()] = value.strip()
        assert "transfer-encoding" not in response_header
        assert "content-encoding" not in response_header
        content = response.read()
        soc.close()
        return content

