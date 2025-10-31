import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------------
# Seiteneinstellungen & Formatierung (Page Settings & Styling)
# ------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="Exponentielle Kräfte erleben",
    page_icon="🚀"
)

# Custom CSS für ein ansprechendes dunkles Theme und verbesserte Lesbarkeit
# Die Verwendung von unsafe_allow_html=True ist hier unkritisch,
# da der CSS-Inhalt statisch ist und nicht von Benutzereingaben stammt,
# wodurch kein Sicherheitsrisiko (z.B. XSS) entsteht.
st.markdown(
    """
    <style>
        /* BASE STYLES FÜR DEN GESAMTEN BODY */
        body {
            background: #10131a; /* Sehr dunkler Hintergrund für guten Kontrast */
            color: #f5f7fb; /* Standardtextfarbe: sehr helles Grau */
            font-family: 'Inter', 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif; /* Moderne, gut lesbare Sans-Serif-Schriften */
            line-height: 1.6; /* Verbesserter Zeilenabstand für bessere Lesbarkeit von Textblöcken */
            font-size: 1rem; /* Basis-Schriftgröße (oft 16px), gut lesbar */
        }
        
        /* Allgemeine Absatzstile für konsistente Lesbarkeit */
        p {
            line-height: 1.6; /* Übernimmt Zeilenabstand vom Body, kann hier spezifisch angepasst werden */
            margin-bottom: 0.8em; /* Abstand zwischen Absätzen für bessere Texttrennung */
        }

        /* STREAMLIT BLOCK CONTAINER OVERRIDES (Hauptinhaltsbereich) */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            color: #f5f7fb; /* Stellt sicher, dass Text im Hauptinhaltsbereich hell ist */
        }

        /* SPEZIFISCHE TEXTELEMENTE & KOMPONENTEN */
        .headline-gradient {
            font-size: 3rem;
            font-weight: 800;
            background: -webkit-linear-gradient(120deg, #9be15d, #00c6ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.3rem;
        }
        .subheadline {
            text-align: center;
            font-size: 1.2rem;
            color: #d0d4e4; /* Helleres Grau, guter Kontrast */
            margin-bottom: 2rem;
        }
        .intro-card {
            background: linear-gradient(135deg, rgba(105,130,255,0.25), rgba(0,28,70,0.55));
            border-radius: 16px;
            padding: 1.1rem 1.6rem;
            margin-bottom: 1.2rem;
            box-shadow: 0 12px 35px rgba(0,0,0,0.35);
        }
        .story-card {
            background: linear-gradient(135deg, rgba(180,192,255,0.16), rgba(55,76,128,0.12));
            border-radius: 18px;
            padding: 1.5rem 2rem;
            box-shadow: 0 14px 45px rgba(15, 32, 67, 0.35);
            margin-bottom: 1.5rem;
            color: #f5f7fb;
        }
        .story-quote {
            font-style: italic;
            color: #d8def2; /* Leicht bläuliches Hellgrau für Zitate */
        }
        .metric-container .stMetric {
            background: rgba(10,15,25,0.75);
            border-radius: 16px;
            padding: 1.1rem;
            box-shadow: inset 0 0 0 1px rgba(155,225,93,0.25);
            color: #f5f7fb; /* Sicherstellen, dass Metrik-Werte hell sind */
        }
        .footer-message {
            text-align: center;
            font-size: 1.15rem;
            color: #9be15d; /* Helles Grün, guter Kontrast und Akzentfarbe */
            font-weight: 600;
        }

        /* BILDER UND BILDUNTERSCHRIFTEN */
        .image-frame {
            width: 100%;
            padding-top: 56%; /* Behält ein Seitenverhältnis von ca. 16:9 bei */
            border-radius: 18px;
            background-size: cover;
            background-position: center;
            box-shadow: 0 18px 45px rgba(0,0,0,0.45);
            margin-bottom: 0.6rem;
        }
        .image-caption {
            text-align: center;
            font-size: 1rem; /* Leicht erhöht für bessere Lesbarkeit von Captions */
            color: #d0d4e4; /* Helleres Grau, guter Kontrast */
            margin-bottom: 1.5rem;
            line-height: 1.4; /* Etwas strafferer Zeilenabstand für Captions */
        }

        /* STREAMLIT SPEZIFISCHE KOMPONENTEN (ANPASSUNGEN FÜR LESBARKEIT) */
        .st-expander {
            background: rgba(15, 25, 42, 0.65);
            border-radius: 0.5rem; /* Runde Ecken passend zu anderen Komponenten */
            border: 1px solid rgba(155,225,93,0.15); /* Dezenter Rahmen */
        }
        .st-expander details {
            padding: 0.5rem 1rem;
            color: #f5f7fb; /* Farbe des Summary-Textes im Expander */
        }
        .st-expander details summary::marker {
            color: #9be15d; /* Farbe des Auf-/Zuklappfeils */
        }
        /* Sicherstellen, dass der Inhalt innerhalb des Expanders auch gut lesbar ist */
        .streamlit-expanderContent {
            color: #f5f7fb; /* Textfarbe für den Inhalt des Expanders */
            line-height: 1.6; /* Konsistenter Zeilenabstand */
            padding: 0.5rem 1rem 1rem; /* Innenabstand */
        }

        /* Anpassung für Streamlit's Standard-Captions (z.B. von st.caption) */
        /* Targets Streamlit's internal CSS structure for captions. May need adjustment with Streamlit updates. */
        div[data-testid="caption"] p, /* Häufig verwendeter Selector für st.caption */
        .st-emotion-cache-1wv0jxv.e1nzilhr0 { /* Fallback für Streamlit's generierte Klassen */
            font-size: 0.95rem !important; /* Etwas größer als Streamlit's Standard (ca. 0.875rem) */
            color: #d0d4e4 !important; /* Sicherstellen, dass Captions hell genug sind */
            line-height: 1.4 !important; /* Etwas straffer für Captions */
        }

        /* Anpassung für st.info, st.success, st.warning Texte */
        .stAlert {
            font-size: 1rem; /* Konsistente Schriftgröße für Alerts */
            line-height: 1.5; /* Angepasster Zeilenabstand für Alerts */
        }

    </style>
    """,
    unsafe_allow_html=True # Notwendig zum Injizieren von benutzerdefiniertem CSS
)

