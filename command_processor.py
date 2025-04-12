# command_processor.py
import spacy
from social_media_handler import SocialMediaHandler
from scheduler import Scheduler

class CommandProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.social_media = SocialMediaHandler()
        self.scheduler = Scheduler()
        
    def process_command(self, text):
        doc = self.nlp(text)
        intent = self._extract_intent(doc)
        entities = self._extract_entities(doc)
        
        response = self._execute_action(intent, entities)
        return response
    
    def _extract_intent(self, doc):
        # Simple rule-based intent extraction
        if any(token.text.lower() in ["post", "share", "tweet"] for token in doc):
            return "social_media_post"
        elif any(token.text.lower() in ["remind", "schedule", "later"] for token in doc):
            return "schedule_task"
        return "unknown"
    
    def _extract_entities(self, doc):
        entities = {
            "platform": None,
            "content": None,
            "time": None
        }
        
        # Simple entity extraction
        for token in doc:
            if token.text.lower() in ["twitter", "linkedin", "instagram"]:
                entities["platform"] = token.text.lower()
                
        # Extract message content (simplified approach)
        if '"' in doc.text:
            import re
            match = re.search(r'"([^"]*)"', doc.text)
            if match:
                entities["content"] = match.group(1)
                
        # Extract time (simplified)
        for ent in doc.ents:
            if ent.label_ == "TIME":
                entities["time"] = ent.text
                
        return entities
    
    def _execute_action(self, intent, entities):
        if intent == "social_media_post":
            if entities["platform"] and entities["content"]:
                return self.social_media.post(
                    platform=entities["platform"],
                    content=entities["content"]
                )
            return {"success": False, "message": "Missing platform or content"}
            
        elif intent == "schedule_task":
            if entities["time"] and entities["content"]:
                return self.scheduler.schedule_task(
                    time=entities["time"],
                    task=entities["content"]
                )
            return {"success": False, "message": "Missing time or task content"}
            
        return {"success": False, "message": "I don't understand that command"}