import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analyse Démographique", layout="wide")

excel_file = "RGPH__2024.xlsx"

@st.cache_data
def load_home_data():
    return pd.read_excel(excel_file, sheet_name="Population")

pop = load_home_data()

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Accueil", 
        "Analyse Régionale",
        "Population et Sexe", 
        "Structure par Âge", 
        "État Matrimonial", 
        "Fécondité et Handicap",
        "Ménages",
        "Province de Guelmim", 
        "Province de Sidi Ifni", 
        "Province de Tan-Tan", 
        "Province d'Assa-Zag"
    ]
)

if page == "Accueil":
    
    st.markdown("""
    <div style="background-color: #262730; padding: 20px; border-radius: 10px; border: 1px solid #464855; margin-bottom: 25px; display: flex; justify-content: space-between; align-items: center;">
        <div style="font-family: 'Arial'; color: #FFFFFF;">
            <p style="margin: 0; font-weight: bold; font-size: 14px;">Royaume du Maroc</p>
            <p style="margin: 0; font-size: 13px;">Haut-Commissariat au Plan</p>
            <p style="margin: 0; font-size: 13px; color: #B0B3B8;">Direction Régionale du Plan de Guelmim</p>
        </div>
        <div style="text-align: center; font-family: 'Arial'; flex-grow: 1; margin: 0 20px;">
            <h1 style="margin: 0; color: #1F88D2; font-size: 26px; font-weight: bold;">Tableau de Bord Régional</h1>
            <p style="margin: 5px 0 0 0; color: #E4E6EB; font-size: 18px; font-weight: 500;">Suivi des indicateurs territoriaux</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div style="background-color: #1F88D2; padding: 10px 15px; border-top-left-radius: 5px; border-top-right-radius: 5px; color: white; font-weight: bold; font-size: 16px;">
        Présentation générale de la Région Guelmim-Oued Noun
    </div>
    <div style="background-color: #1E1E24; padding: 15px; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; border: 1px solid #1F88D2; border-top: none; margin-bottom: 25px; color: #E4E6EB; line-height: 1.6; text-align: justify;">
        La région de <b>Guelmim-Oued Noun</b>, porte d'entrée du Sahara marocain, constitue une structure territoriale et économique stratégique. Elle couvre une superficie d'environ <b>46 108 km²</b> (soit 6,49 % du territoire national) et se caractérise par une dynamique démographique importante mise en valeur par le Recensement Général de la Population (RGPH 2024). Ce tableau de bord permet de centraliser, organiser et visualiser les données clés afin d'appuyer le suivi et l'évaluation du développement territorial.
    </div>
    """, unsafe_allow_html=True)

   
    col_gauche, col_droite = st.columns([1.2, 1])

    with col_gauche:
        st.markdown("""
        <div style="background-color: #1F88D2; padding: 10px 15px; border-top-left-radius: 5px; border-top-right-radius: 5px; color: white; font-weight: bold; font-size: 16px;">
            Carte de la région de Guelmim-Oued Noun
        </div>
        """, unsafe_allow_html=True)
        
        st.image("image.png", use_container_width=True)
            
    with col_droite:
        st.markdown("""
        <div style="background-color: #1F88D2; padding: 10px 15px; border-top-left-radius: 5px; border-top-right-radius: 5px; color: white; font-weight: bold; font-size: 16px;">
            Organisation administrative
        </div>
        """, unsafe_allow_html=True)
        
       
        data_admin = {
            "Région / Province": ["Guelmim-Oued Noun", "Guelmim", "Sidi Ifni", "Tan-Tan", "Assa-Zag"],
            "Cercles": ["9", "3", "2", "2", "2"],
            "Communes": ["53", "20", "19", "7", "7"]
        }
        df_admin = pd.DataFrame(data_admin)
        st.dataframe(df_admin, hide_index=True, use_container_width=True)
        
        st.markdown("""
        <div style="background-color: #1E1E24; padding: 12px; border-radius: 5px; border: 1px solid #464855; margin-top: 10px; font-size: 13px; color: #E4E6EB; line-height: 1.5; text-align: justify;">
            Cet encadrement spatial est d'une importance capitale pour interpréter les indicateurs démographiques régionaux, notamment dans un territoire marqué par la diversité des contextes communaux, entre centres urbains dynamiques et zones rurales dispersées.
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    
    st.markdown("<h3 style='color: #1F88D2;'>🔍 Focus sur les Provinces de la Région</h3>", unsafe_allow_html=True)
    
    prov1, prov2, prov3, prov4 = st.columns(4)
    
    with prov1:
        st.markdown("""
        <div style="background-color: #1E1E24; padding: 15px; border-radius: 8px; border-left: 5px solid #1F88D2; border-top: 1px solid #464855; border-right: 1px solid #464855; border-bottom: 1px solid #464855; min-height: 200px;">
            <h4 style="margin: 0 0 10px 0; color: #1F88D2;">Province de Guelmim</h4>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Chef-lieu :</b> Guelmim</p>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Communes :</b> 20 communes</p>
            <p style="font-size: 13px; margin: 5px 0; color: #B0B3B8; text-align: justify;">Regroupe la majeure partie de l'activité administrative et économique de la région.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with prov2:
        st.markdown("""
        <div style="background-color: #1E1E24; padding: 15px; border-radius: 8px; border-left: 5px solid #2ECC71; border-top: 1px solid #464855; border-right: 1px solid #464855; border-bottom: 1px solid #464855; min-height: 200px;">
            <h4 style="margin: 0 0 10px 0; color: #2ECC71;">Province de Sidi Ifni</h4>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Chef-lieu :</b> Sidi Ifni</p>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Communes :</b> 19 communes</p>
            <p style="font-size: 13px; margin: 5px 0; color: #B0B3B8; text-align: justify;">Zone côtière ouverte sur l'Atlantique, caractérisée par une forte dispersion rurale.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with prov3:
        st.markdown("""
        <div style="background-color: #1E1E24; padding: 15px; border-radius: 8px; border-left: 5px solid #E67E22; border-top: 1px solid #464855; border-right: 1px solid #464855; border-bottom: 1px solid #464855; min-height: 200px;">
            <h4 style="margin: 0 0 10px 0; color: #E67E22;">Province de Tan-Tan</h4>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Chef-lieu :</b> Tan-Tan</p>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Communes :</b> 7 communes</p>
            <p style="font-size: 13px; margin: 5px 0; color: #B0B3B8; text-align: justify;">Pôle halieutique et portuaire majeur, avec une population fortement urbanisée.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with prov4:
        st.markdown("""
        <div style="background-color: #1E1E24; padding: 15px; border-radius: 8px; border-left: 5px solid #9B59B6; border-top: 1px solid #464855; border-right: 1px solid #464855; border-bottom: 1px solid #464855; min-height: 200px;">
            <h4 style="margin: 0 0 10px 0; color: #9B59B6;">Province d'Assa-Zag</h4>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Chef-lieu :</b> Assa</p>
            <p style="font-size: 13px; margin: 5px 0; color: #E4E6EB;"><b>Communes :</b> 7 communes</p>
            <p style="font-size: 13px; margin: 5px 0; color: #B0B3B8; text-align: justify;">Zone à caractère saharien et pastoral étendu, avec des spécificités démographiques propres.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")

    
    st.markdown("""
    <div style="background-color: #1F88D2; padding: 10px 15px; border-top-left-radius: 5px; border-top-right-radius: 5px; color: white; font-weight: bold; font-size: 16px;">
        Développement territorial et objectif du projet de recherche
    </div>
    <div style="background-color: #1E1E24; padding: 15px; border-bottom-left-radius: 5px; border-bottom-right-radius: 5px; border: 1px solid #1F88D2; border-top: none; color: #E4E6EB; line-height: 1.6; text-align: justify;">
        Dans le contexte de la régionalisation avancée, ce projet de recherche (Baht) s'inscrit dans l'analyse critique des indicateurs démographiques fiables et territorialisés. L'objectif est d'offrir une vision synthétique et dynamique des structures de population, de l'état matrimonial, de la fécondité et des conditions ménagères pour éclairer au mieux les décisions d'aménagement régional.
    </div>
    """, unsafe_allow_html=True)
elif page == "Analyse Régionale":
    st.title("Tableau de Bord Démographique de la Région Guelmim-Oued Noun")
    st.write("---")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Population totale", value="448 685")
    with col2:
        st.metric(label="Population urbaine", value="299 543")
    with col3:
        st.metric(label="Population rurale", value="149 142")
    with col4:
        st.metric(label="Nombre de ménages", value="105 394")

    st.write("---")

    fig = px.bar(
        pop, 
        x="province", 
        y="Population", 
        title="Population par Province",
        color_discrete_sequence=["#1F4E79"]
    )
    fig.update_layout(
        template="plotly_dark", 
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Province",
        yaxis_title="Somme de Population"
    )
    st.plotly_chart(fig, use_container_width=True)

    df_urb_rur = pd.read_excel(excel_file, sheet_name="population urbaine_rurale")
    
    fig2 = px.bar(
        df_urb_rur,
        x="province",
        y=["Population_Urbaine", "Population_Rurale"],
        barmode="group",
        title="Population Urbaine et Population Rurale par Province",
        color_discrete_sequence=["#1F4E79", "#3A8BCD"]
    )
    fig2.update_layout(
        template="plotly_dark", 
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Province",
        yaxis_title="Somme de Population"
    )
    st.plotly_chart(fig2, use_container_width=True)

    df_menage = pd.read_excel(excel_file, sheet_name="menage par province")
    
    fig3 = px.bar(
        df_menage,
        x="Province",
        y="Nombre de ménages",
        title="Nombre de Ménages par Province",
        color_discrete_sequence=["#1F4E79"]
    )
    fig3.update_layout(
        template="plotly_dark", 
        plot_bgcolor="rgba(0,0,0,0)", 
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Province",
        yaxis_title="Somme de Nombre de ménages"
    )
    st.plotly_chart(fig3, use_container_width=True)

elif page == "Population et Sexe":
    df_sexe = pd.read_excel(excel_file, sheet_name="masculin_féminin")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Hommes (%)", value="49,30%")
    with col2:
        st.metric(label="Femmes (%)", value="50,70%")
        
    st.write("---")
    
    chart_col1, chart_col2 = st.columns(2)
    
    col_province = df_sexe.columns[0]
    col_femmes = df_sexe.columns[1]
    col_hommes = df_sexe.columns[2]
    
    with chart_col1:
        fig_bar = px.bar(
            df_sexe,
            x=col_province,
            y=[col_hommes, col_femmes],
            barmode="group",
            title="Répartition des Femmes et des Hommes par Province",
            color_discrete_sequence=["#1F4E79", "#3A8BCD"]
        )
        fig_bar.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Province",
            yaxis_title="Pourcentage",
            legend_title="Sexe"
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with chart_col2:
        fig_pie = px.pie(
            names=["Femmes", "Hommes"],
            values=[50.7, 49.3],
            hole=0.5,
            title="Répartition de la Population selon le Sexe",
            color_discrete_sequence=["#3A8BCD", "#1F4E79"]
        )
        fig_pie.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
elif page == "Structure par Âge":
    import plotly.graph_objects as go
    
    st.title("Structure de la Population selon l'Âge et le Sexe")
    st.write("---")
    
    
    df_age = pd.read_excel(excel_file, sheet_name="pyramide_ages_region")
    df_groups = pd.read_excel(excel_file, sheet_name="age")
    

    col_groupes = df_age.columns[1]  
    col_femmes = df_age.columns[2]   
    col_hommes = df_age.columns[3]   
        
    categories_originales = df_age[col_groupes].astype(str).tolist()
    hommes_values = df_age[col_hommes].astype(float)
    femmes_values = df_age[col_femmes].astype(float)
    hommes_neg = -hommes_values
        
    fig_pyramide = go.Figure()
        
    fig_pyramide.add_trace(go.Bar(
            y=df_age[col_groupes],
            x=hommes_neg,
            name='Hommes',
            orientation='h',
            marker=dict(color="#197EDC"),
            hoverinfo='text',
            text=[f"{val}%" for val in hommes_values]
        ))
        
    fig_pyramide.add_trace(go.Bar(
            y=df_age[col_groupes],
            x=femmes_values,
            name='Femmes',
            orientation='h',
            marker=dict(color="#D2149C"),
            hoverinfo='text',
            text=[f"{val}%" for val in femmes_values]
        ))
        
    fig_pyramide.update_layout(
            title="Pyramide des Âges de la Région (%)",
            barmode='relative',
            bargap=0.1,
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(
                title="Pourcentage (%)",
                tickvals=[-12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12],
                ticktext=["12%", "10%", "8%", "6%", "4%", "2%", "0%", "2%", "4%", "6%", "8%", "10%", "12%"]
            ),
            yaxis=dict(
                title="Groupes d'âge",
                type='category',
                categoryorder='array',
                categoryarray=categories_originales
            )
        )
    st.plotly_chart(fig_pyramide, use_container_width=True)
        
    col_groupes_large = df_groups.columns[0]
    col_pourcentage = df_groups.columns[1]
        
    fig_donut = px.pie(
            df_groups,
            names=col_groupes_large,
            values=col_pourcentage,
            hole=0.5,  
            title="Répartition par Grands Groupes d'âge",
            color_discrete_sequence=["#1F4E79", "#3A8BCD", "#A0C4DF"]
        )
        
    fig_donut.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            legend_title="Groupes d'âge"
        )
        
        
    fig_donut.update_traces(textinfo='percent+label')
        
    st.plotly_chart(fig_donut, use_container_width=True)
elif page == "État Matrimonial":
    st.title("Statut Matrimonial de la Population")
    st.write("---")
    
   
    df_matrimonial = pd.read_excel(excel_file, sheet_name="État Matrimonial")
    df_mariage = pd.read_excel(excel_file, sheet_name="mariage") 
    
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label="Célibataire (%)", value="34,40%")
    with col2:
        st.metric(label="Marié.e (%)", value="56,80%")
    with col3:
        st.metric(label="Divorcé.e (%)", value="3,30%")
    with col4:
        st.metric(label="Veuf.ve (%)", value="5,50%")
    with col5:
        st.metric(label="Âge moyen au 1er mariage", value="30,60")
        
    st.write("---")
    
    
    categories_matrimoniales = ["Célibataire", "Marié.e", "Divorcé.e", "Veuf.ve"]
    valeurs_regionales = [34.4, 56.8, 3.3, 5.5] 
    
    fig_donut = px.pie(
        names=categories_matrimoniales,
        values=valeurs_regionales,
        hole=0.5,
        title="Répartition Régionale de la Population selon l'État Matrimonial",
        color_discrete_sequence=["#1F4E79", "#3A8BCD", "#A0C4DF", "#D9E1F2"]
    )
    fig_donut.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        legend_title="État Matrimonial"
    )
    fig_donut.update_traces(textinfo='percent+label')
    st.plotly_chart(fig_donut, use_container_width=True)
    
    st.write("---")
    
    
    fig_stacked = px.bar(
        df_matrimonial,
        x="Province",
        y=["Célibataire", "Marié.e", "Divorcé.e", "Veuf.ve"],
        barmode="group",
        text_auto='.1f', 
        title="Répartition de la Population selon l'État Matrimonial par Province",
        color_discrete_sequence=["#1F4E79", "#3A8BCD", "#A0C4DF", "#D9E1F2"]
    )
    fig_stacked.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Province",
        yaxis_title="Pourcentage (%)",
        legend_title="État Matrimonial"
    )
    
    
    fig_stacked.update_traces(textposition='outside')
    
    st.plotly_chart(fig_stacked, use_container_width=True)
    
    
    fig_age_mariage = px.bar(
        df_mariage,
        x="Province",
        y="Âge moyen singulier au mariage",
        title="Âge Moyen au Premier Mariage par Province",
        color_discrete_sequence=["#3A8BCD"]
    )
    fig_age_mariage.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Province",
        yaxis_title="Âge moyen"
    )
    st.plotly_chart(fig_age_mariage, use_container_width=True)
elif page == "Fécondité et Handicap":
    st.title("Fécondité et Handicap de la Population")
    st.write("---")
    
    
    df_fec = pd.read_excel(excel_file, sheet_name="fecondite")
    df_hand_sexe = pd.read_excel(excel_file, sheet_name="handicap_sexe")
    df_hand_prov = pd.read_excel(excel_file, sheet_name="handicap_province")
    
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label="Indicateur conjoncturel fécondité", value="1,89")
    with col2:
        st.metric(label="Descendance finale des femmes", value="2,80")
    with col3:
        st.metric(label="Taux de prévalence du handicap (%)", value="4,60")
    with col4:
        st.metric(label="Hommes handicapés (%)", value="4,70")
    with col5:
        st.metric(label="Femmes handicapées (%)", value="4,50")
        
    st.write("---")
    
    
    graph_col1, graph_col2 = st.columns(2)
    
    
    with graph_col1:
       
        df_fec_sorted = df_fec.sort_values(by="fecondite", ascending=False)
        fig_fec = px.bar(
            df_fec_sorted,
            x="province",
            y="fecondite",
            text_auto='.1f',
            title="Indicateur de fécondité par province",
            color_discrete_sequence=["#1F4E79"] 
        )
        fig_fec.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="province",
            yaxis_title="Somme de fecondite"
        )
        fig_fec.update_traces(textposition='outside')
        st.plotly_chart(fig_fec, use_container_width=True)
        
    
    with graph_col2:
        fig_pie_hand = px.pie(
            df_hand_sexe,
            names="Sexe",
            values="handicap",
            title="Répartition des personnes en situation de handicap selon le Sexe",
            color_discrete_sequence=["#2066a8", "#3A8BCD"] 
        )
        fig_pie_hand.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            legend_title="Sexe"
        )
        fig_pie_hand.update_traces(textinfo='percent+value')
        st.plotly_chart(fig_pie_hand, use_container_width=True)
    st.write("---")   
    

       
    df_hand_prov_sorted = df_hand_prov.sort_values(by="handicap", ascending=False)
    fig_hand = px.bar(
            df_hand_prov_sorted,
            x="province",
            y="handicap",
            text_auto='.1f',
            title="Prévalence du handicap par province",
            color_discrete_sequence=["#1F4E79"]
        )
    fig_hand.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="province",
            yaxis_title="Somme de handicap"
        )
    fig_hand.update_traces(textposition='outside')
    st.plotly_chart(fig_hand, use_container_width=True)
elif page == "Ménages":
    st.title("Caractéristiques des Ménages")
    st.write("---")
    
   
    df_menage = pd.read_excel(excel_file, sheet_name="Ménages_Urbains")
    
   
    total_urbain = df_menage["ménage_urbains"].sum()
    total_rural = df_menage["ménage_Ruraux"].sum()
    total_menages = total_urbain + total_rural
    
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Nombre Total de Ménages", value=f"{total_menages:,}".replace(",", " "))
    with col2:
        st.metric(label="Ménages urbains", value=f"{total_urbain:,}".replace(",", " "))
    with col3:
        st.metric(label="Ménages ruraux", value=f"{total_rural:,}".replace(",", " "))
        
    st.write("---")
    
   
    graph_col1, graph_col2 = st.columns(2)
    
   
    with graph_col1:
        
        df_menage["Total_Province"] = df_menage["ménage_urbains"] + df_menage["ménage_Ruraux"]
        df_sorted_total = df_menage.sort_values(by="Total_Province", ascending=False)
        
        fig_total_prov = px.bar(
            df_sorted_total,
            x="province",
            y="Total_Province",
            text_auto='.2s', 
            title="Répartition des ménages par Province",
            color_discrete_sequence=["#1F4E79"]
        )
        fig_total_prov.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Province",
            yaxis_title="Somme de Nombre de ménages"
        )
        fig_total_prov.update_traces(textposition='outside')
        st.plotly_chart(fig_total_prov, use_container_width=True)
        
    
    with graph_col2:
        labels_milieu = ["Ménage urbains", "Ménage ruraux"]
        values_milieu = [total_urbain, total_rural]
        
        fig_donut_milieu = px.pie(
            names=labels_milieu,
            values=values_milieu,
            hole=0.6, 
            title="Répartition des ménages selon le milieu de résidence",
            color_discrete_sequence=["#1F4E79", "#3A8BCD"]
        )
        fig_donut_milieu.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            legend_title="Milieu"
        )
        fig_donut_milieu.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_donut_milieu, use_container_width=True)
    st.write("---")  
    
    df_sorted_comp = df_menage.sort_values(by="ménage_urbains", ascending=False)
        
    fig_comp = px.bar(
            df_sorted_comp,
            x="province",
            y=["ménage_urbains", "ménage_Ruraux"],
            barmode="group",
            text_auto='.2s',
            title="Comparaison des ménages urbains et ruraux par province",
            color_discrete_sequence=["#1F4E79", "#3A8BCD"]
        )
    fig_comp.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="province",
            yaxis_title="Somme de ménage",
            legend_title="Type de Ménage"
        )
    fig_comp.update_traces(textposition='outside')
    st.plotly_chart(fig_comp, use_container_width=True)
elif page == "Province de Guelmim":
    st.title("Tableau de bord - Province de Guelmim")
    st.write("---")
    
    
    df_pop = pd.read_excel(excel_file, sheet_name="guelmim_population")
    df_sexe = pd.read_excel(excel_file, sheet_name="guelmim_sexe")
    df_fec = pd.read_excel(excel_file, sheet_name="guelmim_fecondite")
    df_hand = pd.read_excel(excel_file, sheet_name="guelmim_handicap")
    
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Population total", value="196 267")
    with col2:
        st.metric(label="Population urbaine", value="153 238")
    with col3:
        st.metric(label="Population rurale", value="43 029")
    with col4:
        st.metric(label="Nombre de ménages", value="47 250")
        
    st.write("---")
    
   

    df_pop_sorted = df_pop.sort_values(by="Population", ascending=False)
    fig_pop = px.bar(
            df_pop_sorted,
            x="Commune",
            y="Population",
            text_auto='.2s',
            title="Population par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
    fig_pop.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Population"
        )
    fig_pop.update_traces(textposition='outside')
    st.plotly_chart(fig_pop, use_container_width=True)
        
   
    st.write("---")
       
    df_sexe_sorted = df_sexe.sort_values(by="Femmes", ascending=False)
    fig_sexe = px.bar(
            df_sexe_sorted,
            x="Commune",
            y=["Femmes", "Hommes"],
            barmode="group",
            text_auto='.2s',
            title="Répartition des Femmes et des Hommes par Commune",
            color_discrete_sequence=["#1F4E79", "#3A8BCD"]
        )
    fig_sexe.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Femmes et Somme de H...",
            legend_title="Sexe"
        )
    fig_sexe.update_traces(textposition='outside')
    st.plotly_chart(fig_sexe, use_container_width=True)
    st.write("---")    
    
    
    df_fec_sorted = df_fec.sort_values(by="Fécondité", ascending=False)
    fig_fec = px.bar(
            df_fec_sorted,
            x="Commune",
            y="Fécondité",
            text_auto='.1f',
            title="Indicateur de Fécondité par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
    fig_fec.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Fécondité"
        )
    fig_fec.update_traces(textposition='outside')
    st.plotly_chart(fig_fec, use_container_width=True)
        
    
    st.write("---")
    df_hand_sorted = df_hand.sort_values(by="handicap", ascending=False)
    fig_hand = px.bar(
            df_hand_sorted,
            x="Commune",
            y="handicap",
            text_auto='.1f',
            title="Prévalence du handicap par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
    fig_hand.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de handicap"
        )
    fig_hand.update_traces(textposition='outside')
    st.plotly_chart(fig_hand, use_container_width=True)
elif page == "Province de Sidi Ifni":
    st.title("Tableau de bord - Province de Sidi Ifni")
    st.write("---")
    
   
    df_pop = pd.read_excel(excel_file, sheet_name="sidi ifni_population")
    df_sexe = pd.read_excel(excel_file, sheet_name="sidi ifni_sexe")
    df_fec = pd.read_excel(excel_file, sheet_name="sidi ifni_fecondite")
    df_hand = pd.read_excel(excel_file, sheet_name="sidi ifni_handicap")
    
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Population total", value="104 601")
    with col2:
        st.metric(label="Population urbaine", value="35 556")
    with col3:
        st.metric(label="Population rurale", value="69 045")
    with col4:
        st.metric(label="Nombre de ménages", value="28 539")
        
    st.write("---")
    
   
    df_pop_sorted = df_pop.sort_values(by="Population", ascending=False)
    fig_pop = px.bar(
        df_pop_sorted,
        x="Commune",
        y="Population",
        text_auto='.2s',
        title="Population par Commune",
        color_discrete_sequence=["#1F4E79"]
    )
    fig_pop.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Commune",
        yaxis_title="Somme de Population"
    )
    fig_pop.update_traces(textposition='outside')
    st.plotly_chart(fig_pop, use_container_width=True)
    st.write("---")
    
    
    df_sexe_sorted = df_sexe.sort_values(by="Femmes", ascending=False)
    fig_sexe = px.bar(
        df_sexe_sorted,
        x="Commune",
        y=["Femmes", "Hommes"],
        barmode="group",
        text_auto='.2s',
        title="Répartition des Femmes et des Hommes par Commune",
        color_discrete_sequence=["#1F4E79", "#3A8BCD"]
    )
    fig_sexe.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Commune",
        yaxis_title="Somme de Femmes et Somme de Hommes",
        legend_title="Sexe"
    )
    fig_sexe.update_traces(textposition='outside')
    st.plotly_chart(fig_sexe, use_container_width=True)
    st.write("---")
    
    
    df_fec_sorted = df_fec.sort_values(by="Fecondite", ascending=False)
    fig_fec = px.bar(
        df_fec_sorted,
        x="Commune",
        y="Fecondite",
        text_auto='.1f',
        title="Indicateur de Fécondité par Commune",
        color_discrete_sequence=["#1F4E79"]
    )
    fig_fec.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Commune",
        yaxis_title="Somme de Fécondité"
    )
    fig_fec.update_traces(textposition='outside')
    st.plotly_chart(fig_fec, use_container_width=True)
    st.write("---")
    
   
    df_hand_sorted = df_hand.sort_values(by="handicap", ascending=False)
    fig_hand = px.bar(
        df_hand_sorted,
        x="Commune",
        y="handicap",
        text_auto='.1f',
        title="Prévalence du handicap par Commune",
        color_discrete_sequence=["#1F4E79"]
    )
    fig_hand.update_layout(
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Commune",
        yaxis_title="Somme de handicap"
    )
    fig_hand.update_traces(textposition='outside')
    st.plotly_chart(fig_hand, use_container_width=True)
elif page == "Province de Tan-Tan":
    st.title("Tableau de bord - Province de Tan-Tan")
    st.write("---")
    
    
    df_pop = pd.read_excel(excel_file, sheet_name="tantan_population")
    df_sexe = pd.read_excel(excel_file, sheet_name="tantan_sexe")
    df_fec = pd.read_excel(excel_file, sheet_name="tantan_fecondite")
    df_hand = pd.read_excel(excel_file, sheet_name="tantan_handicap")
    
   
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Population total", value="100 134")
    with col2:
        st.metric(label="Population urbaine", value="85 410")
    with col3:
        st.metric(label="Population rurale", value="14 724")
    with col4:
        st.metric(label="Nombre de ménages", value="23 934")
        
    st.write("---")
    
    
    row1_col1, row1_col2 = st.columns(2)
    
    
    with row1_col1:
        df_pop_sorted = df_pop.sort_values(by="Population", ascending=False)
        fig_pop = px.bar(
            df_pop_sorted,
            x="Commune",
            y="Population",
            text_auto='.2s',
            title="Population par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
        fig_pop.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Population"
        )
        fig_pop.update_traces(textposition='outside')
        st.plotly_chart(fig_pop, use_container_width=True)
        
   
    with row1_col2:
        df_sexe_sorted = df_sexe.sort_values(by="Femmes", ascending=False)
        fig_sexe = px.bar(
            df_sexe_sorted,
            x="Commune",
            y=["Femmes", "Hommes"],
            barmode="group",
            text_auto='.2s',
            title="Répartition des Femmes et des Hommes par Commune",
            color_discrete_sequence=["#1F4E79", "#3A8BCD"]
        )
        fig_sexe.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Femmes et Somme de Hommes",
            legend_title="Sexe"
        )
        fig_sexe.update_traces(textposition='outside')
        st.plotly_chart(fig_sexe, use_container_width=True)
        
    st.write("---") 
    
   
    row2_col1, row2_col2 = st.columns(2)
    
   
    with row2_col1:
        df_fec_sorted = df_fec.sort_values(by="fecondite", ascending=False)
        fig_fec = px.bar(
            df_fec_sorted,
            x="Commune",
            y="fecondite",
            text_auto='.1f',
            title="Indicateur de Fécondité par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
        fig_fec.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Fécondité"
        )
        fig_fec.update_traces(textposition='outside')
        st.plotly_chart(fig_fec, use_container_width=True)
        
   
    with row2_col2:
        df_hand_sorted = df_hand.sort_values(by="handicap", ascending=False)
        fig_hand = px.bar(
            df_hand_sorted,
            x="Commune",
            y="handicap",
            text_auto='.1f',
            title="Prévalence du handicap par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
        fig_hand.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de handicap"
        )
        fig_hand.update_traces(textposition='outside')
        st.plotly_chart(fig_hand, use_container_width=True)
elif page == "Province d'Assa-Zag":
    st.title("Tableau de bord - Province d'Assa Zag")
    st.write("---")
    
  
    df_pop = pd.read_excel(excel_file, sheet_name="assa zag_population")
    df_sexe = pd.read_excel(excel_file, sheet_name="assa zag_sexe")
    df_fec = pd.read_excel(excel_file, sheet_name="assa sag_fecondite")
    df_hand = pd.read_excel(excel_file, sheet_name="assa zag_handicap")
    
   
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Population total", value="53 298")
    with col2:
        st.metric(label="Population urbaine", value="20 357")
    with col3:
        st.metric(label="Population rurale", value="32 941")
    with col4:
        st.metric(label="Nombre de ménages", value="6 297")
        
    st.write("---")
    
   
    row1_col1, row1_col2 = st.columns(2)
    
    
    with row1_col1:
        df_pop_sorted = df_pop.sort_values(by="Population", ascending=False)
        fig_pop = px.bar(
            df_pop_sorted,
            x="Commune",
            y="Population",
            text_auto='.2s',
            title="Population par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
        fig_pop.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Population"
        )
        fig_pop.update_traces(textposition='outside')
        st.plotly_chart(fig_pop, use_container_width=True)
        
    
    with row1_col2:
        df_sexe_sorted = df_sexe.sort_values(by="Hommes", ascending=False)
        fig_sexe = px.bar(
            df_sexe_sorted,
            x="Commune",
            y=["Hommes", "Femmes"],
            barmode="group",
            text_auto='.1f',
            title="Répartition des Hommes et des Femmes par Commune",
            color_discrete_sequence=["#1F4E79", "#3A8BCD"]
        )
        fig_sexe.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Hommes et Somme de Femmes",
            legend_title="Sexe"
        )
        fig_sexe.update_traces(textposition='outside')
        st.plotly_chart(fig_sexe, use_container_width=True)
        
    st.write("---")
    
    
    row2_col1, row2_col2 = st.columns(2)
    
   
    with row2_col1:
        df_fec_sorted = df_fec.sort_values(by="Fecondite", ascending=False)
        fig_fec = px.bar(
            df_fec_sorted,
            x="Commune",
            y="Fecondite",
            text_auto='.2f',
            title="Indicateur de Fécondité par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
        fig_fec.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de Fecondite"
        )
        fig_fec.update_traces(textposition='outside')
        st.plotly_chart(fig_fec, use_container_width=True)
        
   
    with row2_col2:
        #
        df_hand_sorted = df_hand.sort_values(by="handicap", ascending=False) 
        fig_hand = px.bar(
            df_hand_sorted,
            x="Commune",
            y="handicap",
            text_auto='.1f',
            title="Prévalence du handicap par Commune",
            color_discrete_sequence=["#1F4E79"]
        )
        fig_hand.update_layout(
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis_title="Commune",
            yaxis_title="Somme de handicap"
        )
        fig_hand.update_traces(textposition='outside')
        st.plotly_chart(fig_hand, use_container_width=True)