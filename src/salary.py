from flask import Blueprint, render_template, request, flash, g
import cx_Oracle

salary = Blueprint('salary', __name__)
