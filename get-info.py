import requests
import json
from lxml import html
from six.moves import urllib

def get_user_info(user_name):
        url = "https://www.instagram.com/" + user_name + "/?__a=1"
        try:
                r = requests.get(url)
        except requests.exceptions.ConnectionError:
                print 'Seems like dns lookup failed..'
                time.sleep(60)
                return None
        if r.status_code != 200:
                print 'User: ' + user_name + ' status code: ' + str(r.status_code)
                print r
                return None
        info = json.loads(r.text)
        return info['user']

class getInfo():

        def __init__(self, user_name):
                self.username = user_name
                print 'Getting info...'
                self.url = "https://www.instagram.com/" + self.username + "/?_a=1"
                self.r = requests.get(self.url)
                self.content = self.r.text
        
        def followers(self):
                followers = []
                follower_id = self.content.find('Followers')
                for i in range(follower_id-2, follower_id-10, -1):
                        if ord(self.content[i]) >= 48 and ord(self.content[i]) <= 57 or ord(self.content[i]) == 107 or ord(self.content[i]) == 109 or ord(self.content[i]) == 46:
                                followers.append(self.content[i])
                return ''.join(reversed(followers))
        def following(self):
                following = []
                following_id = self.content.find('Following')
                for i in range(following_id-2, following_id-10, -1):
                        if ord(self.content[i]) >= 48 and ord(self.content[i]) <= 57 or ord(self.content[i]) == 107 or ord(self.content[i]) == 109 or ord(self.content[i]) == 46:
                                following.append(self.content[i])
                return ''.join(reversed(following))
        def post(self):
                post = []
                post_id = self.content.find('Posts')
                for i in range(post_id-2, post_id-10, -1):
                        if ord(self.content[i]) >= 48 and ord(self.content[i]) <= 57 or ord(self.content[i]) == 107 or ord(self.content[i]) == 109 or ord(self.content[i]) == 46:
                                post.append(self.content[i])
                return ''.join(reversed(post))
        def getImg(self):
                img = []
                img_id = self.content.find('profile_pic_url_hd')
                for i in range(img_id+22, img_id+139):
                        if ord(self.content[i]) != 34:
                                print self.content[i]
                                img.append(self.content[i])
                return ''.join(img)
def main():
        username = "shivaa.shams"
        obj = getInfo(username)
        followers = obj.followers()
        following = obj.following()
        posts = obj.post()
        print 'User Info:'
        print 'Username:%s' % username
        print 'Followers:%s' % followers
        print 'Following: %s' % followers
        print 'Posts:%s' % posts
        print 'getting image'
        img_url = obj.getImg()
        urllib.request.urlretrieve(img_url, 'img.jpg')
        print 'open image'
if __name__ == '__main__':
        main()
