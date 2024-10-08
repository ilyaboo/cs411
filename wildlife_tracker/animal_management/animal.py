from typing import Any, Optional

class Animal:

    def __init__(self, animal_id: int, species: str, health_status: Optional[str] = None) -> None:
        self.animal_id: int
        self.species: str
        self.health_status: Optional[str] = None




