import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------------------------------------------
# Seiteneinstellungen & Formatierung
# ------------------------------------------------------
st.set_page_config(
    layout="wide",
    page_title="Exponentielle Kräfte erleben",
    page_icon="🚀"
)

st.markdown(
    """
    <style>
        body {
            background: #f4f6fb;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .headline-gradient {
            font-size: 3rem;
            font-weight: 800;
            background: -webkit-linear-gradient(120deg, #1f4b99, #01c38d);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 0.3rem;
        }
        .subheadline {
            text-align: center;
            font-size: 1.2rem;
            color: #4f5d75;
            margin-bottom: 2rem;
        }
        .story-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,255,255,0.75));
            border-radius: 18px;
            padding: 1.5rem 2rem;
            box-shadow: 0 14px 45px rgba(15, 32, 67, 0.12);
            margin-bottom: 1.5rem;
        }
        .story-card strong {
            color: #1f4b99;
        }
        .story-quote {
            font-style: italic;
            color: #2b2d42;
        }
        .metric-container .stMetric {
            background: white;
            border-radius: 16px;
            padding: 1.2rem;
            box-shadow: 0 10px 30px rgba(31, 75, 153, 0.08);
        }
        .tabs-content {
            margin-top: 1rem;
        }
        .footer-message {
            text-align: center;
            font-size: 1.15rem;
            color: #1f4b99;
            font-weight: 600;
        }
        .image-frame {
            width: 100%;
            padding-top: 56%;
            border-radius: 18px;
            background-size: cover;
            background-position: center;
            box-shadow: 0 18px 45px rgba(31, 75, 153, 0.18);
            margin-bottom: 0.6rem;
        }
        .image-caption {
            text-align: center;
            font-size: 0.95rem;
            color: #4f5d75;
            margin-bottom: 1.5rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------
# Hilfsfunktionen
# ------------------------------------------------------
def format_number(value, decimals=0):
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")

def best_comparison(value, comparison_list):
    if value <= 0:
        name, reference = comparison_list[0]
        return f"0× {name}"
    sorted_comparisons = sorted(comparison_list, key=lambda x: x[1])
    for name, reference in reversed(sorted_comparisons):
        if value >= reference:
            factor = value / reference
            return f"{format_number(factor, 1)}× {name}"
    name, reference = sorted_comparisons[0]
    factor = value / reference
    return f"{format_number(factor, 1)}× {name}"

def render_cover_image(url, caption):
    st.markdown(
        f"""
        <div class="image-frame" style="background-image: url('{url}');"></div>
        <p class="image-caption">{caption}</p>
        """,
        unsafe_allow_html=True
    )

# ------------------------------------------------------
# Hero-Bereich
# ------------------------------------------------------
st.markdown('<div class="headline-gradient">Exponentielle Kräfte erleben</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subheadline">'
    'Vier immersive Geschichten, die zeigen, warum sich exponentielle Prozesse so sehr von unserer linearen Intuition unterscheiden.'
    '</div>',
    unsafe_allow_html=True
)

hero_col1, hero_col2 = st.columns([5, 4])
with hero_col1:
    st.markdown(
        """
        <div class="story-card">
            <p class="story-quote">
            „In meinen ersten Semestern dachte ich, 20 % Wachstum klingt nett – heute verstehe ich, 
            dass es mein Geschäftsmodell sprengen kann.“ 
            </p>
            <p>
            Genau diese Erkenntnis wollen wir bei Ihren Studierenden auslösen. Statt trockener Formeln tauchen wir in alltagsnahe 
            Szenarien ein: vom schicksalhaften Schachbrett über das eigene Depot bis zur viralen Idee und dem Raketenstart eines SaaS-Startups.
            </p>
            <p>
            Jede Visualisierung erzählt eine Geschichte, liefert einprägsame Bilder und packende Vergleiche. 
            Am Ende bleibt nicht nur Wissen – sondern das Gefühl, es am eigenen Leib erlebt zu haben.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
with hero_col2:
    render_cover_image(
        "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?auto=format&fit=crop&w=1600&q=80",
        "Wenn Wachstum explodiert, verändern sich Welten."
    )

st.markdown("---")

# Tabs
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
    render_cover_image(
        "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1600&q=80",
        "Reis, so weit das Auge reicht – und doch nur ein Vorgeschmack auf exponentielles Wachstum."
    )

    st.markdown(
        """
        <div class="story-card">
            <strong>Szene:</strong> Der König starrt auf das Schachbrett, das Maßband in der Hand. 
            „Ein paar Reiskörner?“, spottet er. „Schenk ihm die Scheune voller Ernte.“ 
            Doch mit jedem Feld wächst die Last – die Halle füllt sich, dann die Festung, dann die ganze Hauptstadt. 
            Die Hofbeamten simulieren das Logistik-Drama auf Papyrus, während die Händler schon den Kornpreis nach oben treiben.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.subheader("Einstellbare Szene")
        feld_nummer = st.slider("Wähle ein Feld (1–64)", 1, 64, 32)

        koerner_auf_feld = 2 ** (feld_nummer - 1)
        koerner_gesamt = 2 ** feld_nummer - 1

        gewicht_pro_korn_g = 0.025
        gewicht_tonnen = koerner_gesamt * gewicht_pro_korn_g / 1_000_000

        flaeche_pro_korn_cm2 = 0.3
        flaeche_m2 = koerner_gesamt * flaeche_pro_korn_cm2 / 10_000

        gewicht_vergleiche = [
            ("eines 40-Tonnen-Lkw", 40),
            ("des Eiffelturms (10.100 t Stahl)", 10_100),
            ("der Cheops-Pyramide (5.750.000 t)", 5_750_000),
            ("der Weltjahresproduktion an Reis 2022/23 (520 Mio. t)", 520_000_000),
        ]
        flaechen_vergleiche = [
            ("eines Basketballfelds (420 m²)", 420),
            ("des Frankfurter Römerbergs (7.000 m²)", 7_000),
            ("des Frankfurter Flughafens (2.300.000 m²)", 2_300_000),
        ]

    with col2:
        st.subheader(f"Feld {feld_nummer} im Fokus")
        metric_row_1 = st.columns(3, gap="large")
        metric_row_1[0].metric("Reiskörner auf diesem Feld", format_number(koerner_auf_feld))
        metric_row_1[1].metric("Summe bis zu diesem Feld", format_number(koerner_gesamt))
        metric_row_1[2].metric("Gewicht in Tonnen", format_number(gewicht_tonnen, 2))

        metric_row_2 = st.columns(2, gap="large")
        metric_row_2[0].metric("Gewichtsvergleich", best_comparison(gewicht_tonnen, gewicht_vergleiche))
        metric_row_2[1].metric("Flächenbedarf beim Auslegen", best_comparison(flaeche_m2, flaechen_vergleiche))

        st.write("---")
        st.caption("Der größte Teil der Gesamtmenge liegt auf den letzten Feldern – ein Paradebeispiel für den „Ketchup-Effekt“.")

    with st.expander("Visualisierung & Details"):
        df = pd.DataFrame({
            "Feld": range(1, 65),
            "Reiskörner": [2 ** (i - 1) for i in range(1, 65)],
            "Kumuliert": [2 ** i - 1 for i in range(1, 65)]
        })

        fig = px.line(
            df[df["Feld"] <= feld_nummer],
            x="Feld",
            y=["Reiskörner", "Kumuliert"],
            labels={"value": "Anzahl Reiskörner", "variable": "Sicht"},
            title="Exponentielles Wachstum auf dem Schachbrett",
            log_y=True
        )
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig, use_container_width=True)
        st.info("Logarithmische Skala notwendig, da die absoluten Werte sehr schnell explodieren.")

# ------------------------------------------------------
# Tab 2: Der Zinseszins
# ------------------------------------------------------
with tab2:
    render_cover_image(
        "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=1600&q=80",
        "Der Zinseszins ist der leise Architekt beim Vermögensaufbau."
    )

    st.markdown(
        """
        <div class="story-card">
            <strong>Szene:</strong> Zwei Kommilitonen starten mit identischem Sparplan. 
            Lara hält durch und lässt jeden Zins reinvestieren. Tim gönnt sich jährlich einen Urlaub von den Erträgen. 
            Nach 30 Jahren stehen beide auf der Dachterrasse eines Frankfurter Büroturms. 
            Während die Skyline glitzert, erkennt Tim, dass Laras Vermögen nicht doppelt, sondern um ein Vielfaches gewachsen ist.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Finanzielle Ausgangslage")
        startkapital = st.number_input("Startkapital (€)", min_value=0, max_value=500_000, value=5_000, step=500)
        sparrate = st.slider("Monatliche Sparrate (€)", 0, 5_000, 400, 50)
        laufzeit = st.slider("Laufzeit (Jahre)", 5, 50, 25)
        zinssatz = st.slider("Jährlicher Zinssatz (%)", 0.0, 18.0, 7.0, 0.5)

        jahre = list(range(laufzeit + 1))
        kapital_zz = [startkapital]
        kapital_linear = [startkapital]
        eingezahlt = [startkapital]

        for jahr in range(1, laufzeit + 1):
            kapital_zz.append((kapital_zz[-1] + sparrate * 12) * (1 + zinssatz / 100))

            eingezahlt.append(startkapital + sparrate * 12 * jahr)
            zinsen_linear = startkapital * (zinssatz / 100) * jahr
            kapital_linear.append(eingezahlt[-1] + zinsen_linear)

        endkapital = kapital_zz[-1]
        summe_eingezahlt = eingezahlt[-1]
        zinsgewinne = endkapital - summe_eingezahlt
        linear_differenz = kapital_zz[-1] - kapital_linear[-1]

    with col2:
        st.subheader("Vermögensreise über die Jahre")
        plot_df = pd.DataFrame({
            "Jahr": jahre,
            "Zinseszins": kapital_zz,
            "Nur eingezahlt": eingezahlt,
            "Lineares Sparen": kapital_linear
        })

        fig = px.line(
            plot_df,
            x="Jahr",
            y=["Zinseszins", "Nur eingezahlt", "Lineares Sparen"],
            labels={"value": "Kapital in €", "variable": "Szenario"},
            title="Zinseszins vs. lineares Sparen"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.write("---")
        st.subheader(f"Bilanz nach {laufzeit} Jahren")
        metric_col = st.columns(4, gap="large")
        metric_col[0].metric("Gesamtvermögen", f"{format_number(endkapital, 2)} €")
        metric_col[1].metric("Eigenleistung", f"{format_number(summe_eingezahlt, 2)} €")
        metric_col[2].metric("Erarbeitete Zinsen", f"{format_number(zinsgewinne, 2)} €")
        metric_col[3].metric("Vorsprung vs. linear", f"{format_number(linear_differenz, 2)} €")

        if zinsgewinne > summe_eingezahlt:
            st.success("Der Zinseszins schlägt zu: Ihr Kapital arbeitet mittlerweile härter als Sie selbst einzahlen.")

# ------------------------------------------------------
# Tab 3: Viraler Dominoeffekt
# ------------------------------------------------------
with tab3:
    render_cover_image(
        "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?auto=format&fit=crop&w=1600&q=80",
        "Wenn eine Idee den Nerv trifft, vervielfacht sie sich in Wellen."
    )

    st.markdown(
        """
        <div class="story-card">
            <strong>Szene:</strong> Die Marketingabteilung entwirft eine Kampagne für eine nachhaltige Kreditkarte. 
            Ein einziger Influencer postet darüber, ein Mikro-Community-Lead greift es auf, dann folgen Finanzblogs. 
            In der Zentrale gehen die Dashboard-Lichter an: jeder neue Kunde zieht durchschnittlich 1,7 weitere an – 
            und plötzlich reichen die geplanten Call-Center-Schichten nicht mehr.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Dynamik des Netzwerks")
        starter = st.number_input("Initiale Personen", 1, 1_000, 50, 10)
        faktor = st.slider("Multiplikator pro Welle", 0.5, 5.0, 1.7, 0.1)
        runden = st.slider("Anzahl Wellen", 1, 40, 15)

        runden_liste = list(range(1, runden + 1))
        neu = []
        kumulativ = []
        total = 0
        for i in range(runden):
            neu_in_runde = starter * (faktor ** i)
            total += neu_in_runde
            neu.append(neu_in_runde)
            kumulativ.append(total)

        gesamt = kumulativ[-1]
        share_last_wave = neu[-1] / gesamt if gesamt else 0

        vergleich_pop = [
            ("des Deutsche-Bank-Parks (51.500 Plätze)", 51_500),
            ("der Stadt Frankfurt (771.000 Ew.)", 771_000),
            ("des Großraums Rhein-Main (5,8 Mio. Ew.)", 5_800_000),
            ("der Bundesrepublik Deutschland (84 Mio. Ew.)", 84_000_000),
        ]

    with col2:
        st.subheader("Ausbreitung pro Welle")
        viral_df = pd.DataFrame({
            "Runde": runden_liste,
            "Neu erreicht": neu,
            "Gesamt erreicht": kumulativ
        })

        fig = px.bar(
            viral_df,
            x="Runde",
            y="Neu erreicht",
            title="Neu erreichte Personen pro Welle",
            labels={"Neu erreicht": "Personen"}
        )
        fig.update_traces(marker_color="#1f77b4")
        st.plotly_chart(fig, use_container_width=True)

        st.write("---")
        st.subheader("Resultierende Reichweite")
        metric_col = st.columns(3, gap="large")
        metric_col[0].metric("Gesamt erreicht", format_number(gesamt))
        metric_col[1].metric("Vergleich", best_comparison(gesamt, vergleich_pop))
        metric_col[2].metric("Anteil letzte Welle", f"{share_last_wave:.0%}")

        if faktor <= 1:
            st.warning("Mit einem Multiplikator ≤ 1 verflacht der Trend. Erst bei >1 dominiert die exponentielle Phase.")
        else:
            st.caption("Interessant: Der Großteil der Personen kommt ganz am Ende – wichtig für Kapazitätsplanung von Support & Supply.")

# ------------------------------------------------------
# Tab 4: SaaS-Hypergrowth
# ------------------------------------------------------
with tab4:
    render_cover_image(
        "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1600&q=80",
        "Wenn Product-Market-Fit trifft, rast das Wachstum wie eine Rakete."
    )

    st.markdown(
        """
        <div class="story-card">
            <strong>Szene:</strong> Ein junges SaaS-Team pitcht vor Investoren. 
            Die Folie zeigt eine „bescheidene“ monatliche Wachstumsrate von 12 %. 
            Ein Partner lächelt nachdenklich. Er skizziert auf dem iPad, dass 12 % nicht 12 Prozentpunkte bedeuten – 
            sondern eine Verdopplung alle sechs Monate. Plötzlich wird klar: Die Serverkapazitäten, das Team, ja sogar der Cashflow 
            müssen sich auf eine völlig andere Zukunft vorbereiten.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Monatliche Kennzahlen")
        start_mrr = st.number_input("Startumsatz (MRR in €)", 1_000, 1_000_000, 25_000, 1_000)
        monatliche_wachstumsrate = st.slider("Monatliches Wachstum (%)", 0.0, 35.0, 12.0, 0.5)
        monate = st.slider("Planungszeitraum (Monate)", 6, 60, 36, 6)
        lineares_ziel = st.slider("Lineares Monatsziel (Δ MRR)", 0, 200_000, 10_000, 1_000)

        monate_liste = list(range(monate + 1))
        compound_mrr = [start_mrr]
        linear_mrr = [start_mrr]

        for m in range(1, monate + 1):
            compound_mrr.append(compound_mrr[-1] * (1 + monatliche_wachstumsrate / 100))
            linear_mrr.append(start_mrr + lineares_ziel * m)

        gesamt_compound = compound_mrr[-1]
        gesamt_linear = linear_mrr[-1]
        kumulatives_wachstum = compound_mrr[-1] - start_mrr
        letzter_zuwachs = compound_mrr[-1] - compound_mrr[-2] if len(compound_mrr) > 1 else 0
        share_last_month = letzter_zuwachs / kumulatives_wachstum if kumulatives_wachstum > 0 else 0

        team_start = st.slider("Aktuelle FTE", 3, 200, 12)
        produktivitaet = st.slider("MRR pro FTE (€/Monat)", 1_000, 30_000, 12_000, 1_000)
        erforderliche_fte = gesamt_compound / produktivitaet
        fte_gap = max(erforderliche_fte - team_start, 0)

    with col2:
        st.subheader("MRR-Prognose: exponentiell vs. linear")

        saas_df = pd.DataFrame({
            "Monat": monate_liste,
            "Exponential": compound_mrr,
            "Lineares Ziel": linear_mrr
        })
        fig = px.line(
            saas_df,
            x="Monat",
            y=["Exponential", "Lineares Ziel"],
            labels={"value": "MRR in €", "variable": "Szenario"},
            title="Monatlich wiederkehrender Umsatz (MRR)"
        )
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig, use_container_width=True)

        st.write("---")
        st.subheader("Investor-Ready KPIs")
        metric_cols = st.columns(4, gap="large")
        metric_cols[0].metric("MRR nach Plan", f"{format_number(gesamt_compound, 0)} €")
        metric_cols[1].metric("Lineares Ziel", f"{format_number(gesamt_linear, 0)} €")
        metric_cols[2].metric("Zusätzliche FTE benötigt", format_number(fte_gap, 1))
        metric_cols[3].metric("Anteil letzter Monat", f"{share_last_month:.0%}")

        st.caption("Fast die Hälfte des Gesamtwachstums findet in den letzten Monaten statt – bei 12 % Wachstum multipliziert sich das Geschäft von selbst.")

# ------------------------------------------------------
# Abschluss
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