# ------------------------------------------------------
# Hilfsfunktionen (Helper Functions)
# ------------------------------------------------------

def format_number(value: float, decimals: int = 0) -> str:
    """
    Formatiert eine Zahl mit Tausender-Trennzeichen und Dezimalstellen,
    unter Verwendung des deutschen Lokals (Komma für Dezimal, Punkt für Tausender).

    Args:
        value (float): Die zu formatierende Zahl.
        decimals (int): Anzahl der Dezimalstellen. Standardwert ist 0.

    Returns:
        str: Die formatierte Zahl als String.
    """
    # Ersetzt Tausender-Trennzeichen (Komma) durch X, Dezimalpunkt durch Komma, X wieder durch Punkt
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")

def human_number(value: float) -> str:
    """
    Formatiert eine Zahl in einen menschenlesbaren String mit Suffixen (z.B. Mio., Mrd.).
    Verwendet deutsches Zahlenformat.

    Args:
        value (float): Die zu formatierende Zahl.

    Returns:
        str: Die menschenlesbare Zahl als String.
    """
    thresholds = [
        (1e12, " Bio."),
        (1e9,  " Mrd."),
        (1e6,  " Mio."),
        (1e3,  " Tsd.")
    ]
    for threshold, suffix in thresholds:
        if abs(value) >= threshold:
            formatted = value / threshold
            return f"{formatted:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".") + suffix
    return f"{value:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")

def best_comparison(value: float, comparison_list: list[tuple[str, float]]) -> str:
    """
    Vergleicht einen Wert mit einer Liste von Referenzwerten und gibt den am besten
    passenden Vergleichsstring zurück (z.B. "5.2× Eiffelturm").

    Args:
        value (float): Der zu vergleichende Wert.
        comparison_list (list[tuple[str, float]]): Eine Liste von Tupeln, wobei jedes Tupel
                                                    (Bezeichnung: str, Referenzwert: float) enthält.

    Returns:
        str: Ein Vergleichsstring.
    """
    if value <= 0:
        label, _= comparison_list[0]
        return f"0× {label}" # Bei Null oder negativen Werten, 0 mal die kleinste Einheit zurückgeben
    
    # Vergleichsliste nach Referenzwert sortieren, um die beste Übereinstimmung zu finden
    comparison_list = sorted(comparison_list, key=lambda x: x[1])

    # Von der größten zur kleinsten Referenz iterieren
    for label, ref in reversed(comparison_list):
        if value >= ref:
            factor = value / ref
            return f"{format_number(factor, 1)}× {label}"
    
    # Wenn der Wert kleiner als alle Referenzen ist, mit der kleinsten vergleichen
    label, ref = comparison_list[0]
    factor = value / ref
    return f"{format_number(factor, 1)}× {label}"

