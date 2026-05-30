
<br>
<p align="center">
  <h1 align="center"><strong>OMGTex: One-stage Multi-style Facial Texture Reconstruction without Geometry Guidance</strong></h1>
  <h3 align="center">🔥 CVPR 2026 🔥 </h3>
  <p align="center">
    <a href="https://github.com/XZT24" target="_blank">Zitong Xiao</a><sup>1*</sup>&emsp;
    <a href="https://www.semanticscholar.org/author/Yuda-Qiu/51152863" target="_blank">Yuda Qiu</a><sup>1*</sup>&emsp;
    <a href="https://www.linkedin.com/in/yezisheng/" target="_blank">Zisheng Ye</a><sup>1</sup>&emsp;
    <a href="https://dblp.org/pid/60/8294" target="_blank">Xiaoguang Han</a><sup>1,2</sup>
    <br>
    <sup>1</sup>SSE, CUHK-Shenzhen&nbsp;&nbsp;
    <sup>2</sup>Fnii, CUHK-Shenzhen&nbsp;&nbsp;
    <sup>*</sup>Equal Contribution
  </p>
</p>

<div id="top" align="center">
  
[![arXiv](https://img.shields.io/badge/arXiv-2605.25778-blue)](https://arxiv.org/abs/2605.25778)

</div>

<div align="center">
  <img src="assets/teaser.png" alt="Illustration" width="96%">
</div>

---

## 🔥 News
- **[2026-02]** Our paper was accepted by CVPR2026 ! 🥳
- **[2026-04]** Our paper was released on <a href="https://github.com/XZT24/OMGTex/blob/main/OMGTex.pdf" target="_blank">Github</a>.
- **[2026-05]** Our paper was available on <a href="https://arxiv.org/abs/2605.25778" target="_blank">Arxiv</a>. 
- **[2026-05]** The preliminary codebase and checkpoints have been released. If you find our work helpful, please consider giving the repository a ⭐. Thank you for your support!

---

## ⭐ Overview
**OMGTex** is an end-to-end diffusion-based framework for reconstructing high-quality and editable facial UV textures from multi-style facial images.
Existing texture reconstruction methods face two major limitations: 

**(1)** Fragility due to reliance on 3D geometry priors, which are difficult to estimate accurately, especially under facial occlusions or in stylized domains; 

**(2)** A lack of semantic disentanglement, inhibiting region-specific texture editing and style transfer. Our work addresses both challenges simultaneously.

Our core innovation is a geometry-free pipeline that directly maps a 2D face image to its corresponding editable UV texture. We introduce two key techniques: 

**First**, to address the challenge of UV misalignment common in diffusion generation, we introduce a gradient-guided refinement strategy at inference time, which explicitly corrects structural consistency. 

**Second**, we leverage the inherent semantic distribution capability of diffusion models and design a novel training paradigm to enhance this tendency, enabling semantic-aware editing of facial texture. 

**Furthermore**, to address the data scarcity in multi-style texture reconstruction, we construct CANVAS, the first comprehensive paired texture reconstruction dataset covering realistic and diverse stylized domains.
   
---

## 📖 Framework
Coming soon...


---

## 📝 TODO
- \[x\] Release the github page.
- \[x\] Release the paper.
- \[x\] Release the code and pretrained ckpt.

---


## 📢 Preliminary Release

Thanks for your patience!

We have released the preliminary version of the codebase and checkpoints. Please download the checkpoints from the following link:

- **Checkpoint:** [Google Drive](https://drive.google.com/file/d/1CpEy75n9ZwYisvHqPdRrWaOZkMhvEkgG/view?usp=drive_link)

### Important Notes

This is currently a **preliminary release**. The **Gradient-Guided Texture Alignment** module has been disabled by default.

During our internal evaluation, we found that the model used for texture keypoint detection exhibits limited generalization ability in certain cases, which may negatively affect the final reconstruction quality. We are therefore retraining this component and plan to release an improved version in the near future.

To make the complete codebase available before the conference, we decided to temporarily disable this module in the current release. As a result, reconstructed textures may exhibit slight structural misalignments compared to the results reported in the paper.

### Current Solutions

#### Option 1: Use the Current Release Directly

In most cases, the current implementation is already capable of reconstructing diverse and faithful facial textures across a wide range of styles. We recommend trying this option first before enabling additional refinement or optimization steps.

#### Option 2: Enable Gradient-Guided Texture Alignment

The implementation of the **Gradient-Guided Texture Alignment** module is still included in the released code.

You can enable it by setting:

```python
gradient_guided_refine = True
```

in `infer.py`.

After enabling the module, you may replace the texture keypoint detection model with your own trained model by placing it in the corresponding directory specified in the codebase.

#### Option 3: Texture Post-Optimization

As discussed in the paper, the textures reconstructed by **OMGTex** can serve as strong initialization for downstream texture optimization frameworks, leading to more photorealistic results.

We recommend using the optimization pipeline provided by **AvatarTex** or **FFHQ-UV**:

- **AvatarTex:** https://github.com/XZT24/AvatarTex
- **FFHQ-UV:** https://github.com/csbhr/FFHQ-UV

Please refer to the AvatarTex repository for implementation details and optimization instructions.

---

## 📚 Getting Started

Please first download the checkpoints provided above.

We provide two versions of pretrained models:

- **Ver1**: A lightweight implementation that generally achieves better reconstruction fidelity for common facial styles.
- **Ver2**: Offers stronger generalization capability across a wider range of artistic and stylized facial appearances.

Choose the version that best fits your application scenario.

## 🛠️ Environment Setup

Please configure the environment according to the dependencies listed in `requirements.txt`.

Our implementation uses **FLUX.1-dev** as the base diffusion model. The model will be downloaded automatically when running `infer.py` for the first time. Alternatively, you may manually download it from the following Hugging Face repository:

- https://huggingface.co/black-forest-labs/FLUX.1-dev

## 🚀 Reconstruction Example

After completing the environment setup and downloading the required checkpoints, you can reconstruct facial textures by running:

```bash
python infer.py
```

The reconstructed texture maps will be saved to the designated output directory specified in the configuration.

---

## 📬 Contact
If you have questions about the paper, feel free to open an issue or contact:
- **Zitong Xiao**: `120090766@link.cuhk.edu.cn`

---

## 🔗 Citation
If you find our work helpful, please cite:

```bibtex
@misc{xiao2026omgtexonestagemultistylefacial,
      title={OMGTex: One-stage Multi-style Facial Texture Reconstruction without Geometry Guidance}, 
      author={Zitong Xiao and Yuda Qiu and Zisheng Ye and Xiaoguang Han},
      year={2026},
      eprint={2605.25778},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2605.25778}, 
}

