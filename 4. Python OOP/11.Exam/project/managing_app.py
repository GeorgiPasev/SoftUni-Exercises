from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."
        
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."
        
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."
        
        if vehicle_type == "PassengerCar":
            new_vehicle = PassengerCar(brand, model, license_plate_number)
        else:
            new_vehicle = CargoVan(brand, model, license_plate_number)
        
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1
        the_new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(the_new_route)

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = next((c for c in self.users if c.driving_license_number == driving_license_number), None)
        
        if user is None:
            raise ValueError(f"User {driving_license_number} is not registered in the platform!")
        
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        
        vehicle = next((c for c in self.vehicles if c.license_plate_number == license_plate_number), None)
        if vehicle is None:
            raise ValueError(f"Vehicle {license_plate_number} is not registered in the platform!")
        
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        
        route = next((c for c in self.routes if c.route_id == route_id), None)
        if route is None:
            raise ValueError(f"Route {route_id} is not registered in the platform!")
        
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."
        
        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()
        
        status = "OK" if not vehicle.is_damaged else "Damaged"
        return f"{vehicle.brand} {vehicle.model} License plate: {vehicle.license_plate_number} Battery: {vehicle.battery_level}% Status: {status}"
    
    def repair_vehicles(self, count: int):

        damaged_vehicles = [c for c in self.vehicles if c.is_damaged]
        damaged_vehicles.sort(key=lambda b: (b.brand, b.model))
        repaired_vehicles = damaged_vehicles[:count] if count > 0 else damaged_vehicles

        for c in repaired_vehicles:
            c.change_status()
            c.recharge()
        return f"{len(repaired_vehicles)} vehicles were successfully repaired!"

    def users_report(self):

        sorted_users = sorted(self.users, key=lambda b: b.rating, reverse=True)
        user_strings = [str(u) for u in sorted_users]
        report = "*** E-Drive-Rent ***\n" + "\n".join(user_strings)
        
        return report
