from newsapi import NewsApiClient

# Instantiate the NewsApiClient object using your API key / Khởi tạo đối tượng Newsapiclient bằng khóa API của bạn
api = NewsApiClient(api_key='ab4230e7b2b7442e95f2625ae2582266')

# Retrieve the top headlines / Lấy các tiêu đề hàng đầu
top_headlines = api.get_top_headlines()

# Print the titles and descriptions of the articles / In các tiêu đề và mô tả của các bài báo
for article in top_headlines['articles']:
    print('Title:', article['title'])
    print('Description:', article['description'])
    print()



"""
Make sure to replace your_api_key with your actual API key. From > https://newsapi.org/ <
"""