from app import db

class BookModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(70), unique=True)
  description= db.Column(db.String(100))

  __tablename__ = 'Book'

  def __init__(self, title, description):
    self.title = title
    self.description = description
