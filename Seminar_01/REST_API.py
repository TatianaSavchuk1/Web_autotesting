# Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
#
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
# с передачей параметров title, description, content.

import requests as requests
import yaml

with open ('config.yaml', 'r') as f:
    conf = yaml.safe_load(f)


def get_token():
    response = requests.post(url = conf['url_get'], data = {'username':conf['username'], 'password':conf['password']})
    return response.json()['token']


def get(token):
    resource = requests.get(conf["url_post"],
               headers={"X-Auth-Token": token},
               params={"owner": "notMe"})
    return resource.json()



def get_1(token):
    resource = requests.get(conf["url_post"],
               headers={"X-Auth-Token": token},
               params={"description": conf['description']})
    return resource.json()



def create_post(token, title, description, content):
    param = {'title':title, 'description':description, 'content':content}
    new_post = requests.post(conf['url_post'], headers={"X-Auth-Token": token}, params = {"owner": "Me"},
                             data=param)
    return new_post.json()



if __name__ == '__main__':
    temp = get_token()
    print(get(temp))
    print (create_post(get_token(), 'test title', 'test description', 'test content'))
