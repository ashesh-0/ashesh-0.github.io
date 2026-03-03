<!-- ---
title: "PhD & Prior Research"
--- -->

# PhD Research

During my PhD in the [Jug Lab](https://humantechnopole.it/en/people/florian-jug/), I worked on image decomposition tasks for microscopy data. Fluorescence microscopy is a vital tool in life sciences, enabling visualization of cellular and sub-cellular structures using fluorescent markers. However, technical constraints limit the number of structures that can be imaged simultaneously. My PhD addresses this limitation by proposing methods to decompose superimposed fluorescence images—where multiple structures are captured in a single channel—into distinct channels through super- vised image decomposition and unsupervised denoising.

<div style="text-align: center;">
<img src="assets/images/teaser.png" alt="drawing" class="center" width="500px" height="auto"
title="Splitting: An image decomposition task" style="display: block; margin: auto; max-width: 100%; height: auto;"/>
</div>

Below are the specific projects I worked on during my PhD:

* **[scSplit](https://neurips.cc/virtual/2025/loc/mexico-city/poster/115037)**: An architecture designed to have generalization with respect to the mixing-ratio, which is the relative strength of structures superimposed on an image (NeurIPS 25).
* **[MicroSplit](https://www.biorxiv.org/content/10.1101/2025.02.10.637323v1)**: Combining uSplit and denoiSplit into a single network, thereby acquiring GPU efficiency and self-supervised denoising into a single architecture. A comprehensive evaluation on 36 semantic unmixing tasks from 9 datasets, in collaboration with 8 other labs (Accepted at Nature Methods 2026).
* **[denoiSplit](https://ashesh-0.github.io/denoiSplit/)**: An architecture for unsupervised denoising together with decomposition, supporting multi-prediction and model calibration (ECCV 24).
* **[microSSIM](https://ashesh-0.github.io/MicroSSIM/)**: A variant of SSIM suited for unsupervised denoising tasks on microscopy data (BIC workshop, ECCV 24).
* **[uSplit](https://ashesh-0.github.io/uSplit/)**: A HVAE inspired architecture for efficient image decomposition (ICCV 23).
* **[Latent Space Splitting](/structural_noise_removal.md)**: Structural noise removal using contrastive learning on the latent space.

# Prior Research & Experience in Industry

Before my PhD, I worked as a Research Assistant in Taipei, and as a Data Scientist:

* **[Gaze Estimation](/gaze_estimation.md)**: My work on 3D Gaze estimation in the wild at Vision-lab, NTU (BMVC 2021).
* **[Qplum](/qplum.md)**: My experience and learnings working as a Data Scientist at the online investment advisory firm Qplum.
