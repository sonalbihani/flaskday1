from flask import Flask,render_template,request
app = Flask(__name__)
data = [
        {
            'name':'Gatekeepers',
            'category':'Social',
            'public':True
        },
        {
            'name':'Innkeepers',
            'category':'Informal',
            'public':True
        },
        {
            'name':'Bobblekins',
            'category':'Merriment',
            'public':False
        },
        {
            'name':'Housemasters',
            'category':'Social',
            'public':False
        },
        {
            'name':'Childrens',
            'category':'Informal',
            'public':True
        }
        
    ]
@app.route('/club/clubs',methods = ['GET'])
def display_club():
    return render_template('clubs.html',data=data)


if __name__ == '__main__':
    app.run(debug = True)
