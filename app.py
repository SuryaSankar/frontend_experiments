from flask import Flask, request, jsonify
import os
from flask_template_previewer import FlaskTemplatePreviewer

app = Flask(__name__)
FlaskTemplatePreviewer(app)

