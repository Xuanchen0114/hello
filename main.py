from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def hello_world() -> str:
    return """<!doctype html>
<html lang=\"en\">
  <head>
    <meta charset=\"UTF-8\" />
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello World</h1>
  </body>
</html>
"""
