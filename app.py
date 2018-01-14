from flask import Flask, request, jsonify
from bot import bot
import time, datetime, json, os
import models as dbHandler



app = Flask(__name__)

bot_obj = bot.Bot()

@app.route("/set", methods=['GET'])
def api():
    print("Hello")
    if request.method == 'GET':
        try:
            query = request.args.get('q')
            response = bot_obj.get_response(query)
            timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            dbHandler.insert_data(query, response, timestamp)
            return jsonify({
                     'status': 'success',
                     'query' : query ,
                     'response': response,
                     'timestamp': timestamp
                });
            

        except Exception as e:
            return '{ "status" : "error + " , e}'


@app.route("/get", methods=['GET'])
def getApi():
    if request.method == 'GET':
        try:
            x = dbHandler.retrieve_data()
            return jsonify(status="success", data=x)

        except Exception as e:
            print(str(e))
            return e


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

