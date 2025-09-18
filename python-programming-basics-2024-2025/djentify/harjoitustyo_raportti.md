# 🎸 DJENTIFY – Djent Riff Generator 🎸

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

**Tekijä:** Tero Luukkonen  
**Opiskelijatunnus:**
**Kurssi:** Ohjelmoinnin perusteet TT00CD77-3012 (JAMK)  
**Päivämäärä:** 19.4.2025  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

---

## TEHTÄVÄN KUVAUS

Harjoitustyön tavoitteena oli toteuttaa Pythonilla mahdollisimman hyvin toimiva tekstipohjainen ohjelma, joka hyödyntää kurssilla opittuja ohjelmoinnin perusteita (mm. funktiot, ehtolauseet, toistorakenteet, listat, poikkeukset, poikkeusten käsittely jne.).

Toteutin "DJENTIFY – Djent Riff Generator" -ohjelman, joka generoi käyttäjän valintojen perusteella satunnaisia sävelten ja taukojen yhdistelmiä, mahdollistaa niiden tallentamisen MIDI-tiedostona ja täten jatkojalostamisen DAW-ohjelmistossa (Digital Audio Workstation).

## KÄYTÄNNÖN TOTEUTUS

### Sovelluksen toimintaperiaate lyhyesti

DJENTIFY on Pythonilla toteutettu tekstipohjainen ohjelma, joka generoi (tai ainakin pyrkii generoimaan 😂) satunnaisia djent-/metal-tyylisiä kitarariffejä.

