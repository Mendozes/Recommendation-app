from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin
# from sqlalchemy.ext.declarative import declarative_base

# class Base(declarative_base()):
#     pass

class User(db.Model, UserMixin):
    __tablename__ = "user"
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    faculty = db.Column(db.String, nullable=False)
    department = db.Column(db.String, nullable=False)
    userType = db.Column(db.String, nullable=False)

    __mapper_args__ = {
        "polymorphic_on": "type",
        "polymorphic_identity": "user",
    }

    def __init__(self, id,password, username, name, faculty, department):
        self.id=id
        self.set_password(password)
        self.username=username
        self.name=name
        self.faculty=faculty
        self.department=department


    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'faculty': self.faculty,
            'department': self.department
            # 'userType': self.userType
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


