from flask import Flask,render_template,request
app = Flask(__name__)


@app.route('/club/new-club')
def new_club():
    data = ['Gatekeepers','Club of middle aged men engaged in gatekeeping activities','Social']
    return render_template('index.html',data=data)


@app.route('/club/clubs',methods = ['POST'])
def display_club():
    ls = ['Gatekeepers','Club of middle aged men engaged in gatekeeping activities','Social']
    if request.method == 'POST':
        result = request.form
        return render_template("clubs.html",result = result)
    # return render_template('clubs.html')


if __name__ == '__main__':
    app.run(debug = True)