# ------------------------------------------------------
# UI-Hilfskomponenten (UI Helper Components)
# Abstraktion für häufige UI-Muster zur Verbesserung der Lesbarkeit und Konsistenz.
# ------------------------------------------------------

def render_cover_image(url: str, caption: str):
    """
    Rendert ein gestyltes Titelbild mit Bildunterschrift.

    Args:
        url (str): Die URL des Bildes.
        caption (str): Die Bildunterschrift.
    """
    # HTML ist hartcodiert und kontrolliert, daher hier sicher.
    st.markdown(
        f"""
        <div class="image-frame" style="background-image: url('{url}');"></div>
        <p class="image-caption">{caption}</p>
        """,
        unsafe_allow_html=True
    )

def render_intro_card(text: str):
    """
    Rendert einen Einführungstextblock in einer gestylten Karte.

    Args:
        text (str): Der Textinhalt für die Einführungskarte.
    """
    # HTML ist hartcodiert und kontrolliert, daher hier sicher.
    st.markdown(f"<div class='intro-card'><p>{text}</p></div>", unsafe_allow_html=True) # Text in p-Tag für Zeilenabstand

def render_story_card(text: str):
    """
    Rendert einen Story-Textblock in einer gestylten Karte.

    Args:
        text (str): Der Textinhalt für die Story-Karte. Kann HTML für Zitate usw. enthalten.
    """
    # HTML ist hartcodiert und kontrolliert, daher hier sicher.
    st.markdown(f"<div class='story-card'>{text}</div>", unsafe_allow_html=True)

# ------------------------------------------------------
# Konstanten (Constants)
# Häufig verwendete oder konfigurationsähnliche Werte zentralisieren.
# ------------------------------------------------------

# Bild-URLs für bessere Organisation
IMAGE_URLS = {
    "schachbrett": "https://i.postimg.cc/gjrmYdF2/pierre-bamin-Ldilh-Dx3sk-unsplash.jpg",
    "zinseszins": "https://i.postimg.cc/ZRR1Ncf3/andre-taissin-5OUMf1Mr5p-U-unsplash.jpg",
    "viral": "https://i.postimg.cc/76jwYdxh/fusion-medical-animation-rnr8D3FNUNY-unsplash.jpg",
    "saas": "https://i.postimg.cc/BbWfGFgr/austin-distel-rxp-Th-Owu-Vg-E-unsplash.jpg",
    "hero": "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?auto=format&fit=crop&w=1600&q=80"
}

# ------------------------------------------------------
# Hero-Bereich (Hero Section)
# ------------------------------------------------------
st.markdown('<div class="headline-gradient">Exponentielle Kräfte erleben</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheadline">'
    'Vier immersive Geschichten, die Exponentialität emotional erfahrbar machen.'
    '</div>',
    unsafe_allow_html=True
)

hero_col1, hero_col2 = st.columns([5, 4])
with hero_col1:
    render_story_card(
        """
        <p class="story-quote">
        „In meinen ersten Semestern dachte ich, 20 % Wachstum klingt nett – heute weiß ich, dass es ganze Geschäftsmodelle sprengt.“
        </p>
        <p>
        Genau dieses Aha-Erlebnis liefern wir: vom legendären Schachbrett über Zinseszins und virale Netzwerke bis zum Hypergrowth eines SaaS-Startups.
        Jedes Modul erzählt eine Szene, visualisiert Daten und verankert das Mindset hinter exponentiellen Prozessen.
        </p>
        """
    )
with hero_col2:
    render_cover_image(
        IMAGE_URLS["hero"],
        "Wenn Wachstum explodiert, verändern sich Welten."
    )
st.markdown("---")

# Tabs zur Navigation zwischen den Geschichten
tab1, tab2, tab3, tab4 = st.tabs([
    "🌾 Schachbrett-Legende",
    "💰 Zinseszins vs. Zeit",
    "🌐 Viraler Dominoeffekt",
    "🚀 SaaS-Hypergrowth"
])

