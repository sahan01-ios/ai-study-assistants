from agent import Agent

agent = Agent()

test_cases = [
    "calculate 2+2",
    "calculate 10/2",
    "calculate abc",
    "What is Python?",
    "Explain algorithm",
    "What is a loop?",
    ""
]

for test in test_cases:

    print(f"Input: {test}")

    print("Output:", agent.run(test))

    print("-" * 40)
