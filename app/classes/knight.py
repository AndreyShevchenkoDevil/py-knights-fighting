class Knight:
    def __init__(self, knight: dict):
        self.name = knight['name']
        self.power = knight['power']
        self.hp = knight['hp']
        self.armour = knight['armour']
        self.weapon = knight['weapon']
        self.potion = knight['potion']
        self.protection = 0

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_armour(self) -> None:
        for a in self.armour:
            self.protection += a["protection"]

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def full_equip(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion_if_exist()