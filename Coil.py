class Coil:

    hydro_facility = "Hydro Karmoy"

    def __init__(self, coil_id, current_storage = "ASU"):
        self.coil_id = coil_id
        self.current_storage = current_storage

    def __str__(self):
        return "Coil: " + (self.coil_id)

    def get_hydro_facility(self):
        return self.coil_id + " at " + self.hydro_facility + " " + self.current_storage