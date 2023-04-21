from app import app, db
import os

if __name__ == '__main__':
    if not os.path.exists('boxit.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)

