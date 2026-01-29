def hash_to_multiplier(hash_string):
    """
    Formula corretta per Aviator: 99 / (1 - (decimal / 2^48))
    Prende i primi 13 caratteri hex (6.5 bytes)
    """
    # Prendi i primi 13 caratteri hex
    h = int(hash_string[:13], 16)
    
    e = 2**52
    return (((100 * e - h) / (e-h)) // 1) / 100.0


def test_formula():
    examples = [
        ("0a112a9e726287a83a2693fdc0d13ec6c2a1a268b8b4893c39ba3185f92dece1e30f1db4085726b7d8528258ed61c00099eaa9da089a38a0c5e779ac1308d250", 1.84),
        ("4d2a3d5c762c20cf8e5c53ae7eda857fb37f952764889ebe416b56f080223301c79cff31627af96ef6141cc5b170baf5b4ba2030d04263be1c4aa0cdc37d7909", 1.38),
        ("38af859af05aa7f75172b4b675208ce41f12a104ae786b876a208ee86a7aa7c86f6da44b6b554fe985230864e765d47ed8da31c3c4ba30899e9af191b5ef1bf4", 2.64)
    ]
    
    print("Test con formula: 99 / (1 - (decimal / 2^48))")
    print("="*60)
    
    for i, (hash_val, expected) in enumerate(examples, 1):
        calculated = hash_to_multiplier(hash_val)
        hex_part = hash_val[:13]
        decimal_value = int(hex_part, 16)
        
        print(f"\nEsempio {i}:")
        print(f"Hash (primi 13): {hex_part}")
        print(f"Decimale: {decimal_value:,}")
        print(f"Calcolato: {calculated}x")
        print(f"Atteso: {expected}x")
        print(f"Differenza: {abs(calculated - expected):.3f}")

# Prova anche altre varianti
def test_alternative_formulas():
    print("\n" + "="*60)
    print("TEST FORMULE ALTERNATIVE")
    print("="*60)
    
    hash_val = "0a112a9e726287a83a2693fdc0d13ec6c2a1a268b8b4893c39ba3185f92dece1e30f1db4085726b7d8528258ed61c00099eaa9da089a38a0c5e779ac1308d250"
    expected = 1.84
    
    # Test con diversi numeri di caratteri hex
    for hex_len in [8, 10, 12, 13, 16]:
        hex_part = hash_val[:hex_len]
        decimal_value = int(hex_part, 16)
        
        # Formula base crash game
        max_val = 2**(hex_len * 4)  # 4 bits per carattere hex
        normalized = decimal_value / max_val
        
        if normalized < 1:
            multiplier = round(99 / (1 - normalized), 2)
            print(f"Hex len {hex_len:2d}: {hex_part} -> {multiplier}x (vs {expected}x)")

if __name__ == "__main__":
    test_formula()
    test_alternative_formulas()