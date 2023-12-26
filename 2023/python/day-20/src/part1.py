from dotenv import load_dotenv
from collections import deque
import os
import re

load_dotenv()
filename = os.getenv('TEXTS_PATH')+'day-20.txt'
with open(filename, 'r') as file:
    data = file.read()

pulses = []
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


def part1(data: str):
    regex = r"broadcaster -> (?P<broadcaster>.*)|%(?P<flipflop>\w+) -> (?P<flipflop_next>.*)|&(?P<conjuction>\w+) -> (?P<conjuction_next>.*)"

    # Add & to all those words preceeded by & that later didn't have it
    words_with_ampersand = re.findall(r'&(\w+)', data)
    for word in words_with_ampersand:
        data = re.sub(rf"(?<!&)\b{word}\b", f"&{word}", data)
    matches = re.finditer(regex, data)

    broadcaster: list[FlipFlop] = []
    flipflops: dict[str:FlipFlop] = {}
    conjunctions: dict[str:Conjunction] = {}

    for match in matches:
        if match.group('broadcaster'):
            broadcaster.extend(match.group('broadcaster').split(', '))
        elif (id := match.group('flipflop')):
            # Create new instance if it doesn't exist
            if id not in flipflops:
                flipflops[id] = FlipFlop(id)
            for next_id in match.group('flipflop_next').split(', '):
                if next_id.startswith('&'):
                    next_id = next_id[1:]  # Remove &
                    # Create the conjuction if it doesn't exist
                    if next_id not in conjunctions:
                        conjunctions[next_id] = Conjunction(next_id)
                    # Add it to the next_modules list of the current flipflop
                    flipflops[id].next_modules.append(conjunctions[next_id])
                    # Also add current flipflop as a module to the conjunction
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
                    # Also add self as a module to the next_modules
                    conjunctions[next_id].input_states.update({id: 0})
                # Flipflop
                else:
                    if next_id not in flipflops:
                        flipflops[next_id] = FlipFlop(next_id)
                    conjunctions[id].next_modules.append(flipflops[next_id])

    push_button = 1000
    for _ in range(push_button):
        pulses.append(0)
        for id in broadcaster:
            queue.append(["Broadcaster", flipflops[id], 0])

        while queue:
            sender, receiver, pulse = queue.popleft()
            # print(f"\n{sender} sending pulse {pulse} to {receiver}")
            pulses.append(pulse)
            receiver.receive_pulse(sender, pulse)

    res = pulses.count(0)*pulses.count(1)
    pulses.clear()  # So the second test can work since they share pulses array

    return res


if __name__ == "__main__":
    print(part1(data))  # 841763884
