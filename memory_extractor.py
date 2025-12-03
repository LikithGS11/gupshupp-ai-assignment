"""
Memory Extraction Module (Groq API Version)
Extracts user preferences, emotional patterns, and key facts from chat messages
"""

import os
import json
from groq import Groq
import httpx
from typing import Dict, List

class MemoryExtractor:
    def __init__(self):
        """Initialize the memory extractor with Groq API"""
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

        # Create an httpx client that will not pick up system proxies
        httpx_client = httpx.Client(trust_env=False)
        self.client = Groq(api_key=self.api_key, http_client=httpx_client)
        self.model = "llama-3.3-70b-versatile"
    
    def extract_memory(self, chat_messages: str) -> Dict[str, List[str]]:
        """Extract memory components from chat messages"""
        prompt = self._create_extraction_prompt(chat_messages)
        try:
            message = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a memory extraction expert that analyzes chat messages and extracts structured information."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=2000
            )
            response_text = message.choices[0].message.content
            result = self._parse_response(response_text)
            return result
        except Exception as e:
            raise Exception(f"Error calling Groq API: {str(e)}")
    
    def _create_extraction_prompt(self, chat_messages: str) -> str:
        """Create the prompt for memory extraction"""
        prompt = f"""You are a memory extraction expert. Analyze the following chat messages and extract three key components:

1. **User Preferences**: What the user likes/dislikes, their style, habits, and preferences
2. **Emotional Patterns**: Frequency and patterns of emotions like stress, excitement, humor, confusion
3. **Facts Worth Remembering**: Stable details like name, job, goals, background, and other biographical information

Chat Messages:
\"\"\"
{chat_messages}
\"\"\"

IMPORTANT: You must respond ONLY with a valid JSON object in this exact format (no markdown, no code blocks, no explanation):

{{
  "preferences": [
    "preference 1",
    "preference 2"
  ],
  "emotional_patterns": [
    "pattern 1 with frequency indication",
    "pattern 2 with frequency indication"
  ],
  "facts": [
    "fact 1",
    "fact 2"
  ]
}}

Guidelines:
- Extract 3-5 items for each category if available
- Be specific and concrete
- For emotional patterns, indicate frequency (e.g., "Shows excitement 3x when discussing projects")
- For facts, use clear statements (e.g., "Name: Sarah" or "Job: Product Manager")
- If a category has no data, use an empty array []
- Output ONLY the JSON object, nothing else"""
        return prompt
    
    def _parse_response(self, response_text: str) -> Dict[str, List[str]]:
        """Parse the Groq API response into structured format"""
        try:
            cleaned = response_text.strip()
            if cleaned.startswith("```json"):
                cleaned = cleaned[7:]
            if cleaned.startswith("```"):
                cleaned = cleaned[3:]
            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]
            cleaned = cleaned.strip()
            result = json.loads(cleaned)
            if not all(key in result for key in ['preferences', 'emotional_patterns', 'facts']):
                raise ValueError("Missing required keys in response")
            return result
        except json.JSONDecodeError as e:
            return {
                "preferences": [],
                "emotional_patterns": [],
                "facts": []
            }
