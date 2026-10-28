# Gelen Kudeaketa (Ikastetxeak_Kudeatu) — Odoo 17

Odoo 17rako modulu pertsonalizatua, ikastetxeak eta haien gelak era eraginkor eta zentralean kudeatzeko.

Proiektuaren biltegia: [https://github.com/balvarezech/Gelen-kudeaketa](https://github.com/balvarezech/Gelen-kudeaketa)

---

## 🎯 Proiektuaren Helburua eta 1. Fasea

Lehen fase honetan **Ikastetxeak** eta **Gelak** kudeatzeko oinarrizko datu-ereduak, bistak, erlazioak eta menu-egitura osoa garatu dira, zehaztapenekin eta emandako pantaila-argazkiekin bat etorriz:

* ✅ **Ikastetxeen zerrenda-bista (Tree/List View)**: Ikastetxe guztiak, haien kodea, kokalekua, kontaktua eta gela kopurua zerrendatuta.
* ✅ **Ikastetxeen formulario-bista (Form View)**: Datu nagusiak, harremanetarako bideak eta erlazionatutako gelen zerrenda interaktiboa (One2many bidez editagarria).
* ✅ **Gelen zerrenda-bista (Tree/List View)**: Pantaila-argazkiko elementu guztiekin: Gela izena, Ikastetxe izena, Ikastetxea (Many2one), Erreserbatu botoiak, Edukiera, Kokalekua eta Erabilgarritasuna.
* ✅ **Gelen formulario-bista (Form View)**: Gela izena, Edukiera, Baliabideak, Kokalekua, Erlazionatutako Ikastetxe izena (related), Ikastetxea hautatzeko hautatzailea, Erabilgarri marka eta Display Name.
* ✅ **Menu nagusia eta azpimenuak**: `Ikastetxeak_Kudeatu` menu orokorra, `Ikastetxeak` eta `Gelak` azpimenu nagusiak, eta dagozkien ekintza-aukerak (`Ikastetxe zerrenda`, `Erreserbak`, `Gela zerrenda`).
* ✅ **Erlazionatutako eremuak formularioetan**:
  * Many2one (`ikastetxe_id`)
  * One2many (`gela_ids`)
  * Related Field (`ikastetxe_izena` -> `ikastetxe_id.kodea`, automatikoki bistaratua)
  * Computed Field (`gela_kopurua` -> `@api.depends('gela_ids')`)

---

## 🗂️ Moduluaren Egitura

```text
Gelen-kudeaketa/
├── data/
│   └── demo_data.xml               # Hasierako eta frogetako datuak (Zornotza, Ethazi...)
├── models/
│   ├── __init__.py                 # Ereduen inportazioak
│   ├── ikastetxea.py               # 'ikastetxeak.ikastetxea' eredua
│   └── gela.py                     # 'ikastetxeak.gela' eredua
├── security/
│   └── ir.model.access.csv         # Baimenak eta sarbide-arauak (base.group_user)
├── static/
│   └── description/
│       └── icon.png                # Moduluaren ikono ofiziala aplikazioen taulan
├── views/
│   ├── ikastetxea_views.xml        # Ikastetxeen zerrenda, formulario eta bilaketa bistak
│   ├── gela_views.xml              # Gelen zerrenda, formulario eta bilaketa bistak
│   └── menu_views.xml              # Menu nagusia eta azpimenu hierarkikoak
├── .gitignore                      # Git-eko fitxategi baztergarriak
├── __init__.py                     # Moduluaren hasieratzailea
├── __manifest__.py                 # Odoo 17 manifestua
└── README.md                       # Dokumentazio osoa
```

---

## 📊 Datu-Ereduen Xehetasunak (Models)

### 1. `ikastetxeak.ikastetxea` (Ikastetxeak)
Ikastetxe bakoitzaren informazioa biltzen du:
* `name` (*Char*, Beharrezkoa): Ikastetxearen izena (adib. *Zornotza*).
* `kodea` (*Char*, Beharrezkoa, Bakarra): Ikastetxearen kode ofiziala (adib. *102*).
* `helbidea` (*Char*): Kokaleku fisikoa edo helbidea.
* `telefonoa` (*Char*): Harremanetarako telefonoa.
* `emaila` (*Char*): Harremanetarako posta elektronikoa.
* `webgunea` (*Char*): Ikastetxearen web ataria.
* `deskribapena` (*Text*): Ikastetxeari buruzko informazio osagarria.
* `gela_ids` (*One2many* -> `ikastetxeak.gela`): Ikastetxe honi lotutako gela guztiak.
* `gela_kopurua` (*Integer*, Kalkulatua): Ikastetxean erregistratutako gela kopurua.

### 2. `ikastetxeak.gela` (Gelak)
Ikastetxeetako ikasgela eta espazioak kudeatzen ditu:
* `name` (*Char*, Beharrezkoa): Gelaren izena (adib. *Ethazi*).
* `edukiera` (*Integer*): Gelaren ikasle/pertsona kopuru maximoa (adib. *50*).
* `baliabideak` (*Text*): Gelan eskuragarri dauden baliabideak (adib. *proiektorea, ordenagailuak...*).
* `kokalekua` (*Char*): Gelaren kokapena eraikinean (adib. *lehen solairua*).
* `erabilgarri` (*Boolean*): Gela libre edo erabilgarri dagoen adierazten du (Checkbox).
* `ikastetxe_id` (*Many2one* -> `ikastetxeak.ikastetxea`, Beharrezkoa): Zein ikastetxetakoa den.
* `ikastetxe_izena` (*Char*, Erlazionatua / *Related*): Ikastetxearen kodea automatikoki lortzen du (`related="ikastetxe_id.kodea"`), formularioan eta zerrendan erakutsiz.
* `action_erreserbatu()`: Zerrendako *Erreserbatu* botoiaren ekintza.
* `action_erreserbatu_wizard()`: Zerrendako *ErreserbatuWizard* botoiaren ekintza.

---

## 🖥️ Menuen Egitura

Pantaila-argazkian agertzen den hierarkia zehatza inplementatu da:

```text
[Ikastetxeak_Kudeatu] (Menu Nagusia)
│
├── [Ikastetxeak] (1. Azpimenua)
│   └── [Ikastetxe zerrenda]  ──► Ikastetxeen Zerrenda eta Formularioa
│
└── [Gelak] (2. Azpimenua)
    ├── [Erreserbak]          ──► Erreserben kudeaketa (etorkizuneko faseak)
    └── [Gela zerrenda]       ──► ikastetxekoGelak window (Gelen Zerrenda eta Formularioa)
```

---

## 🚀 Nola Instalatu Odoo 17 Zerbitzarian

1. **Biltegia klonatu** Odooren gehigarrien direktorioan (`addons_path`):
   ```bash
   cd /opt/odoo/custom_addons
   git clone https://github.com/balvarezech/Gelen-kudeaketa.git gelen_kudeaketa
   ```

2. **Odoo Zerbitzaria berrabiarazi**:
   ```bash
   sudo systemctl restart odoo17
   # Edo kontsolatik zuzenean exekutatzen bada:
   # ./odoo-bin -c /etc/odoo17.conf -u gelen_kudeaketa
   ```

3. **Modulua Odoon kargatu**:
   * Sartu Odoon administratzaile gisa.
   * Aktibatu Garatzaile Modua (*Developer Mode*): `Ezarpenak` -> `Garatzaile modua aktibatu`.
   * Joan `Aplikazioak` menura eta egin klik goiko **`Eguneratu Aplikazio Zerrenda`** botoian.
   * Bilaketa-barran kendu *Aplikazioak* iragazkia eta bilatu `Gelen Kudeaketa` edo `gelen_kudeaketa`.
   * Egin klik **`Instalatu`** botoian.

---

## 👥 Egilea eta Lizentzia

* **Egilea**: balvarezech
* **Erakundea**: CIFP Zornotza LHII (FP Zornotza)
* **Bertsioa**: Odoo 17.0 Community / Enterprise
* **Lizentzia**: LGPL-3
