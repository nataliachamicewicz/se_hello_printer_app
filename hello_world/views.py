from hello_world import app
from hello_world.formatter import get_formatter
from hello_world.formatter import SUPPORTED, PLAIN
from flask import request
moje_imie = "Natalia"
msg = "Witaj!"
@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, moje_imie,
                         output.lower())

@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
    touch formater.py

PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, imie)
    elif format == JSON:
        result = format_to_json(msg, imie)
    return result


def format_to_json(msg, imie):
    return ('{ "imie":"' + imie + '", "mgs":' +
            msg + '"}')


def plain_text(msg, imie):
    return imie + ' ' + msg


def plain_text_upper_case(msg, imie):
    return plain_text(msg.upper(), imie.upper())


def plain_text_lower_case(msg, imie):
    return plain_text(msg.lower(), imie.lower())
