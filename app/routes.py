from app import app
from flask import render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
import random
