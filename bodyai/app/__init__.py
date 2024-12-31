from flask import Flask

def createapp():
    app=Flask(__name__)
    app.secret_key='asdfghjkl'
    app=Flask(__name__)
    app.config['debug']=True

    from app.routes import home
    app.register_blueprint(home.bp)

    
    return app