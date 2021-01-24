from flask import request
from flask_restplus import Resource, fields
from .schemas import BookSchema
from .models import BookModel
from app import db, apins, token_required

book_schema = BookSchema()
books_schema = BookSchema(many=True)

book_fields = apins.model('Book', {
  'title': fields.String,
  'description': fields.String,
})

@apins.route('/books')
class Books(Resource):
  @apins.expect(book_fields)
  def post(self):
    '''Book create'''
    title = request.json['title']
    description = request.json['description']
    new_book = BookModel(title, description)
    db.session.add(new_book)
    db.session.commit()
    result = book_schema.dump(new_book)
    return {'success': True, 'data': result}, 201
  
  def get(self):
    '''List all Books'''
    all_books = BookModel.query.all()
    result = books_schema.dump(all_books)
    return {'success': True, 'data': result}


@apins.route('/books/<int:id>')
@apins.doc(security='apikey')
class Book(Resource):
  @token_required
  def get(self, id):
    '''Detail of a Book'''
    book = BookModel.query.get(id)
    result = book_schema.dump(book)
    return {'success': True, 'data': result}

  @apins.expect(book_fields)
  @token_required
  def put(self, id):
    '''Update a Book'''
    title = request.json['title']
    description = request.json['description']
    book = BookModel.query.get(id)
    book.title = title
    book.description = description
    db.session.commit()
    result = book_schema.dump(book)
    return {'success': True, 'data': result}

  @token_required
  def delete(self, id):
    '''Delete a Book'''
    task = BookModel.query.get(id)
    db.session.delete(task)
    db.session.commit()
    result = task_schema.dump(task)
    return {'success': True, 'data': result}
