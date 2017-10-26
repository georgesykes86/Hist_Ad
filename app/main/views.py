from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import CountryForm
from .. import db
from ..models import City, Country


@main.route('/', methods=['GET', 'POST'])
def index():
    form = CountryForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))