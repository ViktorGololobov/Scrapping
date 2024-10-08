import csv

from bs4 import BeautifulSoup
import requests


for i in range(1, 6):
    url = 'https://redheadsound.studio/serialy/page/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/126.0.0.0 Mobile Safari/537.36"
    }
    req = requests.get(url + f'{i}/', headers)

    with open('serials.html', 'w', encoding='utf8') as file:
        file.write(req.text)

    with open('serials.html', 'r', encoding='utf8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    articles = soup.find_all('article', class_='card d-flex')
    category_list = []

    for article in articles:
        serial_title = article.find('h2', class_='card__title').find('a')
        serial_urls = []

        for titles in serial_title:
            serial_link = serial_title.get('href')
            serial_urls.append(serial_link)

        for url in serial_urls:
            req = requests.get(url, headers=headers)
            serial_name = url.split('/')[-1][:-5]

            with open(f'data/{serial_name}.html', 'w', encoding='utf8') as file:
                file.write(req.text)

            with open(f'data/{serial_name}.html', 'r', encoding='utf8') as file:
                src = file.read()

            soup = BeautifulSoup(src, 'lxml')
            project_data = soup.find('div', class_='page__subcol-main flex-grow-1 d-flex fd-column').find_all('li')

            for data in project_data:
                category = data.find('div').text
                if category not in category_list and 'перевод' not in category:
                    category_list.append(category)


            #вытягиваем названия столбцов для csv файла и записываем их
            name = category_list[0]
            year = category_list[1]
            country = category_list[2].title()
            season = category_list[3]
            episodes = category_list[4]
            duration = category_list[5]
            studio = category_list[6]
            director = category_list[7]

            # with open('all-serials.csv', 'w', encoding='cp1251') as file:
            #     writer = csv.writer(file, delimiter=';')
            #     writer.writerow(
            #         (
            #             name,
            #             year,
            #             country,
            #             season,
            #             episodes,
            #             duration,
            #             studio,
            #             director
            #         )
            #     )

            count = 0
            items_list = []
            for item in project_data:
                if 'перевод' not in item.text:
                    items_list.append(item.text.strip().replace('\n', ''))
                    count += 1
                    if count == 8:
                        title = items_list[0][len(name):]
                        year = items_list[1][len(year):]
                        country = items_list[2][len(country):]
                        season = items_list[3][len(season):]
                        episodes = items_list[4][len(episodes):]
                        duration = items_list[5][len(duration):]
                        studio = items_list[6][len(studio):]
                        director = items_list[7][len(director):]
                        print(items_list)

                        with open('all-serials.csv', 'a', encoding='cp1251') as file:
                            writer = csv.writer(file, delimiter=';', lineterminator='\n')
                            writer.writerow(
                                (
                                    title,
                                    year,
                                    country,
                                    season,
                                    episodes,
                                    duration,
                                    studio,
                                    director
                                )
                            )




