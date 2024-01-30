from flask import *
from datetime import datetime
from ELO import *
from time import sleep
from random import randrange, choice
import bcrypt, json, secrets, traceback
from flask_cors import CORS

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
CORS(app)
players = []

@app.route('/tos')
def tos():
    try:
        if 'login_id' in request.cookies:
            return render_template('tos.html', base="2")
        else:
            return render_template('tos.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/delete/<path:name>')
def perm(name):
    with open("sessions.json", "r") as s:
        n = json.load(s)
        for session in n:
            if request.cookies.get('login_id') == session['token']:
                with open("users.json", "r+") as f:
                    data = json.load(f)
                    for account in data:
                        if session['username'] == account['username']:
                            data.remove(account)
                        else:
                            return "stop impersonating you bozo"
                    f.seek(0)
                    f.truncate(0)
                    json.dump(data, f, indent=4)
                    return redirect("https://morsecode.fun")
            else:
                return "stop impersonating you bozo"

@app.route('/delete')
def delete():
    with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'] == account['username']:
                                return "Are you sure you'd like to delete your account PERMANENTLY? If this was a mistake, leave immediately. If intentional, proceed to type 'morsecode.fun/delete/" + account['username'] + "'."

@app.route('/cpanel/reports')
def reports():
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'] == account['username']:
                                if account['badge'] == "admin" or account[
                                        'badge'] == "owner" or account[
                                            'badge'] == "god":
                                    with open('./static/misc/reports.txt', 'r') as g:
                                        return render_template('reports.html', base="2", reports=" // ".join(g.read().split('\n')))
                                else:
                                    return "ayo whos tryna ban people without perms huh? go git commit die you sussy baka"
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/')
def index():
    try:
        if 'login_id' in request.cookies:
            return render_template('index.html', base="2")
        else:
            return render_template('index.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/cpanel/ban')
def cpanelban():
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'] == account['username']:
                                if account['badge'] == "admin" or account[
                                        'badge'] == "owner" or account[
                                            'badge'] == "god":
                                    return render_template('ban.html', base="2")
                                else:
                                    return "ayo whos tryna ban people without perms huh? go git commit die you sussy baka"
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
    

@app.route('/learn')
def learn():
    try:
        return render_template('learn.html')
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/learn/1')
def learn1():
    try:
        return render_template('learn/1.html')
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/cpanel')
def cpanel():
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'] == account['username']:
                                if account['badge'] == "admin" or account[
                                        'badge'] == "owner" or account[
                                            'badge'] == "god":
                                    return render_template('cpanel.html', base="2")
                                else:
                                    return "ayo whos tryna ban people without perms huh? go git commit die you sussy baka"
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/home')
def home():
    try:
        if 'login_id' in request.cookies:
            return render_template('home.html', base="2")
        else:
            return render_template('home.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/vs')
def versus():
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'] == account['username']:
                                return render_template('race.html',
                                                       base="2",
                                                       elo=account['elo'])
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


words = u"a · about · all · and · are · as · at · back · be · because · been · but · can · cant · come · could · did · didnt · do · dont · for · from · get · go · going · good · got · had · have · he · her · here · hes · hey · him · his · how · I · if · Ill · Im · in · is · it · its · just · know · like · look · me · mean · my · no · not · now · of · oh · OK · okay · on · one · or · out · really · right · say · see · she · so · some · something · tell · that · thats · the · then · there · they · think · this · time · to · up · want · was · we · well · were · what · when · who · why · will · with · would · yeah · yes · you · your · youre"


@app.route('/matches/<id>')
def matches(id):
    try:
        with open("./static/misc/matches.json", "r") as s:
            for match in json.load(s):
                if match["id"] == int(id):
                    return render_template('match.html',
                                           base="2",
                                           elo=match['p1-elo'],
                                           p1=match['p1'],
                                           elo2=match['p2-elo'],
                                           p2=match['p2']
                                          )
                else:
                    return render_template('/errors/match.html')
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/queue', methods=["POST"])
def queue():
    try:
        return Response(str(len(players)), content_type="text/plain", status=200)
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))



