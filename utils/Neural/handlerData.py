import ollama

def handle_data(query):
    prompt = "System: ТЫ ГОВОРИШЬ ТОЛЬКО ПО РУССКИ"
    query = f"Query from user: {query} "

    response_text = prompt + query
    data = [
      {
        'role': 'user',
        'content': response_text,
      },
    ]
    options = {
        "temperature": 0.8,
    }
    response = ollama.chat(model='llama3', messages=data, options=options)
    return response['message']['content']