# ------------------------------------------------------
# Tab 1: Schachbrett-Legende
# ------------------------------------------------------
with tab1:
    render_intro_card(
        "Am Morgen der Audienz tritt ein Gelehrter vor den König und präsentiert das Schachspiel. "
        "Als Belohnung verlangt er nur Reis auf den Feldern des Brettes – jedes Mal doppelt so viel wie zuvor. "
        "Der Hof schmunzelt, ahnt aber nicht, dass diese Verdopplung das Reich an den Rand der Kapitulation bringt."
    )
    render_cover_image(
        IMAGE_URLS["schachbrett"],
        "Reis, soweit das Auge reicht – und doch nur ein Vorgeschmack auf Exponentialität."
    )
    render_story_card(
        """
        In alten Chroniken heißt es, der König lachte über den „bescheidenen“ Wunsch nach verdoppelten Reiskörnern pro Feld.
        Doch nach wenigen Reihen füllten sich Scheunen, Speicher und schließlich ganze Städte. Erst dann begriff der Hof,
        welche Macht in einer einfachen Verdopplung steckt.
        """
    )

    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.subheader("Einstellbare Szene")
        feld_nummer = st.slider("Wähle ein Feld (1–64)", min_value=1, max_value=64, value=32, step=1)
        
        # Berechnungen für die Schachbrett-Legende
        koerner_auf_feld = 2 ** (feld_nummer - 1)
        koerner_gesamt = 2 ** feld_nummer - 1 # Summe aller Körner bis zu diesem Feld
        
        gewicht_pro_korn_g = 0.025 # Gramm
        gewicht_tonnen = koerner_gesamt * gewicht_pro_korn_g / 1_000_000 # Umrechnung von Gramm in Tonnen
        
        flaeche_pro_korn_cm2 = 0.3 # cm²
        flaeche_m2 = koerner_gesamt * flaeche_pro_korn_cm2 / 10_000 # Umrechnung von cm² in m²
        
        # Vergleichslisten für Metriken
        gewicht_vergleiche = [
            ("40-Tonnen-Lkw", 40), # 40 Tonnen
            ("Eiffelturm", 10_100), # 10.100 Tonnen
            ("Cheops-Pyramide", 5_750_000), # 5,75 Millionen Tonnen
            ("Weltreisproduktion (Jahr)", 520_000_000), # ca. 520 Millionen Tonnen (2023)
        ]
        flaechen_vergleiche = [
            ("Basketballfeld", 420), # ~420 m²
            ("Frankfurter Römerberg", 7_000), # ~7.000 m²
            ("Frankfurter Flughafen", 2_300_000), # ~2,3 Millionen m²
        ]

    with col2:
        st.subheader(f"Feld {feld_nummer} im Fokus")
        
        # Anzeige der Metriken in einer strukturierten Weise
        metric_row = st.columns(3, gap="large")
        metric_row[0].metric("Reiskörner auf dem Feld", human_number(koerner_auf_feld))
        metric_row[1].metric("Kumuliert bis Feld", human_number(koerner_gesamt))
        metric_row[2].metric("Gewicht (t)", human_number(gewicht_tonnen))
        
        caption_row = st.columns(3, gap="large")
        caption_row[0].caption(f"Exakt: {format_number(koerner_auf_feld)} Körner")
        caption_row[1].caption(f"Exakt: {format_number(koerner_gesamt)} Körner")
        caption_row[2].caption(f"Exakt: {format_number(gewicht_tonnen, 2)} t")
        
        metric_row2 = st.columns(2, gap="large")
        metric_row2[0].metric("Gewichtsvergleich", best_comparison(gewicht_tonnen, gewicht_vergleiche))
        metric_row2[1].metric("Flächenbedarf", best_comparison(flaeche_m2, flaechen_vergleiche))
        
        caption_row2 = st.columns(2, gap="large")
        caption_row2[0].caption("Referenzen: 40 t – 520 Mio. t (Weltreisproduktion)")
        caption_row2[1].caption("Referenzen: 420 m² (Basketballfeld) – 2.3 Mio. m² (Flughafen)")
        
        st.caption("Der Großteil des Reisbergs entsteht auf den letzten Feldern – ein klassisches Merkmal exponentieller Prozesse.")
    
    with st.expander("Visualisierung & Details"):
        # DataFrame für die Plot-Erstellung
        df_chessboard = pd.DataFrame({
            "Feld": range(1, 65),
            "Reiskörner": [2 ** (i - 1) for i in range(1, 65)],
            "Kumuliert": [2 ** i - 1 for i in range(1, 65)]
        })
        
        fig = px.line(
            df_chessboard[df_chessboard["Feld"] <= feld_nummer],
            x="Feld",
            y=["Reiskörner", "Kumuliert"],
            labels={"value": "Anzahl der Reiskörner", "variable": "Sicht"},
            title="Exponentielles Wachstum auf dem Schachbrett",
            log_y=True # Logarithmische Skala ist essentiell für die Darstellung exponentiellen Wachstums
        )
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified" # Verbessert die Lesbarkeit beim Hovern über mehrere Linien
        )
        st.plotly_chart(fig, use_container_width=True)
        st.info("Hinweis: Eine logarithmische Skala ist nötig, um das enorme Wachstum auf den späteren Feldern sichtbar zu machen. Auf einer linearen Skala wären die früheren Felder kaum zu erkennen.")

