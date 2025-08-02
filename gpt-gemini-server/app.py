# # from flask import Flask, render_template, request, jsonify
# # import google.generativeai as genai

# # app = Flask(__name__)

# # # 🔐 Replace with your actual Gemini API Key here
# # genai.configure(api_key="AIzaSyCh7gfbDoqtTR9RVF9luo9n7eQDYJERnAU")

# # model = genai.GenerativeModel("gemini-pro")

# # @app.route('/')
# # def index():
# #     return render_template("index.html")

# # @app.route('/ask', methods=["POST"])
# # def ask():
# #     data = request.get_json()
# #     prompt = data.get("prompt", "")
# #     try:
# #         response = model.generate_content(prompt)
# #         return jsonify({"response": response.text})
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500

# # if __name__ == "__main__":
# #     app.run(host="0.0.0.0", port=5050)


from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)
genai.configure(api_key="AIzaSyCh7gfbDoqtTR9RVF9luo9n7eQDYJERnAU")  # Replace with your real key

model = genai.GenerativeModel("gemini-2.0-flash")
# models = genai.list_models()

# for model in models:
#     print(model.name, model.supported_generation_methods)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("prompt", "")
    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)


