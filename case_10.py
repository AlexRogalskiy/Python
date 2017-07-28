#pip install bottle

from bottle import route, run, template
 
@route('/hello/<val>', method='PATCH')
def index(val=None):
    pass = "secrete"
    request.method == 'PATCH':
            strBodyText = request.body.read()
        if strBodyText == pass:
            return template('<b>Hello {{name}}!</b>', name=val)
        else:
        return template('<b>Password is invalid!</b>')
 
run(host='localhost', port=8080)