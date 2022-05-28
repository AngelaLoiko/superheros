import requests
base_url = "https://superheroapi.com/api/"
TOKEN = ''
the_most_intelligent_hero = ''
super_heroes = ['Hulk', 'Captain America', 'Thanos']

class Hero:
    def __init__(self, name, hero_name, id=0, intelligence=0, base_url=base_url, token = TOKEN):
        self.name = name
        self.hero_name = hero_name
        self.id = id
        self.intelligence = intelligence
        # self.pretty_print_name()
        self.getintelligence(token=TOKEN)
    
    def pretty_print_name(self):
        print("This object's name is {}.".format(self.name))
        print("This object's heroname is {}.".format(self.hero_name))
    
    def getintelligence(self, base_url=base_url, token=TOKEN):
        # url = "https://superheroapi.com/api/2619421814940190/search/" + self.hero_name
        url = f'{base_url}{token}/search/{self.hero_name}'
        response = requests.get(url)
        for result in response.json()['results']:         
            if result['name'] == f'{self.hero_name}':
            #  self.id = result['id']
             self.intelligence= result['powerstats']['intelligence']
            else:
               break
        return self.intelligence

    def __str__(self):
        result = f'имя {self.hero_name}, ум {self.intelligence}'
        return result


if __name__ == '__main__':   
    heroes = []
    hero_objects = {}
    for i in range(len(super_heroes)):
        objectname=f'hero_{i}'
        namename=super_heroes[i]
        hero_objects[namename] = hero_objects.get(namename, Hero(name = objectname, hero_name=namename ))
    max_int = 0
    name_h=''
    for key, value in hero_objects.items():
        if int(value.intelligence) > max_int:
           max_int = int(value.intelligence)
           name_h = value.hero_name
        print(value)
    print(f'Среди {super_heroes} самый умный {name_h}') 