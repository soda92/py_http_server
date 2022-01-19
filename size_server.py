# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer


def size_avaliable():
    import shutil

    tup = (total, used, free) = shutil.disk_usage("E:")
    return tuple(map(lambda x: x / (2 ** 30), tup))


def size_avaliable_json():
    total, used, free = size_avaliable()
    data = {"total": total, "used": used, "free": free}
    import json

    return json.dumps(data)


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/size":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(size_avaliable_json(), "utf-8"))
        else:
            self.send_response(404)


def server_thread(webServer: HTTPServer):
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    hostName = "localhost"
    serverPort = 8080

    webServer = HTTPServer((hostName, serverPort), MyServer)
    import threading

    print("Server started http://%s:%s" % (hostName, serverPort))
    t = threading.Thread(target=server_thread, args=[webServer])
    t.start()
