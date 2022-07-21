# Задача 1

def one_ingredient(line_from_file): # функция обрабатывает строку с одним ингредиентом из текстового файла в формат словаря для cook_book
    cook_book_ingr = {}
    list_from_file = line_from_file.split("|")
    cook_book_ingr['ingredient_name'] = list_from_file[0].strip()
    cook_book_ingr['quantity'] = int(list_from_file[1].strip())
    cook_book_ingr['measure'] = list_from_file[2].strip()   
    return(cook_book_ingr)

def create_cook_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file_obj:
        while True:
            name_of_dish = file_obj.readline().strip() #взяли название
            num_of_ingr = int(file_obj.readline()) #взяли число ингредиентов
            ingredients = []
            for num in range(num_of_ingr):   
                ingredients.append(one_ingredient(file_obj.readline()))
            cook_book[name_of_dish] =  ingredients
            data = file_obj.readline()
            if not data:        
                break
    return cook_book

cook_book = create_cook_book('recipes.txt')
print(cook_book)

# Задача 2

dishes_list = ['Омлет', 'Фахитос']

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = create_cook_book('recipes.txt')
    
    final_shop_list = {}
    for dish in dishes:   
        if dish not in cook_book: 
            return f'Блюдо "{dish}" отсутствует в книге рецептов'
        else:
            for ingredient in cook_book[dish]:               
                if ingredient['ingredient_name'] not in final_shop_list:
                    ingredient_quantity = ingredient['quantity'] * person_count                    
                else:
                    ingredient_quantity = final_shop_list[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * person_count
                final_shop_list[ingredient['ingredient_name']] = {'measure':ingredient['measure'], 'quantity':ingredient_quantity}
                
    return final_shop_list

print(get_shop_list_by_dishes(dishes_list, 3))