"""
Personality Engine Module (Groq API Version)
Transforms text into different personality tones
"""

import os
from groq import Groq
import httpx
from typing import Dict

class PersonalityEngine:
    def __init__(self):
        """Initialize the personality engine with Groq API"""
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        # Remove common proxy env vars that may be injected by PowerShell/Windows
        for key in [
            "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "NO_PROXY",
            "http_proxy", "https_proxy", "all_proxy", "no_proxy",
        ]:
            if key in os.environ:
                del os.environ[key]

        httpx_client = httpx.Client(trust_env=False)
        self.client = Groq(api_key=self.api_key, http_client=httpx_client)
        self.model = "llama-3.3-70b-versatile"
        
        self.personality_prompts = {
            "calm mentor": """Transform this text to sound like a calm, wise mentor who:
- Speaks with patience and understanding
- Uses gentle, encouraging language
- Provides structured guidance
- Shows confidence without being pushy
- Uses phrases like "Let's...", "Remember...", "You've got this"
""",
            "witty friend": """Transform this text to sound like a witty, casual friend who:
- Uses humor and pop culture references
- Speaks conversationally with contractions
- Includes light sarcasm or playful teasing
- Uses emojis sparingly (1-2 max)
- Makes the message fun and relatable
""",
            "therapist": """Transform this text to sound like an empathetic therapist who:
- Validates feelings and experiences
- Uses reflective language ("It sounds like...")
- Asks gentle questions
- Emphasizes self-compassion and wellbeing
- Maintains professional warmth
""",
            "formal": """Transform this text to sound formal and professional:
- Uses complete sentences and proper grammar
- Employs structured, systematic language
- Includes numbered lists or clear steps
- Maintains objective, businesslike tone
- Avoids contractions and casual language
""",
            "playful": """Transform this text to sound playful and energetic:
- Uses enthusiastic language with exclamation points
- Includes fun metaphors and comparisons
- Adds 2-4 relevant emojis throughout
- Makes the message feel like an adventure
- Uses words like "exciting", "awesome", "amazing"
"""
        }
    
    def transform_personality(self, base_reply: str, target_personality: str) -> Dict[str, str]:
        """Transform a base reply into a specific personality tone"""
        if target_personality not in self.personality_prompts:
            raise ValueError(f"Unsupported personality: {target_personality}")
        
        prompt = self._create_transformation_prompt(base_reply, target_personality)
        
        try:
            message = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a personality transformation expert that rewrites text in different tones while preserving the core message."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            transformed_text = message.choices[0].message.content.strip()
            
            return {
                "before": base_reply,
                "after": transformed_text
            }
            
        except Exception as e:
            raise Exception(f"Error calling Groq API: {str(e)}")
    
    def _create_transformation_prompt(self, base_reply: str, target_personality: str) -> str:
        """Create the prompt for personality transformation"""
        personality_instruction = self.personality_prompts[target_personality]
        prompt = f"""{personality_instruction}

Original text:
\"\"\"
{base_reply}
\"\"\"

Transform the above text while keeping the core message and intent. Output ONLY the transformed text, with no preamble or explanation."""
        return prompt
