from flask import Blueprint, request, render_template,jsonify

from app.u import getmesexp

from aisetup import rate_prg

bp = Blueprint('home',__name__)

@bp.route('/exp',methods=['POST','GET'])
def exp():
    if request.method=='POST':
        res=getmesexp()
        if res:
            return jsonify({'response':res})        

    return render_template('home.html')



@bp.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')
        


@bp.route('/rate',methods=['POST','GET'])
def rate():
    if request.method=='POST':
        data=request.get_json()
        if not data:
            return 'no data'
        result=rate_prg(data)
        return jsonify({'response':result})
        


