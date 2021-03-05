# Using Transfer Learning for NLP with Small Data

For image classification tasks, transfer learning has proven to be very effective in providing good accuracy with fewer labeled datasets. Transfer learning is a technique that enables the transfer of knowledge learned from one dataset to another. Today, transfer learning in NLP is becoming ubiquitous. 

In this project I a pre-trained GPT-2 model (345M) for the task of Question Answering on the [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) dataset, as well as for text generation on a custom dataset. The inference logic is wrapped in a Flask environment, Docker is used to containerize the Flask application, and the Docker container is hosted on an ec2 instance.

Please visit () to view the final product! (Edit: please send me an email at mattjacobs@g.ucla.edu) if you would like the website link, as I am not leaving the ec2 instance running)


# OpenAI Citation
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
