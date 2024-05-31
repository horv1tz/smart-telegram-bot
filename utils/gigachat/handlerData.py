from gigachat import GigaChat

# Инициализация клиента с вашим API ключом
giga = GigaChat(access_token=KEY, verify_ssl_certs=False)

def handle_data_by_gigachat(query, search):
    # Пример запроса к GigaChat
    prompt = "Ты умный помощник Дворф.\n Ты должен максимально точно отвечать на вопрос:\n"
    query_chat = f"Запрос пользователя: {query} \n"
    search_chat = f"Поиск в поисковике: {search}"

    response_text = prompt + query_chat + search_chat
    response = giga.chat(response_text)
    return response.choices[0].message.content

