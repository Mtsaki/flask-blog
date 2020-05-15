from blog.database import db

class HashTag(db.Model):
    __tablename__ = 'hash_tag'

    tag_id = db.Column(db.Integer, primary_key=True, nullable=True, unique=False)
    tag = db.Column(db.String, nullable=False)
    
    def __init__(self, tag):
        self.tag_id = None
        self.tag = tag
        
def load_tag(tag_id):
    return db.session.query(HashTag).filter(HashTag.tag_id == tag_id)
    
def load_tag_all():
    tag = db.session.query(HashTag).all()
    if tag == None:
        return []
    else:
        return tag

def insert(tag):
    tag = HashTag(tag)
    db.session.add(tag)
    db.session.commit()
    return tag.tag_id

def update(tag_id, tag):
    tag = load_tag(tag_id)
    tag.tag = tag
    db.session.commit()

def delete(tag_id):
    tag = load_tag(tag_id)
    tag.delete()
    db.session.commit()