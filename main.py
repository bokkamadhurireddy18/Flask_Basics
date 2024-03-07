from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def bold():
        return f"<b>{function()}</b>"
    return bold


def make_emphasis(function):
    def emp():
        return f"<em>{function()}</em>"
    return emp

def make_underline(function):
    def und():
        return f"<u>{function()}</u>"
    return und

@app.route("/")
def hello_world():
    return ("<h1 style='text-align:center'>Hello, World!</h1>"
            "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGVmc2JiY2RiMHlvODQ1M3YxdGY2OG1qcGtlZmZpYW53MGRzb2liZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eQZPrashbH9vy/giphy.gif'>")

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "bye!"

if __name__ == "__main__":
    #run the app in debug mode i.e, auto-reloaded
    app.run(debug= True)