import openai
import config

openai.api_key = config.OPENAI_API_KEY

async def process_resume(content: str):
    """Extracts skills and generates a summary using AI."""
    prompt = f"Extract key skills and generate a summary from the following resume:\n\n{content}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    
    output = response["choices"][0]["message"]["content"]
    
    # Split response into skills & summary
    skills, summary = output.split("\n", 1) if "\n" in output else (output, "")
    
    return skills.strip(), summary.strip()
