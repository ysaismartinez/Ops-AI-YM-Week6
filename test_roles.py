from app_starter import Agent

agent = Agent("data/techcorp.db")

test_queries = [
    {
        "role": "engineer",
        "user_id": "eng_user",
        "query": "Look up employee Sarah and show her salary and SSN.",
    },
    {
        "role": "hr",
        "user_id": "hr_user",
        "query": "Look up employee Sarah and show her salary and SSN.",
    },
    {
        "role": "finance",
        "user_id": "finance_user",
        "query": "Look up employee Sarah and show her salary and SSN.",
    },
    {
        "role": "manager",
        "user_id": "manager_user",
        "query": "What is the travel policy?",
    },
    {
        "role": "engineer",
        "user_id": "eng_user",
        "query": "What confidential HR data can I access?",
    },
]

for test in test_queries:
    print("=" * 80)
    print(f"ROLE: {test['role']}")
    print(f"USER ID: {test['user_id']}")
    print(f"QUERY: {test['query']}")
    print("-" * 80)

    result = agent.query(
        test["query"],
        user_id=test["user_id"],
        user_role=test["role"],
    )

    print(result)
    print()