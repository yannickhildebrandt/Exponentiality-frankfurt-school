import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- SEITENKONFIGURATION ---
# "wide" Layout nutzt die volle Bildschirmbreite
# page_title und page_icon sind für den Browser-Tab
st.set_page_config(layout="wide", page_title="Die Macht der Exponentialität", page_icon="📈")


# --- STYLING (Optional, aber für den "polished Look") ---
# CSS, um den Titel zu zentrieren und Abstände anzupassen
st.markdown("""
<style>
    /* Titel zentrieren */
    .block-container h1 {
        text-align: center;
    }
    /* Abstand zwischen den Metriken vergrößern für bessere Lesbarkeit */
    .stMetric {
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)


# --- TITEL UND EINLEITUNG ---
st.title("📈 Die Macht der Exponentialität: Eine interaktive Reise")
st.markdown("<h3 style='text-align: center; color: grey;'>Warum unser Gehirn exponentielles Wachstum nur schwer begreifen kann.</h3>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    "Unser Gehirn ist darauf trainiert, linear zu denken. Wenn wir doppelt so schnell gehen, kommen wir in der halben Zeit an. "
    "Exponentielles Wachstum hingegen ist kontraintuitiv, explosiv und führt oft zu Ergebnissen, die unsere Vorstellungskraft sprengen. "
    "Diese Anwendung soll Ihnen helfen, ein Gefühl für die enorme Kraft zu entwickeln, die hinter diesem Konzept steckt. "
    "Wählen Sie eines der Beispiele aus, um zu starten."
)


# --- TABS FÜR DIE VERSCHIEDENEN BEISPIELE ---
tab1, tab2, tab3 = st.tabs([
    "🌾 Das Schachbrett-Problem",
    "💰 Die Macht des Zinseszins",
    "🌐 Virales Wachstum"
])


# --- TAB 1: DAS SCHACHBRETT-PROBLEM ---
with tab1:
    st.header("Das Reiskorn auf dem Schachbrett")
    st.markdown(
        "Die Legende besagt, dass der Erfinder des Schachspiels vom König einen Wunsch frei hatte. "
        "Sein bescheidener Wunsch: Ein Reiskorn auf das erste Feld, zwei auf das zweite, vier auf das dritte und so weiter – "
        "eine Verdopplung für jedes der 64 Felder. Der König lachte... zu früh."
    )

    # Spalten für eine saubere Anordnung
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Ihre Auswahl:")
        feld_nummer = st.slider(
            "Wählen Sie ein Schachfeld aus (1-64):",
            min_value=1,
            max_value=64,
            value=32, # Guter Startwert, um schon beeindruckende Zahlen zu zeigen
            step=1
        )

        # Berechnungen
        koerner_auf_feld = 2**(feld_nummer - 1)
        koerner_gesamt = sum(2**i for i in range(feld_nummer)) # Summe bis zu diesem Feld

        # Annahmen für die Umrechnung (macht es greifbarer)
        GEWICHT_PRO_KORN_G = 0.025  # Durchschnittsgewicht eines Reiskorns in Gramm
        gewicht_kg = (koerner_gesamt * GEWICHT_PRO_KORN_G) / 1000
        gewicht_tonnen = gewicht_kg / 1000

        # Vergleichsdaten
        WELTREISPRODUKTION_TONNEN = 510_000_000 # ca. 2022/23
        GEWICHT_EVEREST_TONNEN = 162_000_000_000_000

    with col2:
        st.subheader(f"Ergebnis für Feld Nr. {feld_nummer}:")
        
        # Metriken für eine ansprechende Darstellung der Zahlen
        metric_col1, metric_col2 = st.columns(2)
        with metric_col1:
            st.metric(
                label="Reiskörner auf diesem Feld",
                value=f"{koerner_auf_feld:,.0f}".replace(",", ".") # Formatierung für deutsche Zahlen
            )
        with metric_col2:
            st.metric(
                label="Reiskörner INSGESAMT",
                value=f"{koerner_gesamt:,.0f}".replace(",", ".")
            )
        
        st.markdown("---")
        st.subheader("Was bedeutet das in der Realität?")

        metric_col3, metric_col4 = st.columns(2)
        with metric_col3:
            st.metric(
                label="Gesamtgewicht in Tonnen",
                value=f"{gewicht_tonnen:,.2f}".replace(",", ".")
            )
        with metric_col4:
            # Dynamischer Vergleich
            if gewicht_tonnen > GEWICHT_EVEREST_TONNEN:
                vergleich_text = f"{gewicht_tonnen / GEWICHT_EVEREST_TONNEN:.1f}x das Gewicht des Mt. Everest".replace(".",",")
                st.metric(label="Vergleich", value=vergleich_text, help="Gewicht Mt. Everest: ca. 162 Billionen Tonnen")
            elif gewicht_tonnen > WELTREISPRODUKTION_TONNEN:
                vergleich_text = f"{gewicht_tonnen / WELTREISPRODUKTION_TONNEN:.1f}x die jährliche Weltreisproduktion".replace(".",",")
                st.metric(label="Vergleich", value=vergleich_text, help="Weltreisproduktion 2022/23: ca. 510 Mio. Tonnen")
            else:
                 st.metric(label="Vergleich", value="Wächst noch...")

    # Expander für die Details
    with st.expander("Details zur Berechnung und Visualisierung der ersten Felder"):
        # Daten für einen Chart der ersten Felder
        chart_data = pd.DataFrame({
            'Feld': range(1, 65),
            'Reiskörner (logarithmische Skala)': [2**(i-1) for i in range(1, 65)]
        })
        fig = px.line(
            chart_data[chart_data['Feld'] <= feld_nummer], 
            x='Feld', 
            y='Reiskörner (logarithmische Skala)', 
            title='Wachstum der Reiskörner pro Feld (Log-Skala)',
            log_y=True, # Logarithmische Skala ist hier essentiell
            labels={'Reiskörner (logarithmische Skala)': 'Anzahl Reiskörner'}
        )
        fig.update_layout(yaxis_title="Anzahl Reiskörner (logarithmisch)")
        st.plotly_chart(fig, use_container_width=True)
        st.info("Hinweis: Die y-Achse ist logarithmisch, da die Zahlen sonst zu schnell explodieren, um sie grafisch darzustellen.")


# --- TAB 2: DIE MACHT DES ZINSESZINS ---
with tab2:
    st.header("Der Zinseszins-Effekt: Geld, das für Sie arbeitet")
    st.markdown(
        "Albert Einstein soll den Zinseszins als das achte Weltwunder bezeichnet haben. "
        "Im Gegensatz zum linearen, einfachen Zins, bei dem nur das Anfangskapital verzinst wird, werden beim Zinseszins auch die "
        "bereits verdienten Zinsen erneut verzinst. Dieser sich selbst verstärkende Prozess führt zu exponentiellem Wachstum."
    )
    
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Ihre Sparplan-Parameter:")
        startkapital = st.number_input("Startkapital (€)", min_value=0, max_value=100000, value=1000, step=100)
        sparrate = st.slider("Monatliche Sparrate (€)", min_value=0, max_value=2000, value=150, step=25)
        laufzeit = st.slider("Laufzeit (Jahre)", min_value=1, max_value=50, value=30, step=1)
        zinssatz = st.slider("Jährlicher Zinssatz (%)", min_value=0.0, max_value=20.0, value=7.0, step=0.5, format="%.1f%%")

        # Berechnungen
        jahre = list(range(laufzeit + 1))
        kapital_zinseszins = [startkapital]
        kapital_linear = [startkapital]
        eingezahltes_kapital = [startkapital]

        for jahr in range(1, laufzeit + 1):
            # Zinseszins-Berechnung
            neues_kapital_zz = (kapital_zinseszins[-1] + sparrate * 12) * (1 + zinssatz / 100)
            kapital_zinseszins.append(neues_kapital_zz)
            
            # Linear-Berechnung (nur Zinsen auf Startkapital + eingezahltes Geld)
            eingezahlt = startkapital + (sparrate * 12 * jahr)
            zinsen_linear = startkapital * (zinssatz / 100) * jahr
            kapital_linear.append(eingezahlt + zinsen_linear)
            
            eingezahltes_kapital.append(eingezahlt)

        # Endergebnisse
        endkapital_zz = kapital_zinseszins[-1]
        endkapital_eingezahlt = eingezahltes_kapital[-1]
        gewinn_zz = endkapital_zz - endkapital_eingezahlt

    with col2:
        st.subheader("Wachstumsvergleich: Zinseszins vs. Lineares Sparen")
        
        # Daten für den Chart vorbereiten
        plot_data = pd.DataFrame({
            'Jahr': jahre,
            'Zinseszins': kapital_zinseszins,
            'Nur eingezahlt': eingezahltes_kapital,
        })

        fig = px.line(
            plot_data, 
            x='Jahr', 
            y=['Zinseszins', 'Nur eingezahlt'],
            title=f"Vermögensentwicklung über {laufzeit} Jahre",
            labels={'value': 'Kapital in €', 'variable': 'Legende'}
        )
        fig.update_layout(legend_title_text='Szenario')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader("Ihr Ergebnis nach " + str(laufzeit) + " Jahren")
        
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        metric_col1.metric("Endkapital", f"{endkapital_zz:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))
        metric_col2.metric("Eingezahltes Kapital", f"{endkapital_eingezahlt:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))
        metric_col3.metric("Reiner Zinsgewinn", f"{gewinn_zz:,.2f} €".replace(",", "X").replace(".", ",").replace("X", "."))
        
        # Highlight des exponentiellen Effekts
        if laufzeit > 10 and gewinn_zz > endkapital_eingezahlt:
            st.success("🎉 Glückwunsch! Ihr Geld hat mehr Geld verdient, als Sie selbst eingezahlt haben. Das ist die Magie des Zinseszins!")


# --- TAB 3: VIRALES WACHSTUM ---
with tab3:
    st.header("Virales Wachstum: Von einem zu Millionen")
    st.markdown(
        "Ob ein virales Video, ein Trend in sozialen Medien oder die Ausbreitung einer Idee – das Prinzip ist oft exponentiell. "
        "Eine Person teilt es mit einigen anderen, diese teilen es wiederum weiter, und in kürzester Zeit entsteht eine Lawine. "
        "Die 'Wachstumsrate' oder der 'R-Wert' ist hier entscheidend."
    )

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("Simulations-Parameter:")
        start_personen = st.number_input("Anzahl der 'Starter'", 1, 100, 1, 1)
        wachstumsfaktor = st.slider(
            "Wachstumsfaktor (Wie viele Personen steckt jede Person an?)", 
            min_value=0.1, max_value=5.0, value=1.5, step=0.1
        )
        runden = st.slider("Anzahl der Runden/Tage", 1, 50, 20)

        # Berechnungen
        runden_liste = list(range(1, runden + 1))
        neu_pro_runde = []
        kumulativ = []
        total = 0

        for i in range(runden):
            neu_in_runde = start_personen * (wachstumsfaktor ** i)
            total += neu_in_runde
            neu_pro_runde.append(neu_in_runde)
            kumulativ.append(total)

    with col2:
        st.subheader("Ausbreitung über die Zeit")
        
        # Chart Daten
        chart_data_viral = pd.DataFrame({
            'Runde': runden_liste,
            'Neu erreichte Personen': neu_pro_runde,
            'Insgesamt erreicht': kumulativ
        })

        fig = px.bar(
            chart_data_viral, 
            x='Runde', 
            y='Neu erreichte Personen', 
            title=f'Neu erreichte Personen pro Runde (Faktor: {wachstumsfaktor})'
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader(f"Gesamtergebnis nach {runden} Runden")

        # Vergleichsdaten
        FRANKFURT_EINWOHNER = 770_000
        DEUTSCHLAND_EINWOHNER = 84_000_000

        erreichte_personen_gesamt = kumulativ[-1]

        metric_col1, metric_col2 = st.columns(2)
        metric_col1.metric("Insgesamt erreichte Personen", f"{erreichte_personen_gesamt:,.0f}".replace(",", "."))
        
        if erreichte_personen_gesamt > DEUTSCHLAND_EINWOHNER:
             vergleich_text = "Mehr als die Bevölkerung Deutschlands!"
        elif erreichte_personen_gesamt > FRANKFURT_EINWOHNER:
            vergleich_text = "Mehr als die Bevölkerung Frankfurts!"
        else:
            vergleich_text = "Füllt ein kleines Stadion."

        metric_col2.metric("Vergleich", vergleich_text)

        if wachstumsfaktor <= 1.0:
            st.warning("⚠️ Mit einem Wachstumsfaktor von 1.0 oder weniger stirbt der Trend aus oder stagniert. Echtes exponentielles Wachstum beginnt erst bei einem Faktor > 1.")

# --- ABSCHLIESSENDE WORTE ---
st.markdown("---")
st.markdown(
    "<h3 style='text-align: center;'>Zentrale Erkenntnis</h3>"
    "<p style='text-align: center;'>Der größte Teil des exponentiellen Wachstums findet am Ende statt. Die ersten Phasen wirken oft langsam und unspektakulär. "
    "Geduld und Beständigkeit sind daher der Schlüssel, um die volle Kraft der Exponentialität zu nutzen – ob beim Investieren, Lernen oder dem Aufbau eines Netzwerks.</p>",
    unsafe_allow_html=True
)
