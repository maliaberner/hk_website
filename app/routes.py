from flask import Flask

app = Flask(__name__)


#homepage
@app.route('/')
def homepage():
    return "This is the homepage!"

#comments page
@app.route('/photos')
def comments():
    return "This is the photos page!"

#blog page
@app.route('/blogs')
def comments():
    return "This is the photos page!"

#contact page
@app.route('/contact')
def comments():
    return "This is the photos page!"


#errors
@app.errorhandler(401)
def FUN_401(error):
    return render_template("page_401.html"), 401

@app.errorhandler(403)
def FUN_403(error):
    return render_template("page_403.html"), 403

@app.errorhandler(404)
def FUN_404(error):
    return render_template("page_404.html"), 404

@app.errorhandler(405)
def FUN_405(error):
    return render_template("page_405.html"), 405

@app.errorhandler(413)
def FUN_413(error):
    return render_template("page_413.html"), 413



if __name__ == '__main__':
    app.run(Debug=True)
