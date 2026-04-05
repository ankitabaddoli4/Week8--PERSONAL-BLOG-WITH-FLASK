from flask import Blueprint, render_template, request

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def home():
    search = request.args.get('search', '')

    # Blog data (same as your output)
    posts = [
        {
            "title": "Getting Started with Flask Web Development",
            "date": "January 25, 2024",
            "author": "John Doe",
            "category": "Web Development",
            "content": "In this comprehensive guide, we'll explore how to build your first Flask application...",
            "views": 1245,
            "comments": 12,
            "likes": 45,
            "comments_list": [
                {
                    "name": "Jane Smith",
                    "date": "Jan 25, 2024",
                    "text": "Excellent tutorial! The step-by-step approach really helped me understand Flask better."
                },
                {
                    "name": "Alex Johnson",
                    "date": "Jan 26, 2024",
                    "text": "Could you add a section about deployment? That would be really helpful!"
                },
                {
                    "name": "Sarah Williams",
                    "date": "Jan 27, 2024",
                    "text": "The database integration section was particularly useful. Thanks!"
                }
            ]
        }
    ]

    # 🔍 SEARCH
    if search:
        posts = [p for p in posts if search.lower() in p["title"].lower()]

    # 📬 SUBSCRIBE
    if request.method == 'POST':
        email = request.form.get('email')
        print("Subscribed:", email)

    stats = {
        "total_posts": 25,
        "total_comments": 156,
        "categories": 8,
        "popular_post": "Python for Data Science (2,345 views)"
    }

    users = [
        {"name": "John Doe", "posts": 15},
        {"name": "Jane Smith", "posts": 8},
        {"name": "Mike Brown", "posts": 5}
    ]

    return render_template("home.html", posts=posts, stats=stats, users=users)