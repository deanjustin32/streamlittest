import streamlit as st

st.set_page_config(
    page_title="Seattle Crash Assessment",
    page_icon="https://marvel-b1-cdn.bc0a.com/f00000000103807/www.cityyear.org/wp-content/uploads/2020/04/cityscapesCYFullNewColors_SeattleCityscape.png",
)

# Introduction Paragraphs
st.write("# Introduction")
st.write(
    """
    When considering transportation safety, predicting the likelihood of survival from vehicle crashes has emerged as a crucial area of research and development.
    With an ever-increasing number of vehicles on the road and the inherent risks associated with traffic accidents, understanding the factors that contribute to survival outcomes has become key to increasing vehicle crash survival rates.

    By leveraging advancements in data analytics and machine learning, we are striving to develop predictive models capable of accurately estimating the probability of survival in various crash scenarios.
    This promising field not only holds immense potential for improving vehicle safety standards but also offers valuable insights to inform policy decisions, enhance emergency response protocols, and ultimately save countless lives.
    """
)

# Project Background
st.write("# Project Background")
st.write(
    """
    Our group will be developing an app that will predict the degree of injury based on the conditions of crashes in Seattle, Washington.
    This app will ask users a series of questions that will lead the app to a conclusion of the most likely outcome of injury severity.
    By gathering essential information such as the type of collision, vehicle speed, and location, our app will allow users to gain insights into potential injury risks.
    Our project aims to bridge the gap between transportation safety, user-friendly application, and promoting safer experiences on the road.
    """
)

# Data
st.write("# Data")
st.write("Seattle SDOT Collisions Data: [Kaggle Dataset](https://www.kaggle.com/datasets/jonleon/seattle-sdot-collisions-data)")

# Resources
st.write("# Resources")

# Tabs
st.write("# Tabs")
selected_tab = st.sidebar.radio("Select a tab", ["Home", "Prediction Tool", "Map", "Graphs", "Team"])

if selected_tab == "Home":
    # Jumbotron and GIF
    st.image("https://marvel-b1-cdn.bc0a.com/f00000000103807/www.cityyear.org/wp-content/uploads/2020/04/cityscapesCYFullNewColors_SeattleCityscape.png", width=600)
    st.markdown("## Probability of Crash Survival in Seattle, WA.")
    st.markdown("When considering transportation safety, predicting the likelihood of survival from vehicle crashes has emerged as a crucial area of research and development.")
    st.markdown("With an ever-increasing number of vehicles on the road and the inherent risks associated with traffic accidents, understanding the factors that contribute to survival outcomes has become key to increasing vehicle crash survival rates.")

elif selected_tab == "Prediction Tool":
    st.markdown("## Prediction Tool")
    # Add content specific to the Prediction Tool tab

elif selected_tab == "Map":
    st.markdown("## Map")
    # Add content specific to the Map tab

elif selected_tab == "Graphs":
    st.markdown("## Graphs")
    # Add content specific to the Graphs tab

elif selected_tab == "Team":
    st.markdown("## Team")
    # Add content specific to the Team tab