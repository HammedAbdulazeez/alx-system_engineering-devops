import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = Counter()

    # Base case: If there are no more words to search or the subreddit is invalid, print the results
    if not word_list or subreddit is None:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    # Fetch the Reddit API data
    headers = {"User-Agent": "Recursive Reddit API Client"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit is valid and the API request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        # Extract the titles and count the occurrences of keywords
        for post in posts:
            title = post["data"]["title"]
            lowercase_title = title.lower()
            word_count = Counter(re.findall(r"\b\w+\b", lowercase_title))
            for word in word_list:
                if word in word_count:
                    counts[word] += word_count[word]

        # Recursive call with the next page (if available)
        next_after = data["data"]["after"]
        count_words(subreddit, word_list, after=next_after, counts=counts)


# Example usage
count_words("python", ["Python", "programming", "API"])

