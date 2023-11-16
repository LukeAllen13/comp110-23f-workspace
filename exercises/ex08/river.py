"""File to define River class"""
__author__ = "730704135"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class to create a River."""
    day: int
    fish: list[Fish]
    bears: list[Bear]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """check ages."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]
        return None

    def bears_eating(self):
        """bears eating."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """check hunger."""
        Healthy_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                pass
            else:
                Healthy_bears.append(bear)
        self.bears = Healthy_bears
        return None
    
    def check_hunger(self):
        """check hunger."""
        healthy_bears = [bear for bear in self.bears if bear.hunger_score >= 0]
        self.bears = healthy_bears
        return None
        
    def repopulate_fish(self):
        """repopulate the fish."""
        born_fish = []
        for i in range(0, len(self.fish), 2):
            if i + 1 < len(self.fish):
                for _ in range(4):
                    offspring = Fish()
                    born_fish.append(offspring)
        self.fish.extend(born_fish)
        return None
    
    def repopulate_bears(self):
        """repopulate the bears."""
        born_bears = []
        for i in range(0, len(self.bears), 2):
            if i + 1 < len(self.bears):
                offspring = Bear()
                born_bears.append(offspring)
        self.bears.extend(born_bears)
        return None
    
    def view_river(self) -> None:
        """view the river."""
        print(f"~~~ Day {self.day}: ~~~")
        if self.bears == []:
            len(self.bears) == 0
        if self.fish == []:
            len(self.fish) == 0
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None

    def one_river_week(self):
        """Call river day."""
        i: int = 1
        while i < 8:
            self.one_river_day()
            i += 1
        return None
    
    def remove_fish(self, amount: int):
        """Remove fish."""
        i: int = 0
        while i < amount and self.fish:
            self.fish.pop(0)
            i += 1
        return None