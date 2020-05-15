from blog.database import db

class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True, nullable=True, unique=False)
    category = db.Column(db.String, nullable=False)
    
    def __init__(self, category):
        self.category_id = None
        self.category = category
        
def load_category(category_id):
    return db.session.query(Category).filter(Category.category_id == category_id)
    
def load_category_all():
    category = db.session.query(Category).all()
    if category == None:
        return []
    else:
        return category

def insert(category):
    category = Category(category)
    db.session.add(category)
    db.session.commit()
    return category.category_id

def update(category_id, category):
    category = load_category(category_id)
    category.category = category
    db.session.commit()

def delete(category_id):
    category = load_category(category_id)
    category.delete()
    db.session.commit()