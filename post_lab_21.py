import requests

class JSONPlaceholderClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    # Method to fetch all posts
    def get_posts(self):
        url = f"{self.base_url}/posts"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching posts: {response.status_code}")
            return None

    # Method to fetch a single post by ID
    def get_post(self, post_id):
        url = f"{self.base_url}/posts/{post_id}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching post {post_id}: {response.status_code}")
            return None

    # Method to create a new post
    def create_post(self, title, body, user_id):
        url = f"{self.base_url}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(url, json=data)

        if response.status_code == 201:
            return response.json()
        else:
            print(f"Error creating post: {response.status_code}")
            return None


# for Demo :

client = JSONPlaceholderClient()

# Fetch all posts
print("Fetching posts...")
posts = client.get_posts()
if posts:
    for p in posts[:5]:
        print(f"- {p['title']}")

# Fetch a single post
print("\nFetching post with ID 3...")
single_post = client.get_post(3)
print(single_post)

# Create a new post
print("\nCreating a new post...")
new_post = client.create_post(
    title="My API Post",
    body="This is a post created through the API client class.",
    user_id=10
)
print(new_post)
