import os
from bottle import *

@route("/")
def helloworld():
  return ("<h1>Hello World</h1>")

run(host="0.0.0.0", port=os.environ.get("PORT"))
