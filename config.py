import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "")
    OWNER = os.environ.get("OWNER_ID", "")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
<b>You can Download almost anything From your Instagram Account.</b>

<b>What Can Be Downloaded?:</b>

1. <code>All posts of any Profile.</code> (<i>Both Public and Private,for private profiles you need to be a follower</i>.)
2. <code>All Posts from your feed.</code>
3. <code>Stories of any profile</code> (<i>Both Public and Private,for private profiles you need to be a follower</i>.)
4. <code>DP of any profile</code> (<i>No need to follow</i>)
5. <code>Followers and Following List of any Profile.</code>
6. <code>Stories of your Followers.</code>
7. <code>Tagged posts of any profile.</code>
8. <code>Your saved Posts.</code>
9. <code>IGTV videos.</code>
10. <code>Highlights from any profiles.</code>
11. <code>Any Public Post from Link</code>(<i>Post/Reels/IGTV</i>)


<b>How to Download:</b>

Its Easy!!
You Need to login into your account by /login. 

You have two Options:

1. From Username:

Just send any instagram username.

For Example:
<code>leomessi</code>
<code>Amani_m_h_d</code>
<code>mahi7781</code>


2. From URL:

You can also sent a post link to download the post or video.

For Example:
<code>https://www.instagram.com/p/CL_-eqLJZyf/?utm_medium=copy_link</code>


<b>Available Commands and Usage</b>

/start - Check wheather bot alive.
/restart - Restart the bot (If you messed up anything use /restart.)
/help - Shows this menu.
/login - Login into your account.
/logout - Logout of your account.
/account - Shows the details of logged in account.

/posts <username> - Download posts of any username. Use /posts to download own posts or <code> /posts <username> </code>for others.
Example : <code>/posts samantharuthprabhuoffl</code>

/igtv <username> - Download IGTV videos from given username. If no username given, downloads your IGTV.

/feed <number of posts to download> - Downloads posts from your feed.If no number specified all posts from feed will be downloaded.
Example: <code>/feed 10</code> to download latest 10 posts from feed.

/saved <number of posts to download> - Downloads your saved posts. If no number specified all saved posts will be downloaded.
Example: <code>/saved 10</code> to download latest 10 saved posts.

/followers <username> - Get a list of all followers of given username. If no username given, then your list will be retrieved.
Example: <code>/followers samantharuthprabhuoffl</code>

/followees <username> - Get a list of all followees of given username. If no username given, then your list will be retrieved.

/tagged <username> - Downloads all posts in which given username is tagged. If nothing given your tagged posts will be downloaded.

/story <username> - Downloads all stories from given username. If nothing given your stories will be downloaded.

/stories - Downloads all the stories of all your followees.

/highlights <username> - Downloads highlights from given username, If nothing given your highlights will be downloaded.


"""
    HOME_TEXT = """
<b>Helo, [{}](tg://user?id={})

This is a bot of [{}](www.instagram.com/{}) to manage his Instagram account.
I can only work for my master [{}](tg://user?id={}).

Use /help to know What I can Do?</b>

<code>സൂക്ഷിച്ചു നോക്കേണ്ട ഉണ്ണീ, ഞാൻ നിനക്ക് വർക്കാകില്ല™</code>

🏷 <b>Maintained By: @Amani_m_h_d</b>
"""
    HOME_TEXT_OWNER = """
<b>Helo, [{}](tg://user?id={})
I am your assistant to manage your Instagram account.

Use /help to know what I can do for you.</b>
"""