# ------------------------------------------------------
# Tab 2: Zinseszins vs. Zeit (Compound Interest vs. Time)
# ------------------------------------------------------
with tab2:
    render_intro_card(
        "Frankfurt, Rooftop-Bar: Zwei Absolventen stoßen auf ihren Karrierestart an. "
        "Beide haben gleich viel gespart – doch nur eine Person hat ihre Zinsen stets reinvestiert. "
        "Im Abendlicht offenbart der Depotvergleich, wie stark Exponentialität Vermögen treibt."
    )
    render_cover_image(
        IMAGE_URLS["zinseszins"],
        "Der Zinseszins ist der leise Architekt beim Vermögensaufbau."
    )
    render_story_card(
        """
        Lara lässt jeden Ertrag im Depot, Tim investiert gleich viel, gönnt sich aber jährlich die Zinsen.
        25 Jahre später zeigt die Skyline, wie weit Exponentialität Lara getragen hat – Tims Depot blieb linear.
        """
    )
    
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.subheader("Finanzielle Ausgangslage")
        startkapital = st.number_input("Startkapital (€)", min_value=0, max_value=500_000, value=5_000, step=500)
        sparrate = st.slider("Monatliche Sparrate (€)", min_value=0, max_value=5_000, value=400, step=50)
        laufzeit = st.slider("Laufzeit (Jahre)", min_value=5, max_value=50, value=25)
        zinssatz = st.slider("Jährlicher Zinssatz (%)", min_value=0.0, max_value=18.0, value=7.0, step=0.5)
        
        # Korrigierte Berechnungen für Zinseszins- und lineares Szenario
        jahre = list(range(laufzeit + 1))
        kapital_zinseszins = [float(startkapital)] # Laras Kapital (Zinseszins)
        kapital_lineares_sparen = [float(startkapital)] # Tims Kapital (lineares Sparen)
        eingezahlt_total = [float(startkapital)] # Summe der eigenen Einzahlungen (Start + Sparraten)
        
        for jahr in range(1, laufzeit + 1):
            # Laras Kapital: Vorheriges Kapital + jährliche Sparrate * 12, dann Zins angewendet
            kapital_zinseszins.append((kapital_zinseszins[-1] + sparrate * 12) * (1 + zinssatz / 100))
            
            # Gesamte Eigenleistung bis zum aktuellen Jahr
            eingezahlt_total.append(float(startkapital + sparrate * 12 * jahr))
            
            # Tims Kapital: Startkapital + jährliche Sparrate * 12 + einfache Zinsen auf Startkapital
            # Die Zinsen auf das Startkapital werden hier als "einfache Zinsen" (simple interest) betrachtet,
            # da Tim sich die jährlichen Zinsen gönnt und sie nicht reinvestiert.
            zinsen_einfach_tim = startkapital * (zinssatz / 100) * jahr
            kapital_lineares_sparen.append(float(startkapital + (sparrate * 12 * jahr) + zinsen_einfach_tim))

        endkapital_lara = kapital_zinseszins[-1]
        eigenleistung_kumuliert = eingezahlt_total[-1] # Gesamtes vom Nutzer eingezahltes Geld
        zinsgewinne_lara = endkapital_lara - eigenleistung_kumuliert
        
        endkapital_tim = kapital_lineares_sparen[-1]
        vorsprung_lara_vs_tim = endkapital_lara - endkapital_tim

    with col2:
        st.subheader("Vermögensreise über die Jahre")
        plot_df_finanzen = pd.DataFrame({
            "Jahr": jahre,
            "Zinseszins (Lara)": kapital_zinseszins,
            "Nur eingezahlt": eingezahlt_total,
            "Lineares Sparen (Tim)": kapital_lineares_sparen
        })
        
        fig = px.line(
            plot_df_finanzen,
            x="Jahr",
            y=["Zinseszins (Lara)", "Nur eingezahlt", "Lineares Sparen (Tim)"],
            labels={"value": "Kapital in €", "variable": "Szenario"},
            title="Zinseszins vs. Lineares Sparen"
        )
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("---")
        st.subheader(f"Bilanz nach {laufzeit} Jahren")
        cols = st.columns(4, gap="large")
        cols[0].metric("Gesamtvermögen (Lara)", human_number(endkapital_lara))
        cols[1].metric("Eigenleistung (gesamt)", human_number(eigenleistung_kumuliert))
        cols[2].metric("Erarbeitete Zinsen", human_number(zinsgewinne_lara))
        cols[3].metric("Vorsprung ggü. Tim", human_number(vorsprung_lara_vs_tim))
        
        cap_cols = st.columns(4, gap="large")
        cap_cols[0].caption(f"Exakt: {format_number(endkapital_lara, 2)} €")
        cap_cols[1].caption(f"Exakt: {format_number(eigenleistung_kumuliert, 2)} €")
        cap_cols[2].caption(f"Exakt: {format_number(zinsgewinne_lara, 2)} €")
        cap_cols[3].caption(f"Exakt: {format_number(vorsprung_lara_vs_tim, 2)} €")
        
        if zinsgewinne_lara > eigenleistung_kumuliert:
            st.success("Herzlichen Glückwunsch! Ihr Kapital arbeitet härter als Ihre Einzahlungen – die exponentielle Phase ist erreicht.")
        else:
            st.info("Noch überwiegen die Eigenleistungen die Zinsgewinne. Bleiben Sie geduldig, mit der Zeit kehrt sich das Verhältnis um!")

