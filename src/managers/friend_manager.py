class Friend:
    """
    代表一个朋友的博客信息。
    """
    def __init__(self, name, url, avatar, feed_url=None, feed_type=None, isError=False):
        self.isError = isError
        self.name = name # 博客站点名称
        self.url = url
        self.avatar = avatar
        self.feed_url = feed_url
        self.feed_type = feed_type
        self.articles = []
        self.articles_num = 0

    def add_articles(self, articles):
        """
        添加文章到朋友的博客数据中
        """
        self.articles.extend(articles)
        self.articles_num = len(self.articles)

    def clear_articles(self):
        """
        清空该朋友的文章数据
        """
        self.articles = []
        self.articles_num = 0

class Friends:
    """
    代表一组朋友的博客信息。
    """
    def __init__(self):
        self.friends = [Friend]
        self.error_num = 0
        self.correct_num = 0

    def add_friend(self, friend : Friend): 
        """
        添加一个朋友到列表中
        """
        self.friends.append(friend)
        if friend.isError:
            self.error_num += 1
        else:
            self.correct_num += 1

    def clear_friends(self):
        """
        清空朋友列表
        """
        self.friends = []
        self.error_num = 0
        self.correct_num = 0

    def get_friends(self):
        """
        获取朋友列表
        """
        return self.friends
    
    def get_error_num(self):
        """
        获取错误的朋友数量
        """
        return self.error_num
    
    def get_correct_num(self):
        """
        获取正确的朋友数量
        """
        return self.correct_num
    
    def get_total_num(self):
        """
        获取朋友总数
        """
        return self.error_num + self.correct_num
    
    def get_articles_num(self):
        """
        获取所有朋友的文章总数
        """
        return sum(friend.articles_num for friend in self.friends)
    
    def get_friend_with_url(self, url):
        """
        通过 URL 获取朋友对象
        """
        return next((friend for friend in self.friends if friend.url == url), None)