Käyttäjä määrittää:
- Nuottien ja taukojen yhteislukumäärän
- Juurisävelen (esim. C, D#, A)
- Sävelasteikon (esim. major, minor, phrygian, harmonic_minor)
- Oktaavin (esim. 2–5)

Ohjelma muodostaa satunnaisen sävelkulun (valitun sävellajin mukaan) sekä rytmin ja yhdistää ne riffiksi. Halutessaan käyttäjä voi tallentaa riffin MIDI-tiedostona koneelleen "MIDI Exports" -kansioon. Tallentamisen jälkeen käyttäjä voi viedä MIDI-tiedoston haluamaansa DAW-ohjelmistoon ja ohjata esimerkiksi virtuaalisen kitara-pluginin toistamaan generoidun MIDI-tiedoston.

#### Esimerkki käytöstä

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

### Funktiot, niiden kuvaukset ja keskinäiset suhteet

`main()` | Käynnistää ohjelman, käsittelee käyttäjän syötteet ja ohjaa ohjelman kulkua
`generate_scale(root, scale_type)` | Luo sävelasteikon juurisävelen ja skaalatyypin perusteella
`generate_random_rhythm(num_of_notes)` | Luo satunnaisen rytmijonon (nuotit ja tauot)
`generate_riff(num_of_notes, root, scale_type, octave)` | Yhdistää skaalan ja rytmin riffiksi
`note_to_midi(note)` | Muuntaa sävelen nimeämistavasta vastaavaan MIDI-numeroon
`duration_to_ticks(duration, ticks_per_beat=480)` | Muuntaa nuottien kestot MIDI-tikseiksi
`save_riff_to_midi(riff, output_filename="djentify_riff.mid", ticks_per_beat=480)` | Tallentaa generoidun riffin `.mid`-tiedostoksi
`validate_num_of_notes(value)` | Tarkistaa, että syötetty määrä on positiivinen kokonaisluku
`validate_root_note(value)` | Tarkistaa, että syötetty sävel on kelvollinen juurisävel
`validate_scale_type(value)` | Tarkistaa, että skaalatyyppi on tuettu
`validate_octave(value)` | Tarkistaa, että oktaavi on väliltä 1–8

Ohjelman rakenne on jaettu loogisiin kokonaisuuksiin. `main()`-funktio toimii ohjelman käyttöliittymänä: se kerää käyttäjältä tarvittavat syötteet, validoi ne kutsumalla validointifunktioita ja ohjaa ohjelman kulkua kutsumalla muita funktioita.

Varsinaisen riffin rakentaminen perustuu kahteen keskeiseen osaan:

- `generate_scale()` luo sävelskaalan valitun juurisävelen ja sävelasteikon perusteella.

- `generate_random_rhythm()` muodostaa rytmijonon, joka sisältää satunnaisesti nuotteja ja taukoja.

Nämä yhdistetään `generate_riff()`-funktiossa, joka muodostaa riffin valitulle oktaaville. Tuloksena saatu riffi voidaan tallentaa MIDI-tiedostona `save_riff_to_midi()`-funktion avulla. Sävelkorkeudet muutetaan MIDI-muotoon `note_to_midi()`-funktiolla ja rytmien kestot muunnetaan tikseiksi `duration_to_ticks()`-funktiolla.

Kaikki käyttäjän syötteet tarkistetaan omilla validointifunktioillaan `validate_num_of_notes()`, `validate_root_note()`, `validate_scale_type()`, `validate_octave()`, mikä varmistaa ohjelman vakauden ja helpon käytettävyyden.

### Tietovarastot

Ohjelma ei käytä tietokantoja. Ohjelman tuottamat MIDI-tiedostot tallennetaan "MIDI Exports/" –kansioon. Esimerkiksi: `MIDI Exports/esimerkkiriffi.mid`.

### Lähdekoodit

Koko ohjelmakoodi on selattavissa verkossa GitLabissa:  
`djentify.py` - sisältää kaikki funktiot ja pääohjelman  
`README.md` ja `harjoitustyo_raportti.md` - dokumentaatio

## AJAN KÄYTTÖ

Harjoitustyöhön käytettyä aikaa on hyvin vaikea arvioida. Sen osaan kuitenkin sanoa, että kauan meni, varmaan liian kauan. 🫣 Olin jo aloittanut harjoitustyön tekemisen, kun jouduin yllättäen keskeyttämään opinnot työmuutosten takia hyvin pitkäksi aikaa. Tästä johtuen jouduin opiskelemaan ja perehtymään asiaan myöhemmin uudestaan ja aikaa kului. Halusin myös selvittää ja selkeyttää asioita itselleni perinpohjaisesti aina silloin, kun jokin epäselvä tai mieltä askaruttava seikka tuli vastaan projektin myötä.

Suurpiirteisesti arvioitu työaika:

Ideointi ja suunnittelu:        5h
Koodaaminen:                    30h
Testaus ja virheenkorjaukset:   10h 
Dokumentointi ja palautus:      5h 

Yhteensä:                       50h

## ITSEARVIO

Oma arvio harjoitustyön pistemäärästä: **40 / 50**

VAHVUUDET

+ Olen ylpeä siitä, että sain ohjelman lopulta toimimaan.
+ En olisi uskonut ennen kurssia, että voisin saada edes jotain tällaista aikaiseksi.
+ Ohjelmaani suunnitellessa hyödynsin musiikkiosaamistani sekä DAW-osaamistani/tietämystäni.
+ Sain ideaani upotettua paljon kurssilla opittua ja uusiakin asioita mm. mido
+ Tuli tutustuttua pygameen. Olisin käyttänyt "riffin esikuuntelu"-vaiheessa. Lopulta en käyttänyt, kun tuli tunne, että lähtee laajuus lapasesta. 
+ MIDI-tiedoston tallennus ja DAW-yhteensopivuus
+ Koodi kokemattomalla silmälläni melko selkeää
+ Ohjelman rakenne selkeästi jaettu toiminnallisiin kokonaisuuksiin (funktiot erikseen)
+ Kaikki syötteet tarkistetaan välittömästi ja palautetaan virheviestit käyttäjälle

KEHITETTÄVÄÄ

- Musiikillisesti riffit täysin satunnaisia (ei rakennetta, logiikkaa tai toistuvuutta). Kun kuuntelee generoituja MIDI-tiedostoja, voisi kuvitella ohjelman nimen olevan "Cat Walking on a Piano". 
- Riffin sävelalue on rajattu yhteen oktaaviin
- Ohjelmassa ei ole graafista käyttöliittymää
- Ei esikuuntelumahdollisuutta, jonka jälkeen riffiä voisi vielä muokata ennen tallennusta

## LOPPUSANAT

Minulle kurssi oli kaiken kaikkiaan erittäin opettavainen. Rehellisesti sanottuna en olisi uskonut joitakin kuukausia sitten, että olisin saanut koodia aikaiseksi saati ymmärtänyt siitä mitään. DJENTIFY ohjelmasta olen ylpeä. Erityisesti siitä, että se toimii. Toki tuosta on vielä pitkä matka hyödylliseksi ohjelmaksi mutta tärkeintä on se, että sain visioni jossain määrin toteutettua. 

Myönnän avoimesti käyttäneeni oppimisen tukena tekoälyä (ChatGPT) ohjelmien ideoinnissa ja suunnittelussa, virheiden etsimisessä ja korjaamisessa sekä teknisten ratkaisujen ja uusien asioiden ymmärtämisessä. Ilman sitä oppimiseni olisi ollut huomattavasti hitaampaa ja suppeampaa. Hyödyntämiskulmani oli kuitenkin sellainen, että tekoäly oli kaverinani selittävänä osapuolena. Pyrin aina varmistamaan, että ymmärsin ratkaisut ja lopputulemat itse.