@app.route('/ranked', methods=['POST'])
def ranked():
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'] == account['username']:
                                me = [account['username'], int(account['elo'])]
                                if me not in players:
                                    players.append(me)
                                success = False
                                print(players)
                                rg = 10
                                rival = None
                                while not success:
                                    rg += 2
                                    try:
                                        for player in players:
                                            if player != me and abs(
                                                    player[1] -
                                                    me[1]) <= rg:
                                                rival = player
                                                success = True
                                        sleep(0.2)
                                    except:
                                        pass
                                with open("./static/misc/matches.json",
                                          "r+") as s:
                                    matches = json.load(s)
                                    target = []
                                    for i in range(15):
                                        target.append(
                                            choice(words.split(u" · ")))
                                    matches.insert(
                                        0, {
                                            "id": matches[0]["id"] + 1,
                                            "finished": False,
                                            "winner": None,
                                            "p1": me[0],
                                            "p2": rival[0],
                                            "p1-elo": me[1],
                                            "p2-elo": rival[1],
                                            "target": " ".join(target),
                                            "replay": "0,0",
                                            "current-progress": [0, 0],
                                            "spectators": []
                                        })
                                    s.seek(0)
                                    s.truncate(0)
                                    json.dump(matches, s, indent=2)
                                    return "id" + str(matches[0]["id"])
    except:
        traceback.print_exc()
        return "500"


@app.route('/chat-v2')
def chat_v2():
    try:
        if 'login_id' in request.cookies:
            return render_template('chat-v2.html', base="2")
        else:
            return render_template('chat-v2.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/rules')
def rules():
    try:
        if 'login_id' in request.cookies:
            return render_template('rules.html', base="2")
        else:
            return render_template('rules.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/keyer')
def keyer():
    try:
        if 'login_id' in request.cookies:
            return render_template('keyer.html', base="2")
        else:
            return render_template('keyer.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/ranks')
def ranks():
    try:
        if 'login_id' in request.cookies:
            return render_template('ranks.html', base="2")
        else:
            return render_template('ranks.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/login')
