def get_food_words():
    food_words = {}
   
   
    """ Universal Indicator """
    
    food_words['general'] = list(['meal', 'meals', 'food', 'foods', 'dinner', 'lunch', 'breakfast'])
  
    """Meat"""
    
    food_words['beef'] = list(['beef', 'cattle', 'boeuf', 'oxen', 'kine', 'steak', 'cow', 'brisket', 'veal', 'tenderloin', 'sirloin'])
    food_words['lamb'] = list(['lamb', 'sheep'])
    food_words['pork'] = list(['pork', 'swine', 'ham', 'bacon','chorizo', 'salami', 'pig'])
    food_words['chicken'] = list(['chicken', 'poultry', 'poulet', 'volaille'])
    food_words['meat'] = list(['meat', 'saussage', 'rib', 'goat', 'pastrami', 'kidney', 'liver', 
                               'pork', 'swine', 'ham', 'bacon','chorizo', 'salami','lamb', 'sheep', 
                               'beef', 'cattle', 'boeuf', 'oxen', 'kine', 'steak', 'cow', 'brisket', 'veal', 'tenderloin', 'sirloin', 'pig',
                               'chicken', 'poultry', 'poulet', 'volaille'])
    
    
    """ Cereals """
    
    food_words['rice'] = list(['rice'])
    food_words['wheat'] = list(['wheat', 'bread', 'flour', 'atta', 'gluten', 'starch', 'farina', 'bran','pasta', 'nuddle', 'ravioli', 'beer', 'scotch', 'barley']) 
    food_words['corn'] = list(['corn', 'maize', 'whisky', 'oat', 'ethanol', 'biofuel']) 
    food_words['cereals'] = list(['wheat', 'bread', 'flour', 'atta', 'gluten', 'starch', 'farina', 'bran','pasta', 'nuddle', 'ravioli', 'beer', 'scotch', 'barley' 
                                  , 'corn', 'maize', 'whisky', 'oat', 'ethanol', 'biofuel', 'rice'])
    
    
    
    """ Oil """
    
    food_words['oil_plant'] = list(['coconut oil', 'corn oil', 'olive oil', 'palm oil','peanut oil', 'sunflower oil', 'rapeseed oil', 'safflower oil','soybean oil', 'sunflower oil', 'soybeans', 'soya', 'soy sauce', 'soja' ])
    food_words['soy'] = list([ 'soybeans', 'soya', 'soy sauce', 'soja'])
    
    
    """Sugar"""
    
    food_words['sugar'] = list(['sugar', 'syrup', 'gatorade', 'cola', 'sugarcane','cookie', 'chocolate', 'nestle'])
   
    """Dairy"""
    
    food_words['egg'] = list(['egg'])
    food_words['milk'] = list(['milk']) 
    food_words['dairy'] = list(['dairy', 'egg', 'milk', 'SMP', 'WMP' 'chese', 'kefir','cream', 'butter', 'yogurt', 'quark', 
                                'mozzarella', 'cheddar', 'parmesan', 'buttermilk', 'ricotta', 'feta', 'romano', 'provolone', 'colby', 'edam', 'eggnog','pimento', 'cheshire', 'roquefort'])
    
   
    
    """Other food of interest"""
    
    food_words['tea'] = list(['tea'])
    food_words['coffee'] = list(['coffee'])
    food_words['fish'] = list(['fish', 'carp', 'catfish', 'prawn', 'seafood', 'salmon', 'oyster', 'sardine', 'herring'])
    food_words['salt'] = list(['salt']) 
    food_words['potato'] = list(['potato', 'potatos', 'tater', 'spud'])
    food_words['coca'] = list(['coca'])

    

    return food_words


def getFoodWordList():
    l = get_food_words().values()
    return [item for sublist in l for item in sublist]

def getFoodCatList():
    return get_food_words().keys()

def print_foods():
    foods = get_food_words()
    for food in foods.keys():
        print(foods[food])