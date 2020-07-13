from flask import Flask, render_template, request, redirect, url_for
from models.user import Db, User
from userform import UserForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/usersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
Db.init_app(app)

@app.route('/')
def index():
# Query all
	users = User.query.all()

# Iterate and print
	for user in users:
		User.toString(user)

	return render_template("index.html", len = len(users), user=users)

# @route /adduser - GET, POST
@app.route('/adduser', methods=['GET', 'POST'])
def addUser():
	form = UserForm()
# If GET
	if request.method == 'GET':
		return render_template('adduser.html', form=form)
# If POST
	else:
		if form.validate_on_submit():
			first_name = request.form['first_name']
			age = request.form['age']
			new_user = User(first_name=first_name, age=age)
			Db.session.add(new_user)
			Db.session.commit()
			return redirect(url_for('index'))
		else:
			return render_template('adduser.html', form=form)

        # @route /adduser/<first_name>/<age>
@app.route('/adduser/<first_name>/<age>')
def addUserFromUrl(first_name, age):
    Db.session.add(User(first_name=first_name, age=age))
    Db.session.commit()
    return redirect(url_for('index'))

# Read route for an individual user
@app.route('/viewuser/<first_name>')
def viewUserFromUrl(first_name):
	# Query all
	users = User.query.filter_by(first_name=first_name).all()

	# Iterate and print
	for user in users:
		User.toString(user)

	return render_template("index.html", len = len(users), user=users)

# Route to delete a user by id
@app.route('/deleteuser', methods=['GET', 'POST'])
def deleteUser():
	form = UserForm()
# If GET
	if request.method == 'GET':
		return render_template('deleteuser.html', form=form)
# If POST
	else:
		if form.validate_on_submit():
			user_id = request.form['user_id']
			deleted_user = User.query.filter_by(user_id=user_id).first()
			Db.session.delete(deleted_user)
			Db.session.commit()
			return redirect(url_for('index'))
		else:
			return render_template('deleteuser.html', form=form)

# Route to update a user's name or age
@app.route('/updateuser', methods=['GET', 'POST'])
def updateUser():
	form = UserForm()
# If GET
	if request.method == 'GET':
		return render_template('updateuser.html', form=form)
# If POST
	else:
		if form.validate_on_submit():
			first_name_old = request.form['first_name']
			age_old = request.form['age']
			first_name_new = request.form['first_name_new']
			age_new = request.form['age_new']
			old_user = User.query.filter_by(first_name=first_name_old).first()
			new_user = User(first_name=first_name_new, age=age_new)
			Db.session.delete(old_user)
			Db.session.add(new_user)
			Db.session.commit()
			return redirect(url_for('index'))
		else:
			return render_template('updateuser.html', form=form)

# Route to generate mock data of any amount
@app.route('/mockuser', methods=['GET', 'POST'])
def mockUser():
	form = UserForm()
# If GET
	if request.method == 'GET':
		return render_template('mockuser.html', form=form)
# If POST
	else:
		if form.validate_on_submit():
			mock_num = request.form['mock_num']

			# Iterate and print
			for i in range(0,int(mock_num)):
				mockUser = User(first_name="test",age=i+1)
				Db.session.add(mockUser)
				Db.session.commit()

			return redirect(url_for('index'))
		else:
			return render_template('mockuser.html', form=form)