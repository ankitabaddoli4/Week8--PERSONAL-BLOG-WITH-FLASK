from app.comments import comments

@comments.route("/comments")
def all_comments():
    return "All Comments"

@comments.route("/add-comment")
def add_comment():
    return "Add Comment Page"