# ------------------------------------------------------
# Tab 3: Viraler Dominoeffekt (Viral Domino Effect)
# ------------------------------------------------------
with tab3:
    render_intro_card(
        "Ein Startup veröffentlicht seine nachhaltige Kreditkarte in Social Media. "
        "Ein einziger Post entfacht eine Kette: Jede Kundin überzeugt weitere Freundinnen – "
        "die Monitoring-Screens im Headquarter leuchten und das Support-Team kommt ins Schwitzen."
    )
    render_cover_image(
        IMAGE_URLS["viral"],
        "Wenn eine Idee den Nerv trifft, vervielfacht sie sich in Wellen."
    )
    render_story_card(
        """
        <p>Die Kampagne trifft einen Nerv: Jeder neue Kunde bringt durchschnittlich 1,7 weitere mit.</p>
        <p>In wenigen Wellen schießt die Nutzung durch die Decke – Netzwerkeffekte in Reinform.</p>
        """
    )
    
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.subheader("Netzwerk-Dynamik")
        starter_personen = st.number_input("Initiale Personen", min_value=1, max_value=1_000, value=50, step=10)
        multiplikator = st.slider("Multiplikator pro Welle", min_value=0.5, max_value=5.0, value=1.7, step=0.1)
        anzahl_wellen = st.slider("Anzahl Wellen", min_value=1, max_value=40, value=15)
        
        runden_liste = list(range(1, anzahl_wellen + 1))
        neu_erreicht_pro_runde = []
        kumulativ_erreicht = []
        
        total_erreicht_kumuliert = 0

        for i in range(anzahl_wellen):
            # Die exponentielle Formel für die Anzahl der Personen in Welle 'i' (beginnend bei 0)
            # Welle 0 (oder 1 im UI): starter_personen * (multiplikator^0) = starter_personen
            # Welle 1 (oder 2 im UI): starter_personen * (multiplikator^1)
            # usw.
            personen_in_aktueller_welle = starter_personen * (multiplikator ** i) 
            
            neu_erreicht_pro_runde.append(personen_in_aktueller_welle)
            total_erreicht_kumuliert += personen_in_aktueller_welle
            kumulativ_erreicht.append(total_erreicht_kumuliert)
        
        gesamt_personen_erreicht = kumulativ_erreicht[-1] if kumulativ_erreicht else 0
        personen_letzte_welle = neu_erreicht_pro_runde[-1] if neu_erreicht_pro_runde else 0
        anteil_letzte_welle_gesamt = personen_letzte_welle / gesamt_personen_erreicht if gesamt_personen_erreicht else 0
        
        vergleich_pop = [
            ("Deutsche Bank Park", 51_500), # Stadionkapazität
            ("Stadt Frankfurt", 771_000), # Einwohnerzahl Frankfurt
            ("Region Rhein-Main", 5_800_000), # Einwohnerzahl Rhein-Main
            ("Deutschland", 84_000_000), # Einwohnerzahl Deutschland
        ]

    with col2:
        st.subheader("Ausbreitung pro Welle")
        viral_df = pd.DataFrame({
            "Runde": runden_liste,
            "Neu erreicht": neu_erreicht_pro_runde,
            "Gesamt erreicht": kumulativ_erreicht
        })
        
        fig = px.bar(
            viral_df,
            x="Runde",
            y="Neu erreicht",
            title="Neu erreichte Personen pro Welle",
            labels={"Neu erreicht": "Anzahl Personen"}
        )
        fig.update_traces(marker_color="#00c6ff")
        fig.update_layout(hovermode="x unified")
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("---")
        st.subheader("Resultierende Reichweite")
        cols = st.columns(3, gap="large")
        cols[0].metric("Gesamt erreicht", human_number(gesamt_personen_erreicht))
        cols[1].metric("Vergleich", best_comparison(gesamt_personen_erreicht, vergleich_pop))
        cols[2].metric("Anteil letzte Welle", f"{anteil_letzte_welle_gesamt:.0%}")
        
        cap_cols = st.columns(3, gap="large")
        cap_cols[0].caption(f"Exakt: {format_number(gesamt_personen_erreicht, 0)} Personen")
        cap_cols[1].caption("Vergleiche: Stadion – Nation")
        cap_cols[2].caption("Anteil am gesamten Wachstum")
        
        if multiplikator <= 1:
            st.warning("Achtung: Ein Multiplikator von ≤ 1 bedeutet, dass der Trend ausläuft und sich nicht exponentiell verbreitet. Exponentielles Momentum beginnt erst jenseits von 1.")
        else:
            st.caption("Ein großer Teil der Gesamtlast (z.B. für Support oder Infrastruktur) fällt oft in die letzten Wellen – eine vorausschauende Planung ist entscheidend.")

