import streamlit as st
import pandas as pd
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
            background: #10131a;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            color: #f5f7fb;
        }
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
            color: #d0d4e4;
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
            color: #d8def2;
        }
        .metric-container .stMetric {
            background: rgba(10,15,25,0.75);
            border-radius: 16px;
            padding: 1.1rem;
            box-shadow: inset 0 0 0 1px rgba(155,225,93,0.25);
        }
        .footer-message {
            text-align: center;
            font-size: 1.15rem;
            color: #9be15d;
            font-weight: 600;
        }
        .image-frame {
            width: 100%;
            padding-top: 56%;
            border-radius: 18px;
            background-size: cover;
            background-position: center;
            box-shadow: 0 18px 45px rgba(0,0,0,0.45);
            margin-bottom: 0.6rem;
        }
        .image-caption {
            text-align: center;
            font-size: 0.95rem;
            color: #d0d4e4;
            margin-bottom: 1.5rem;
        }
        .st-expander {
            background: rgba(15, 25, 42, 0.65);
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

def human_number(value):
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

def best_comparison(value, comparison_list):
    if value <= 0:
        label, _ = comparison_list[0]
        return f"0× {label}"
    comparison_list = sorted(comparison_list, key=lambda x: x[1])
    for label, ref in reversed(comparison_list):
        if value >= ref:
            factor = value / ref
            return f"{format_number(factor, 1)}× {label}"
    label, ref = comparison_list[0]
    factor = value / ref
    return f"{format_number(factor, 1)}× {label}"

def render_cover_image(url, caption):
    st.markdown(
        f"""
        <div class="image-frame" style="background-image: url('{url}');"></div>
        <p class="image-caption">{caption}</p>
        """,
        unsafe_allow_html=True
    )

def render_intro(text):
    st.markdown(f"<div class='intro-card'>{text}</div>", unsafe_allow_html=True)

# ------------------------------------------------------
# Hero-Bereich
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
    st.markdown(
        """
        <div class="story-card">
            <p class="story-quote">
            „In meinen ersten Semestern dachte ich, 20 % Wachstum klingt nett – heute weiß ich, dass es ganze Geschäftsmodelle sprengt.“
            </p>
            <p>
            Genau dieses Aha-Erlebnis liefern wir: vom legendären Schachbrett über Zinseszins und virale Netzwerke bis zum Hypergrowth eines SaaS-Startups.
            Jedes Modul erzählt eine Szene, visualisiert Daten und verankert das Mindset hinter exponentiellen Prozessen.
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
    render_intro(
        "Am Morgen der Audienz tritt ein Gelehrter vor den König und präsentiert das Schachspiel. "
        "Als Belohnung verlangt er nur Reis auf den Feldern des Brettes – jedes Mal doppelt so viel wie zuvor. "
        "Der Hof schmunzelt, ahnt aber nicht, dass diese Verdopplung das Reich an den Rand der Kapitulation bringt."
    )

    render_cover_image(
        "https://i.postimg.cc/gjrmYdF2/pierre-bamin-Ldilh-Dx3sk-unsplash.jpg",
        "Reis, soweit das Auge reicht – und doch nur ein Vorgeschmack auf Exponentialität."
    )

    st.markdown(
        """
        <div class="story-card">
            In alten Chroniken heißt es, der König lachte über den „bescheidenen“ Wunsch nach verdoppelten Reiskörnern pro Feld.
            Doch nach wenigen Reihen füllten sich Scheunen, Speicher und schließlich ganze Städte. Erst dann begriff der Hof,
            welche Macht in einer einfachen Verdopplung steckt.
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
            ("40-Tonnen-Lkw", 40),
            ("Eiffelturm", 10_100),
            ("Cheops-Pyramide", 5_750_000),
            ("Weltreisproduktion (Jahr)", 520_000_000),
        ]
        flaechen_vergleiche = [
            ("Basketballfeld", 420),
            ("Frankfurter Römerberg", 7_000),
            ("Frankfurter Flughafen", 2_300_000),
        ]

    with col2:
        st.subheader(f"Feld {feld_nummer} im Fokus")
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
        caption_row2[0].caption("Referenzen: 40 t – 520 Mio. t")
        caption_row2[1].caption("Referenzen: 420 m² – 2,3 Mio. m²")

        st.caption("Der Großteil des Reisbergs entsteht auf den letzten Feldern – typisch für exponentielle Prozesse.")

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
            labels={"value": "Anzahl", "variable": "Sicht"},
            title="Exponentielles Wachstum auf dem Schachbrett",
            log_y=True
        )
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig, use_container_width=True)
        st.info("Logarithmische Skala nötig – auf linearer Skala wären die späteren Felder nicht mehr sichtbar.")

