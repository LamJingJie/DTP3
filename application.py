from app import application, db
from app.models import FoodSecurityIndex

@application.shell_context_processor
def make_shell_context():
	return {'db': db, 'fsi': FoodSecurityIndex}


if __name__ == "__main__":
	application.run(host="0.0.0.0", port=8080, debug=True)
