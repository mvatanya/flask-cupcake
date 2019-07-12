from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """connect to database."""

    db.app = app
    db.init_app(app)

class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    flavor = db.Column(
        db.String(20),
        nullable=False
    )

    size = db.Column(
        db.String(20),
        nullable=False
    )

    rating = db.Column(
        db.Float,
        nullable=False
    )
    image = db.Column(
        db.String(),
        default="https://tinyurl.com/truffle-cupcake"
    )

    def __repr__(self):
        c = self
        return f"<Cupcake: {c.id}, {c.flavor}, {c.size}, {c.rating}>"