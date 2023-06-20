# Aligning Large Multi-Modal Model with Robust Instruction Tuning
[Fuxiao Liu](https://fuxiaoliu.github.io/), [Kevin Lin](https://sites.google.com/site/kevinlin311tw/me), [Linjie Li](https://www.microsoft.com/en-us/research/people/linjli/), [Jianfeng Wang](http://jianfengwang.me/), [Yaser Yacoob](https://www.umiacs.umd.edu/people/yaser), [Lijuan Wang](https://www.microsoft.com/en-us/research/people/lijuanw/)

[[Project Page](https://fuxiaoliu.github.io/LRV/)] [[Paper](https://fuxiaoliu.github.io/LRV/)] [[Demo](https://fuxiaoliu.github.io/LRV/)]  [[Data](https://fuxiaoliu.github.io/LRV/)] [[Model](https://fuxiaoliu.github.io/LRV/)]

Here is an overview of our work:

<p align="center">
    <a href="https://llava.hliu.cc/"><img src="./model.png" width="70%"></a> <br>
</p>

## Release
- [6/17] 🔥 Our technical report is available on [arxiv](https://fuxiaoliu.github.io/LRV/) and [demo](https://fuxiaoliu.github.io/LRV/).


## Visual Instruction Data (LRV-Instruction)
We release a dataset consisting of 120k visual instructions generated by GPT4, covering 16 vision-and-language tasks with open-ended instructions and answers. LRV-Instruction include both positive and negative instructions for more robust visual instruction tuning. The images of our dataset are from [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf). Our data can be accessed in `data/filter_cap.json`.
```
{'image_id': '2392588', 'question': 'Can you see a blue teapot on the white electric stove in the kitchen?', 'answer': 'There is no mention of a teapot on the white electric stove in the kitchen.', 'task': 'negative'}
```
For each instance, `image_id` refers to the image from [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf). `question` and `answer` refer to the instruction-answer pair. `task` indicates the task name.

## GPT4 Prompt
We provide our prompts for GPT-4 queries to better facilitate research in this domain. Please check out the `prompts` folder for positive and negative instance generation.

## GPT4-Assisted Visual Instruction Evaluation
