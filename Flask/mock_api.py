from flask import Flask, jsonify, request

app = Flask(__name__)

@app.post('/api/lead_post')
def apiLeadPost():
    args = request.get_json()
    print(args)
    if "FirstName" in args:
        if args["FirstName"] == "None":
            return "First Name is null", 500
        else:
            return jsonify({"message": "success"}), 200
    return "First Name parameter is missing", 404
    
    

if __name__ == '__main__':
    app.run(port=5001, debug=True)