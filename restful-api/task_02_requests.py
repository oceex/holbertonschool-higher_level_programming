#!/usr/bin/python3
import requests, csv

r = requests.get("https://jsonplaceholder.typicode.com/posts")

def fetch_and_print_posts():
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post)

def fetch_and_save_posts():
    if r.status_code == 200:
        posts = r.json()
        v = []
        for post in posts:
            v.append([["id"], post["title"], post["body"]])
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "title", "body"])
            writer.writerows(v)