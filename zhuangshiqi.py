from functools import wraps
from flask import session,render_template,redirect,url_for
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('session_id'):
             func(*args,**kwargs)
        else:
             return redirect(url_for('denglu'))
        return wrapper
