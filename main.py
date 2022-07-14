from flask import Flask, render_template
import requests
from post import Post


posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objs = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objs.append(post_obj)


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=post_objs)


@app.route("/post/<int:post_id>")
def show_post(post_id):
    required_post = None
    for blog_post in post_objs:
        if blog_post.id == post_id:
            required_post = blog_post
    return render_template("post.html", rpost=required_post)


if __name__ == "__main__":
    app.run(debug=True)
