from flask import Flask, render_template


class Blockchain:

    def __init__(self):
        self.transactions = []
        self.chain = []


blockchain = Blockchain()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('./index.html')


if(__name__ == '__main__'):
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5001,
                        type=int, help="port to listen to")
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port, debug=True)
