import re
from itertools import product
import streamlit as st

def solve_subtraction(minuend, subtrahend1, subtrahend2, result):
    # Ersetze Platzhalter (z.B. '□') durch ein Regex-Muster, das jede Ziffer abgleicht
    patterns = [minuend, subtrahend1, subtrahend2, result]
    filled_patterns = [pattern.replace('□', '{}') for pattern in patterns]
    
    # Zähle die Anzahl der Platzhalter, um die Anzahl der benötigten Kombinationen zu bestimmen
    num_placeholders = sum(pattern.count('□') for pattern in patterns)
    
    # Erzeuge alle möglichen Kombinationen von Ziffern für die Platzhalter
    for digits in product(range(10), repeat=num_placeholders):
        try:
            # Fülle die Platzhalter mit den generierten Ziffern
            filled_values = [filled_patterns[i].format(*digits[sum(pattern.count('□') for pattern in patterns[:i]):sum(pattern.count('□') for pattern in patterns[:i+1])]) for i in range(4)]
            filled_values = [int(value) for value in filled_values]
        except ValueError:
            continue
        
        # Überprüfe, ob die Subtraktion korrekt ist
        filled_minuend, filled_subtrahend1, filled_subtrahend2, filled_result = filled_values
        if filled_minuend - filled_subtrahend1 - filled_subtrahend2 == filled_result:
            return filled_values
    
    # Wenn keine Lösung gefunden wird
    return None

def run_interface_kaggle():
    # Sammle Benutzereingaben in einer Kaggle-freundlichen Weise (z.B. mit Eingabeaufforderungen)
    st.title("Subtraktion leicht gemacht. Entwickler: Joachim Lorenz")
    st.write("Geben Sie die Werte mit Platzhaltern ('□') für die unbekannten Ziffern ein.")
    
    minuend = st.text_input("Minuend (verwenden Sie '□' für Unbekannte):", value="4□67")
    subtrahend1 = st.text_input("Subtrahend 1 (verwenden Sie '□' für Unbekannte):", value="4□9")
    subtrahend2 = st.text_input("Subtrahend 2 (verwenden Sie '□' für Unbekannte):", value="987□")
    result = st.text_input("Ergebnis (verwenden Sie '□' für Unbekannte):", value="□987")
    
    if st.button("Lösen"):
        solution = solve_subtraction(minuend, subtrahend1, subtrahend2, result)
        
        if solution:
            filled_minuend, filled_subtrahend1, filled_subtrahend2, filled_result = solution
            st.success(f"Lösung gefunden:\nMinuend = {filled_minuend}\nSubtrahend 1 = {filled_subtrahend1}\nSubtrahend 2 = {filled_subtrahend2}\nErgebnis = {filled_result}")
        else:
            st.error("Keine Lösung gefunden.")

# Beispielaufruf für Kaggle oder Streamlit
if __name__ == "__main__":
    run_interface_kaggle()
