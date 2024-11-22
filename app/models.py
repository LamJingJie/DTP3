from app import db
from datetime import datetime 


# association_table = db.Table('association', 
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
# )

# Target table
class FoodSecurityIndex(db.Model):
    __tablename__ = "fsi"
    id = db.Column(db.Integer, primary_key=True)
    self_sufficiency = db.Column(db.Float)
    security_index = db.Column(db.Float)
    