# This repository contains a preliminary implementation of OMGTex.
# The codebase is built upon and modified from EasyControl:
# https://github.com/Xiaojiu-z/EasyControl

import torch
from PIL import Image
from src.pipeline import FluxPipeline
from src.transformer_flux import FluxTransformer2DModel
from src.lora_helper import set_single_lora, set_multi_lora

def clear_cache(transformer):
    for name, attn_processor in transformer.attn_processors.items():
        attn_processor.bank_kv.clear()

# Initialize the model
device = "cuda"
base_path = "black-forest-labs/FLUX.1-dev"  # Path to your base model
pipe = FluxPipeline.from_pretrained(base_path, torch_dtype=torch.bfloat16, device=device)
transformer = FluxTransformer2DModel.from_pretrained(
    base_path, 
    subfolder="transformer",
    torch_dtype=torch.bfloat16, 
    device=device
)
pipe.transformer = transformer
pipe.to(device)

lora_path = "./checkpoint/lora.safetensors"

# Single condition control example
set_single_lora(pipe.transformer, lora_path, lora_weights=[1], cond_size=512)

# Set your control image path
subject_image_path = "./test_imgs/1.png"
control_image = Image.open(subject_image_path).convert("RGB")
prompt = "The texture map of human face."

image = pipe(
    prompt,
    height=512,
    width=512,
    guidance_scale=3.5,
    num_inference_steps=25,
    max_sequence_length=512,
    spatial_images=[],
    subject_images=[control_image],
    cond_size=512,
    gradient_guided_refine=False,
).images[0]
# Clear cache after generation
clear_cache(pipe.transformer)
image.save("output.png")