def login():
    try:
        if 'login_id' in request.cookies:
            return render_template('login.html', base="2")
        else:
            return render_template('login.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/register', methods=['POST', 'GET'])
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            confirm_password = request.form['repeat']
            if username.lower() == "reserved":
                if 'login_id' in request.cookies:
                    return render_template('errors/invalid.html', base="2")
                else:
                    return render_template('errors/invalid.html', base="")
            else:
                if password == confirm_password:
                    with open("users.json", "r+") as f:
    
                        for account in json.load(f):
                            if account['username'].lower() == username.lower():
                                if 'login_id' in request.cookies:
                                    return render_template('errors/taken.html',
                                                           base="2")
                                else:
                                    return render_template('errors/taken.html',
                                                           base="")
    
                        f.seek(0)
    
                        data = json.loads(
                            "[{\"username\": \"\", \"password\": \"\", \"badge\": null, \"bio\": \"\", \"pfp\": \"https://st.depositphotos.com/1052233/2885/v/600/depositphotos_28850541-stock-illustration-male-default-profile-picture.jpg\", \"blocked\": [], \"elo\": 1000}, "
                            + f.read()[1:])
                        data[0]['username'] = username
                        data[0]['password'] = bcrypt.hashpw(
                            password.encode('utf-8'),
                            bcrypt.gensalt()).decode('utf-8')
                        f.seek(0)
                        f.truncate(0)
                        json.dump(data, f, indent=2)
    
                else:
                    return render_template('errors/pass.html')
            if 'login_id' in request.cookies:
                return render_template(
                    'register.html',
                    success="Successfully created your account!",
                    base="2")
            else:
                return render_template(
                    'register.html',
                    success="Successfully created your account!",
                    base="")
        else:
            if 'login_id' in request.cookies:
                return render_template('register.html', success="", base="2")
            else:
                return render_template('register.html', success="", base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/words', methods=['POST', 'GET'])
def words_():
    with open('./static/misc/words.txt') as f:
        return Response(f.read(), mimetype='text/plain')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    try:
        if request.method == 'POST':
            with open("sessions.json", "r+") as f:
                data = json.load(f)
                for token in data:
                    if token['token'] == request.cookies.get('login_id'):
                        data.pop(data.index(token))
                        f.seek(0)
                        f.truncate(0)
                        json.dump(data, f, indent=2)
                        if 'login_id' in request.cookies:
                            resp = make_response(
                                render_template('success-signout.html', base="2"))
                        else:
                            resp = make_response(
                                render_template('success-signout.html', base=""))
                        resp.set_cookie('login_id', '', expires=0)
                        return resp
        else:
            with open("sessions.json", "r") as s:
                n = json.load(s)
                for session in n:
                    if request.cookies.get('login_id') == session['token']:
                        name = session["username"]
            if 'login_id' in request.cookies:
                return render_template('logout.html', base="2", name=name)
            else:
                return render_template('logout.html', base="", name=name)
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/chat')
def chat():
    try:
        with open("./static/misc/channels/general.txt", "a") as f:
            with open("sessions.json", "r") as s:
                n = json.load(s)
                for session in n:
                    if request.cookies.get('login_id') == session['token']:
                        name = session["username"]
            f.write("\\n" + "[SERVER] " + name.upper() +
                    " JOINED THE CHANNEL.")
            if 'login_id' in request.cookies:
                return render_template('chat.html', base="2")
            else:
                return render_template('chat.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/credits')
def credits():
    if 'login_id' in request.cookies:
        return render_template('credits.html', base="2")
    else:
        return render_template('credits.html', base="")


@app.route('/cookies')
def cookies():
    try:
        if 'login_id' in request.cookies:
            return render_template('cookies.html', base="2")
        else:
            return render_template('cookies.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/me')
def me():
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    name = session["username"]
    
        return redirect("/@" + name)
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/@<username>')
def profile(username):
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
            for user in data:
                if user['username'].upper() == username.upper():
                    badge = user['badge']
                    if badge == None:
                        badge = "none"
                    bio = user['bio']
                    pfp = user['pfp']
                    elo = user['elo']
                    rank = "unknown"
                    if int(elo) >= 2750:
                        rank = "ss"
                    elif int(elo) >= 2500:
                        rank = "s"
                    elif int(elo) >= 2300:
                        rank = "a+"
                    elif int(elo) >= 2100:
                        rank = "a"
                    elif int(elo) >= 2000:
                        rank = "a-"
                    elif int(elo) >= 1800:
                        rank = "b+"
                    elif int(elo) >= 1600:
                        rank = "b"
                    elif int(elo) >= 1500:
                        rank = "b-"
                    elif int(elo) >= 1250:
                        rank = "c+"
                    elif int(elo) >= 1000:
                        rank = "c"
                    elif int(elo) >= 900:
                        rank = "c-"
                    else:
                        rank = "d"
        if badge == "admin" or badge == "god":
            if 'login_id' in request.cookies:
                return render_template('admin.html',
                                       name=username.upper(),
                                       badge=badge,
                                       bio=bio,
                                       pfp=pfp,
                                       rank=rank,
                                       elo=elo,
                                       base="2")
            else:
                return render_template('admin.html',
                                       name=username.upper(),
                                       badge=badge,
                                       bio=bio,
                                       pfp=pfp,
                                       rank=rank,
                                       elo=elo,
                                       base="")
        elif badge == "owner":
            if 'login_id' in request.cookies:
                return render_template('owner.html',
                                       name=username.upper(),
                                       badge=badge,
                                       bio=bio,
                                       pfp=pfp,
                                       rank=rank,
                                       elo=elo,
                                       base="2")
            else:
                return render_template('owner.html',
                                       name=username.upper(),
                                       badge=badge,
                                       bio=bio,
                                       pfp=pfp,
                                       rank=rank,
                                       elo=elo,
                                       base="")
        else:
            if 'login_id' in request.cookies:
                return render_template('profile.html',
                                       name=username.upper(),
                                       badge=badge,
                                       bio=bio,
                                       pfp=pfp,
                                       rank=rank,
                                       elo=elo,
                                       base="2")
            else:
                return render_template('profile.html',
                                       name=username.upper(),
                                       badge=badge,
                                       bio=bio,
                                       pfp=pfp,
                                       rank=rank,
                                       elo=elo,
                                       base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/action/<username>')
def action(username):
    if 'login_id' in request.cookies:
        return render_template('act.html', name=username, base="")
    else:
        return render_template('act.html', name=username, base="")


@app.route('/act/<username>')
def act(username):
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    name = session["username"]
    
        with open("users.json", "r+") as f:
            data = json.load(f)
            for account in data:
                if account['username'] == name:
                    account['blocked'].append(username)
                    f.seek(0)
                    f.truncate(0)
                    json.dump(json.loads(json.dumps(data)), f, indent=2)
                    return "Successfully blocked " + username + "."
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/report/<username>')
def report(username):
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    name = session["username"]
    
        with open("users.json", "r+") as f:
            data = json.load(f)
            for account in data:
                if account['username'] == name:
                    account['blocked'].append(username)
                    f.seek(0)
                    f.truncate(0)
                    json.dump(json.loads(json.dumps(data)), f, indent=2)
    
        with open("./static/misc/reports.txt", "a") as f:
            f.write("\nREPORT AT " + str(datetime.now()) + " BY " + name +
                    " AGAINST " + username)
            return "Successfully reported and blocked " + username + "."
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/ban/<username>')
def ban(username):
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'] == account['username']:
                                if account['badge'] == "admin" or account[
                                        'badge'] == "owner" or account[
                                            'badge'] == "god":
                                    if username == "juicy" or username == "ian":
                                        return "shut up dont ban me you sussy baka"
                                    else:
                                        with open("./static/misc/banned.txt",
                                                  "a") as b:
                                            b.write(username + "\n")
                                            return "Successfully banned user."
                                else:
                                    return "ayo whos tryna ban people without perms huh? go git commit die you sussy baka"
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/unban/<username>')
def unban(username):
    try:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    with open("users.json", "r") as u:
                        for account in json.load(u):
                            if session['username'] == account['username']:
                                if account['badge'] == "admin" or account[
                                        'badge'] == "owner":
                                    with open("./static/misc/banned.txt",
                                              "r+") as f:
                                        banned = f.read().splitlines()
                                        if username in banned:
                                            banned.pop(banned.index(username))
                                            f.truncate(0)
                                            f.write("\n".join(banned))
                                            return "Successfully unbanned user."
                                        else:
                                            return "This user is not banned."
                                else:
                                    return "ayo whos tryna unban people without perms huh? go git commit die you sussy baka"
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.before_request
def block_method():
    if 'login_id' in request.cookies:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    name = session["username"]
    else:
        return

    with open("./static/misc/banned.txt", "r") as f:
        if name in f.read().splitlines():
            abort(
                make_response(
                    "You are currently banned from using our services. If you think this is a mistake, then let us know."
                ))


@app.route('/keyer-v2')
def keyer_v2():
    try:
        if 'login_id' in request.cookies:
            return render_template('keyer-v2.html',
                                   lang=request.args.get('lang'),
                                   base="2")
        else:
            return render_template('keyer-v2.html',
                                   lang=request.args.get('lang'),
                                   base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

@app.route('/signin_result', methods=['POST'])
def signin_result():
    try:
        username = request.form['username']
        password = request.form['password']
    
        with open("users.json", "r") as f:
    
            for account in json.load(f):
                try:
                    if account['username'].upper() == username.upper():
                        if bcrypt.checkpw(password.encode('utf-8'),
                                          account['password'].encode('utf-8')):
                            with open("sessions.json", "r+") as f:
                                f.seek(0)
                                data = json.loads(
                                    "[{\"username\": \"\", \"token\": \"\"}, " +
                                    f.read()[1:])
                                data[0]['username'] = username
                                data[0]['token'] = secrets.token_urlsafe(22)
                                f.seek(0)
                                f.truncate(0)
                                json.dump(data, f, indent=2)
                            if 'login_id' in request.cookies:
                                resp = make_response(
                                    render_template('success.html', base="2"))
                            else:
                                resp = make_response(
                                    render_template('success.html', base=""))
                            resp.set_cookie('login_id', data[0]['token'])
                            return resp
                        else:
                            if 'login_id' in request.cookies:
                                return render_template('errors/details.html',
                                                       base="2")
                            else:
                                return render_template('errors/details.html',
                                                       base="")
                    else:
                        pass
                except json.decoder.JSONDecodeError:
                    pass
            if 'login_id' in request.cookies:
                return render_template('errors/details.html', base="2")
            else:
                return render_template('errors/details.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    try:
        with open("sessions.json", "r") as s:
            for session in json.load(s):
                if request.cookies.get('login_id') == session['token']:
                    name = session["username"]
                    with open("users.json", "r") as f:
                        for account in json.load(f):
                            if session['username'].upper() == account['username'].upper():
                                u = account
                                bio = account['bio']
                                pfp = account['pfp']
    
        if request.method == "POST":
            with open("users.json", "r+") as f:
                data = json.load(f)
                if 'oldpw' in request.form:
                    if bcrypt.checkpw(request.form['oldpw'].encode('utf-8'),
                                      u['password'].encode('utf-8')):
                        if request.form['newpw'] == request.form['cnewpw']:
                            data[data.index(u)]['password'] = bcrypt.hashpw(
                                request.form['newpw'].encode('utf-8'),
                                bcrypt.gensalt()).decode('utf-8')
                            f.seek(0)
                            f.truncate(0)
                            json.dump(data, f, indent=2)
                            return render_template(
                                'settings.html',
                                name=name,
                                bio=bio,
                                pfp=pfp,
                                base="2",
                                success="Password was successfully changed!")
                    else:
                        return render_template(
                            'settings.html',
                            name=name,
                            bio=bio,
                            pfp=pfp,
                            base="2",
                            error=
                            "Error: Your Original Password was typed incorrectly!")
                elif 'bio' in request.form:
                    if bcrypt.checkpw(request.form['pw'].encode('utf-8'),
                                      u['password'].encode('utf-8')):
                        with open("sessions.json", "r") as s:
                            for session in json.load(s):
                                if request.cookies.get(
                                        'login_id') == session['token']:
                                    username = session['username']
                        for account in data:
                            if account['username'].lower(
                            ) == request.form['username'].lower() and request.form[
                                    'username'].lower() != username.lower():
                                if 'login_id' in request.cookies:
                                    return render_template(
                                        'settings.html',
                                        name=name,
                                        bio=bio,
                                        pfp=pfp,
                                        base="2",
                                        error=
                                        "Error: Your Username is already taken.")
                                else:
                                    return render_template(
                                        'settings.html',
                                        name=name,
                                        bio=bio,
                                        pfp=pfp,
                                        base="",
                                        error=
                                        "Error: Your Username is already taken.")
                        data[data.index(u)]['bio'] = request.form['bio']
                        u['bio'] = request.form['bio']
                        data[data.index(u)]['pfp'] = request.form['pfp']
                        u['pfp'] = request.form['pfp']
                        data[data.index(u)]['username'] = request.form['username']
                        f.seek(0)
                        f.truncate(0)
                        json.dump(data, f, indent=2)
                        return render_template(
                            'settings.html',
                            name=name,
                            bio=bio,
                            pfp=pfp,
                            base="2",
                            success="Account Details were successfully changed!")
                    else:
                        return render_template(
                            'settings.html',
                            name=name,
                            bio=bio,
                            pfp=pfp,
                            base="2",
                            error="Error: Your Password was typed incorrectly!")
    
        if 'login_id' in request.cookies:
            return render_template('settings.html',
                                   name=name,
                                   bio=bio,
                                   pfp=pfp,
                                   base="2")
        else:
            return render_template('settings.html',
                                   name=name,
                                   bio=bio,
                                   pfp=pfp,
                                   base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

prevmin = None
previd = None


@app.route('/logs@<channel>')
def logs(channel):
    with open("sessions.json", "r") as s:
        n = json.load(s)
        for session in n:
            if request.cookies.get('login_id') == session['token']:
                name = session["username"]

    with open("users.json", "r+") as f:
        data = json.load(f)
        for account in data:
            if account['username'] == name:
                blocked = account['blocked']

    with open(f"./static/misc/channels/{channel}.txt", "r") as f:
        content = f.read().split("\\n")
        for i in content:
            if i[:5] == "*****":
                content.remove(i)
        return Response("\\n".join(content), mimetype='text/plain')

@app.route('/pinned@<channel>')
def pinned(channel):
    with open(f"./static/misc/channels/{channel}.txt", "r") as f:
        content = f.read()
        pins = []
        for i in content.split("\\n"):
            if i[:5] == "*****":
                pins.append(i[5:])
    return Response("\\n".join(pins), mimetype='text/plain')


@app.route('/logs-v2')
def logs_v2():
    with open("sessions.json", "r") as s:
        n = json.load(s)
        for session in n:
            if request.cookies.get('login_id') == session['token']:
                name = session["username"]

    with open("users.json", "r+") as f:
        data = json.load(f)
        for account in data:
            if account['username'] == name:
                blocked = account['blocked']

    with open("./static/misc/channels/general.txt", "r") as f:
        log = f.read().split("\\n")
        msgs = log[-10:]

        messages = []

        for msg in msgs:
            parts = msg.split(" - ")
            messages.append(
                f"<div class='card text-white bg-dark'>\n<div class='card-header'>\n{parts[1]}\n</div>\n<div class='card-body'>\n<h5 class='card-title'>{parts[0]}</h5>\n<p class='card-text'>{parts[2]}</p>\n<button class='btn btn-success' onclick='play(\'{parts[2]}\');'>Play message</button>\n</div>\n</div><br>"
            )

        return Response('{"logs": "' +
                        "\\n".join("\n".join(messages).splitlines()) +
                        '", "blocked": ' + str(json.dumps(blocked)) + '}',
                        mimetype='text/plain')
        # return Response(f.read(), mimetype='text/plain')


@app.route('/getvar@<channel>', methods=['POST'])
def getvar(channel):
    global prevmin
    global previd
    log = request.form['javascript_data']

    with open(f"./static/misc/channels/{channel}.txt", "a") as f:
        with open("sessions.json", "r") as s:
            n = json.load(s)
            for session in n:
                if request.cookies.get('login_id') == session['token']:
                    name = session["username"]
            prevmin = datetime.now().minute
            previd = name.upper()
            if len(str(datetime.now().minute)) == 1:
                f.write("\\n" + name.upper() + " - " +
                        str(datetime.now().hour) + ":0" +
                        str(datetime.now().minute) + " - " + log)
            else:
                f.write("\\n" + name.upper() + " - " +
                        str(datetime.now().hour) + ":" +
                        str(datetime.now().minute) + " - " + log)

    if 'login_id' in request.cookies:
        return render_template('chat.html', base="2")
    else:
        return render_template('chat.html', base="")

@app.route('/translator')
def translator():
    try:
        if 'login_id' in request.cookies:
            return render_template('translator.html', base="2")
        else:
            return render_template('translator.html', base="")
    except Exception as e:
        if 'login_id' in request.cookies:
            return render_template('error.html',
                                   base="2",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))
        else:
            return render_template('error.html',
                                   base="",
                                   exception="\n".join(
                                       traceback.format_tb(e.__traceback__)))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)