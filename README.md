# Using Transfer Learning for NLP with Small Data

For image classification tasks, transfer learning has proven to be very effective in providing good accuracy with fewer labeled datasets. Transfer learning is a technique that enables the transfer of knowledge learned from one dataset to another. Today, transfer learning in NLP is becoming ubiquitous. 

In this project I utilized a pre-trained GPT-2 model (345M) for the task of Question Answering on the [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/) dataset, as well as for text generation on a custom Star Wars dataset. The inference logic is wrapped in a Flask environment, Docker is used to containerize the Flask application, and the Docker container is hosted on an ec2 instance.

### How to use

Please visit [this link](http://ec2-18-216-18-180.us-east-2.compute.amazonaws.com/) to view the final product and try it yourself!

Simply add any context paragraph you like, ask a question, and get a response from the model.


# OpenAI Citation
@article{radford2019language,
  title={Language Models are Unsupervised Multitask Learners},
  author={Radford, Alec and Wu, Jeff and Child, Rewon and Luan, David and Amodei, Dario and Sutskever, Ilya},
  year={2019}
}
