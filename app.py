from flask import Flask, abort, jsonify
import json

app = Flask(__name__)

#defining static data at first
datas = [
[
    {
      "ID": "1",
      "Name": "Harmony",
      "price": "20",
      "APY": "10-12",
      "Info": "Harmony insert decription",
      "total_delegagation" : "1111",
      "Validators": [
            {
                "Address": "one1kf42rl6yg2avkjsu34ch2jn8yjs64ycn4n9wdj",
                "Name": "P-OPS Validator",
                "fees": "5",
                "delegation": "250000000"
            },
            {
                "Address": "one19ugus2az5a9m8tcgeq2pazcdht5kn3pe86434u",
                "Name": "Stakehere",
                "fees": "10",
                "delegation": "15000000"
            }
      ]
    },
    {
        "ID": "2",
        "Name": "Solana",
        "price": "0.2",
        "APY": "15",
        "Info": "Solana insert decription",
        "total_delegagation" : "1111",
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "fees": "5",
                "delegation": "250000000"
            },
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Mindstyle",
                "fees": "10",
                "delegation": "15000000"
            }
        ]
    },
    {
        "ID": "3",
        "Name": "Avalanche",
        "price": "0.2",
        "APY": "15",
        "Info": "Avalanche insert description",
        "total_delegagation" : "1111",
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "fees": "5",
                "delegation": "250000000"
            },
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Mindstyle",
                "fees": "10",
                "delegation": "15000000"
            }
        ]
    },
    {
        "ID": "4",
        "Name": "The Graph",
        "price": "0.2",
        "APY": "15",
        "Info": "The Graph insert description",
        "total_delegagation" : "1111",
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "fees": "5",
                "delegation": "250000000"
            },
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Mindstyle",
                "fees": "10",
                "delegation": "15000000"
            }
        ]
    },
    {
        "ID": "5",
        "Name": "Stafi",
        "price": "4",
        "APY": "15",
        "Info": "Stafi insert description",
        "total_delegagation" : "1111",
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "fees": "5",
                "delegation": "250000000"
            }
        ]
    }
]


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@app.route('/')
def hello_world():
    return 'Hello to POPS Validator data API endpoint!'

@app.route('/networks/harmony')
def harmony_data():
    try:
        return datas[0]
    except:
        abort(404, description="Harmony ressource not found")

@app.route('/networks/solana')
def solana_data():
    try:
        return datas[1]
    except:
        abort(404, description="Solana ressource not found")

@app.route('/networks/avalanche')
def avalanche_data():
    try:
        return datas[2]
    except:
        abort(404, description="Avalanche ressource not found")

@app.route('/networks/thegraph')
def thegraph_data():
    try:
        return datas[3]
    except:
        abort(404, description="The Graph ressource not found")

@app.route('/networks/stafi')
def stafi_data():
    try:
        return datas[4]
    except:
        abort(404, description="Stafi ressource not found")


@app.route('/networks')
def all():
    try:
        return jsonify(datas)
    except:
        abort(404, description="Solana ressource not found")