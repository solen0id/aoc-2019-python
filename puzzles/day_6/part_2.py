from typing import List, Optional
from pathlib import Path


class Graph:
    def __init__(self, nodes: Optional[dict] = None):
        self.nodes = nodes if nodes else {}

    def add_node_pair(self, node: str, other_node: str) -> None:
        self.nodes[node] = other_node

    def count_orbits(self, node: str) -> int:
        if node not in self.nodes:
            return 0

        return 1 + self.count_orbits(self.nodes[node])

    def count_all_orbits(self) -> int:
        return sum(self.count_orbits(node) for node in self.nodes)

    def get_ancestors(self, node: str) -> List[str]:
        if node not in self.nodes:
            return []

        ancestor = self.nodes[node]
        return [ancestor] + self.get_ancestors(ancestor)

    def transfers_required(self, node, other_node):
        pass

    @classmethod
    def from_file(cls, filepath: str) -> "Graph":
        graph = cls()
        node_pairs = Path(filepath).read_text().split()

        for node_pair in node_pairs:
            center, orbitter = node_pair.split(")")
            graph.add_node_pair(orbitter, center)

        return graph


def run_tests():
    graph = Graph.from_file("/home/max/Projects/aoc-2019-python/puzzles/day_6/test.txt")
    orbit_count = graph.count_all_orbits()

    print(orbit_count)


def run():
    graph = Graph.from_file(
        "/home/max/Projects/aoc-2019-python/puzzles/day_6/input.txt"
    )
    orbit_count = graph.count_all_orbits()

    print(orbit_count)


if __name__ == "__main__":
    run_tests()
    run()

