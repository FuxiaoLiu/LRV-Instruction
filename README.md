# Aligning Large Multi-Modal Model with Robust Instruction Tuning
[Fuxiao Liu](https://fuxiaoliu.github.io/), [Kevin Lin](https://sites.google.com/site/kevinlin311tw/me), [Linjie Li](https://www.microsoft.com/en-us/research/people/linjli/), [Jianfeng Wang](http://jianfengwang.me/), [Yaser Yacoob](https://www.umiacs.umd.edu/people/yaser), [Lijuan Wang](https://www.microsoft.com/en-us/research/people/lijuanw/)

[[Project Page](https://fuxiaoliu.github.io/LRV/)] [[Paper](https://fuxiaoliu.github.io/LRV/)] [[Demo](https://fuxiaoliu.github.io/LRV/)]  [[Data](https://fuxiaoliu.github.io/LRV/)] [[Model](https://fuxiaoliu.github.io/LRV/)]
### Introduction
Despite the promising progress in multi-modal tasks, current large multi-modal models (LMM) are prone to hallucinate inconsistent descriptions with respect to the associated image and human instructions.

LRV-Instruction. We addresses this issue by introducing the first large and diverse visual instruction tuning dataset, named Large-scale Robust Visual (LRV)-Instruction. Our dataset consists of 120k visual instructions generated by GPT4, covering 16 vision-and-language tasks with open-ended instructions and answers. We also design LRV-Instruction to include both positive and negative instructions for more robust visual instruction tuning. Our negative instructions are designed at two semantic levels: (i) Nonexistent Element Manipulation and (ii) Existent Element Manipulation.
GAVIE. To efficiently measure the hallucination generated by LMMs, we propose GPT4-Assisted Visual Instruction Evaluation (GAVIE), a novel approach to evaluate visual instruction tuning without the need for human-annotated groundtruth answers and can adapt to diverse instruction formats. We conduct comprehensive experiments to investigate the hallucination of LMMs.
Result. Our results demonstrate that existing LMMs exhibit significant hallucination when presented with our negative instructions, particularly with Existent Element Manipulation instructions. Moreover, by finetuning MiniGPT4 on LRV-Instruction, we successfully mitigate hallucination while improving performance on public datasets using less training data compared to state-of-the-art methods. Additionally, we observed that a balanced ratio of positive and negative instances in the training data leads to a more robust model.

Here is an overview of our work:

<p align="center">
    <a href="https://llava.hliu.cc/"><img src="./model.png" width="70%"></a> <br>
</p>

## Release
- [6/17] 🔥 Our technical report is available on [arxiv](https://fuxiaoliu.github.io/LRV/) and [demo](https://fuxiaoliu.github.io/LRV/).


## Install
### 1. Prepare the code and the environment
### 2. Prepare the pretrained Vicuna weights

## Launching Demo Locally

## Visual Instruction Data

## GPT4-Assisted Visual Instruction Evaluation
