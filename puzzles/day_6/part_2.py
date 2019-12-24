
    def get_ancestors(self, node: str) -> List[str]:
        if node not in self.nodes:
            return []

        ancestor = self.nodes[node]
        return [ancestor] + self.get_ancestors(ancestor)

    def transfers_required(self, node, other_node):
        pass