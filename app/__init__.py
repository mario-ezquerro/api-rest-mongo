"""This is init module."""
import os
from flask import Flask

# Place where app is defined
app = Flask(__name__)

from app import sensorsData
