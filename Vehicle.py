class Vehicle:

    hydro_facility = "Hydro Karmøy"

    def __init__(self, vehicle_id ="Pallet Truck #100", current_area = "ASU", direction_vector = [0 ,0]):
        self.vehicle_id = vehicle_id
        self.current_area = current_area
        self.direction_vector = direction_vector

    def __str__(self):
        return "Vehicle: " + (self.vehicle_id)

    def get_hydro_facility(self):
        return self.vehicle_id + " at " + self.hydro_facility + " " + self.current_area

    def set_direction_vector(self, direction_vector):
        self.direction_vector = direction_vector