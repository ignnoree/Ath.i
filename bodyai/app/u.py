from flask import request
from aisetup import create_prg



def getmesexp():
    data=request.get_json()
    if not data:
        return 'no data'

    expected_keys = [
        'training_type', 'weight', 'height', 'Waist', 'hip_circ', 'chest_circ', 
        'body_fat', 'shoulder_circ', 'maxlifts', 'cardio_benchmark',
        'goals', 'dailyactivity', 'time', 'training_env','experience','age'
        'more_info'
        
    ]
    userdata={}

    for i in expected_keys:
        userdata[i]=data.get(i,'unknown')

            
    fin='\n'.join([f"{key}: {value}" for key, value in userdata.items()])

  
    prg=create_prg(fin)
    print(prg)
    return prg
