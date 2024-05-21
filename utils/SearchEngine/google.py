import logging
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_data_from_google(query, num_results=5):
    """
    Выполняет поиск в Google, извлекает текст из первых результатов и возвращает результаты.

    :param query: Строка запроса для поиска.
    :param num_results: Количество результатов для обработки.
    :return: Словарь с URL и извлеченным текстом.
    """
    logging.info(f"Выполнение поиска по запросу: {query}")
    results = []
    try:
        search_google = search(query, lang="ru", stop=num_results)
        search_results = list(search_google)
        logging.info(f"Найдено {len(search_results)} результатов.")
    except Exception as e:
        logging.error(f"Ошибка при выполнении поиска: {e}")
        return {"links": [], "text": ""}

    search_results = search_results[:num_results]
    logging.info(f"Будет обработано {len(search_results)} результатов.")

    for result in search_results:
        logging.info(f"Обработка результата: {result}")
        try:
            response = requests.get(result, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Извлекаем текст из всех тегов <p>
                paragraphs = soup.find_all('p')
                page_text = ' '.join([para.get_text() for para in paragraphs])
                results.append({
                    'url': result,
                    'text': page_text
                })
                logging.info(f"Текст успешно извлечен из: {result}")
            else:
                logging.warning(f"Не удалось получить данные с {result}. Статус-код: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Ошибка при получении данных с {result}: {e}")

    # Формируем итоговый текст и список ссылок
    text = ""
    links = []

    for result in results:
        links.append(result["url"])
        text += "\n"
        text += result["text"]

    logging.info("Формирование итогового текста и списка ссылок завершено.")
    return {
        "links": links,
        "text": text
    }

# Пример использования:
if __name__ == "__main__":
    query = 'курица'
    result = get_data_from_google(query)
    print(result)
