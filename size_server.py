# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import shutil

hostName = "localhost"
serverPort = 8080


def size_avaliable():
    tup = (total, used, free) = shutil.disk_usage("E:")
    return tuple(map(lambda x: x / (2 ** 30), tup))

def size_avaliable_json():
    total, used, free = size_avaliable()
    data = {
        "total": total,
        "used": used,
        "free": free
    }
    import json
    return json.dumps(data)



class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(
            bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8")
        )
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    # webServer = HTTPServer((hostName, serverPort), MyServer)
    # print("Server started http://%s:%s" % (hostName, serverPort))

    # try:
    #     webServer.serve_forever()
    # except KeyboardInterrupt:
    #     pass

    # webServer.server_close()
    # print("Server stopped.")
    print(size_avaliable())
    print(size_avaliable_json())
