import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import base64
import plotly.express as px
import seaborn as sns
import io
import time as ti
def load_data():
    df = pd.read_csv('assets/data.csv')
    df.replace({'H': 'HOME', 'A': 'AWAY', 'CF ': 'CF', 'Dec-13': '13/14', 'LW ': 'LW'}, inplace=True)
    df.loc[(df['Playing_Position'].isna()) & (df['Club'] == 'Manchester United'), 'Playing_Position'] = 'RW'
    df.loc[(df['Playing_Position'].isna()) & (df['Club'] == 'Real Madrid'), 'Playing_Position'] = 'LW'
    df.loc[(df['Playing_Position'].isna()) & (df['Club'] == 'Sporting CP'), 'Playing_Position'] = 'RW'
    shot = ['Right-footed shot', 'Left-footed shot']
    df.loc[(df['Type'].isnull()), 'Type'] = np.random.choice(shot)
    df.drop(df[df['Competition'] == 'UEFA Champions League Qualifying'].index, axis=0, inplace=True)
    return df
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
def unique_df(df):
    data = pd.DataFrame(df.apply(lambda col: len(col.unique())), columns=['uniq_count'])
    return data
st.set_page_config(page_title="dasboard",page_icon=":material/bar_chart:")
st.markdown(
    """
    <style>
    .stApp h1 {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# st.title("Ur.cristiano🐐")
st.sidebar.title('Cr7-ANALYTICS-📊')
st.sidebar.image('assets/cristiano_poster2.jpg', use_column_width=True)
sections = ['introduction', 'basic_exploration', 'goals per competion', 'goals per position', 'goals per club',
            'goals per season', 'goal types', 'scoreline after goals', 'assists providers', 'favorite opponent',
            'goal per minute', 'goals per venue']
selections = st.sidebar.radio('navigate to', sections)
image_base64 = get_base64_image("assets/sidebar_bw_potriat.jpg")

st.markdown(
    f"""
    <style>
    [data-testid="stSidebar"] {{
        background: linear-gradient(rgba(0, 0, 0, -0.9), rgba(0, 0, 0, 0.0)),
                    url("data:image/jpeg;base64,{image_base64}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .slide_in {
        animation: slideIn 0.5s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

df = load_data()
ti.sleep(0.3)
st.markdown('<div class="slide_in">',unsafe_allow_html=True)

if selections == 'introduction':
    st.markdown(
        '<h3 style="color:yellow;">Introduction</h3>',
        unsafe_allow_html=True
    )
    image_base64 = get_base64_image("assets/intro_bg.jpg")

    # Apply CSS with the Base64 image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1)),
                    url("data:image/jpeg;base64,{image_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: scroll;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "Cristiano Ronaldo dos Santos Aveiro is a Portuguese professional footballer who plays as a forward for and captains both the Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won numerous individual accolades throughout his career, such as five Ballon d'Or awards, a record three UEFA Men's Player of the Year Awards, four European Golden Shoes, and was named five times the world's best player by FIFA,[note 3] the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, most appearances (30), assists (8), goals in the European Championship (14), international appearances (217) and international goals (135). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 900 official senior career goals for club and country, making him the top goalscorer of all time")
    st.markdown('<center>',unsafe_allow_html=True)
    st.write(f'Date of birth :5 February 1985 (age 38) ')
    st.write(f'Place of birth :Funchal, Madeira, Portugal')
    st.write(f' Position (st) :Forward ')
    st.write(f'Current team :Al Nassr')
    st.markdown('</center>',unsafe_allow_html=True)
    # st.text('')
    st.image('assets/career_journey.jpg',use_column_width=True)
    st.markdown(
        '<h3 style="color:yellow;">Career Journey</h3>',
        unsafe_allow_html=True
    )
    st.write(
        "Ronaldo began his senior career with Sporting CP, before signing with Manchester United in 2003, winning the FA Cup in his first season. He went on to win three consecutive Premier League titles, the Champions League and the FIFA Club World Cup; at age 23, he won his first Ballon d'Or. Ronaldo was the subject of the then-most expensive association football transfer when he signed for Real Madrid in 2009 in a transfer worth €94 million (£80 million). He became a key contributor and formed an attacking trio with Karim Benzema and Gareth Bale which was integral to the team winning four Champions Leagues from 2014 to 2018, including La Décima. During this period, he won back-to-back Ballons d'Or in 2013 and 2014, and again in 2016 and 2017, and was runner-up three times behind Lionel Messi, his perceived career rival. He also became the club's all-time top goalscorer and the all-time top scorer in the Champions League, and finished as the competition's top scorer for six consecutive seasons between 2012 and 2018. With Real, Ronaldo won four Champions Leagues, two La Liga titles, two Copas del Rey, two UEFA Super Cups and three Club World Cups. In 2018, he signed for Juventus in a transfer worth an initial €100 million (£88 million), the most expensive transfer for an Italian club and for a player over 30 years old. He won two Serie A titles and broke several goalscoring records for Juventus. He returned to Manchester United in 2021, before his contract was terminated in 2022. In 2023, he signed for Al Nassr")
    st.markdown(
        '<h3 style="color:yellow;">Collective Awards</h3>',
        unsafe_allow_html=True
    )
    st.write("Over the course of his career, Portuguese footballer Cristiano Ronaldo has received five Ballon d'Or/FIFA Ballon d'Or awards,[a] the most for a European player. Widely regarded as one of the greatest players of all time, Ronaldo holds the record for most goals in the UEFA Champions League (140 goals), and the record for most goals in the UEFA European Championship (14), its qualification stage (40), and the FIFA Club World Cup (7), as well as most goals scored in a UEFA Champions League season (17 in 2013–14), most international goals (135), and most appearances in a national team (217). He has scored a record 919 senior career goals for club and country. Moreover, he is one of the few recorded players to have made over 1,250 professional career appearances.")
    st.write("Collectively, Ronaldo has won 33 senior trophies in his career. He has also attained one title from youth and at least five titles from friendly competitions. All in all he had won over 300 trophies and medals by January 2021, with some of them dating back to his childhood")
    # st.markdown(
    #     '<h3 style="color:yellow;">Current Club:Al nassr</h3>',
        # unsafe_allow_html=True
     # )
    st.image("assets/trophies.jpg",use_column_width=True)
    st.markdown('<a href="https://www.bing.com/search?q=ronaldo%20current%20club&pc=0P453&ptag=C999ABAE753BAF6&form=PCF444&conlogo=CT3210127">click here to know morw about him</a>',unsafe_allow_html=True)
elif selections == "basic_exploration":
    st.subheader('overall data card')
    st.markdown('**untill 2022**')
    st.dataframe(df.head(15))
    st.markdown("**Categorical data description**")
    st.dataframe(df.describe(include=['object']).T)
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.markdown("**Dataset information**")
    st.text(s)
    st.markdown("**unique values in dataset**")
    data = unique_df(df)
    st.dataframe(data)
elif selections == 'goals per competion':
    fig = px.histogram(df, x='Competition', color='Club', hover_name='Club', hover_data=['Competition', 'Club'],
                       title='goals per competion', height=500)
    st.markdown('**goals per competion**')
    st.plotly_chart(fig)
    st.markdown('**data table for above graphs**')
    st.dataframe(df['Competition'].value_counts())
    fif1 = px.histogram(df, x='Competition', color='Type', hover_data=['Competition', 'Club'],
                        title='goals per competion (Type)', height=800)
    st.plotly_chart(fif1)
    st.write('dataset for above graph')
    dc = df.groupby(['Type', 'Competition']).count()
    dc.drop(['Matchday', 'Date', 'Venue', 'Club',
             'Opponent', 'Result', 'Playing_Position', 'Minute', 'At_score',
             'Goal_assist'], axis=1, inplace=True)
    dc.columns=['goals']
    st.dataframe(dc)
elif selections == 'goals per position':
    fig = px.histogram(df, x='Playing_Position', color='Type', hover_name='Playing_Position',
                       hover_data=['Playing_Position', 'Club'], title='goals per position', height=800)
    st.plotly_chart(fig)
    st.write('Datatable for above graph')
    st.dataframe(pd.DataFrame(df['Playing_Position'].value_counts()))
    fig1 = px.histogram(df, x='Playing_Position', color='Club', title='played position inn different clubs',color_discrete_map={'Sporting CP':'green', 'Manchester United':'red' ,'Real Madrid':'silver' ,'Juventus FC':'black'
 ,'Al-Nassr FC':'yellow'})
    fig1.update_layout(plot_bgcolor='white')
    st.plotly_chart(fig1)
    nw_df=df.groupby(['Playing_Position','Club']).count()
    nw_df=pd.DataFrame(nw_df['Season'])
    nw_df.columns = ['goals']
    st.write('Datacard for above graph')
    st.dataframe(nw_df)
elif selections == 'goals per club':
    fig = px.histogram(df, x='Club', color='Competition', hover_name='Playing_Position',
                       hover_data=['Playing_Position', 'Competition'], title='goals per club', height=800,animation_frame='Playing_Position',animation_group='Venue')
    fig.update_layout(template='presentation')
    fig.update_layout(
        updatemenus=[
            {
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [None, {"frame": {"duration": 5000, "redraw": True}, "fromcurrent": True}],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate"}],
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "type": "buttons",
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top",
            }
        ]
    )

    st.plotly_chart(fig)
    st.write('Datatable for above graph')
    st.dataframe(df['Club'].value_counts())
elif selections == 'goals per season':
    df['Season'] = df['Season'].sort_values()
    fig = px.histogram(df, x='Season', color='Competition', hover_name='Playing_Position',
                       hover_data=['Playing_Position', 'Club', 'Type'], title='goals per season', height=500)
    st.plotly_chart(fig)
    st.write('Datatable for above graph')
    st.dataframe(df['Season'].sort_index().value_counts())
elif selections=="assists providers":
    df1 = pd.DataFrame(df.Goal_assist.value_counts())[:10]
    df1.reset_index(inplace=True)
    df1.columns = ['players','assist']
    df1=df1.sort_values('assist',ascending=False)
    ranks=[]
    for i in range(10):
        ranks.append(f'Rank{i+1}')
    df1['Ranks']=ranks
    fig=px.bar(df1,x='assist',title="top 10 assist providers",y='players',color='assist',orientation='h',hover_data=['Ranks'])
    st.write('Data card for the above graph')
    st.plotly_chart(fig)
    st.dataframe(df1)
elif selections=='goal types':
    fig=px.histogram(df,height=800,x='Type',color='Venue',hover_data=['Club'],title='types of goals',color_discrete_map={'HOME':'lightgreen','AWAY':'yellow'})
    dc=df.groupby(['Type','Venue']).count()
    dc=dc[['Season']]
    # dc.reset_index(inplace=True)
    dc.columns=['goals']
    st.plotly_chart(fig)
    st.write("Data card for above graph")
    st.dataframe(dc)
elif selections=='goal per minute':
    df['min_label']=df['Minute'].apply(eval)
    bn=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 130]
    lbl=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-8-0','80-90','90-130(extra time)']
    df['min_label']=pd.cut(df['min_label'],bins= bn,labels=lbl)
    df.sort_values('min_label',ascending=True,inplace=True)
    fig=px.histogram(df,x='min_label',color='Club',title='goals per minutes',hover_data=['Minute'],height=800,color_discrete_map={'Sporting CP':'green', 'Manchester United':'red' ,'Real Madrid':'silver' ,'Juventus FC':'black'
 ,'Al-Nassr FC':'yellow'})
    st.plotly_chart(fig)
elif selections=="goals per venue":
    fig=px.histogram(df,x='Venue',color='Competition',title="goals per venue",width=1000,height=800,hover_data=['Opponent'])
    st.plotly_chart(fig)
    st.write('data for above graph')
    dc=df.groupby(['Venue']).count()
    st.dataframe(dc['Season'])
elif selections=='favorite opponent':
    dc = pd.DataFrame(df['Opponent'].value_counts()[:10])
    dc.reset_index(inplace=True)
    dc.columns = ['opponents', 'goals']
    fig=px.bar(dc,y='goals',x='opponents',title='top ten fav opponents',color='opponents')
    st.plotly_chart(fig)
    st.write('Datacard for above graph')
    st.dataframe(dc)
elif selections=="scoreline after goals":
    dc=dc=pd.DataFrame(df.At_score.value_counts()[:10])
    dc.reset_index(inplace=True)
    dc.columns = ['score_stamp', 'counts']
    fig=px.bar(dc,x='score_stamp',y='counts',title="score_stamp after thee goal",color='counts')
    st.plotly_chart(fig)
    st.write("datacard for above chart")
    st.dataframe(dc)
st.markdown('</div>',unsafe_allow_html=True)
