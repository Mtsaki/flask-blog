from blog.database import db

class Image(db.Model):
    __tablename__ = 'image'

    image_id = db.Column(db.Integer, primary_key=True, nullable=True, unique=False)
    file_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image_file = db.Column(db.LargeBinary, nullable=False)
    
    def __init__(self, file_name, description, image_file):
        self.image_id = None
        self.file_name = file_name
        self.description = description
        self.image_file = image_file
        
def load_image(image_id):
    return db.session.query(Image).filter(Image.image_id == image_id).first()
    
def load_image_all():
    image = db.session.query(Image).all()
    if image == None:
        return []
    else:
        return image

def load_image_all_without_binary():
    image = db.session.query(Image.image_id, Image.file_name, Image.description).all()
    if image == None:
        return []
    else:
        return image

def insert(file_name, description, image_file):
    image = Image(file_name, description, image_file)
    db.session.add(image)
    db.session.commit()
    return image.image_id

def update(image_id, file_name, description, image_file):
    image = load_image(image_id)
    image.file_name = file_name
    image.description = description
    image.image_file = image_file
    db.session.commit()

def delete(image_id):
    image = load_image(image_id)
    image.delete()
    db.session.commit()