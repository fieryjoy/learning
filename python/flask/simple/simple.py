from flask import Flask, url_for, request, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page"


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post of the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request):
            return log_the_user_in()
    else:
        error = 'Invalid username/password'
    return render_template('login.html', error=error)

def log_the_user_in():
    print "The user is logged in"
    return render_template('hello.html')

def valid_login(request):
    print "Validating login"
    return True


if __name__ == "__main__":
    with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login', next='/')
        print url_for('profile', username='John Doe')
    with app.test_request_context('/hello', method='POST'):
        assert request.path == '/hello'
        assert request.method == 'POST'
    app.run()
