# Import libraries
import streamlit as st
import os, sys
from pymongo import MongoClient
from urllib.request import urlopen
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings
from llama_index.llms.groq import Groq
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.core import VectorStoreIndex

sys.path.insert(0, './')

# Add helper client
from AtlasClient import AtlasClient

st.set_page_config(layout="wide")

# Define variables
DB_NAME = 'steam_games2'
COLLECTION_NAME = 'embedded_games2'
INDEX_NAME  = 'games_index2'

ATLAS_URI = st.secrets["ATLAS_URI"]
GROQ_API = st.secrets["GROQ_API"]


# Initialization function
def initialize():
    print(f"ATLAS_URI detected is: {ATLAS_URI}")

    if not ATLAS_URI:
        raise Exception ("'ATLAS_URI' is not set. Please set it in .env before continuing...")

    ip = urlopen('https://api.ipify.org').read()
    print (f"My public IP is '{ip}.  Make sure this IP is allowed to connect to cloud Atlas")

    os.environ['LLAMA_INDEX_CACHE_DIR'] = os.path.join(os.path.abspath('./'), 'cache')

    st.session_state.atlas_client = AtlasClient(ATLAS_URI, DB_NAME)
    print ('Atlas client succesfully initialized!')

    # Generate embeddings for the given query
    embed_model = HuggingFaceEmbedding(model_name='Alibaba-NLP/gte-base-en-v1.5', device='cuda', trust_remote_code=True)
    llm = Groq(model="mixtral-8x7b-32768", api_key=GROQ_API)

    # Set the LLM and embed_model in the Settings for further usage
    Settings.llm = llm
    Settings.embed_model = embed_model

# Query function
def run_vector_query (query):
    output_container = st.empty()

    with output_container.container():
        st.write (f'Running query for: ***{query}***')
        mongodb_client = MongoClient(ATLAS_URI)

        try:
            # Initialize a MongoDBAtlasVectorSearch instance with the MongoDB client, database name, collection name, and index name.
            # This object will be used for vector search operations on the specified MongoDB collection.
            vector_store = MongoDBAtlasVectorSearch(mongodb_client, db_name=DB_NAME, collection_name=COLLECTION_NAME, index_name=INDEX_NAME)

            # Create an index using the VectorStoreIndex class, initializing it with the provided vector store.
            # This index will enable efficient search operations on the vectors stored in the MongoDB collection.
            index = VectorStoreIndex.from_vector_store(vector_store)

            response = index.as_query_engine().query(query)

            # Create list for unique data
            unique_data = []

            # Loop through each node in response.source_nodes
            for node_with_score in response.source_nodes:
                # Access the metadata of the current node
                metadata = node_with_score.node.metadata

                # Get value of metadata
                name = metadata.get('Name')
                about = metadata.get('About the game')
                price = metadata.get('Price')
                date = metadata.get('Release date')
                image = metadata.get('Header image')
                developer = metadata.get('Developers')
                publisher = metadata.get('Publishers')

                # Add data to list if its unique
                if name not in [data.get('Name') for data in unique_data]:
                    unique_data.append({'Name': name, 'About the game': about, 'Price': price, 'Release date': date, 'Image': image, 'Developers': developer, 'Publishers': publisher})

            st.markdown(f"<p style='font-size:25px'>{response}</p>", unsafe_allow_html=True)
            for data in unique_data:
                st.markdown(f"<h1 style='text-align: center; margin-top: 50px'><b>{data['Name']}</b></h1>", unsafe_allow_html=True)
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(' ')
                with col2:
                    st.image(data['Image'], caption=data['Name'], use_column_width='auto')
                with col3:
                    st.write(' ')
                st.markdown(f"<p>{data['About the game']}</p>", unsafe_allow_html=True)
                st.markdown(f"<p><b>Price: $ {data['Price']}</b></p>", unsafe_allow_html=True)
                st.markdown(f"<p><b>Release date: {data['Release date']}</b></p>", unsafe_allow_html=True)
                st.markdown(f"<p><b>Developers: {data['Developers']}</b></p>", unsafe_allow_html=True)
                st.markdown(f"<p><b>Publishers: {data['Publishers']}</b></p>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Somethings wrong with the Llama API. Please try again. {str(e)}")

# Configuring the display
# Initiatize only once
if 'atlas_client' not in st.session_state:
    initialize()

# Streamlit App
st.markdown("<h1 style='text-align: center; font-size:50px; margin-bottom: 50px'><b>Games Recommender Capstone Project</b></h1>", unsafe_allow_html=True)

# User Input: Search Query
user_query = st.text_input("What kind of games do you want to play?")

# Button to trigger the recommendation
if st.button("Submit"):
    output_container = st.container()
    search_result = run_vector_query(user_query)
