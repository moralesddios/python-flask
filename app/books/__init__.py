from flask import Blueprint

booksbp = Blueprint('books', __name__)

from . import routes