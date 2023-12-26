from dotenv import load_dotenv
from collections import deque
import math
import os
import re

# Load environment variables
load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-20.txt'
with open(filename, 'r') as file:
    data = file.read()

# Queue for processing events in order
queue = deque()


class FlipFlop():
    def __init__(self, module_id: str) -> None:
        self.state = 0
        self.id = module_id
        self.next_modules = []

    def __repr__(self) -> str:
        return f"<FlipFlop id:{self.id} state:{self.state}>"

    def receive_pulse(self, sender: str, pulse: int) -> None:
        # print(f"{self.id} receiving {pulse} from {sender}")
        if not pulse:
            self.state ^= 1
            self.send_pulse(self.state)

    def send_pulse(self, pulse: int) -> None:
        for receiver in self.next_modules:
            queue.append((self.id, receiver, pulse))


class Conjunction():
    def __init__(self, module_id: str) -> None:
        self.state = 0
        self.id = module_id
        self.next_modules = []
        self.input_states = {}

    def __repr__(self) -> str:
        return f"<Conjunction id:{self.id} state:{self.state}/{len(self.input_states)}>"

    def receive_pulse(self, sender: str, pulse: int) -> None:
        # print(f"{self.id} receiving {pulse} from {sender}")
        self.input_states[sender] = pulse
        self.state = sum(self.input_states.values())

        if self.state == len(self.input_states):
            self.send_pulse(0)
        else:
            self.send_pulse(1)

    def send_pulse(self, pulse: int) -> None:
        for receiver in self.next_modules:
            queue.append((self.id, receiver, pulse))


def parse_data(data: str):
    regex = r"broadcaster -> (?P<broadcaster>.*)|%(?P<flipflop>\w+) -> (?P<flipflop_next>.*)|&(?P<conjuction>\w+) -> (?P<conjuction_next>.*)"
    words_with_ampersand = re.findall(r'&(\w+)', data)
    for word in words_with_ampersand:
        data = re.sub(rf"(?<!&)\b{word}\b", f"&{word}", data)

    flipflops = {}
    conjunctions = {}
    broadcasters = []

    for match in re.finditer(regex, data):
        if match.group('broadcaster'):
            broadcasters.extend(match.group('broadcaster').split(', '))
        if (id := match.group('flipflop')):
            # Create new instance if it doesn't exist
            if id not in flipflops:
                flipflops[id] = FlipFlop(id)
            for next_id in match.group('flipflop_next').split(', '):
                if next_id.startswith('&'):
                    next_id = next_id[1:]  # Remove &
                    # Create the conjuction if it doesn't exist
                    if next_id not in conjunctions:
                        conjunctions[next_id] = Conjunction(next_id)
                    # Add it to the next list of the current flipflop
                    flipflops[id].next_modules.append(conjunctions[next_id])
                    # Also add current flipflop as a module to the Conjunction
                    conjunctions[next_id].input_states.update({id: 0})
                # Flipflop
                else:
                    if next_id not in flipflops:
                        flipflops[next_id] = FlipFlop(next_id)
                    flipflops[id].next_modules.append(flipflops[next_id])

        elif (id := match.group('conjuction')):
            # Create new instance if it doesn't exist
            if id not in conjunctions:
                conjunctions[id] = Conjunction(id)
            for next_id in match.group('conjuction_next').split(', '):
                # Conjunction
                if next_id.startswith('&'):
                    next_id = next_id[1:]
                    if next_id not in conjunctions:
                        conjunctions[next_id] = Conjunction(next_id)
                    conjunctions[id].next_modules.append(conjunctions[next_id])
                    # Also add self as a module to the next
                    conjunctions[next_id].input_states.update({id: 0})
                # Flipflop
                else:
                    if next_id not in flipflops:
                        flipflops[next_id] = FlipFlop(next_id)
                    conjunctions[id].next_modules.append(flipflops[next_id])

    return broadcasters, flipflops, conjunctions


def simulate_network(broadcasters: list, flipflops: dict, conjunctions: dict):
    # Find the conjunction that leads to 'rx'
    (final_conjunction,) = [
        c.id for c in conjunctions.values() if c.next_modules[0].id == 'rx']

    button_presses = 0
    cycles = {}
    # Don't stop until all the cycles have been found
    while len(cycles) < 4:
        for id in broadcasters:
            queue.append(("Broadcaster", flipflops[id], 0))
        button_presses += 1

        while queue:
            sender, receiver, pulse = queue.popleft()
            # If we're sending 1 to final conjunction we found a cycle
            if pulse and receiver.id == final_conjunction:
                cycles[sender] = button_presses

            # print(f"\n{sender} sending pulse {pulse} to {receiver}")
            receiver.receive_pulse(sender, pulse)

    return math.lcm(*cycles.values())


def part2(data: str):
    broadcasters, flipflops, conjunctions = parse_data(data)
    return simulate_network(broadcasters, flipflops, conjunctions)


if __name__ == "__main__":
    print(part2(data))  # 246006621493687
