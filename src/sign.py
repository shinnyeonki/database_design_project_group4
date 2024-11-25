from flask import Blueprint, render_template, request, flash, g
import cx_Oracle

sign = Blueprint('sign', __name__)
