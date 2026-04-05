from app.posts import posts

@posts.route("/posts")
def all_posts():
    return "All Posts"

@posts.route("/create-post")
def create_post():
    return "Create Post Page"