from . import db

class Properties(db.Model):
    
    __tablename__ = "Properties"
    
    propID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(150))
    descr = db.Column(db.String(120))
    numRooms = db.Column(db.String(120))
    numBaths = db.Column(db.String(120))
    price = db.Column(db.String(120))
    propType = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    filename = db.Column(db.String(350))

    def __int__(self, title, descr, numRooms, numBaths, price, propType, location, photo, filename):
        self.title = title
        self.descr = descr
        self.numRooms = numRooms
        self.numBaths = numBaths
        self.price = price
        self.propType = propType
        self.location = location
        self.photo = photo
        self.filename = filename
    
    def __repr__(self):
        return '<User %r>' % (self.title)