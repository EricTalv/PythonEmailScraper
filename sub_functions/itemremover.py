urls = ['facebook.com', 'youtube.com', 'gold']
blockers = ['facebook', 'netflix','youtube']

urls = [url for url in urls if not any(blocker in url for blocker in blockers)]

print(urls)
