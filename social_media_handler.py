# social_media_handler.py
import tweepy
import requests
from linkedin_api import Linkedin

class SocialMediaHandler:
    def __init__(self):
        # Twitter setup
        self.twitter_auth = tweepy.OAuthHandler(
            "YOUR_TWITTER_API_KEY", 
            "YOUR_TWITTER_API_SECRET"
        )
        self.twitter_auth.set_access_token(
            "YOUR_ACCESS_TOKEN", 
            "YOUR_ACCESS_TOKEN_SECRET"
        )
        self.twitter_api = tweepy.API(self.twitter_auth)
        
        # LinkedIn setup
        self.linkedin = Linkedin("YOUR_LINKEDIN_EMAIL", "YOUR_LINKEDIN_PASSWORD")
        
    def post(self, platform, content):
        try:
            if platform == "twitter":
                return self._post_twitter(content)
            elif platform == "linkedin":
                return self._post_linkedin(content)
            else:
                return {"success": False, "message": f"Platform {platform} not supported"}
        except Exception as e:
            return {"success": False, "message": str(e)}
    
    def _post_twitter(self, content):
        self.twitter_api.update_status(content)
        return {"success": True, "message": "Posted to Twitter successfully"}
    
    def _post_linkedin(self, content):
        self.linkedin.post(content)
        return {"success": True, "message": "Posted to LinkedIn successfully"}