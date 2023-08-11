## Evaluation on VQA datasets
We run evaluation on [GQA](https://cs.stanford.edu/people/dorarad/gqa/download.html) dataset by randomly selecting 500 samples and evaluating by GPT4 ([prompt](Evaluation/GQA_Evaluation_prompt.txt)) from [paper](https://arxiv.org/abs/2305.10355).

In order to reproduce the results, first download [GQA](https://cs.stanford.edu/people/dorarad/gqa/download.html) and select the samples. Second, format the input data as json file and set the path of the inference instruction file [here](MiniGPT-4/minigpt4/conversation/conversation.py/#L237), inference image folder [here](MiniGPT-4/minigpt4/conversation/conversation.py/#L234) and output location [here](MiniGPT-4/minigpt4/conversation/conversation.py/#L300). Third, after getting the output from models, follow the [prompt](Evaluation/GQA_Evaluation_prompt.txt) to format the input for GPT4. One example is below:
```
You are an examiner who can judge whether students' answer match the correct answers. Next, I will provide you with the question, students' answer and groundtruth answer as reference. Please judge which answers are better.

Question: Which kind of furniture is in front of the mirror?"
Correct Answer: couch

Student Answer1: Leaning brown leather sofa
Student Answer2: </Img> There are two people sitting on a couch in front of the mirror.</s>

output format:
Student Answer1:
Student Answer2:
```

