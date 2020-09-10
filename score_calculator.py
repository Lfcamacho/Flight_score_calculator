class Score:
    def __init__(self, balls, payload, wingspan, cargo_bay_length):
        self.balls = balls
        self.payload = payload
        self.wingspan = wingspan
        self.cargo_bay_length = cargo_bay_length

    def calculate_score(self):
        flight_score = 120 * ((2 * self.balls + self.payload)/(self.wingspan + self.cargo_bay_length))
        return flight_score


class Element:
    def _init_(min, max, gap):
        self.min = min
        self.max = max
        self.gap = gap

    
balls = Element(min_balls, max_balls, gap_balls)
payload = Element(min_payload, max_payload, gap_payload)
wingspan = Element(min_wingspan, max_wingspan, gap_wingspan)
cargo_bay = Element(min_cargo_bay, max_cargo_bay, gap_cargo_bay)

elements = [balls, payload, wingspan, cargo_bay]
