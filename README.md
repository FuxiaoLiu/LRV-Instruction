# Aligning Large Multi-Modal Model with Robust Instruction Tuning
[Fuxiao Liu](https://fuxiaoliu.github.io/), [Kevin Lin](https://sites.google.com/site/kevinlin311tw/me), [Linjie Li](https://www.microsoft.com/en-us/research/people/linjli/), [Jianfeng Wang](http://jianfengwang.me/), [Yaser Yacoob](https://www.umiacs.umd.edu/people/yaser), [Lijuan Wang](https://www.microsoft.com/en-us/research/people/lijuanw/)

[[Project Page](https://fuxiaoliu.github.io/LRV/)] [[Paper](http://arxiv.org/abs/2306.14565)] [[Online Demo](https://91d97bb65ef3654938.gradio.live)]

If the online demo doesn't work, please email `fl3es@umd.edu`.

Here is an overview of our work:

<p align="center">
    <a href="https://llava.hliu.cc/"><img src="./model.png" width="70%"></a> <br>
</p>

## Updates
- [x/x] We will release more data and finetuned checkpoints for different LMMs.
- [6/27] 🔥 Our paper is tweeted by [AK](https://twitter.com/_akhaliq).
- [6/26] 🔥 Our technical report is available on [arxiv](http://arxiv.org/abs/2306.14565).

## Contents
- [Dataset](#Visual_Instruction_Data_(LRV-Instruction))
- [Evaluation](#GAVIE)
- [Inference](#Inference)
- [Demo](#Demo)

## Visual Instruction Data (LRV-Instruction)
We **update** the dataset with 150k visual instructions generated by GPT4, covering 16 vision-and-language tasks with open-ended instructions and answers. LRV-Instruction include both positive instructions (85k) and negative instructions (70k) for more robust visual instruction tuning. The images of our dataset are from [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf). Our data can be accessed in `data/filter_cap.json` or download from [here](download.txt#L5).
```
{'image_id': '2392588', 'question': 'Can you see a blue teapot on the white electric stove in the kitchen?', 'answer': 'There is no mention of a teapot on the white electric stove in the kitchen.', 'task': 'negative'}
```
For each instance, `image_id` refers to the image from [Visual Genome](https://arxiv.org/pdf/1602.07332v1.pdf). `question` and `answer` refer to the instruction-answer pair. `task` indicates the task name. You can download the images from [here](download.txt#L12).

We provide our prompts for GPT-4 queries to better facilitate research in this domain. Please check out the `prompts` folder for positive and negative instance generation. `negative1_generation_prompt.txt` contains the prompt to generate negative instructions with Nonexistent Element Manipulation. `negative2_generation_prompt.txt` contains the prompt to generate negative instructions with Existent Element Manipulation. You can refer to the code [here](https://github.com/FuxiaoLiu/LRV-Instruction/blob/main/data/data_generation.py) to generate more data. Please see our paper for more details.

## GPT4-Assisted Visual Instruction Evaluation
We introduce GPT4-Assisted Visual Instruction Evaluation (GAVIE) as a more flexible and robust approach to measure the hallucination generated by LMMs without the need for human-annotated groundtruth answers. GPT4 takes the dense captions with bounding box coordinates as the image content and compares human instructions and model response. Then we ask GPT4 to work as a smart teacher and score (0-10) students’ answers based on two criteria: (1) Accuracy: whether the response is accurate concerning the image content.
(2) Relevancy: whether the response directly follows the instruction. `prompts/GAVIE.txt` contains the prompt of GAVIE. Please see our paper for more details.

## Model Setup

**1. Clone this repository**
```bash
https://github.com/FuxiaoLiu/LRV-Instruction.git
```

**2. Install Package**
```Shell
conda env create -f environment.yml --name LRV
conda activate LRV
```

**3.  Prepare the Vicuna weights** 

Our model is finetuned on MiniGPT-4 with Vicuna-7B. Please refer to instruction [here](https://github.com/Vision-CAIR/MiniGPT-4/blob/main/PrepareVicuna.md) to prepare the Vicuna weights or download from [here](download.txt#L8). Then, set the path to the Vicuna weight in [MiniGPT-4/minigpt4/configs/models/minigpt4.yaml](MiniGPT-4/minigpt4/configs/models/minigpt4.yaml#L15) at Line 15.

**4. Prepare the pretrained checkpoint of our model**

Download the pretrained checkpoints from [here](https://drive.google.com/drive/folders/15Uve6Av31Zd467aAc8N5Q_TkSdCjYoS1?usp=share_link).

Then, set the path to the pretrained checkpoint in [MiniGPT-4/eval_configs/minigpt4_eval.yaml](MiniGPT-4/eval_configs/minigpt4_eval.yaml#L11) at Line 11. This checkpoint is based on [MiniGPT-4-7B](https://github.com/Vision-CAIR/MiniGPT-4). We will release the checkpoints for  MiniGPT-4-13B and LLaVA in the future.

**5. Set the dataset path**

After getting the dataset, then set the path to the dataset path in [MiniGPT-4/minigpt4/configs/datasets/cc_sbu/align.yaml](MiniGPT-4/minigpt4/configs/datasets/cc_sbu/align.yaml#L5) at Line 5. The structure of the dataset folder is similar to the following:

```
/MiniGPt-4/cc_sbu_align
├── image(Visual Genome images)
├── filter_cap.json
```

## Inference

Set the path of the inference instruction file [here](MiniGPT-4/minigpt4/conversation/conversation.py/#L237), inference image folder [here](MiniGPT-4/minigpt4/conversation/conversation.py/#L234) and output location [here](MiniGPT-4/minigpt4/conversation/conversation.py/#L300).

```
cd ./MiniGPT-4
python inference.py --cfg-path eval_configs/minigpt4_eval.yaml  --gpu-id 0
```
## Demo

**Online Demo**

You can access to our online demo [here](https://91d97bb65ef3654938.gradio.live). If this link doesn't work, please email `fl3es@umd.edu` to update the link.

**Local Demo**

Try out the demo [demo.py](demo.py) of our finetuned model on your local machine by running

```
cd ./MiniGPT-4
python demo.py --cfg-path eval_configs/minigpt4_eval.yaml  --gpu-id 0
```
You can try the examples in [here](sample_images).


## Acknowledgement

- [Vicuna](https://github.com/lm-sys/FastChat): The fantastic language ability of Vicuna amazing.
- [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4): Many thanks to MiniGPT4, many of our codes are based on it!
- [Awesome-Multimodal-Large-Language-Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models#multimodal-instruction-tuning). The survey of LMMs is very helpful!


## Citation

If you find our work useful for your your research and applications, please cite using this BibTeX:
```bibtex
@article{Liu2023AligningLM,
  title={Aligning Large Multi-Modal Model with Robust Instruction Tuning},
  author={Fuxiao Liu and Kevin Lin and Linjie Li and Jianfeng Wang and Yaser Yacoob and Lijuan Wang},
  journal={ArXiv},
  year={2023},
  volume={abs/2306.14565}
}
```

## License
This repository is under [BSD 3-Clause License](LICENSE.md). 
Many codes are based on [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4) 
with BSD 3-Clause License [here](LICENSE_MiniGPT4.md).
