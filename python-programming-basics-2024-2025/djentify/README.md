# 🎸 DJENTIFY – Djent Riff Generator 🎸

**Ohjelmoinnin perusteet (JAMK) – Harjoitustyö**  
**Tero Luukkonen**  
**Päivämäärä:** 18.4.2025

---

## Kuvaus

**DJENTIFY** on Pythonilla toteutettu tekstipohjainen ohjelma, joka generoi (tai ainakin pyrkii generoimaan 😂) satunnaisia djent-/metal-tyylisiä kitarariffejä.

Käyttäjä määrittää:
- Nuottien ja taukojen yhteislukumäärän
- Juurisävelen (esim. C, D#, A)
- Sävelasteikon (esim. major, minor, phrygian, harmonic_minor)
- Oktaavin (esim. 2–5)

Ohjelma muodostaa satunnaisen sävelkulun (valitun sävellajin mukaan) sekä rytmin ja yhdistää ne riffiksi. Halutessaan käyttäjä voi tallentaa riffin MIDI-tiedostona koneelleen "MIDI Exports" -kansioon. Tallentamisen jälkeen käyttäjä voi viedä MIDI-tiedoston haluamaansa DAW-ohjelmistoon ja ohjata esimerkiksi virtuaalisen kitara-pluginin toistamaan generoidun MIDI-tiedoston.

---

## Käyttöohjeet

### 1. Asenna tarvittavat kirjastot

```bash
pip install mido
```

### 2. Aja ohjelma

```bash
python djentify.py
```

### 3. Esimerkki käytöstä

```text
🎸 Djent Riff Generator -- DJENTIFY 🎸
Enter number of riff elements to generate (each will be a note or a rest): 8
Enter root note (e.g., C, D#, A): D
Enter scale type (options: major, minor, phrygian, aeolian, chromatic, dorian, harmonic_minor): phrygian
Enter desired octave (e.g., 2, 3, 4): 3

Generated Riff:
rest - 1/8
rest - 1/8 dotted
rest - 1/16 dotted
rest - 1
A3 - 1/2 dotted
rest - 1/8
D3 - 1/16 dotted
F3 - 1/4

Do you want to save the riff as a MIDI file? (y/n): y
Enter filename (default: djentify_riff.mid): esimerkkiriffi
✅ Riff saved to MIDI Exports/esimerkkiriffi.mid
```

### 4. Kansiorakenne

```bash
djentify/
├── djentify.py                 # Pääohjelma ja logiikka
├── README.md                   # Tämä tiedosto
├── harjoitustyo_raportti.md    # Dokumentaatio
└── MIDI Exports/               # Tallennetut MIDI-tiedostot
    └── esimerkkiriffi.mid
```