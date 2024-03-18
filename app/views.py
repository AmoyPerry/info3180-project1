"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os

from sqlalchemy import table
from app import app
from flask import flash, render_template, request, redirect, url_for
from app.forms import PropForm
from werkzeug.utils import secure_filename
from app.models import Properties
from app import db

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Amoy Perry")

@app.route("/properties/create", methods=['POST', 'GET'])
def createProp():
    form = PropForm()
    
    if form.validate_on_submit():
        title = form.title.data
        descr = form.descr.data
        numRooms = form.numRooms.data
        numBaths = form.numBaths.data
        price = form.price.data
        propType = form.propType.data
        location = form.location.data
        photo = form.photo.data
        
        filename = secure_filename(photo.filename )
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        propDetails = Properties(title = title, descr = descr, numRooms= numRooms, numBaths = numBaths, 
                                 price = price, propType = propType, location = location, filename=photo)
        
        db.session.add(propDetails) 
        db.session.commit()
        
        flash('Sucessfully added a new property')
        return redirect(url_for('displayProp')) #remember to create
    else:
        return render_template('createProp.html', form = form)


@app.route('/properties') 
def displayProp():
    
    # prp = db.session.execute(db.select(Properties)).scalars()
    prp = Properties.query.all()
    return render_template('allProperties.html', prp=prp)
    

@app.route('/properties/<propertyid>') 
def viewProp(id):
    prp = Properties.query.filter_by(photo=id).first()
    return render_template("indiProp.html", prp=id)


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
