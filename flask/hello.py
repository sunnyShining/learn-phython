from flask import Flask

app = Flask(__name__)

@app.route('/')
def my_view():
    return 'hello sunny!'

@app.route('/test')
def my_view2():
    html = '''
    <h1>来啊，互相伤害呀</h1>
    <h2>来啊，互相伤害呀</h2>
    <h3>来啊，互相伤害呀</h3>
    <h4>来啊，互相伤害呀</h4>
    '''
    return html