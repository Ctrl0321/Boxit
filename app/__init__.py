from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "1291073129749013740932ABFG"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///boxit.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

admin = Admin(app, name="Admin", template_mode="bootstrap3")

from app.DB import Country, Calculation


class CalculationView(ModelView):
    column_display_pk = True
    column_hide_backrefs = False
    column_list = (
        "id",
        "from_country",
        "to_country",
        "normal_one_kg",
        "normal_additional_per_kg",
        "normal_above_ten_kg",
        "express_one_kg",
        "express_additional_per_kg",
        "express_above_ten_kg",
    )


admin.add_view(ModelView(Country, db.session))
admin.add_view(CalculationView(Calculation, db.session))

from app import routes
