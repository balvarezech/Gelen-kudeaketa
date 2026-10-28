# Gelen Kudeaketa (Ikastetxeak_Kudeatu) — Odoo 17

Odoo 17rako modulu pertsonalizatua, ikastetxeak, gelak eta gelen erreserbak era eraginkor eta zentralean kudeatzeko.

Proiektuaren biltegia: [https://github.com/balvarezech/Gelen-kudeaketa](https://github.com/balvarezech/Gelen-kudeaketa)

---

## 🎯 Proiektuaren Ezaugarriak

Pantaila-argazkietan eta eskakizunetan oinarrituta, **Ikastetxeak**, **Gelak** eta **Erreserbak** kudeatzeko sistema integrala garatu da:

* ✅ **Ikastetxeen zerrenda-bista (Tree/List View)**: Ikastetxe guztiak, haien kodea, kokalekua, kontaktua eta gela kopurua zerrendatuta.
* ✅ **Ikastetxeen formulario-bista (Form View)**: Datu nagusiak, kontaktu-taldea eta erlazionatutako gelen zerrenda interaktiboa (One2many bidez editagarria).
* ✅ **Gelen zerrenda-bista (Tree/List View - 5. irudia)**:
  * Zutabeak: *Gela izena*, *Ikastetxe izena*, *Ikastetxea*, `[Erreserbatu]` botoia, `[ErreserbatuWizard]` botoia, *Edukiera*, *Kokalekua*, *Erabilgarri*.
  * Leiho-ekintza: `ikastetxekoGelak window`.
* ✅ **Gelen formulario-bista (Form View - 1. eta 4. irudiak)**:
  * Ezker zutabea: *Gela izena*, *Edukiera*, *Eskuragarri dauden baliabideak*, *Kokalekua*, *Ikastetxe izena* (Related eremua).
  * Eskuin zutabea: *Ikastetxea* (Many2one), *Erabilgarri* (checkbox), *Display Name*.
  * Erreserben fitxa (Notebook / Page) eta Stat-button-a.
* ✅ **Erreserben kudeaketa eta Erreserbatu botoiak (5. irudia)**:
  * `[Erreserbatu]` botoia: Gelatik zuzenean ordu bateko erreserba azkarra sortzen du.
  * `[ErreserbatuWizard]` botoia: Modal pop-up bat irekitzen du hasiera-data, amaiera-data, erabiltzailea eta oharrak hautatuz erreserba osatzeko.
  * `ikastetxeak.erreserba` eredua: Egutegi-bista (Calendar), Zerrenda eta Formularioa egoerekin (*zirriborroa*, *baieztatua*, *baliogabetua*).
* ✅ **Menu nagusia eta azpimenuak (2. eta 3. irudiak)**:
  * `Ikastetxeak_Kudeatu` aplikazio-menua.
  * `Ikastetxeak` azpimenua -> `Ikastetxe zerrenda`.
  * `Gelak` azpimenua -> `Erreserbak` eta `Gela zerrenda`.

---

## 🗂️ Moduluaren Egitura

```text
Gelen-kudeaketa/
├── data/
│   └── demo_data.xml               # Hasierako eta frogetako datuak (Zornotza, Ethazi, Erreserbak...)
├── models/
│   ├── __init__.py                 # Ereduen inportazioak
│   ├── ikastetxea.py               # 'ikastetxeak.ikastetxea' eredua
│   ├── gela.py                     # 'ikastetxeak.gela' eredua (botoiak barne)
│   ├── erreserba.py                # 'ikastetxeak.erreserba' eredua
│   └── erreserba_wizard.py         # 'ikastetxeak.erreserba.wizard' TransientModel (morroia)
├── security/
│   └── ir.model.access.csv         # Sarbide-baimenak (base.group_user)
├── static/
│   └── description/
│       └── icon.png                # Moduluaren ikono ofiziala
├── views/
│   ├── ikastetxea_views.xml        # Ikastetxeen zerrenda, formulario eta bilaketa bistak
│   ├── gela_views.xml              # Gelen zerrenda, formulario eta bilaketa bistak (5. irudia)
│   ├── erreserba_views.xml         # Erreserben zerrenda, formulario eta egutegi bistak
│   ├── erreserba_wizard_views.xml  # Erreserba morroiaren pop-up formularioa
│   └── menu_views.xml              # Menu nagusia eta azpimenu hierarkikoak (2. eta 3. irudiak)
├── .gitignore                      # Git-eko fitxategi baztergarriak
├── __init__.py                     # Moduluaren hasieratzailea
├── __manifest__.py                 # Odoo 17 manifestua
└── README.md                       # Dokumentazio osoa
```

---

## 📊 Datu-Ereduen Xehetasunak (Models)

### 1. `ikastetxeak.ikastetxea` (Ikastetxeak)
* `name` (*Char*, Beharrezkoa): Ikastetxearen izena (adib. *Zornotza*).
* `kodea` (*Char*, Beharrezkoa, Bakarra): Ikastetxearen kode ofiziala (adib. *102*).
* `helbidea`, `telefonoa`, `emaila`, `webgunea`, `deskribapena`.
* `gela_ids` (*One2many* -> `ikastetxeak.gela`): Lotutako gelak.
* `gela_kopurua` (*Integer*, Kalkulatua): Gela kopurua.

### 2. `ikastetxeak.gela` (Gelak)
* `name` (*Char*, Beharrezkoa): Gelaren izena (adib. *Ethazi*).
* `edukiera` (*Integer*): Gelaren edukiera (adib. *50*).
* `baliabideak` (*Text*): Eskuragarri dauden baliabideak.
* `kokalekua` (*Char*): Eraikineko kokapena (adib. *lehen solairua*).
* `erabilgarri` (*Boolean*): Erabilgarri dagoen adierazteko marka.
* `ikastetxe_id` (*Many2one* -> `ikastetxeak.ikastetxea`): Zein ikastetxeri dagokion.
* `ikastetxe_izena` (*Char*, Related): `related="ikastetxe_id.kodea"`.
* `erreserba_ids` (*One2many* -> `ikastetxeak.erreserba`): Gelaren erreserbak.
* `erreserba_kopurua` (*Integer*, Kalkulatua).
* `action_erreserbatu()`: 5. irudiko `Erreserbatu` botoia.
* `action_erreserbatu_wizard()`: 5. irudiko `ErreserbatuWizard` botoia.

### 3. `ikastetxeak.erreserba` (Erreserbak)
* `name` (*Char*): Erreserbaren kodea (adib. *ERR-20261028-001*).
* `gela_id` (*Many2one* -> `ikastetxeak.gela`): Erreserbatutako gela.
* `ikastetxe_id` (*Many2one* -> `ikastetxeak.ikastetxea`, Related).
* `erabiltzaile_id` (*Many2one* -> `res.users`): Erreserbaren arduraduna.
* `hasiera_data` (*Datetime*): Erreserbaren hasiera.
* `amaiera_data` (*Datetime*): Erreserbaren amaiera.
* `oharrak` (*Text*): Xedea edo arrazoia.
* `state` (*Selection*): `zirriborroa`, `baieztatua`, `baliogabetua`.

### 4. `ikastetxeak.erreserba.wizard` (Morroia / Wizard)
* Gelaren erreserba modu interaktiboan kudeatzeko leiho ibiltaria (*TransientModel*).

---

## 🖥️ Menuen Egitura

```text
[Ikastetxeak_Kudeatu] (Menu Nagusia)
│
├── [Ikastetxeak] (1. Azpimenua)
│   └── [Ikastetxe zerrenda]  ──► Ikastetxeen Zerrenda eta Formularioa
│
└── [Gelak] (2. Azpimenua)
    ├── [Erreserbak]          ──► Erreserben Zerrenda, Formularioa eta Egutegia
    └── [Gela zerrenda]       ──► ikastetxekoGelak window (Gelen Zerrenda eta Formularioa)
```

---

## 🚀 Instalazioa

1. Biltegia klonatu edo eguneratu Odooren gehigarrien karpetan:
   ```bash
   cd /opt/odoo/custom_addons
   git clone https://github.com/balvarezech/Gelen-kudeaketa.git gelen_kudeaketa
   ```
2. Odoo berrabiarazi:
   ```bash
   sudo systemctl restart odoo17
   ```
3. Odoon Aplikazio Zerrenda eguneratu eta modulua instalatu/eguneratu.
