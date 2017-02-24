# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home_pagina():
    return render_template("home.html")

@app.route("/api/track/<track>")
def api_track(track):
    params = get_track(track)
    return jsonify(params)

def get_track(track):

    headers = {
    "client_id": "665943a15f884bef9a0c8b0cb7864daf",
    "cliente_secret": "c47b8817bb9748f694769c1b3f6b63a4"
    }

    response = requests.get("https://api.spotify.com/v1/search?q=" + track +"&type=track", headers=headers)

    if response.status_code == 200:
        print(response.text)
        response_dict = response.json()
        results = response_dict["tracks"]
        items = results ["items"]
        for value in items:
            print value["id"]



    params = {
    "tracks": track
    }

    return params







if __name__ == "__main__":
    app.run(debug=True)
