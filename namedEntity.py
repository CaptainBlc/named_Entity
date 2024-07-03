import spacy

nlp = spacy.load("en_core_web_sm")

texts = [
    "Apple is looking at buying U.K. startup for $1 billion. Elon Musk founded SpaceX.",
    "Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University.",
    "Microsoft Corporation is an American multinational technology company with headquarters in Redmond, Washington.",
    "The Eiffel Tower is located in Paris, France and is one of the most recognizable structures in the world.",
    "The COVID-19 pandemic caused a global economic downturn and led to numerous restrictions and lockdowns."
]

for text in texts:
    doc = nlp(text)
    print(f"Text: {text}")
    print("Entities:")
    for ent in doc.ents:
        print(f"  - {ent.text}: {ent.label_}")
    print("\n" + "-"*50 + "\n")
