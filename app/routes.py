import os
import json
from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import LoginForm, RegistrationForm,AddNewHillForm, EditHillForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from sqlalchemy import func
from app.models import User, Hill, HillInfo
from urllib.parse import urlsplit
from datetime import datetime, timezone

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    last_hill = Hill.query.filter_by(user_id=current_user.id).order_by(Hill.id.desc()).first()
    username = current_user.username.title()
    return render_template('index.html', title="Home", last_hill=last_hill, username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
        
@app.route('/logout')
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created. Please log in")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@login_required
@app.route('/hills')
def hills():
    hills = Hill.query.filter_by(user_id=current_user.id).all()
    return render_template('hills.html', hills=hills)

@login_required
@app.route('/account')
def account():
    hills = Hill.query.filter_by(user_id=current_user.id).all()
    total_distance = sum(hill.distance for hill in hills)
    total_height = sum(hill.height for hill in hills)
    return render_template('account.html', title="Account", 
                           user=current_user, hills=hills, total_distance=total_distance,
                           total_height=total_height)


@login_required
@app.route('/hills/new', methods=['POST', 'GET'])
def add_new_hill():
    all_hills = HillInfo.query.all()
    hill_id = request.args.get('hill_id')
    hill_data = None
    if hill_id:
        hill_data = HillInfo.query.filter_by(id=hill_id).first()
    form = AddNewHillForm()
    if form.validate_on_submit():
        existing_hill = Hill.query.filter(func.lower(Hill.title) == func.lower(form.title.data), Hill.user_id == current_user.id).first()
        if existing_hill:
            flash("Looks like you've already logged this hill")
            return redirect(url_for('add_new_hill')) 
        hill = Hill(
            title=form.title.data, 
            distance=form.distance.data or 0,
            height=form.height.data or 0,
            time=form.time.data or 0,
            latitude=form.latitude.data or 0,
            longitude=form.longitude.data or 0,
            user_id=current_user.id
            )
        db.session.add(hill)
        db.session.commit()
        flash("Hill added")
        return redirect(url_for('hills'))
    return render_template('new_hill.html', form=form, all_hills=all_hills, hill_data=hill_data)


@app.route('/api/hill_data', methods=['GET'])
def hill_data():
    all_hills = HillInfo.query.all()
    # Serialize the list of hills to JSON
    hills_json = [{
        'title': hill.title,
        'distance': hill.distance,
        'height': hill.height,
        'latitude': hill.latitude,
        'longitude': hill.longitude
    } for hill in all_hills]
    return jsonify(hills_json)

@login_required
@app.route('/edit_hill/<int:hill_id>', methods=['GET', 'POST'])
def edit_hill(hill_id):
    hill = Hill.query.get_or_404(hill_id)
    form = EditHillForm(obj=hill)
    if form.validate_on_submit():
        hill.title=form.title.data
        hill.distance=form.distance.data
        db.session.commit()
        flash('Hill updated successfully')
        return redirect(url_for('hills'))
    return render_template('edit_hill.html', form=form)

@login_required
@app.route('/delete_hill/<int:hill_id>', methods=['GET', 'POST'])
def delete_hill(hill_id):
    hill = Hill.query.get_or_404(hill_id)
    try:
        db.session.delete(hill)
        db.session.commit()
        flash('Hill deleted succesfully', 'success')
        return redirect(url_for('hills'))
    except Exception as e:
        db.session.rollback()
        flash('Error deleting hill', 'error')
        return redirect(url_for('hills'))
    

@login_required
@app.route('/all_hills')
def all_hills():
    hills = HillInfo.query.all()
    return render_template('all_hills.html', hills=hills)