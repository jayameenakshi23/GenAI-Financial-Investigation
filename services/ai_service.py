import ollama

def investigate_transaction(transaction):

    prompt = f"""
You are a Senior Financial Fraud Investigator.

Analyze this banking transaction.

Transaction:
{transaction}

Return ONLY in this exact format.

Risk Level:
(High / Medium / Low)

Summary:
(One sentence)

Reasons:
- Reason 1
- Reason 2
- Reason 3

Recommendation:
- Recommendation 1
- Recommendation 2
- Recommendation 3
"""

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]