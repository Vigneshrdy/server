# from flask import Flask, render_template, request, jsonify
# import google.generativeai as genai

# app = Flask(__name__)

# # # 🔐 Replace with your actual Gemini API Key here
# genai.configure(api_key="AIzaSyD5RcSbctOxhwK5-IG8nIK1HKPRYXluovM")

# model = genai.GenerativeModel("gemini-pro")

# @app.route('/')
# def index():
#     return render_template("templates/index.html")

# @app.route('/ask', methods=["POST"])
# def ask():
#     data = request.get_json()
#     prompt = data.get("prompt", "")
#     try:
#         response = model.generate_content(prompt)
#         return jsonify({"response": response.text})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
# # 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5050)


# from flask import Flask, request, jsonify, render_template
# import google.generativeai as genai

# app = Flask(__name__)
# genai.configure(api_key="AIzaSyD5RcSbctOxhwK5-IG8nIK1HKPRYXluovM")  # Replace with your real key

# model = genai.GenerativeModel("gemini-2.0-flash")
# # models = genai.list_models()

# # for model in models:
# #     print(model.name, model.supported_generation_methods)

# @app.route("/")
# def index():
#     return render_template("index.html")
# @app.route("/ask", methods=["POST"])
# def ask():
#     data = request.get_json()
#     user_input = data.get("prompt", "")
#     try:
#         response = model.generate_content(user_input)
#         return jsonify({"response": response.text})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5051)



# from flask import Flask, render_template, request, redirect, url_for, flash
# import requests

# app = Flask(__name__)
# app.secret_key = "AIzaSyD5RcSbctOxhwK5-IG8nIK1HKPRYXluovM"  # for flashing messages

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit_key():
#     api_key = request.form.get('api_key')

#     if not api_key:
#         flash("Please enter a Gemini API key!", "error")
#         return redirect(url_for('home'))

#     # Example test call (you can change this to your actual Gemini API usage)
#     test_url = "https://generativelanguage.googleapis.com/v1beta/models"
#     headers = {"Authorization": f"Bearer {api_key}"}

#     try:
#         response = requests.get(test_url, headers=headers)
#         if response.status_code == 200:
#             flash("✅ API key is valid and working!", "success")
#         else:
#             flash(f"❌ Invalid API Key or Request Failed ({response.status_code})", "error")
#     except Exception as e:
#         flash(f"Error connecting to API: {str(e)}", "error")

#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, jsonify, session
# import google.generativeai as genai

# app = Flask(__name__)
# app.secret_key = "myflasksecret123"

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/set_key', methods=["POST"])
# def set_key():
#     """Takes API key from frontend and configures Gemini"""
#     data = request.get_json()
#     api_key = data.get("api_key", "AIzaSyD5RcSbctOxhwK5-IG8nIK1HKPRYXluovM").strip()

#     if not api_key:
#         return jsonify({"error": "API key is required"}), 400

#     try:
#         genai.configure(api_key=api_key)
#         # Test model initialization
#         model = genai.GenerativeModel("gemini-pro")
#         model.generate_content("hello")  # test minimal call
#         session['api_key'] = api_key
#         return jsonify({"message": "API key set successfully!"})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# @app.route('/ask', methods=["POST"])
# def ask():
#     """Handles user chat prompts"""
#     if 'api_key' not in session:
#         return jsonify({"error": "API key not configured"}), 403

#     data = request.get_json()
#     user_input = data.get("prompt", "").strip()
#     if not user_input:
#         return jsonify({"error": "Prompt cannot be empty"}), 400

#     try:
#         genai.configure(api_key=session['api_key'])
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(user_input)
#         return jsonify({"response": response.text})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5050, debug=True)


# from flask import Flask, render_template, request, jsonify, session
# import google.generativeai as genai

# app = Flask(__name__)
# app.secret_key = "myflasksecret123"  # session secret

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/set_key', methods=["POST"])
# def set_key():
#     """Set the Gemini API key from the frontend"""
#     data = request.get_json()
#     api_key = data.get("api_key", "").strip()

#     if not api_key:
#         return jsonify({"error": "API key is required"}), 400

#     try:
#         genai.configure(api_key=api_key)
#         # test minimal model call
#         model = genai.GenerativeModel("gemini-pro")
#         model.generate_content("test connection")

#         session['api_key'] = api_key
#         return jsonify({"message": "✅ API key set successfully!"})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# @app.route('/ask', methods=["POST"])
# def ask():
#     """Handle chat messages with the Gemini model"""
#     if 'api_key' not in session:
#         return jsonify({"error": "API key not configured"}), 403

#     data = request.get_json()
#     prompt = data.get("prompt", "").strip()

#     if not prompt:
#         return jsonify({"error": "Prompt cannot be empty"}), 400

#     try:
#         genai.configure(api_key=session['api_key'])
#         model = genai.GenerativeModel("gemini-pro")
#         response = model.generate_content(prompt)
#         return jsonify({"response": response.text})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5050, debug=True)

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ✅ Set your Gemini API key here directly
genai.configure(api_key="AIzaSyD5RcSbctOxhwK5-IG8nIK1HKPRYXluovM")

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("prompt", "").strip()

    if not user_input:
        return jsonify({"error": "Please enter a question"}), 400

    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
