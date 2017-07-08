from flask import Flask, Response, jsonify
from flask_restplus import Api, Resource, fields, reqparse

# From https://datascience.ibm.com/blog/deploy-your-python-functions-as-a-rest-api/

def affirmation(name):
    return "{0}. You're Good Enough, You're Smart Enough, and Doggone It, People Like You".format(name)

app = Flask(__name__)

api = Api(app, version='1.0', title='APIs for self affirmation', validate=False)
ns = api.namespace('affirm', 'Returns affirmations')

model_input = api.model('Enter your name:', { 'NAME': fields.String })

@ns.route('/me')
class affirm(Resource):
    @api.response(200, 'Success', model_input)
    @api.expect(model_input)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('NAME', type=str)
        args = parser.parse_args()
        inp = args['NAME']
        result = affirmation(inp)
        return jsonify({"affirmation": result})

# run      
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8080, debug=False)

