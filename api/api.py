from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class listAll(Resource):
    def get(self, dtype):
        topk = request.args.get('top', defualt=-1)
        if dtype == 'csv':
                return csv_format()
        return json_format()

class listOpenOnly(Resource):
    def get(self, dtype):
        topk = request.args.get('top', defualt=-1)
        if dtype == 'csv':
                return csv_format()
        return json_format()

class listCloseOnly(Resource):
    def get(self, dtype):
        topk = request.args.get('top', defualt=-1)
        if dtype == 'csv':
                return csv_format()
        return json_format()

api.add_resource(listAll, '/listAll', '/listAll/<string:dtype>')
api.add_resource(listOpenOnly, '/listOpenOnly', '/listOpenOnly/<string:dtype>')
api.add_resource(listCloseOnly, '/listCloseOnly', '/listCloseOnly/<string:dtype>')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
