from apiflask import HTTPError
from app.models.users import Users
from app.crud.userscrud import crudinit
from flask import Response, json
from app.services.utils import addmin, dateverify, generateverificationcode, passwordecode,passwordencode,sendemail,valid_email
from flask_httpauth import HTTPBasicAuth
from apiflask import APIFlask
from flaskext.mysql import MySQL
from app.config.conf import env
app = APIFlask(__name__)
app.debug = False
mysql = MySQL() 
app.config['MYSQL_DATABASE_USER'] = env['MYSQL_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = env['MYSQL_ROOT_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = env['MYSQL_DB']
app.config['MYSQL_DATABASE_HOST'] = env['MYSQL_HOST']

mysql.init_app(app)

conn = mysql.connect()
cursor =conn.cursor()
auth = HTTPBasicAuth()
app.config['BASIC_AUTH_FORCE'] = True

crudinit().createtable(cursor, conn)


BAD_REQU = 'bad request'

"""
signup method to create new users with verification email method call

Raises:
    HTTPError: custom HTTP error response with Response et defined the HTTP status with HTTP status code

Returns:
    _type_: custom return with staus param, message and data with Response and json.dumps
"""
@app.post('/singup')
@app.input(Users)
def register(users: Users):
    try:
        data = users
        if(not valid_email(data['email']) or valid_email(data['email']) == False):
            return Response(json.dumps({'status':400, 'message': 'Email format is not correct', 'data': []}), status=400, mimetype='application/json')
        password = passwordencode(str(data['password']))
        time = addmin(1)
        code = generateverificationcode()  
        crudinit().insertusers(cursor, conn, data['email'], password,code, time.timestamp())
        sendemail(data['email'], code)
        return Response(json.dumps({'status':201, 'message': f'created successfully, veuillez verifier votre email', 'data': {'codeVerify': code}}), status=201, mimetype='application/json')
    except Exception:
        return Response(json.dumps({'status':400, 'message': BAD_REQU, 'data': []}), status=400, mimetype='application/json')


"""
basic auth verify method decorator 
"""
@auth.verify_password
def authenticate(username: str, password: str):
    if username and password:
        user= crudinit().getusers(cursor, conn, username)
        if(user):
            verif = passwordecode(password, user['password'])
            if user['status'] == 0 :
                raise HTTPError(404, 'please verify your email')
            if verif :
                return True
        return False
    return False


"""
singin method to connect user

Raises:
    HTTPError: custom HTTP error response with Response et defined the HTTP status with HTTP status code

Returns:
    _type_: custom return with staus param, message and data with Response and json.dumps
"""
@app.route('/singin')
@auth.login_required
def login():
    try:
        return Response(json.dumps({'status':200, 'message': 'successfully connected', 'data': []}), status=200, mimetype='application/json')
    except Exception:
        return Response(json.dumps({'status':400, 'message': BAD_REQU, 'data': []}), status=400, mimetype='application/json')


"""
verify method to verify email code and activate login for current user

Raises:
    HTTPError: custom HTTP error response with Response et defined the HTTP status with HTTP status code

Returns:
    _type_: custom return with staus param, message and data with Response and json.dumps
"""
@app.get('/verify/<email>/<code>')
def verif(email: str, code: int):
    try:
        user = crudinit().getusersbycode(cursor, conn,email, code)
        if user :
            dateverif = dateverify(user['verify_time'])
            if int(code) != int(user['email_verify']):
                return Response(json.dumps({'status':404, 'message': 'your code is incorrect or wrong', 'data': []}), status=404, mimetype='application/json')
            if dateverif == True:
                crudinit().updateuser(cursor, conn, user['email'], code)
                return Response(json.dumps({'status':200, 'message': 'Email successfully activated', 'data': []}), status=200, mimetype='application/json')
            else:
                return Response(json.dumps({'status':404, 'message': 'Email is already activated or your code is wrong', 'data': []}), status=404, mimetype='application/json')
        return Response(json.dumps({'status':400, 'message': 'your code or your email is incorrect or wrong', 'data': []}), status=400, mimetype='application/json')
    except Exception:
        return Response(json.dumps({'status':400, 'message': BAD_REQU, 'data': []}), status=400, mimetype='application/json')




