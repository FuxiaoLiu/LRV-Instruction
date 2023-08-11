### 🐒LRV-Mplug-Owl Setup

**1. Install the environment according to [mplug-owl](https://github.com/X-PLUG/mPLUG-Owl#Usage).**

We finetuned mplug-owl on 8 V100. If you meet any questions when implement on V100, feel free to let me know!

**2. Download the Checkpoint**

First download the checkpoint of mplug-owl from [link](https://huggingface.co/MAGAer13/mplug-owl-llama-7b-ft) and the trained lora model weight from [link](https://huggingface.co/MAGAer13/mplug-owl-llama-7b-ft)(released soon!).

**3. Edit the Code**

As for the `mplug-owl/serve/model_worker.py`, edit the following code and enter the path of the lora model weight in lora_path.
```
self.image_processor = MplugOwlImageProcessor.from_pretrained(base_model)
self.tokenizer = AutoTokenizer.from_pretrained(base_model)
self.processor = MplugOwlProcessor(self.image_processor, self.tokenizer)
self.model = MplugOwlForConditionalGeneration.from_pretrained(
     base_model,
     load_in_8bit=load_in_8bit,
     torch_dtype=torch.bfloat16 if bf16 else torch.half,
     device_map="auto"
 )
self.tokenizer = self.processor.tokenizer

        
peft_config = LoraConfig(target_modules=r'.*language_model.*\.(q_proj|v_proj)', inference_mode=False, r=8,lora_alpha=32, lora_dropout=0.05)
self.model = get_peft_model(self.model, peft_config)
lora_path = 'Your lora model path'
prefix_state_dict = torch.load(lora_path, map_location='cpu')
self.model.load_state_dict(prefix_state_dict)
```

**4. Local Demo**

When you launch the demo in local machine, you might find there is no space for the text input. This is because of the version conflict between python and gradio. The simplest solution is to do `conda activate LRV`

```
python -m serve.web_server --base-model 'the mplug-owl checkpoint directory' --bf16
```

**5. Model Inference**

First git clone the codr from [mplug-owl](https://github.com/X-PLUG/mPLUG-Owl), replace the `/mplug/serve/model_worker.py` with our `/utils/model_worker.py` and add the file `/utils/inference.py`. Then edit the [input data file](utils/inference.py#L405) and [image folder path](utils/inference.py#L401). Finally run:

```
python -m serve.inference --base-model 'your checkpoint directory' --bf16
```

## License
This repository is under [BSD 3-Clause License](LICENSE.md). 
Many codes are based on [MiniGPT4](https://github.com/Vision-CAIR/MiniGPT-4) and [mplug-Owl](https://github.com/Vision-CAIR/MiniGPT-4)
with BSD 3-Clause License [here](LICENSE_MiniGPT4.md).
