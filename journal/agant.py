from tools.search_tool import search
from tools.calculator import calculate


class Agent:
    def run(self, query):
        query = query.lower()

        # Empty input validation
        if not query.strip():
            return "Please enter a valid question."

        # Calculator tool
        if "calculate" in query:
            return calculate(query)

        # Search tool
        return search(query)
