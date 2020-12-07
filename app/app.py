import os
from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def deploy():
    result = {'status': None, 'message': None}

    params = json.loads(request.data.decode('utf-8'))
    deploy_app = params['app']
    token = params['token']

    if token == os.environ['TOKEN']:
        deploy_sh = './deploy/%s.sh' % deploy_app
        if os.path.exists(deploy_sh):
            os.system('sh ./deploy/%s.sh &' % deploy_app)
        else:
            # デプロイするappが見つからない
            result['status'] = 'NG'
            result['message'] = 'No such app: %s' % deploy_app
            return result, 400

    else:
        # トークン認証に失敗
        result['status'] = 'NG'
        result['message'] = 'Unauthorized token'
        return result, 401

    result['status'] = 'OK'
    result['message'] = 'success'
    return result, 200


if __name__ == '__main__':
    if 'TOKEN' not in os.environ:
        raise Exception('トークンを配置してください')

    app.run(debug=True)
