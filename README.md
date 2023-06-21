# Teknostart 2022

I denne teknostarten skal dere i en gruppe lage en fjernstyrt bil og en AI-bildegjenkjenningsmodul. Dere skal få jobbe med Raspberry Pi, Arduino Uno og LOBE. Det er ikke forventet at du skal kunne noe om dette fra før av eller vite hva det er, teknostart vil fungere som en introduksjon til dette, som dere vil få god bruk for senere.  Dere skal også bygge bilen, koble den opp få alt til å fungere sammen. 
Hovedkonkurransen er TBA. Det er også poeng for estetikk, så bruk kreativiteten, maling og tusjer til å lage bilen som dere ønsker. 
Dere bør dele dere opp og jobbe på hver deres del. En viktig del av teknostart er å samarbeide godt og fordele arbeidsoppgaver. Dette er ulike deler dere kan jobbe på. Vi foreslår at dere fordeler dere på disse hovedoppgavene:
1.	Den som ønsker en utfordring, kan jobbe med Raspberry Pien. Her er det viktig å holde tungen beint i bunnen og følge oppskriften til punkt og prikke for at ting skal fungere. Får dere problemer her, ta kontakt med en student assistent. 
2.	Dere får også muligheten til å lage en egen bildegjenkjenningsmodul med LOBE. Vi har også laget en modul dere kan bruke, men vi oppfordrer dere til å lage en egen om dere får tid. 
3.	En annen oppgave er å sette opp Arduinoen med motordriver, og laste opp den ferdigskrevne koden. 
4.	Til slutt kan dere alle samarbeide om å koble alt sammen og få bilen til å fungere sammen. Vent på en studass før dere får batteriet og får startet bilen. 
5.	Når dere har bygget ferdig bilen kan dere gå videre med utvidelsene for bilen og begynne å skreddersy den slik dere ønsker.


