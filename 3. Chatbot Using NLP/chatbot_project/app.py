from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
from nlp.chatbot_logic import generate_response

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def index():
    """Render the main chat interface."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat messages from the frontend."""
    user_input = request.json.get("message")
    app.logger.debug(f"Received message: {user_input}")

    # Validate input
    if not user_input:
        app.logger.warning("No message provided in request")
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate chatbot response
        response = generate_response(user_input)
        return jsonify({"response": response})
    except Exception as e:
        app.logger.error(f"Error generating response: {e}")
        return jsonify({"error": "An internal error occurred"}), 500

if __name__ == "__main__":
    # Run the app
    debug = True  # Set to False in production
    port = 5000
    app.run(debug=debug, port=port)


# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

# @app.route("/chat", methods=["POST"])  # Ensure this is POST
# def chat():
#     user_input = request.json.get("message")
#     if not user_input:
#         return jsonify({"error": "No message provided"}), 400
#     try:
#         # Replace this with your chatbot logic
#         response = f"Echo: {user_input}"
#         return jsonify({"response": response})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)