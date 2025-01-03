import json
from datetime import datetime
import random

class Post:
    def __init__(self, content, scheduled_time, platform, post_id=None):
        self.post_id = random.randint(1000, 9999) if post_id is None else post_id
        self.content = content
        self.scheduled_time = scheduled_time
        self.platform = platform

    def edit_content(self, new_content):
        self.content = new_content

    def change_scheduled_time(self, new_time):
        self.scheduled_time = new_time

    def display_post_details(self):
        return {
            "Post ID": self.post_id,
            "Content": self.content,
            "Scheduled Time": self.scheduled_time,
            "Platform": self.platform
        }

class Scheduler:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def remove_post(self, post_id):
        for post in self.posts:
            if post.post_id == post_id:
                self.posts.remove(post)
                return
            else:
                print("Invalid post ID!")

    def view_all_posts(self):
        all_posts = []
        for post in self.posts:
            post_details = post.display_post_details()
            all_posts.append(post_details)
        return all_posts

    def save_posts_to_file(self, filename):
        with open(filename, 'w') as file:
            posts_data = [
                {"post_id": post.post_id, "content": post.content, "scheduled_time": post.scheduled_time, "platform": post.platform}
                for post in self.posts
            ]
            json.dump(posts_data, file, indent=4)

    def load_posts_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                posts_data = json.load(file)
                self.posts = [Post(p['content'], p['scheduled_time'], p['platform'],p['post_id']) for p in posts_data]
        except FileNotFoundError:
            print("File not found!")

def menu():
    scheduler = Scheduler()
    filename = "Social_media_scheduler/data.txt"
    while True:
        print("\nSocial Media Post Scheduler")
        print("1. Add a new post")
        print("2. Edit post content and scheduled time")
        print("3. Remove a post")
        print("4. View all scheduled posts")
        print("5. Save posts to a file")
        print("6. Load posts from a file")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            content = input("Enter post content: ")
            scheduled_time = input("Enter scheduled time ('6:00 AM'): ")
            platform = input("Enter platform (e.g. Instagram, Twitter, Facebook): ")
            scheduler.add_post(Post(content, scheduled_time, platform))
            print("Post added successfully!")
        elif choice == '2':
            post_id = int(input("Enter post ID: "))
            if 0 <= post_id:
                new_content = input("Enter new content: ")
                new_time = input("Enter new scheduled time: ")
                for post in scheduler.posts:
                    if post.post_id == post_id:
                        post.edit_content(new_content)
                        post.change_scheduled_time(new_time)
                        break
                print("Post updated successfully!")
            else:
                print("Invalid post ID!")
        elif choice == '3':
            post_id = int(input("Enter post ID to remove: "))
            scheduler.remove_post(post_id)
            print("Post removed successfully!")
        elif choice == '4':
            all_posts = scheduler.view_all_posts()
            if all_posts:
                for post in all_posts:
                    print(post)
            else:
                print("No posts scheduled!")
        elif choice == '5':
            scheduler.save_posts_to_file(filename)
            print(f"Posts saved to {filename}!")
        elif choice == '6':
            scheduler.load_posts_from_file(filename)
            print(f"Posts loaded from {filename}!")
        elif choice == '7':
            print("Exiting the scheduler. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
