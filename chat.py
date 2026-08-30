from mistralai import Mistral
import os

api_key = "ApGWFGKJYrwwCIfZglvcBct9xurtHact"  # ou use os.environ.get("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)

response = client.chat.complete(
    model="mistral-large-latest",  # ou "mistral-small-latest", "open-mistral-nemo", etc.
    messages=[
        {
            "role": "user",
            "content": "In one sentence, what is CS50?"
        }
    ]
)

print(response.choices[0].message.content)