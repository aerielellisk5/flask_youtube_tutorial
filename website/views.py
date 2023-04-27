from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
@login_required
# for some odd reason this isnt working and I have no idea why....
def home():
    # pass - what does pass do?
    return render_template("home.html")