from . import db
class PropertiesT(db.Model):
    
    __tablename__ = "bubble"
    
    propID = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150))
    descr = db.Column(db.String(120))
    numRooms = db.Column(db.Integer)
    numBaths = db.Column(db.Integer)
    price = db.Column(db.String(300))
    propType = db.Column(db.String(80))
    location = db.Column(db.String(80))
    photo = db.Column(db.String(380))
    # filename = db.Column(db.String(350))

    def __int__(self, title, descr, numRooms, numBaths, price, propType, location, photo):
        self.title = title
        self.descr = descr
        self.numRooms = numRooms
        self.numBaths = numBaths
        self.price = price
        self.propType = propType
        self.location = location
        self.photo = photo
        # self.filename = filename
    
    def __repr__(self):
        return '<PropertiesT %r>' % (self.title)