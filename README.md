# Building Customized RAG Model Project Bounty

[Recommender-Games-Project App](https://recommender-games-project.streamlit.app/)

For this project, I am developing an application that assists users in providing game recommendations to help gamers find games that match their preferences, such as genre, publisher, developer, rating, and more. To build this project, I am utilizing MongoDB's Atlas Vector Search, the Groq API ([https://groq.com/](https://groq.com/)) for the Large Language Model (LLM), and the Alibaba-NLP/gte-base-en-v1.5 model ([https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5)) to create embeddings. As for the game dataset, I am using the FronkonGames/steam-games-dataset ([https://huggingface.co/datasets/FronkonGames/steam-games-dataset](https://huggingface.co/datasets/FronkonGames/steam-games-dataset)). I have included a file named populate_rag_database.ipynb ([https://github.com/ikhsanashki/RAG-Bounty-Project/blob/main/populate_rag_database.ipynb](https://github.com/ikhsanashki/RAG-Bounty-Project/blob/main/populate_rag_database.ipynb)) to prepare the dataset, index it, and upload it to the MongoDB database. Don't forget to create an Atlas Vector Search and modify the Index Definition to:
![2](https://github.com/ikhsanashki/RAG-Bounty-Project/assets/169969056/396dc7cd-3435-4704-8112-c588ce6d9b33)


Once everything is set up and ready, the application is prepared to be launched and put into operation.

![1](https://github.com/ikhsanashki/RAG-Bounty-Project/assets/169969056/1096c4e2-cca9-404a-acf9-bd10084c3a0d)


##
I will explain some details about this application as follows:


![3](https://github.com/ikhsanashki/RAG-Bounty-Project/assets/169969056/499dee9d-49dc-491b-ba81-78a5a35a892a)

First, the user will be prompted to enter a query about anything they want to ask regarding games.
##

![4](https://github.com/ikhsanashki/RAG-Bounty-Project/assets/169969056/b37bda32-ba38-497b-ab3c-933e37c8c274)

Next, this is the result of the answer generated by the AI in response to the user's query, based on the dataset that we previously prepared.
##

![5](https://github.com/ikhsanashki/RAG-Bounty-Project/assets/169969056/0d3cd6c1-bddc-45ce-a121-e9bb6c10bd5e)
![6](https://github.com/ikhsanashki/RAG-Bounty-Project/assets/169969056/00841f6d-4f1e-449f-b835-326baf52f5a2)

Lastly, this is the result from the user's query, retrieved from the game dataset that we had previously prepared.
##
I would like to express my gratitude to StackUp and MongoDB for organizing this bounty, as it has allowed me to learn about the Retrieval-Augmented Generation (RAG) model as well as Vector Search. This opportunity has been incredibly valuable in expanding my knowledge and skills.
