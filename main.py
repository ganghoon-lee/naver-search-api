from flask import Flask, request, jsonify
from serpapi import GoogleSearch

app = Flask(__name__)

@app.route('/naver_search', methods=['GET'])
def naver_search():
    query = request.args.get("query")
    params = {
        "engine": "naver",
        "query": query,
        "api_key": "8a37d0dd24948784d4a68e6a8cca5f70501a37f917c9628331ea5ef2db4bcbcf"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic = results.get("organic_results", [])

    data = [
        {
            "title": item.get("title"),
            "link": item.get("link"),
            "snippet": item.get("snippet")
        }
        for item in organic
    ]

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
