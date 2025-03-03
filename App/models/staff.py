from App.database import db
from App.models import User

class Staff(User):
    __tablename__ = 'staff'
    # staff has a list of notification objects
    notificationList = db.relationship('Notification', backref=db.backref('staff', lazy='joined'))
    # staff has a list of request objects
    requests = db.relationship('Request', backref=db.backref('staff', lazy='joined'))
    
    __mapper_args__ = {
        "polymorphic_identity": "staff",
    }

    def __init__(self, id, username, password, name, faculty, department):
        self.id = id
        self.username = username
        self.set_password(password)
        self.name = name
        self.faculty = faculty
        self.department = department
        self.userType = "staff"

    def toJSON(self):
        return {
            'staffId': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'department': self.department
        }
    
    def toJSON_with_notifications(self):
        return {
            'staffId': self.id,
            'name': self.name,
            'faculty': self.faculty,
            'department': self.department,
            'notificationList': [notif.toJSON() for notif in self.notificationList]
        }