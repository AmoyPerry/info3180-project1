from . import db
property = "bubble"
class PropertiesT(db.Model):
    
    __tablename__ = property
    
    propID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(150))
    descr = db.Column(db.String(120))
    numRooms = db.Column(db.Integer)
    numBaths = db.Column(db.Integer)
    price = db.Column(db.Float)
    propType = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(80))
    #filename = db.Column(db.String(350))

    def __int__(self, title, descr, numRooms, numBaths, price, propType, location, photo):
        self.title = title
        self.descr = descr
        self.numRooms = numRooms
        self.numBaths = numBaths
        self.price = price
        self.propType = propType
        self.location = location
        self.photo = photo
        #self.filename = filename
    
    def __repr__(self):
        return '<PropertiesT %r>' % (self.title)