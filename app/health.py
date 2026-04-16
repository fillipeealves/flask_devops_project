from flask import Blueprint, jsonify

health = Blueprint("health", __name__)

@health.route("/health")
def check():
    return jsonify({
        "status": "healthy"
    })