# ------------------------------------------------------
# Tab 2: Zinseszins vs. Zeit
# ------------------------------------------------------
with tab2:
    render_intro(
        "Frankfurt, Rooftop-Bar: Zwei Absolventen stoßen auf ihren Karrierestart an. "
        "Beide haben gleich viel gespart – doch nur eine Person hat ihre Zinsen stets reinvestiert. "
        "Im Abendlicht offenbart der Depotvergleich, wie stark Exponentialität Vermögen treibt."
    )

    render_cover_image(
        "https://i.postimg.cc/ZRR1Ncf3/andre-taissin-5OUMf1Mr5p-U-unsplash.jpg",
        "Der Zinseszins ist der leise Architekt beim Vermögensaufbau."
    )

    st.markdown(
        """
        <div class="story-card">
            Lara lässt jeden Ertrag im Depot, Tim investiert gleich viel, gönnt sich aber jährlich die Zinsen.
            25 Jahre später zeigt die Skyline, wie weit Exponentialität Lara getragen hat – Tims Depot blieb linear.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Finanzielle Ausgangslage")
        startkapital = st.number_input("Startkapital (€)", 0, 500_000, 5_000, 500)
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
        eigenleistung = eingezahlt[-1]
        zinsgewinne = endkapital - eigenleistung
        linear_vorsprung = kapital_zz[-1] - kapital_linear[-1]

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
        cols = st.columns(4, gap="large")
        cols[0].metric("Gesamtvermögen", human_number(endkapital))
        cols[1].metric("Eigenleistung", human_number(eigenleistung))
        cols[2].metric("Erarbeitete Zinsen", human_number(zinsgewinne))
        cols[3].metric("Vorsprung vs. linear", human_number(linear_vorsprung))
        cap_cols = st.columns(4, gap="large")
        cap_cols[0].caption(f"Exakt: {format_number(endkapital, 2)} €")
        cap_cols[1].caption(f"Exakt: {format_number(eigenleistung, 2)} €")
        cap_cols[2].caption(f"Exakt: {format_number(zinsgewinne, 2)} €")
        cap_cols[3].caption(f"Exakt: {format_number(linear_vorsprung, 2)} €")

        if zinsgewinne > eigenleistung:
            st.success("Ihr Kapital arbeitet härter als Ihre Einzahlungen – die exponentielle Phase ist erreicht.")

# ------------------------------------------------------
# Tab 3: Viraler Dominoeffekt
# ------------------------------------------------------
with tab3:
    render_intro(
        "Ein Startup veröffentlicht seine nachhaltige Kreditkarte in Social Media. "
        "Ein einziger Post entfacht eine Kette: Jede Kundin überzeugt weitere Freundinnen – "
        "die Monitoring-Screens im Headquarter leuchten und das Support-Team kommt ins Schwitzen."
    )

    render_cover_image(
        "https://i.postimg.cc/76jwYdxh/fusion-medical-animation-rnr8D3FNUNY-unsplash.jpg",
        "Wenn eine Idee den Nerv trifft, vervielfacht sie sich in Wellen."
    )

    st.markdown(
        """
        <div class="story-card">
            Die Kampagne trifft einen Nerv: Jeder neue Kunde bringt durchschnittlich 1,7 weitere mit.
            In wenigen Wellen schießt die Nutzung durch die Decke – Netzwerkeffekte in Reinform.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Netzwerk-Dynamik")
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
        anteil_letzte_welle = neu[-1] / gesamt if gesamt else 0

        vergleich_pop = [
            ("Deutsche Bank Park", 51_500),
            ("Stadt Frankfurt", 771_000),
            ("Region Rhein-Main", 5_800_000),
            ("Deutschland", 84_000_000),
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
        fig.update_traces(marker_color="#00c6ff")
        st.plotly_chart(fig, use_container_width=True)

        st.write("---")
        st.subheader("Resultierende Reichweite")
        cols = st.columns(3, gap="large")
        cols[0].metric("Gesamt erreicht", human_number(gesamt))
        cols[1].metric("Vergleich", best_comparison(gesamt, vergleich_pop))
        cols[2].metric("Letzte Welle", f"{anteil_letzte_welle:.0%}")
        cap_cols = st.columns(3, gap="large")
        cap_cols[0].caption(f"Exakt: {format_number(gesamt, 0)} Personen")
        cap_cols[1].caption("Vergleiche: Stadion – Nation")
        cap_cols[2].caption("Anteil an allen erreichten Personen")

        if faktor <= 1:
            st.warning("Multiplikator ≤ 1: Der Trend stirbt aus. Exponentielles Momentum beginnt erst jenseits von 1.")
        else:
            st.caption("Der Großteil der Last landet in den letzten Wellen – wichtig für Support- und Supply-Planung.")

# ------------------------------------------------------
# Tab 4: SaaS-Hypergrowth
# ------------------------------------------------------
with tab4:
    render_intro(
        "Pitch-Deck im Boardroom: Das junge SaaS-Team zeigt 12 % monatliches Wachstum. "
        "Ein Investor hebt die Augenbrauen – denn 12 % im Monat bedeutet eine Verdopplung in sechs Monaten. "
        "Cashflow, Server, Hiring – alles muss in exponentiellen Kategorien gedacht werden."
    )

    render_cover_image(
        "https://i.postimg.cc/BbWfGFgr/austin-distel-rxp-Th-Owu-Vg-E-unsplash.jpg",
        "Wenn Product-Market-Fit trifft, rast das Wachstum wie eine Rakete."
    )

    st.markdown(
        """
        <div class="story-card">
            Der 3D-holografische MRR-Chart schießt wie eine Rakete nach oben.
            Das Team spürt: Jetzt entscheidet die Fähigkeit, exponentielles Wachstum zu managen – nicht nur zu wünschen.
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
        anteil_letzter_monat = letzter_zuwachs / kumulatives_wachstum if kumulatives_wachstum > 0 else 0

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
        cols = st.columns(4, gap="large")
        cols[0].metric("MRR nach Plan", human_number(gesamt_compound))
        cols[1].metric("Lineares Ziel", human_number(gesamt_linear))
        cols[2].metric("Zusätzliche FTE", human_number(fte_gap))
        cols[3].metric("Anteil letzter Monat", f"{anteil_letzter_monat:.0%}")
        cap_cols = st.columns(4, gap="large")
        cap_cols[0].caption(f"Exakt: {format_number(gesamt_compound, 0)} €")
        cap_cols[1].caption(f"Exakt: {format_number(gesamt_linear, 0)} €")
        cap_cols[2].caption(f"Gesamtbedarf: {format_number(erforderliche_fte, 1)} FTE")
        cap_cols[3].caption("Vom gesamten Wachstum im Planzeitraum")

        st.caption("Fast die Hälfte des Gesamtwachstums passiert in den letzten Monaten – Hypergrowth braucht Vorbereitung.")

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
