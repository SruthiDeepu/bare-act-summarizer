import openai

def summarize_text(text):
    prompt = f"Summarize the following legal text into bullet points and a flowchart:\n\n{text}\n\nSummary:"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response['choices'][0]['message']['content']
