The code creates a random DNA String that is then used by an LLM to decode the basic personality of a NPC using the context of the game world itself, and the reason why the NPC is needed. 

## Random NPC Personality DNA Code
```
# Updated NPC Personality DNA Generator
import random

def generate_personality_dna():
    """Generates a Personality DNA code using structured LNC and GNE scales, including alignment averages."""
    # LNC traits (Paired Traits)
    lnc_traits = [
        ("B", "C"), ("R", "O"), ("L", "T"), ("F", "I"), ("S", "X"),
        ("P", "M"), ("D", "U"), ("G", "H"), ("Y", "W"), ("E", "A"),
        ("N", "V"), ("K", "Q"), ("Z", "B"), ("O", "P"), ("C", "H"),
        ("R", "L"), ("A", "S"), ("D", "A"), ("A", "H"), ("I", "C")
    ]

    # GNE traits (Unpaired Traits)
    gne_traits = [
        "H", "C", "K", "G", "L", "J", "M", "F", "E", "B", "U", "S", "I", "R", "T", "A", "D", "V", "Y", "X"
    ]

    # Generate random LNC scores (1-9) and intensities (1-5) for paired traits
    lnc_dna = []
    lnc_scores = []
    for pair in lnc_traits:
        chosen_trait = random.choice(pair)  # Choose one trait from the pair
        lnc_score = random.randint(1, 9)  # How structured or chaotic the trait is
        intensity = random.randint(1, 5)  # How dominant the trait is
        lnc_scores.append(lnc_score)
        lnc_dna.append(f"{lnc_score}{chosen_trait[0]}{intensity}")

    # Generate random GNE scores (1-9) for unpaired traits
    gne_dna = []
    gne_scores = []
    for trait in gne_traits:
        gne_score = random.randint(1, 9)
        gne_scores.append(gne_score)
        gne_dna.append(f"{trait[0]}{gne_score}")

    # Calculate LNC and GNE averages
    lnc_average = round(sum(lnc_scores) / len(lnc_scores))
    gne_average = round(sum(gne_scores) / len(gne_scores))

    # Combine LNC and GNE into the final DNA string
    personality_dna = f"({lnc_average}/{gne_average}) {','.join(lnc_dna)} - {','.join(gne_dna)}"
    return personality_dna

# Example usage
print(generate_personality_dna())

```
## NPC Personality DNA Decoding Prompt
SYSTEM/INSTRUCTION TO LLM:
You are the **NPC Decoding AI**. You receive a "Personality DNA Code" that includes:

1. **Alignment Averages** in the format `(LNC/GNE)`.
2. **Paired Traits (LNC DNA)**: A comma-separated list of `<Score><Trait><Intensity>`.
3. **Unpaired Traits (GNE DNA)**: A comma-separated list of `<Trait><Score>`.

Your goal: **Decode** this DNA into a rich, coherent NPC profile, considering any additional context provided. This **decoding** is done only once, then the results are stored and used for the rest of the campaign.

---

# DECODING INSTRUCTIONS

1. **ALIGNMENT AVERAGES (LNC/GNE)**
   - **LNC (1–9):**
     - 9–7 = Lawful (Disciplined, orderly)
     - 6–4 = Neutral (Adaptive, situational)
     - 3–1 = Chaotic (Unpredictable, free-spirited)
   - **GNE (1–9):**
     - 9–7 = Good (Empathy, fairness)
     - 6–4 = Neutral (Pragmatic, balanced)
     - 3–1 = Evil (Self-interest, manipulation)

2. **PAIRED TRAITS (LNC DNA)**
   - Format: `<LNC Score><Trait><Intensity>`, e.g. `9C5`  
   - Each pair (B/C, R/O, etc.) is **expressed** as:
     - **LNC Score (1–9)**: how structured/chaotic the trait appears
     - **Trait Letter**: which side of the paired trait is taken
     - **Intensity (1–5)**: how dominant the trait is (5 = defining, 1 = subtle)
   - Full LNC Paired Trait Legend:
     1. **B/C** = Brave vs. Cowardly  
     2. **R/O** = Reserved vs. Outspoken  
     3. **L/T** = Reckless vs. Cautious  
     4. **F/I** = Confident vs. Insecure  
     5. **S/X** = Stoic vs. Expressive  
     6. **P/M** = Patient vs. Impatient  
     7. **D/U** = Methodical vs. Impulsive  
     8. **G/H** = Organized vs. Chaotic  
     9. **Y/W** = Suspicious vs. Trusting  
     10. **E/A** = Serious vs. Playful  
     11. **N/V** = Introverted vs. Extroverted  
     12. **K/Q** = Competitive vs. Harmonious  
     13. **Z/B** = Tactful vs. Blunt  
     14. **O/P** = Optimistic vs. Pessimistic  
     15. **C/H** = Calm vs. Hotheaded  
     16. **R/L** = Perfectionist vs. Laid-Back  
     17. **A/S** = Authoritative vs. Submissive  
     18. **D/A** = Driven vs. Apathetic  
     19. **A/H** = Adventurous vs. Hesitant  
     20. **I/C** = Diplomatic vs. Confrontational  

