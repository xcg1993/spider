from flask import Flask, render_template, request, jsonify

app=Flask(__name__)
# @app.route('/translate/',methods=['GET','POST'])
# def translate():
#     if request.method=='GET':
#         return render_template('translate.html',**locals())



@app.route('/update/<id>/',methods=['PUT','PATCH'])
def update(id):
    json_data=request.get_json()
    return jsonify('status','ok')


@app.route('/upload_log/',methods=['POST'])
def upload_log():
    print('上传日志')
    print(request.data)
    print(request.form)
    return jsonify({'status':'ok'})
if __name__ == '__main__':
    app.run()