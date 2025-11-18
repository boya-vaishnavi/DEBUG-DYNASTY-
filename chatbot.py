from transformers import pipeline

# Initialize IBM Granite model
pipe = pipeline(
    "text-generation",
    model="ibm-granite/granite-3.3-2b-instruct"
)

def ask_granite(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = pipe(messages, max_new_tokens=250)
    return response[0]["generated_text"]
