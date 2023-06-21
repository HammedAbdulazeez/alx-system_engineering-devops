import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    '''Recursively counts the occurrences of given keywords in the titles
    of hot articles in a given subreddit.
    '''
    if not word_list:
        return

    if after is None:
        word_count.clear()

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        posts = data.get('children')
        for post in posts:
            title = post.get('data').get('title').lower()
            for word in word_list:
                count = title.count(' ' + word.lower() + ' ')
                if word not in word_count:
                    word_count[word] = count
                else:
                    word_count[word] += count
        after = data.get('after')
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                if count > 0:
                    print('{}: {}'.format(word.lower(), count))
    else:
        return

