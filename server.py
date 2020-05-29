
"""Example inference server for Cloud AI Platform Prediction."""
 
import logging
import os
import flask
app = flask.Flask(__name__)
 
@app.route("/v1/models/<model>/versions/<version>:predict", methods=["POST"])
def predict(model, version):
  return flask.jsonify({
    "predictions": ["Hello from the custom container!"],
    "request": flask.request.get_data(as_text=True),
    "headers": dict(flask.request.headers),
    "environment": dict(os.environ)
  })
 
@app.route("/v1/models/<model>/versions/<version>", methods=["GET"])
  def health(model, version):
    return flask.jsonify({})
