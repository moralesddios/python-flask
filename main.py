from app import db, create_app
app = create_app()

@app.cli.command()
def createdb():
  db.create_all()

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=False, port=80)