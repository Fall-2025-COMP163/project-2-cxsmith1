import random

# =====================================================================
# BASE CLASS
# =====================================================================
class Character:
    def __init__(self, name, health, strength, magic):
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic

    def attack(self, target):
        """Base attack uses strength for damage."""
        print(f"{self.name} attacks {target.name} for {self.strength} damage!")
        target.take_damage(self.strength)

    def take_damage(self, damage):
        """Reduce health but not below 0."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def display_stats(self):
        """Show basic character info."""
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Magic: {self.magic}")

# =====================================================================
# PLAYER CLASS (inherits from Character)
# =====================================================================
class Player(Character):
    def __init__(self, name, character_class, health, strength, magic):
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.xp = 0

    def display_stats(self):
        """Override Character's display_stats to add more info."""
        super().display_stats()
        print(f"Class: {self.character_class}")
        print(f"Level: {self.level}")
        print(f"XP: {self.xp}")

# =====================================================================
# WARRIOR CLASS
# =====================================================================
class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)

    def attack(self, target):
        """Warriors use extra physical strength."""
        damage = self.strength + 5
        print(f"{self.name} slashes {target.name} for {damage} damage!")
        target.take_damage(damage)

    def super_slash(self, target):
        """Warrior special move: extra-heavy slash."""
        damage = self.strength + 15
        print(f"{self.name} uses Super Slash on {target.name} for {damage} damage!")
        target.take_damage(damage)

# =====================================================================
# MAGE CLASS
# =====================================================================
class Mage(Player):
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)

    def attack(self, target):
        """Mages attack using magic instead of strength."""
        damage = self.magic
        print(f"{self.name} casts a spell on {target.name} for {damage} damage!")
        target.take_damage(damage)

    def spirit_nuke(self, target):
        """Mage special ability: super magic attack."""
        damage = self.magic + 10
        print(f"{self.name} launches a Spirit Nuke at {target.name} for {damage} damage!")
        target.take_damage(damage)

# =====================================================================
# ROGUE CLASS
# =====================================================================
class Rogue(Player):
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)

    def attack(self, target):
        """Rogue has a chance for a critical hit."""
        crit = random.randint(1, 10)
        if crit <= 3:
            damage = self.strength * 2
            print(f"{self.name} lands a CRITICAL hit on {target.name} for {damage} damage!")
        else:
            damage = self.strength
            print(f"{self.name} stabs {target.name} for {damage} damage!")
        target.take_damage(damage)

    def eye_poke(self, target):
        """Rogue special: guaranteed critical hit."""
        damage = self.strength * 2
        print(f"{self.name} pokes {target.name}'s eyes for {damage} damage!")
        target.take_damage(damage)

# =====================================================================
# WEAPON CLASS (composition)
# =====================================================================
class Weapon:
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus

    def display_info(self):
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")

# =====================================================================
# SIMPLE BATTLE SYSTEM
# =====================================================================
class SimpleBattle:
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2

    def fight(self):
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()

        print(f"\n--- Round 1 ---")
        self.char1.attack(self.char2)
        if self.char2.health > 0:
            self.char2.attack(self.char1)

        print(f"\n--- Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        if self.char1.health > self.char2.health:
            print(f"{self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"{self.char2.name} wins!")
        else:
            print("It's a tie!")

# =====================================================================
# TEST (optional)
# =====================================================================
if __name__ == "__main__":
    warrior = Warrior("Zygor")
    mage = Mage("Parlay")
    rogue = Rogue("LeBomb Stanks")
    dummy = Character("Dummy", 100, 0, 0)

    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()

    print("\n⚔️ Testing Polymorphism:")
    for c in [warrior, mage, rogue]:
        c.attack(dummy)
        dummy.health = 100

    print("\n✨ Special Abilities:")
    warrior.super_slash(dummy)
    mage.spirit_nuke(dummy)
    rogue.eye_poke(dummy)

    print("\n🗡️ Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    sword.display_info()

    print("\n⚔️ Battle System Test:")
    SimpleBattle(warrior, mage).fight()
