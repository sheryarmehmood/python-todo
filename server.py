from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from db import get_tasks
from db import add_task
from db import toggle_task
from db import update_task
from db import delete_task
from db import setup_database

import json


class TodoHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):

        self.send_response(status)
        self.send_header(
            "Content-type",
            "application/json"
        )
        self.end_headers()

        self.wfile.write(
            json.dumps(data).encode()
        )

    def read_json(self):

        content_length = int(
            self.headers["Content-Length"]
        )

        body = self.rfile.read(
            content_length
        )

        return json.loads(
            body.decode()
        )

    def do_GET(self):

        if self.path == "/":

            with open("index.html", "rb") as file:

                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                self.wfile.write(file.read())

        elif self.path == "/style.css":

            with open("style.css", "rb") as file:

                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.end_headers()

                self.wfile.write(file.read())

        elif self.path == "/script.js":

            with open("script.js", "rb") as file:

                self.send_response(200)
                self.send_header("Content-type", "text/javascript")
                self.end_headers()

                self.wfile.write(file.read())

        elif self.path == "/tasks":

            tasks = get_tasks()

            self.send_json(tasks)

        else:

            self.send_response(404)
            self.end_headers()

    def do_POST(self):

        if self.path == "/add-task":

            data = self.read_json()

            add_task(
                data["title"]
            )

            self.send_json({"success": True})

        elif self.path == "/toggle-task":

            data = self.read_json()

            toggle_task(
                data["id"]
            )

            self.send_json({"success": True})

        elif self.path == "/update-task":

            data = self.read_json()

            update_task(
                data["id"],
                data["title"]
            )

            self.send_json({"success": True})

        elif self.path == "/delete-task":

            data = self.read_json()

            delete_task(
                data["id"]
            )

            self.send_json({"success": True})

        else:

            self.send_response(404)
            self.end_headers()


setup_database()

server = HTTPServer(
    ("localhost", 8000),
    TodoHandler
)

print("Server Running...")
print("http://localhost:8000")

server.serve_forever()
