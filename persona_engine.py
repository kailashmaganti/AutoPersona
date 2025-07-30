import cohere

# Load your Cohere API key
cohere_api_key = "YfYYyltPWR63LMwRWj2YN8BaFAF8QDRR3n56Amjt"  # 🔐 Replace this with your actual key
co = cohere.Client(cohere_api_key)

def generate_persona(name, hobbies, tone, style):
    # Build the prompt based on style
    if style == "professional":
        prompt = f"Write a professional AI persona for {name}, who enjoys {hobbies}, with a {tone} tone."
    elif style == "fantasy":
        prompt = f"Create a fantasy character profile for {name}, who enjoys {hobbies}, with a {tone} voice."
    elif style == "rpg":
        prompt = f"Generate an RPG-style character named {name}, passionate about {hobbies}, speaking in a {tone} way."
    elif style == "sci-fi":
        prompt = f"Create a futuristic AI identity for {name}, obsessed with {hobbies}, using a {tone} tone."
    elif style == "funny":
        prompt = f"Write a funny, ridiculous persona for {name}, who loves {hobbies}, with a silly and {tone} vibe."
    else:
        prompt = f"Create a persona for {name}, who enjoys {hobbies}, speaking in a {tone} tone."

    # Call Cohere's chat API
    response = co.chat(
        message=prompt,
        model="command-r-plus",  # Use "command-r" if you're not whitelisted for plus
        temperature=0.7,
        max_tokens=300
    )

    return response.text
