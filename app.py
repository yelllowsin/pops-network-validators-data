from flask import Flask, abort, jsonify
import json

app = Flask(__name__)

#defining static data at first
datas = [
    {
        "ID": "1",
        "Name": "Harmony",
        "price": "20",
        "APY": "10-12",
        "Fees" : "5",
        "Info": "Harmony insert decription",
        "Total_delegagation" : "1111",
        "Project_website" : "https://www.harmony.one",
        "Project_documentations" : ["https://github.com/harmony", "https://medium.com/harmony"],
        "Validators": [
            {
                "Address": "one1kf42rl6yg2avkjsu34ch2jn8yjs64ycn4n9wdj",
                "Name": "P-OPS Validator",
                "Fees": "5",
                "Delegation": "250000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            },
            {
                "Address": "one19ugus2az5a9m8tcgeq2pazcdht5kn3pe86434u",
                "Name": "Stakehere",
                "Fees": "10",
                "Delegation": "15000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            }
        ]
    },
    {
        "ID": "2",
        "Name": "Solana",
        "price": "0.2",
        "Fees" : "5",
        "APY": "15",
        "Info": "Solana insert decription",
        "Total_delegagation" : "1111",
        "Project_website" : "https://www.solana.com",
        "Project_documentations" : ["github.com/solana", "medium.com/solana"],
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "Fees": "5",
                "Delegation": "250000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            },
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Mindstyle",
                "Fees": "10",
                "Delegation": "15000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            }
        ]
    },
    {
        "ID": "3",
        "Name": "Avalanche",
        "price": "0.2",
        "APY": "15",
        "Fees" : "5",
        "Info": "Avalanche insert description",
        "Total_delegagation" : "1111",
        "Project_website" : "https://www.avalabs.org/",
        "Project_documentations" : ["github.com/avalabs", "medium.com/avalabs"],
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "Fees": "5",
                "Delegation": "250000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            },
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Mindstyle",
                "Fees": "10",
                "Delegation": "15000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            }
        ]
    },
    {
        "ID": "4",
        "Name": "The Graph",
        "price": "0.2",
        "APY": "15",
        "Fees" : "5",
        "Info": "The Graph insert description",
        "Total_delegagation" : "1111",
        "Project_website" : "https://thegraph.com/",
        "Project_documentations" : ["github.com/thegraph", "medium.com/thegraph"],
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "Fees": "5",
                "Delegation": "250000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            },
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Mindstyle",
                "Fees": "10",
                "Delegation": "15000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
            }
        ]
    },
    {
        "ID": "5",
        "Name": "Stafi",
        "price": "4",
        "APY": "15",
        "Fees" : "5",
        "Info": "Stafi insert description",
        "Total_delegagation" : "1111",
        "Project_website" : "https://www.stafi.io",
        "Project_documentations" : ["github.com/stafi", "medium.com/stafi"],
        "Validators": [
            {
                "Address": "D8P3w7GQ4zTYbJfEGgfdQWQ1vrL6umGYAUrMz4hBJjrN",
                "Name": "Soph",
                "Fees": "5",
                "Delegation": "250000000",
                "Stake_link": "https://stake_link_to_be_filled_up"
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