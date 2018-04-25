from flask import Flask,render_template,request,url_for,redirect,session
import config
import pymysql
# pymysql.install_as_MySQLdb()#解决出现没有mysqldb模块
from exts import db
from models import User,Text,Pinglun
from datetime import datetime
from zhuangshiqi import login_required
app=Flask(__name__)
app.config.from_object(config)
db.init_app(app)#将db和app绑定，解决循环引用
with app.app_context():#防止出现没有将app绑定在db上面
    db.create_all()
@app.route('/')
def shouye():

    return render_template('shouye.html')
@app.route('/denglu/',methods=['GET','POST'])
def denglu():
    if request.method=='GET':
        return render_template('denglu.html')
    else:
        phone=request.form.get('phone')
        username=request.form.get('username')
        password=request.form.get('password')
        name=request.form.get('name')
        user=User.query.filter(User.username==username,User.password==password).first()
        if user:
            # session['session_id']=user.id
            session['session_name']=user.name
            session.permanent=True#设置session的过期时间
            return redirect(url_for('shouye'))
        else:
            return '手机号码或者密码错误'

@app.route('/zhuce',methods=['GET','POST'])
def zhuce():
    if request.method=='GET':
        return render_template('zhuce.html')
    else:

        phone=request.form.get('phone')
        username=request.form.get('username')
        password=request.form.get('password')
        password1=request.form.get('password1')
        name=request.form.get('name')
        user=User.query.filter(User.phone==phone).first()#执行查询命令
        user1=User.query.filter(User.name==name).first()

        if user:
            return '你注册的手机号码已存在'
        else:
            if user1:
                return '您输入的用户名已存在'
            else:
                if password!=password1:
                    return '您两次输入的密码不一致，请重新输入'
                else:

                    user=User(phone=phone,username=username,password=password,name=name)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('denglu'))
@app.route('/zhuxiao/')
def zhuxiao():
    session.clear()#删除session
    return redirect(url_for('shouye'))
@app.context_processor#钩子函数，返回的一个字典全文都可以用
def my_context_processor():
        user_name=session.get('session_name')
        if user_name != False:
            user=User.query.filter(User.name==user_name).first()
            return {'user':user}
        else:
            return {}
@app.route('/tianjia/',methods=['GET','POST'])

def tianjia():
    if session.get('session_name'):#这个也是判断看用户是否登录，若未登录则不能添加案例，直接跳转到登录页面
        if request.method=='GET':
            return render_template('tianjia.html')
        else:
            title=request.form.get('title')
            content=request.form.get('content')
            user_name=session.get('session_name')
            user=User.query.filter(User.name==user_name).first()
            text=Text(title=title,content=content)#固定格式，还没搞懂意思
            text.author=user
            db.session.add(text)
            db.session.commit()
            return redirect(url_for('anli'))
    else:
        return redirect(url_for('denglu'))
@app.route('/xiangqing/<text_id>',methods=['GET','POST'])
def xiangqing(text_id):
    if request.method=='GET':
        # pinglun={
        #     'pinglun': Pinglun.query.all()
        # }
        text=Text.query.filter(Text.id==text_id).first()
        pinglun={
            'pinglun': text.pinglun1
        }
        return render_template('xiangqing.html',text=text,**pinglun)
    else:
        if session.get('session_name'):
            text=Text.query.filter(Text.id==text_id).first()
            pinglun=request.form.get('pinglun')
            pl=Pinglun(pinglun=pinglun)
            # text1=Text.query.filter(Text.id==text_id).first()
            pl.text=text
            user=User.query.filter(User.name==session.get('session_name')).first()
            pl.user=user

            db.session.add(pl)
            db.session.commit()
            pinglun={
                'pinglun': text.pinglun1
            }
            return render_template('xiangqing.html',**pinglun,text=text)
        else:
            return redirect(url_for('denglu'))
@app.route('/wodeanli/')
def wodeanli():
    user_name=session.get('session_name')
    if user_name:                                                 #此处设计判断是否登录，如果登录，则跳转到wodeanli，如果未登录，则跳转到到denglu页面
        user=User.query.filter(User.name==user_name).first()
        text={
            'text': user.text
        }
        return render_template('wodeanli.html',**text)
    else:
        return redirect(url_for('denglu'))
@app.route('/anli')
def anli():
    text={
        'text': Text.query.all()
    }
    return render_template('anli.html',**text)
@app.route('/jieshao')
def jieshao():
    return render_template('jieshao.html')
@app.route('/taocan')
def taocan():
    return render_template('taocan.html')
@app.route('/jiaruwomen')
def jiaruwomen():
    return render_template('jiaruwomen.html')







if __name__== '__main__':
    app.run()
