from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_openai(prompt, model="gpt-3.5-turbo", temperature=0.7):
    """
    Calls the OpenAI chat completion API using SDK v1.x syntax.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ OpenAI call failed: {str(e)}"

def get_related_roles_via_openai(target_role):
    """
    Uses OpenAI to return a list of job titles related to the given role.
    """
    prompt = f"""
    List 4–6 job titles that are commonly related, interchangeable, or overlapping with the role: "{target_role}". 
    These titles should be realistic alternatives a recruiter might consider when hiring for "{target_role}".
    Respond as a plain Python list of strings.
    """
    response = call_openai(prompt)
    try:
        return eval(response.strip()) if response.strip().startswith("[") else []
    except Exception:
        return []
