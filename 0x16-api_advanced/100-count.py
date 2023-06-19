import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

    if after == '':
        # Base case: end of posts
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        for child in children:
            title = child['data']['title']
            for word in word_list:
                if word.lower() in title.lower().split():
                    count_dict[word.lower()] = count_dict.get(word.lower(), 0) + 1

        after = data['data']['after']
        count_words(subreddit, word_list, after, count_dict)
    else:
        print("Invalid subreddit or no posts match.")

# Example usage
subreddit = "python"
word_list = ["python", "javascript", "java"]

count_words(subreddit, word_list)