# Table of Contents
- [Teknostart 2022](#teknostart-2022)
- [Table of Contents](#table-of-contents)
- [Veiledning for montering av Teknobilen 2023](#veiledning-for-montering-av-teknobilen-2023)
  - [Steg 1: Montering av motorer](#steg-1-montering-av-motorer)
  - [Steg 2: Sammensetting av baseplate og avlange plater](#steg-2-sammensetting-av-baseplate-og-avlange-plater)
  - [Steg 3: Ledninger](#steg-3-ledninger)
  - [Steg 4: Montering av bunnplate](#steg-4-montering-av-bunnplate)
  - [Steg 5: Raspbian](#steg-5-raspbian)
  - [Steg 6: Montering av komponenter](#steg-6-montering-av-komponenter)
  - [Steg 7: Montering av frontplate og kamera](#steg-7-montering-av-frontplate-og-kamera)
  - [Steg 8: Oppkobling av GPIO](#steg-8-oppkobling-av-gpio)
  - [Steg 9: Oppkobling av LED-lys](#steg-9-oppkobling-av-led-lys)
  - [Steg 10: Kontroll og kobling av batteri](#steg-10-kontroll-og-kobling-av-batteri)
  - [Steg 11: Montering av bakplate og topplokk](#steg-11-montering-av-bakplate-og-topplokk)
  - [Steg 12: Ferdig produkt](#steg-12-ferdig-produkt)
  - [Raspberry Pi](#raspberry-pi)
    - [Sette opp SD-kortet](#sette-opp-sd-kortet)
    - [Sette opp Raspberry Pi headless](#sette-opp-raspberry-pi-headless)
      - [SSH inn til Raspberry Pi](#ssh-inn-til-raspberry-pi)
      - [Sette opp Eduroam på Raspberry Pi](#sette-opp-eduroam-på-raspberry-pi)
      - [Få inn riktig programvare](#få-inn-riktig-programvare)
  - [Arduino](#arduino)
    - [Skaff Arduino Software til egen PC](#skaff-arduino-software-til-egen-pc)
    - [Last inn koden til Arduinoen](#last-inn-koden-til-arduinoen)
  - [(Bonus) Lobe](#bonus-lobe)
    - [Lag deres egen modell med maskinlæring](#lag-deres-egen-modell-med-maskinlæring)
      - [Last ned LOBE](#last-ned-lobe)
      - [Last ned riktig programvare for å kunne ta bilder med RPi](#last-ned-riktig-programvare-for-å-kunne-ta-bilder-med-rpi)
      - [Ta bilder](#ta-bilder)
      - [Lag gjenkjenningsmodell](#lag-gjenkjenningsmodell)
      - [Bruk modellen](#bruk-modellen)

# Veiledning for montering av Teknobilen 2023

Følg trinnene nedenfor nøye for å montere Teknobilen 2023. Alle bilder nevnt i veiledningen kan finnes i mappen [teknobil2023/-/tree/main/Media/teknobil](https://gitlab.stud.idi.ntnu.no/ELSYS_teknostart/teknobil2023/-/tree/main/Media/teknobil).

## Steg 1: Montering av motorer

Start med å feste motorene til følgende plater med de 25mm lange M3 skruene. Ettersom vi ikke benytter muttere vær oppmerksom på ikke å stramme skruene for hardt.

<p float="left">
  <img src="Media/teknobil/01.png" width="300" />
</p>

## Steg 2: Sammensetting av baseplate og avlange plater

Fest så de avlange platene sammen med baseplaten (den store med hull). Pass på at baseplaten er riktig vei.

<p float="left">
  <img src="Media/teknobil/02.png" width="300" />
  <img src="Media/teknobil/03.png" width="300" />
</p>

## Steg 3: Ledninger

Nå kan det være lurt å føre ledningene fra motorene igjennom de to firkantede hullene i baseplaten.

<p float="left">
  <img src="Media/teknobil/04.png" width="300" />
</p>

## Steg 4: Montering av bunnplate

Fest bunnplaten som vist i bildet.

## Steg 5: Raspbian

Før dere fortsetter med å feste komponentene bør dere laste ned Raspbian på et SD-kort som vist [her](URL_til_veiledning).

## Steg 6: Montering av komponenter

Legg komponentene som vist på bildet og skru dem fast inn i baseplaten med de 10mm lange M2.5 skruene.

<p float="left">
  <img src="Media/teknobil/05.png" width="300" />
  <img src="Media/teknobil/06.png" width="300" />
</p>

## Steg 7: Montering av frontplate og kamera

Fest frontplaten og skru fast kameraet til platen med de 4mm lange M2 skruene.

<p float="left">
  <img src="Media/teknobil/07.png" width="300" />
  <img src="Media/teknobil/08.png" width="300" />
</p>

## Steg 8: Oppkobling av GPIO

Koble opp GPIO som vist på bildet.

<p float="left">
  <img src="Media/teknobil/09.png" width="300" />
</p>

## Steg 9: Oppkobling av LED-lys

Koble opp ledsene som anvist i figuren under.

<p float="left">
  <img src="Media/teknobil/10.png" width="300" />
  <img src="Media/teknobil/11.png" width="300" />
</p>

## Steg 10: Kontroll og kobling av batteri

Når ledsene er koblet opp kan dere få bilen deres kontrollert hos en læringsassistent. Dersom alt er korrekt kan dere få utlevert et batteri, den kobles til som vist på bildet. Pass på at bryteren er satt til 5 V før dere skrur den på.

<p float="left">
  <img src="Media/teknobil/12.png" width="300" />
  <img src="Media/teknobil/13.png" width="300" />
</p>

## Steg 11: Montering av bakplate og topplokk

Fest bakplaten og sett på topplokket.

<p float="left">
  <img src="Media/teknobil/14.png" width="300" />
</p>

## Steg 12: Ferdig produkt

Bilen skal nå se slik ut.

<p float="left">
  <img src="Media/teknobil/15.png" width="300" />
</p>

Lykke til med monteringen!

| Arduino | Raspberry Pi |
|---------|--------------|
| A5      | GPIO 6       |
| A4      | GPIO 13      |
| A3      | GPIO 19      |
| A2      | GPIO 26      |
| GND     | GND          |


## Raspberry Pi

Raspberry Pi er en lavkostnads, kredittkort-størrelse datamaskin, der alt du trenger for å bruke som en hvilken som helst annen PC en monitor/TV, et tastatur, og en mus. Den klarer alt som er å forvente av en PC, i alt fra websurfing til å spille av høydefinerte videoer, spill og mye mer.
Videre, kan Raspberry Pi muligheten til å samhandle med resten av verden, og har blitt brukt til en rekke digitale skaper-prosjekter. Disse prosjektene tar på alt fra musikkskaping og værstasjoner til selvkjørende droner og fuglehus som poster på Instagram.
I dette prosjektet brukes modellen Raspberry Pi 3B+. Den brukes til å lage en webserver som streamer live-video fra et Raspberry kamera, hvor du, mens du er i nettleseren, kan bruke piltastene til å styre bilen. Dette gjøres ved at du sender informasjon om tastetrykk til RPi-en, og denne sender videre informasjon til arduinoen, som er et mikrokontrollerkort. I dagligtale er det, i et slikt prosjekt, vanlig å kalle Pien for hjernen, som bruker arduino som slave.
Som alle andre datamaskiner har denne også et operasjonssystem, eller OS. Raspberry Pi sitt OS ligger på et SD-kort, som er mulig å ta ut og inn. Dette SD-kortet fungerer også som maskinens harddrive. Derfor er det naturlig at prosessen med å klargjøre Raspberry Pi-en starter i å sette opp SD-kortet.

### Sette opp SD-kortet

Utstyr:

- Laptop
- SD-kort
- SD-kortleser

SD-kortene dere har fått utdelt inneholder ingen informasjon dere kan bruke. Derfor må dere starte med å laste opp en OS til dette kortet. RPi bruker ikke Windows eller MacOS, men et operativsystem som ofte kalles Rasbian/Debian, som er en versjon av Linux. For å kunne laste opp dette OS-et til kortet kreves et eget skrivebordsprogram som heter Raspberry Pi Imager.

Slik går du fram for å sette opp SD-kortet:

1. Last ned Raspberry Pi Imager
2. Sett inn SD-kortet inn i SD-kortleseren
3. Åpne Raspberry Pi Imager
4. Trykk på «CHOOSE OS» og velg: «Raspberry Pi OS (32-bit)»
5. Videre «CHOOSE STORAGE», og velg det SD-kortet du satte inn.
6. Gå inn på settings:

   ![Raspberry Pi Imager](Media/rpi/01Pi-imager.png)

   1. Sett hostname til «ELSYS"gruppenummer"», eksempel: ELSYS14
   2. Enable SSH
      - Use password authentication
   3. Set username and password
      - Username: teknostart NB! viktig at dere kun skriver “teknostart”
      - Password: "123", eller noe annet dere lett kan huske
   4. Enable Set locale settings:
      - Time zone: Europe/Oslo
      - Keyboard layout: no
   5. Når du er ferdig skal det se noe tilsvarende:

   ![Raspberry Pi Imager settings](Media/rpi/02settings.png)

7. Lagre innstillingene, og trykk på write, dette kan ta litt tid.
8. Når SD-kortet er ferdig skrevet vil du få en beskjed om at det er trygt å ta det ut av maskinen. Ta det ut, og sett inn i Pi-en.


### Sette opp Raspberry Pi headless
Som sagt er Raspberry Pi en datamaskin, men som du kanskje ser er det ikke akkurat en laptop. Det fine med Raspberry Pi er at den kan settes opp og styres headless, altså at man verken trenger et eksternt monitor eller tastatur. For å bruke den headless tar vi i bruk Secure Shell Protocol eller også kjent som SSH, som du aktiverte i “Advanced options”.

Utstyr:
- Laptop
- Ethernet kabel
- Ethernet inngang (adapter hvis laptopen ikke har en dedikert inngang spør en studass ved behov)
- Raspberry Pi med ferdig installert SD-kort

#### SSH inn til Raspberry Pi

1. For å koble deg til Pi-en kobler du Raspberry Pi til laptopen via ethernet kabelen og ved behov en ethernet adapter.
2. Åpne en terminal på laptopen:
   - For Windows kan dere søke opp:
     - Terminal (🪟 + x)
     - Windows PowerShell
     - Command Promt
   - For Mac kan dere søke opp:
     - Terminal
3. For å SSH inn til Pi-en går du inn på terminalen og skriver (du kan også copypaste ved kopiere vanlig for så å lime inn med høyre klikk inne på terminalen.):
   ```bash
   ssh teknostart@<hostname>.local
   ```
   - Som du satte i Raspberry Pi imager F.eks:
     ```bash 
     teknostart@ELSYS1.local 
     ```
     -NB! Det kan ta litt tid før Pi-en skrur seg på, så om den ikke finner Pi-en med en gang så bare vent noen minutter og prøv igjen.
     _ Når den spør om du ønsker å koble deg til skriver du “yes” og trykker enter.
     _ Du vil få noe tilsvarende:
     ![SSH into Raspberry Pi](Media/rpi/03SSH.png)
Gratulerer du har nå SSH-et inn til deres Raspberry Pi. Kommandoene du nå skriver skjer inne på selve Raspberry Pi.



Vi skal nå få inn riktig programvare, samt laste inn alt av kode som skal ligge lokalt på Pien.

1. Start med å sjette at klokken inne på Raspberry Pien stemmer med kommandoen:

```bash
date
```
![Date](Media/rpi/08check_date.png)
    * Dersom dato og klokken er feil kan du fikse opp i dette ved å bruke kommandoen (Husk å endre dato/klokkeslett til gjeldende tid):

```bash
sudo date -s '18 Aug 2022 13:00'
```
![Change](Media/rpi/09change_date.png)
2. Nå kan du oppdatere og oppgradere med kommandoene

```bash
sudo apt-get update
sudo apt-get dist-upgrade
```

- Trykk enter når dem spør om du ønsker å fortsette.


3. Nå kan du klone git-en som inneholder koden som Raspberry Pi-en skal kjøre med kommandoen:

```bash
git clone [git@github.com:PeterhdPham/Teknostart.git](https://github.com/PeterhdPham/Teknostart.git)
```
    *NB dette kan ta litt tid
4. Videre kan du navigere deg inn på "Teknostart" mappen med kommandoen:
   
```bash 
cd Teknostart/
```

5. Last ned ekstra progrmvare som kreves for å kjøre koden med kommandoen:
```bash
pip3 install -r requirements.txt
sudo apt-get install libatlas-base-dev
sudo apt-get install python3-pyro4
```
6. Naviger videre inn i "projectfolder" med kommandoen:

```bash
cd projectfolder/
```
7. Når Arduino koden er ferdig lastet kan du kjøre Python koden med kommandoen:

```python
python runCode.py
```

## Arduino
Arduino er en open-source elektronikkplattform basert på hardware og software designet for å være enkelt å bruke. Arduinokortene er rusta til å lese ulike inputs - lys på en sensor, knappetrykk, en Twittermelding – og bruke denne dataen til å sende et outputsignal – aktivere en motor, skru på en LED, publisere noe på nett. Du kan fortelle kortet hva den skal gjøre, ved å sende opp sett med instruksjoner til mikrokontrolleren på kortet i form av kodesnutter i programmeringsspråket C. Disse instruksjonene sendes til kortet via en USB-kabel fra din PC, men for at denne informasjonen skal lastes opp riktig må vi ha koden vår i en Arduino Software (IDE).

### Skaff Arduino Software til egen PC

Last ned Arduino IDE
* [Windows](https://docs.arduino.cc/software/ide-v1/tutorials/Windows#download-the-arduino-software-ide)
* [MacOS](https://docs.arduino.cc/software/ide-v1/tutorials/macOS?_gl=1*17wzpvg*_ga*MTY2NjU1MjEzOC4xNjI5OTYzMDk1*_ga_NEXN8H46L5*MTY1NTIwNjQyMy4zMy4xLjE2NTUyMDk1MTcuNjA.)
* [Linux](https://docs.arduino.cc/software/ide-v1/tutorials/Linux?_gl=1*xpugwf*_ga*MTY2NjU1MjEzOC4xNjI5OTYzMDk1*_ga_NEXN8H46L5*MTY1NTIwNjQyMy4zMy4xLjE2NTUyMDk1NDcuMzA.)

### Last inn koden til Arduinoen
Utstyr:
1. Laptop
2. Usb-A til usb-b kabel
3. Arduino Uno

Oppsett:
1. Koble til arduino-kortet til din PC med en USB-B ledningen
2. Sørg for at softwaren fungerer for riktig type arduinokort, her Arduino Uno
    * Gå inn på «Verktøy»/«Tools»
    * Velg riktig kort og port (porten er hvilken inngang/utgang du bruker på PC-en. Kan komme feilmelding om det velges feil)

![Arduino](Media/arduino/01toolssetup.png)

3. Videre erstatter du teksten med koden under:
    <details>
    <summary>Klikk her</summary>

    ```c
    //MOTOR SETUP
const int E1 = 3; ///<Motor1 Speed - Back Right
const int E2 = 11;///<Motor2 Speed - Front Right
const int E3 = 5; ///<Motor3 Speed - Front Left
const int E4 = 6; ///<Motor4 Speed - Back Left

const int M1 = 4; ///<Motor1 Direction - Back Right
const int M2 = 12;///<Motor2 Direction - Front Right
const int M3 = 8; ///<Motor3 Direction - Front Left
const int M4 = 7; ///<Motor4 Direction - Back Left


/////////LOGIC/////////////////////////////////
//INPUT PINS
int drive = A0;
int reverse = A1;
int rightTurn = A2;
int leftTurn = A3;

//BOOLS
int go = 0;
int back = 0;
int left = 0;
int right = 0;


//SPEEDS
int drivingSpeed = 150;
int turningSpeed = 50;


//////DRIVING FUNCTIONS//////////////////////
void speedSet(String motors, int Speed){
  //Choose speed from 0-255
  if(motors == "right"){
    analogWrite(E1, Speed);
    analogWrite(E3, Speed);
    }
  else if(motors == "left"){
    analogWrite(E2, Speed);
    analogWrite(E4, Speed);
  }
  else if(motors = "both"){
    analogWrite(E1, Speed);
    analogWrite(E2, Speed);
    analogWrite(E3, Speed);
    analogWrite(E4, Speed);
  }
}

//DRIVING FUNCTION
void driving(String motors, bool Direction){
  //Direction = 0 -> forward
  //Dircetion = 1 -> reverse
  if (motors == "both"){
  digitalWrite(M1, Direction);
  digitalWrite(M2, Direction);
  digitalWrite(M3, Direction);
  digitalWrite(M4, Direction);
  }
  else if (motors = "right"){
    digitalWrite(M1, Direction);
    digitalWrite(M3, Direction);
  }
  else if (motors = "left"){
    digitalWrite(M2, Direction);
    digitalWrite(M4, Direction);
  }
}


////SETUP///////////////////////
void setup() {
  Serial.begin(9600);   
  Serial.println("Starting session...");

  //SET PINS 
  pinMode(drive,INPUT);
  pinMode(reverse, INPUT);
  pinMode(leftTurn, INPUT);
  pinMode(rightTurn, INPUT);
  for(int i=3;i<9;i++)
    pinMode(i,OUTPUT);
  for(int i=11;i<13;i++)
    pinMode(i,OUTPUT);
    
}

void loop() {
//UPDTAING THE BOOLEANS
  go = digitalRead(drive);
  back = digitalRead(reverse);
  left = digitalRead(leftTurn);
  right = digitalRead(rightTurn);

  
/////FORWARD DRIVE/////////////////////////////////////////
  if(go && !back){  
    driving("both", 0);  
    //FORWARD WITH A RIGHT TURN
    if(right){
      speedSet("right",turningSpeed);
    }
    //FORWARD WITH A LEFT TURN
    else if(left){
      speedSet("left",turningSpeed);
    }
    else{
      speedSet("both", drivingSpeed);
      Serial.println("FORWARD");
    }
  }

  
  //REVERSE
  else if(back && !go){
    driving("both", 1);
    //REVERSE WITH RIGHTTURN
    if(right){
      speedSet("right",turningSpeed);
    }
    //REVERSE WITH LEFTTURN
    else if(left){
      speedSet("left", turningSpeed);
    }
    else{
      speedSet("both", drivingSpeed);      
      Serial.println("REVERSE");
    }
  }



 //RIGHTTURN
  else if(right && !go && !back){
    speedSet("both", turningSpeed);
    if(!left){
      digitalWrite(M1,1);
      digitalWrite(M3,1);
      digitalWrite(M2,0);
      digitalWrite(M4,0);
      //driving("left", 0);
      Serial.println("RIGHTTURN");
    }
    
    //IF YOU PRESS BOTH LEFT AND RIGHT
    else{
      driving("both", 0);
    }
  }

  //LEFTTURN
  else if(left && !go && !back){
    speedSet("both", turningSpeed);
    if(!right){
      digitalWrite(M1,0);
      digitalWrite(M3,0);
      digitalWrite(M2,1);
      digitalWrite(M4,1);
      //driving("right",0);
      //driving("left", 1 );
      Serial.println("LEFTTURN");
    }
  
  //IF YOU PRESS BOTH LEFT AND RIGHT
    else{
      driving("both", 0);
    }
  }

  //IF YOU DON'T PRESS ANYTHNIG
  else{
    speedSet("both", 0);
    Serial.println("STOP");
 }
}
    </details>

4. Last opp koden til arduinokortet. Blå først for å verifisere koden (dobbeltsjekke at det ikke er noen feil med koden). Deretter rød for å laste opp.

<img src="Media/arduino/02yeah.png" width="240">

NB: Om motoren skulle gått i feil retning når dere tester full oppkobling, er det trolig noe feil i oppkoblingen (enten feil motor til feil port, eller feil på +/- på motordriverens innganger). Dette kan dere prøve å endre på selv i arduino-koden under «MOTOR SETUP», for å slippe å gjøre omkoblinger, og for en liten ekstra utfordring:)

## (Bonus) Lobe

### Lag deres egen modell med maskinlæring
Det vi kaller object detection, eller objekt gjenkjenning, er en teknikk en datamaskin tar i bruk for å lokalisere objekter i bilder eller videoer. Vi mennesker kjenner fort igjen ulike objekter i bilder og videoer, og skille dem, ila. millisekunder. Målet med object detection er å kunne gjenskape denne egenskapen i en datamaskin. For å få til dette er det ofte tatt i bruk machine learning, som går ut på at maskinen lærer opp seg selv. 
For å slippe å skrive egen kode for dette skal vi benytte et open-source program kalt LOBE. I dette programmet kan en legge inn bilder av de objektene man ønsker at maskinen/programmet skal kunne kjenne igjen, og sette merkelapp på dem. Disse bildene vil så LOBE bruke til å trene opp en modell (type program), til den klarer å kjenne igjen alle objektene den har merkelapp til. Denne modellen, i form av en mappe, legger vi inn på vår RPi, og du vil ha en egenlaget og fungerende gjenkjenningsmodell når du kjører bilen!


####	Last ned LOBE
-	Trykk på Download på denne nettsiden

Bildene som skal brukes til å lage denne modellen skal tas med RPi, og for å få lagret disse lokalt på PC-en skal vi benytte en ny programvare
#### Last ned riktig programvare for å kunne ta bilder med RPi
-	git clone https://github.com/silvanmelchior/RPi_Cam_Web_Interface.git
-	cd RPi_Cam_Web_Interface
-	./install.sh
Under nedlastingen vil du få opp denne menyen:
 <img src="Media/Lobe/01.jpg" height=350>

Sørg for at alle parametere er like som på bildet over!

#### Ta bilder
1.	Start programvaren med å skrive kommandoen /.start.sh i terminalen
2.	Åpne en ny fane i nettleseren og bruk RPi-en sin IP-adresse som nettstedssøk
Hvis du ikke vet IP-adressen fra før kan du finne den med kommando ifconfig

<img src="Media/Lobe/02.jpg" height=300>

På plassen markert i rødt vil IP-adressen stå

3.	Når du kommer inn på nettsiden følger du linken html. Da burde du komme hit:
<img src="Media/Lobe/03.jpg" height=350> 

Om bildet er opp ned kan du gå inn på Camera Settings og sette flip-instillingen til Vertical

4.	Trykk på record image for å ta bilder. Tips for best mulig gjenkjenningsmodell:
-	Ta mange bilder av hvert objekt
-	Helst fra ulike vinkler
-	Kan vurdere ulike bakgrunner/underlag

5.	For å få lastet ned, trykk på Download Videos ond Images  Select All  Get Zip
Denne vil bli lastet ned lokalt på egen PC, velg en filplassering du husker.

#### Lag gjenkjenningsmodell
1.	Åpne Lobe
2.	Velg New Project
3.	Inne på Label (i sidemenyen), trykk på Import
-	Her skal du velge de bildene du tok i forrige steg
Tips når du skal sette label (to alternativer):
a)	Last opp bildene til ett objekt om gangen, da kan du markere alle bildene med Ctrl+A, og skrive label for alle bildene samtidig. Dette gjøres ved Import -> Images

b)	Legg alle bildene av samme objekt i en egen mappe, der mappenavnet er labelen til objektet. Sett deretter alle objekt-mappene i en felles mappe. Last opp ved å trykke på Import -> Dataset. Eksempel:


<img src="Media/Lobe/04.jpg" height=150>

4.	Når alle bildene har fått label, gå inn på Train, og vent til denne har kommet til 100%

<img src="Media/Lobe/05.jpg" height=100>

####   Bruk modellen
1.	Gå inn på Use, deretter trykk på export
2.	Velg alternativet TensorFlow Lite, dette vil gi deg en mappe som brukes i koden for RPi-en, derfor er det viktig å gi denne mappen navnet «Lobe», og plassere denne et sted du husker!
3.	For å få denne inn i mappestrukturen til RPi-en deres så modellen deres faktisk blir brukt, må den erstatte den modellen som allerede ligger inne. Derfor er det nødvendig å laste ned et skrivebordsprogram som lar deg overføre filer og mapper mellom to maskiner, her egen PC og RPi

    Windows:
    1.	Last ned WinSCP
    2.	Når nedlastningen er ferdig, åpne programmet
    3.	Skriv inn Vertsnavn (Hostname), brukernavn og passord til RPi-en deres for å få en tilkobling. Det vil da komme opp mappestrukturen til RPi-en på venstre side av programvinduet
    4.	Erstatt Lobe-mappen som ligger på RPi-en fra før, med den du nettopp har laget

    MacOs
    1.	Last ned FileZilla
    2.	Åpne programmet når nedlastningen er ferdig
    3.	Fyll inn Vert (Hostname), brukernavn og passordet til RPi-en deres for å få en tilkobling. Det vil da komme opp mappestrukturen til RPi-en på venstre side av programvinduet
    4.	Erstatt Lobe-mappen som ligger

Når du kjører «runCode.py» fra RPi-en nå, vil den ta i bruk deres egen object detection!!! 
