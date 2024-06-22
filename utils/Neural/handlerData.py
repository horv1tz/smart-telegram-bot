import ollama
import logging

def handle_data(query, chat_history):
    logging.info("Starting handle_data function")
    prompt = "System: ТЫ ГОВОРИШЬ ТОЛЬКО ПО РУССКИ"
    query = f"Query from user: {query} "

    # Формирование истории чата для модели
    data = [
        {
            'role': 'system',
            'content': prompt,
        },
    ] + chat_history + [
        {
            'role': 'user',
            'content': query,
        },
    ]

    options = {
        "temperature": 0.8,
    }
    
    logging.info("Prepared data for model: %s", data)

    try:
        response = ollama.chat(model='llava:13b', messages=data, options=options)
        logging.info("Received response from model")
        return response['message']['content']
    except Exception as e:
        logging.error(f"Ошибка при работе с моделью: {e}")
        return "Произошла ошибка при обработке запроса. Пожалуйста, попробуйте еще раз."
