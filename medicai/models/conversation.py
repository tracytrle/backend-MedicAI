

from medicai.extensions import db
from datetime import datetime

class Conversation(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    conversationId = db.Column(db.Integer, nullable=False)
    sender = db.Column(db.String(50), nullable=True)
    message = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_updated_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"Conversation('{self.userId}', '{self.message}', '{self.response}')"