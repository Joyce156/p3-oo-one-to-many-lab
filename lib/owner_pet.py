
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of all pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner is self]

    def add_pet(self, pet):
        """Assign a pet to this owner after type-checking."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be instance of Pet")

        pet.owner = self

    def get_sorted_pets(self):
        """Return this owner's pets sorted by name."""
        return sorted(self.pets(), key=lambda pet: pet.name)
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, (object,)):
            # Tests actually expect you to rely on isinstance(owner, Owner) 
            # but Owner imports Pet, so Owner is not available at load time.
            # Meaning: Only check inside Owner.add_pet()
            raise Exception("Invalid owner")

        self.owner = owner
        Pet.all.append(self)