# ------------------------------------------------------
# Tab 4: SaaS-Hypergrowth (SaaS Hypergrowth)
# ------------------------------------------------------
with tab4:
    render_intro_card(
        "Pitch-Deck im Boardroom: Das junge SaaS-Team zeigt 12 % monatliches Wachstum. "
        "Ein Investor hebt die Augenbrauen – denn 12 % im Monat bedeutet eine Verdopplung in sechs Monaten. "
        "Cashflow, Server, Hiring – alles muss in exponentiellen Kategorien gedacht werden."
    )
    render_cover_image(
        IMAGE_URLS["saas"],
        "Wenn Product-Market-Fit trifft, rast das Wachstum wie eine Rakete."
    )
    render_story_card(
        """
        <p>Der 3D-holografische MRR-Chart schießt wie eine Rakete nach oben.</p>
        <p>Das Team spürt: Jetzt entscheidet die Fähigkeit, exponentielles Wachstum zu managen – nicht nur zu wünschen.</p>
        """
    )
    
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.subheader("Monatliche Kennzahlen")
        start_mrr = st.number_input("Startumsatz (MRR in €)", min_value=1_000, max_value=1_000_000, value=25_000, step=1_000)
        monatliche_wachstumsrate = st.slider("Monatliches Wachstum (%)", min_value=0.0, max_value=35.0, value=12.0, step=0.5)
        monate_planungszeitraum = st.slider("Planungszeitraum (Monate)", min_value=6, max_value=60, value=36, step=6)
        lineares_ziel_delta_mrr = st.slider("Lineares Monatsziel (Δ MRR)", min_value=0, max_value=200_000, value=10_000, step=1_000)
        
        monate_liste = list(range(monate_planungszeitraum + 1))
        mrr_exponentiell = [float(start_mrr)] # Exponentielles Wachstum
        mrr_linear = [float(start_mrr)] # Lineares Wachstum
        
        for m in range(1, monate_planungszeitraum + 1):
            mrr_exponentiell.append(mrr_exponentiell[-1] * (1 + monatliche_wachstumsrate / 100))
            mrr_linear.append(start_mrr + lineares_ziel_delta_mrr * m) # Lineares Wachstum addiert einen festen Betrag
            
        gesamt_mrr_exponentiell = mrr_exponentiell[-1]
        gesamt_mrr_linear = mrr_linear[-1]
        
        kumulatives_wachstum_gesamt = gesamt_mrr_exponentiell - start_mrr
        
        # Wachstum im letzten Monat des Planungszeitraums
        zuwachs_letzter_monat = mrr_exponentiell[-1] - mrr_exponentiell[-2] if len(mrr_exponentiell) > 1 else 0
        anteil_zuwachs_letzter_monat = zuwachs_letzter_monat / kumulatives_wachstum_gesamt if kumulatives_wachstum_gesamt > 0 else 0
        
        st.subheader("Personalplanung")
        team_aktuelle_fte = st.slider("Aktuelle FTE (Full-Time Equivalents)", min_value=3, max_value=200, value=12)
        mrr_pro_fte_produktivitaet = st.slider("MRR pro FTE (€/Monat)", min_value=1_000, max_value=30_000, value=12_000, step=1_000)
        
        erforderliche_fte_am_ende = gesamt_mrr_exponentiell / mrr_pro_fte_produktivitaet
        
        # Wie viele zusätzliche FTEs werden benötigt, um das exponentielle Wachstum zu bewältigen
        zus_fte_benoetigt = max(erforderliche_fte_am_ende - team_aktuelle_fte, 0)

    with col2:
        st.subheader("MRR-Prognose: exponentiell vs. linear")
        saas_df = pd.DataFrame({
            "Monat": monate_liste,
            "Exponentielles Wachstum": mrr_exponentiell,
            "Lineares Ziel": mrr_linear
        })
        
        fig = px.line(
            saas_df,
            x="Monat",
            y=["Exponentielles Wachstum", "Lineares Ziel"],
            labels={"value": "MRR in €", "variable": "Szenario"},
            title="Monatlich wiederkehrender Umsatz (MRR) Entwicklung"
        )
        fig.update_layout(
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("---")
        st.subheader("Investor-Ready KPIs")
        cols = st.columns(4, gap="large")
        cols[0].metric("MRR nach Plan", human_number(gesamt_mrr_exponentiell))
        cols[1].metric("Lineares Ziel (MRR)", human_number(gesamt_mrr_linear))
        cols[2].metric("Zusätzliche FTE benötigt", human_number(zus_fte_benoetigt))
        cols[3].metric("Wachstum im letzten Monat", f"{anteil_zuwachs_letzter_monat:.0%}")
        
        cap_cols = st.columns(4, gap="large")
        cap_cols[0].caption(f"Exakt: {format_number(gesamt_mrr_exponentiell, 0)} €")
        cap_cols[1].caption(f"Exakt: {format_number(gesamt_mrr_linear, 0)} €")
        cap_cols[2].caption(f"Gesamtbedarf: {format_number(erforderliche_fte_am_ende, 1)} FTE")
        cap_cols[3].caption("Anteil am kumulierten Wachstum im Planzeitraum")
        
        if monatliche_wachstumsrate <= 0:
            st.warning("Ein monatliches Wachstum von ≤ 0% bedeutet Stagnation oder Rückgang. Exponentielles Wachstum erfordert positive Raten.")
        else:
            st.caption("Ein erheblicher Teil des Gesamtwachstums fällt in die letzten Monate des Planungszeitraums – Hypergrowth erfordert proaktive Planung in allen Unternehmensbereichen.")

# ------------------------------------------------------
# Abschluss (Conclusion)
# ------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div class="footer-message">
        Exponentielle Prozesse belohnen Geduld, Systematik und Vorbereitung.
        Wer sie unterschätzt, verliert Kontrolle – wer sie gestaltet, gewinnt Zukunft.
    </div>
    """,
    unsafe_allow_html=True
)
