import requests
import img2pdf


def image_gen():
    headers ={
        'Accept-Ranges': "bytes",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/126.0.0.0 Mobile Safari/537.36'
    }

    img_list = []
    for i in range(1, 49):
        url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f'data/{i}.jpg', 'wb') as file:
            file.write(response)
            img_list.append(f'data/{i}.jpg')
            print(f'Картинка #{i} записана.')

    print('#' * 20)

    with open('catalog.pdf', 'wb') as f:
        f.write(img2pdf.convert(img_list))
        print('Каталог готов')


def main():
    image_gen()


if __name__ == '__main__':
    main()


