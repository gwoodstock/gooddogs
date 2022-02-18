# sources: https://towardsdatascience.com/embedding-tableau-in-streamlit-a9ce290b932b
        #  https://docs.streamlit.io/library/components/components-api

import streamlit as st
import streamlit.components.v1 as components

def main():
    st.header('Explore Shelter Dog Data')

    # st.text('Insert executive summary/info about project here')

    # st.sidebar.image(
    #     'https://images.unsplash.com/photo-1586671267731-da2cf3ceeb80?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8ZG9nfGVufDB8MXwwfHw%3D&auto=format&fit=crop&w=800&q=60',
    #     use_column_width=True
    #     )

    html_temp = """<div class='tableauPlaceholder' id='viz1645160046723' style='position: relative'><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FindyourDog&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1645160046723');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1220px';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1220px';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1477px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
    # components.html(html_temp, scrolling=True, width=1220, height=560)
    components.html(html_temp, scrolling=True, width=1550, height=950)

if __name__ == "__main__":    
    main()