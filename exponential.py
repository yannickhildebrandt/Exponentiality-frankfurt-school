import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Seiten-Konfiguration ---
st.set_page_config(
    layout="wide",
    page_title="Die Macht der Exponentialität",
    page_icon="📈"
)

# --- Styling für den “polished” Look ---
st.markdown("""
<style>
    .block-container h1 {
        text-align: center;
    }
    .stMetric {
        padding: 10px;
    }
    section.main > div {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Titel & Intro ---
st.title("📈 Die Macht der Exponentialität: Eine interaktive Reise")
st.markdown(
    "<h3 style='text-align: center; color: grey;'>Warum unser Gehirn exponentielles Wachstum nur schwer begreift.</h3>",
    unsafe_allow_html=True
)
st.markdown("---")
st.markdown(
    "Unser Denken ist intuitiv linear – exponentielle Prozesse dagegen wirken anfangs harmlos, explodieren aber später. "
    "Wählen Sie eines der folgenden Beispiele, um dieses Phänomen interaktiv zu erforschen."
)

# --- Tabs ---
tab1, tab2, tab3 = st.tabs([
    "🌾 Das Schachbrett-Problem",
    "💰 Die Macht des Zinseszins",
    "🌐 Virales Wachstum"
])

# --- Tab 1: Schachbrett ---
with tab1:
    st.header("Das Reiskorn auf dem Schachbrett")
    st.markdown(
        "64 Felder, jedes verdoppelt die Anzahl der Reiskörner – ein scheinbar kleiner Wunsch mit gigantischem Ergebnis."
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Ihre Auswahl:")
        feld_nummer = st.slider(
            "Wählen Sie ein Schachfeld (1–64):",
            min_value=1,
            max_value=64,
            value=32
        )

        koerner_auf_feld = 2 ** (feld_nummer - 1)
        koerner_gesamt = sum(2 ** i for i in range(feld_nummer))

        GEWICHT_PRO_KORN_G = 0.025
        gewicht_kg = koerner_gesamt * GEWICHT_PRO_KORN_G / 1000
        gewicht_tonnen = gewicht_kg / 1000

        WELTREISPRODUKTION_TONNEN = 510_000_000
        GEWICHT_EVEREST_TONNEN = 162_000_000_000_000

    with col2:
        st.subheader(f"Ergebnis für Feld Nr. {feld_nummer}:")
        metric_col1, metric_col2 = st.columns(2)
        metric_col1.metric(
            "Reiskörner auf diesem Feld",
            f"{koerner_auf_feld:,.0f}".replace(",", ".")
        )
        metric_col2.metric(
            "Reiskörner insgesamt",
            f"{koerner_gesamt:,.0f}".replace(",", ".")
        )

        st.markdown("---")
        st.subheader("Was bedeutet das in der Realität?")
        metric_col3, metric_col4 = st.columns(2)
        metric_col3.metric(
            "Gesamtgewicht in Tonnen",
            f"{gewicht_tonnen:,.2f}".replace(",", ".")
        )

        if gewicht_tonnen > GEWICHT_EVEREST_TONNEN:
            vergleich = f"{gewicht_tonnen / GEWICHT_EVEREST_TONNEN:.1f}× Mt. Everest"
        elif gewicht_tonnen > WELTREISPRODUKTION_TONNEN:
            vergleich = f"{gewicht_tonnen / WELTREISPRODUKTION_TONNEN:.1f}× Weltreisproduktion"
        else:
            vergleich = "Noch im Rahmen..."
        metric_col4.metric("Vergleich", vergleich.replace(".", ","))

    with st.expander("Details & Visualisierung"):
        df = pd.DataFrame({
            "Feld": range(1, 65),
            "Reiskörner": [2 ** (i - 1) for i in range(1, 65)]
        })
        fig = px.line(
            df[df["Feld"] <= feld_nummer],
            x="Feld",
            y="Reiskörner",
            title="Wachstum der Reiskörner pro Feld (logarithmisch)",
            log_y=True,
            labels={"Reiskörner": "Anzahl Reiskörner"}
        )
        st.plotly_chart(fig, use_container_width=True)
        st.info("Logarithmische Skala nötig – sonst wären die Werte nicht darstellbar.")

# --- Tab 2: Zinseszins ---
with tab2:
    st.header("Der Zinseszins-Effekt: Geld, das für Sie arbeitet")
    st.markdown(
        "Zinseszins bedeutet, dass Erträge reinvestiert werden und ihrerseits wieder Erträge erwirtschaften. "
        "Dieser Selbstverstärkungseffekt erzeugt exponentielles Wachstum."
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Sparplan-Parameter:")
        startkapital = st.number_input("Startkapital (€)", 0, 100000, 1000, 100)
        sparrate = st.slider("Monatliche Sparrate (€)", 0, 2000, 150, 25)
        laufzeit = st.slider("Laufzeit (Jahre)", 1, 50, 30, 1)
        zinssatz = st.slider("Jährlicher Zinssatz (%)", 0.0, 20.0, 7.0, 0.5)

        jahre = list(range(laufzeit + 1))
        kapital_zz = [startkapital]
        eingezahlt = [startkapital]

        for jahr in range(1, laufzeit + 1):
            kapital_zz.append((kapital_zz[-1] + sparrate * 12) * (1 + zinssatz / 100))
            eingezahlt.append(startkapital + sparrate * 12 * jahr)

        endkapital = kapital_zz[-1]
        summe_eingezahlt = eingezahlt[-1]
        gewinn = endkapital - summe_eingezahlt

    with col2:
        st.subheader("Wachstumsvergleich")
        plot_df = pd.DataFrame({
            "Jahr": jahre,
            "Zinseszins": kapital_zz,
            "Nur eingezahlt": eingezahlt
        })
        fig = px.line(
            plot_df,
            x="Jahr",
            y=["Zinseszins", "Nur eingezahlt"],
            labels={"value": "Kapital in €", "variable": ""},
            title=f"Vermögensentwicklung über {laufzeit} Jahre"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader(f"Ergebnis nach {laufzeit} Jahren")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("Endkapital", f"{endkapital:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))
        col_b.metric("Eingezahlt", f"{summe_eingezahlt:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))
        col_c.metric("Zinsgewinne", f"{gewinn:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))

        if laufzeit > 10 and gewinn > summe_eingezahlt:
            st.success("🎉 Die Erträge übertreffen Ihre Einzahlungen – die Magie des Zinseszins!")

# --- Tab 3: Virales Wachstum ---
with tab3:
    st.header("Virales Wachstum: Von einer Idee zu Millionen")
    st.markdown(
        "Jede Person gibt den Impuls an mehrere andere weiter. Schon wenige Runden genügen, um enorme Reichweiten zu erzielen."
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Simulationsparameter:")
        starter = st.number_input("Initiale Personen", 1, 100, 1)
        faktor = st.slider("Wachstumsfaktor pro Runde", 0.1, 5.0, 1.5, 0.1)
        runden = st.slider("Anzahl Runden", 1, 50, 20)

        runden_liste = list(range(1, runden + 1))
        neu = []
        kumulativ = []
        total = 0

        for i in range(runden):
            neu_in_runde = starter * (faktor ** i)
            total += neu_in_runde
            neu.append(neu_in_runde)
            kumulativ.append(total)

    with col2:
        st.subheader("Ausbreitung über die Zeit")
        viral_df = pd.DataFrame({
            "Runde": runden_liste,
            "Neu": neu,
            "Kumulativ": kumulativ
        })
        fig = px.bar(
            viral_df,
            x="Runde",
            y="Neu",
            title=f"Neu erreichte Personen pro Runde (Faktor: {faktor})",
            labels={"Neu": "Neu erreichte Personen"}
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader(f"Gesamtergebnis nach {runden} Runden")
        gesamt = kumulativ[-1]
        col_x, col_y = st.columns(2)
        col_x.metric("Insgesamt erreicht", f"{gesamt:,.0f}".replace(",", "."))

        FRANKFURT = 770_000
        DEUTSCHLAND = 84_000_000
        if gesamt > DEUTSCHLAND:
            vergleich = "Mehr als die Bevölkerung Deutschlands!"
        elif gesamt > FRANKFURT:
            vergleich = "Mehr als die Bevölkerung Frankfurts!"
        else:
            vergleich = "Füllt ein vollbesetztes Stadion."
        col_y.metric("Vergleich", vergleich)

        if faktor <= 1.0:
            st.warning("⚠️ Mit Faktor ≤ 1 stagniert oder stirbt der Trend aus. Exponentielles Wachstum startet erst bei > 1.")

# --- Abschluss ---
st.markdown("---")
st.markdown(
    "<h3 style='text-align: center;'>Zentrale Erkenntnis</h3>"
    "<p style='text-align: center;'>Der größte Teil eines exponentiellen Prozesses spielt sich am Ende ab – "
    "die frühen Phasen wirken harmlos. Geduld und Konsequenz sind entscheidend, um das Potenzial vollständig auszuschöpfen.</p>",
    unsafe_allow_html=True
)
