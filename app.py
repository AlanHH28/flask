from flask import Flask

# No need for `distutils.log.debug` in modern Flask development

app = Flask(__name__)


@app.route('/')
def home():
    return "Alan Hernández Hernández 9 B "  # Consistent indentation for readability


if __name__ == '__main__':
    app.run(debug=True)
