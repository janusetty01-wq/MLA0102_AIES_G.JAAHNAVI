# Smart Healthcare Diagnosis using Logic Reasoning

# -----------------------------
# Facts
# -----------------------------
facts = {
    "Fever(Ravi)",
    "Cough(Ravi)",
    "BodyPain(Ravi)"
}

print("Initial Facts:")
for fact in facts:
    print("-", fact)

# -----------------------------
# Rule 1: Fever AND Cough -> Flu
# -----------------------------
if "Fever(Ravi)" in facts and "Cough(Ravi)" in facts:
    facts.add("Flu(Ravi)")
    print("\nRule 1 Applied:")
    print("Fever(Ravi) AND Cough(Ravi) -> Flu(Ravi)")

# -----------------------------
# Rule 2: Flu AND BodyPain -> Viral
# -----------------------------
if "Flu(Ravi)" in facts and "BodyPain(Ravi)" in facts:
    facts.add("Viral(Ravi)")
    print("\nRule 2 Applied:")
    print("Flu(Ravi) AND BodyPain(Ravi) -> Viral(Ravi)")

# -----------------------------
# Rule 3: Viral -> Medical Attention
# -----------------------------
if "Viral(Ravi)" in facts:
    facts.add("MedicalAttention(Ravi)")
    print("\nRule 3 Applied:")
    print("Viral(Ravi) -> MedicalAttention(Ravi)")

# -----------------------------
# Final Results
# -----------------------------
print("\nFinal Knowledge Base:")
for fact in facts:
    print("-", fact)

# -----------------------------
# Conclusion
# -----------------------------
if "Viral(Ravi)" in facts:
    print("\nConclusion:")
    print("Ravi has a viral infection.")
    print("Ravi requires medical attention.")
else:
    print("\nConclusion:")
    print("Viral infection could not be proved.")
