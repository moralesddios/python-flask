from app import ma

class BookSchema(ma.Schema):
  class Meta:
    fields = ('id', 'title', 'description')
