import os
from flask import Flask, request, jsonify
from backend.generate_blog import generate_blog_post

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_blog_endpoint():
    """Handle blog post generation requests."""

    # Fix: Correct method
    data = request.get_json()
    topic = data.get("topic", "")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    # Fix: Correct function name
    blog = generate_blog_post(topic)

    # Fix: Correct filename format
    blog_filename = f"blogs/{topic.replace(' ', '_').lower()}.md"

    with open(blog_filename, "w", encoding="utf-8") as f:
        f.write(blog)

    return jsonify({
        "message": "Blog generated successfully",
        "blog": blog,
        "filename": blog_filename
    })


if __name__ == "__main__":
    os.makedirs("blogs", exist_ok=True)
    app.run(debug=True)