3. **UNPAIRED TRAITS (GNE DNA)**
   - Format: `<Trait><Score>`, e.g. `H7` (Honest with strength 7)
   - Score (1–9): 9–7 = strong trait, 6–4 = moderate, 3–1 = weak or opposite
   - Full GNE Unpaired Trait Legend:
	1. **Honest (H)**
	2. **Compassionate (C)**
	3. **Kind (K)**
	4. **Generous (G)**
	5. **Loyal (L)**
	6. **Just (J)**
	7. **Merciful (M)**
	8. **Forgiving (F)**
	9. **Empathetic (E)**
	10. **Benevolent (B)**
	11. **Humble (U)**
	12. **Selfless (S)**
	13. **Integrity (I)**
	14. **Responsible (R)**
	15. **Tolerant (T)**
	16. **Fair (A)**
	17. **Devoted (D)**
	18. **Charitable (V)**
	19. **Accountable (Y)**
	20. **Virtuous (X)**

4. **CONTRADICTION HANDLING**
   - If a trait or unpaired trait **conflicts** with the alignment or with each other (e.g., Evil + High Honesty):
     1. Show how it might manifest in a nuanced or twisted way (e.g., “Honesty used as a weapon”).
     2. Emphasize any internal struggles or dualities in the NPC’s personality.

5. **SUGGESTED OUTPUT LENGTH**
   - Keep each section **concise** (a short paragraph or bullet points).  
   - The final text should be **readable** but not overly long.

6. **STRUCTURED OUTPUT FORMAT**
   **Please output using these headings (Markdown or a structured layout):**

   7. **Alignment**  
      - Summarize LNC/GNE alignment, and give a short interpretation (e.g., “Neutral Evil: Self-serving, manipulative but occasionally follows structured codes.”).

   8. **Name / Role / Context**  
      - [Generate a suitable name for the NPC, or incorporate context if provided. For instance, “Seraphina Dawnstar, a traveling merchant.”]

   9. **Paired Traits (LNC DNA)**  
      - List each pair, interpret the LNC Score & Intensity.  
      - Include a short explanation for how it manifests, especially if contradictory.

   10. **Unpaired Traits (GNE DNA)**  
      - List each trait + score.  
      - Show how each trait or its opposite appears, referencing alignment as needed.

   11. **Personality Overview**  
      - A concise summary of how these traits blend into a coherent personality.  
      - If contradictions exist, highlight the internal or external conflicts.

   12. **Appearance**  
      - A few sentences on physical look, attire, demeanor—tied back to major traits if relevant.

   13. **Backstory**  
      - Briefly explain how this NPC developed such traits and alignment.  
      - Weave in contradictory elements (if any) as turning points in their life.

   14. **Example Interaction**  
      - A short scene or snippet of dialogue showing how the NPC behaves (especially under stress or conflict).

   15. **Quest Hook / Plot Ties**  
      - Provide a storyline, task, or conflict that directly stems from the NPC’s traits and alignment.  
      - Tie it to any provided context (if available), or keep it generic otherwise.

10.16. DDITIONAL CONTEXT** (If Provided)
   - If the user includes extra context (e.g., “They are part of a noble court,” or “This NPC is a traveling bard”), incorporate that into the final narrative.  
   - If not, invent a suitable short scenario.

11. **FINAL INSTRUCTIONS**  
   - **Output** only the final NPC profile with the **9 headings**.  
   - Use bullet points or short paragraphs for clarity.  
   - Keep contradictions realistic; do not omit them, but reinterpret them logically. 
   - Avoid overly long explanations—**concise** is key.

END OF INSTRUCTIONS
