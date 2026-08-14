# Smart Healthcare Diagnosis System
# Using basic First-Order Logic concepts

# -------------------------------
# 1. Knowledge Base
# -------------------------------

facts = {
    ("fever", "Ravi"),
    ("cough", "Ravi"),
    ("body_pain", "Ravi")
}

rules = [
    # If fever and cough -> flu
    (("fever", "cough"), "flu"),

    # If flu and body pain -> viral infection
    (("flu", "body_pain"), "viral_infection"),

    # If viral infection -> advise test
    (("viral_infection",), "advise_test")
]


# -------------------------------
# 2. Unification
# -------------------------------

def unify(fact1, fact2):
    """
    Simple unification for predicates.
    Example:
    fever(x) with fever(Ravi)
    gives x = Ravi
    """

    if fact1[0] == fact2[0]:
        return {"x": fact2[1]}
    return None


print("=== UNIFICATION ===")

result = unify(("fever", "x"), ("fever", "Ravi"))

if result:
    print("Fever(x) and Fever(Ravi) unify.")
    print("Substitution:", result)
else:
    print("Unification failed.")


# -------------------------------
# 3. Forward Chaining
# -------------------------------

def forward_chaining(facts, rules):

    facts = set(facts)

    changed = True

    while changed:
        changed = False

        for conditions, conclusion in rules:

            # Check whether all conditions are satisfied
            if all((condition, "Ravi") in facts
                   for condition in conditions):

                new_fact = (conclusion, "Ravi")

                if new_fact not in facts:
                    facts.add(new_fact)
                    changed = True

                    print(
                        "Rule applied:",
                        " AND ".join(conditions),
                        "->",
                        conclusion
                    )
                    print("New fact:", new_fact)

    return facts


print("\n=== FORWARD CHAINING ===")

final_facts = forward_chaining(facts, rules)

print("\nDerived Facts:")

for fact in final_facts:
    print(fact)


# -------------------------------
# 4. Backward Chaining
# -------------------------------

def backward_chaining(goal, facts, rules):

    # If goal is already a fact
    if goal in facts:
        return True

    # Search for a rule that concludes the goal
    for conditions, conclusion in rules:

        if conclusion == goal[0]:

            print(
                "Trying to prove:",
                goal
            )

            # Prove all conditions
            for condition in conditions:

                subgoal = (condition, goal[1])

                if not backward_chaining(
                    subgoal, facts, rules
                ):
                    return False

            return True

    return False


print("\n=== BACKWARD CHAINING ===")

query = ("advise_test", "Ravi")

if backward_chaining(query, facts, rules):
    print("Query proved:", query)
else:
    print("Query cannot be proved:", query)


# -------------------------------
# 5. Resolution-style Proof
# -------------------------------

print("\n=== RESOLUTION ===")

query = ("viral_infection", "Ravi")

print("Query:", query)
print("Assume the opposite: NOT viral_infection(Ravi)")

if query in final_facts:
    print("Derived:", query)
    print("Opposite assumption: NOT viral_infection(Ravi)")
    print("Contradiction found!")
    print("Therefore, viral_infection(Ravi) is TRUE.")
else:
    print("Query cannot be proved.")


# -------------------------------
# 6. Final Diagnosis
# -------------------------------

print("\n=== FINAL DIAGNOSIS ===")

if ("viral_infection", "Ravi") in final_facts:
    print("Ravi may have a viral infection.")
    print("Ravi should be advised to take a test.")
else:
    print("No viral infection detected.")
