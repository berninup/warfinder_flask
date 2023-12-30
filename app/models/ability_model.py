import re
class Ability:
    '''Blueprint to create abilities'''    
    
    ABILITY_LEVELS = {
        'perk1' : 1,
        'perk2' : 2,
        'perk3' : 3,
        'flaw1' : -1,
        'flaw2' : -2,
        'flaw3' : -3,
    }
    
    ALT_STATS = {
    "strike": "sorcery",
    "sorcery": "strike",
    "armor": "warding",
    "warding": "armor"        
    }
            
    def __init__(self, name: str, description: str, level: str):
        
        if not name:
            raise ValueError("Namme cannont be empty")
        if not description:
            raise ValueError("Description cannont be empty")
        if level not in Ability.ABILITY_LEVELS:
            raise ValueError(f"Invalid level: {level}")
        self._name = name
        self._description = description
        self._level = level
        self.alt_name = ""
        self.alt_description= description
        self.create_alt_version()      
                
    @property
    def name(self):
        '''Name getter'''
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        '''Name setter'''
        if not new_name:
            raise ValueError("Name cannot be empty")
        self._name = new_name
        
    @property
    def description(self):
        '''Description getter'''
        return self._description
    
    @description.setter
    def description(self, new_description: str):
        '''Description setter'''
        if not new_description:
            raise ValueError("Description cannont be empty")
        self._description = new_description
        
    def create_alt_version(self):
            '''Creates an alternate ability if possible'''
            self.alt_description = re.sub(r'\b' + '|'.join(re.escape(key) for key in self.ALT_STATS.keys()) + r'\b', lambda m: self.ALT_STATS[m.group(0)], self.alt_description)
            self.alt_name = "Magical " + self._name