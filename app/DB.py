from app import db


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(225), unique=True, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=True)

    def __repr__(self):
        return f"Country('{self.name}', '{self.code}')"


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    from_country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    to_country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    normal_one_kg = db.Column(db.Float, nullable=True)
    normal_additional_per_kg = db.Column(db.Float, nullable=True)
    normal_above_ten_kg = db.Column(db.Float, nullable=True)
    express_one_kg = db.Column(db.Float, nullable=True)
    express_additional_per_kg = db.Column(db.Float, nullable=True)
    express_above_ten_kg = db.Column(db.Float, nullable=True)

    from_country = db.relationship('Country', foreign_keys=[from_country_id])
    to_country = db.relationship('Country', foreign_keys=[to_country_id])

    def __repr__(self):
        return f"Calculation('{self.id}'"
