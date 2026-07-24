<!-- ---
title: "PhD & Prior Research"
--- -->

# Overview
The main focus of this lab is to apply deep-learning techniques, preferably to biological and biomedical data. Within this data domain, image/video data and protein sequence data are the ones for which projects are ongoing. However, outside this domain, deep learning based computer vision tasks on natural images can also be of interest provided the student has a plan (and can convince me ;)). 

## Specific tasks
Self-supervison methods for representation learning and self-supervised finetuning, semantic unmixing, tasks involving protein sequence (using Alphafold family): for instance Amyloidogenic nature prediction, and segmentation and tracking. 

### Representation Learning
Annotations are generally hard to come by in biological data. 
Morever, the inherent variability in acquisition: arising from a plethora of hyper-parameters like different hardware, dwell time, laser power etc etc, renders the small set of annotated datasets less generalizable. This calls for SSL (self-supervised learning) on a much larger set of unannotated data. Such pretrained networks can then easily be adapted to a specific task with small annotated datasets. In this lab, we plan to persue several tasks on this theme, some of which are in progress and some of which will be taken up soon. Capturing the representation of diverse Mitochondria phenotypes in the latent space is one direction. 

The other use of SSL is in self-supervised finetuning, which is another option if one already has pre-trained models, trained on an annotated data, and the objective is to use it on another data with a relatively small distribution shift: large enough to cause the pre-trained models yield inferior performance, but small enough to be within the capability of SSL finetuning. One such application is in Semantic unmixing, which is covered next. 

### Semantic Unmixing
In semantic unmixing, given a superimposed input image $x=c_1 + c_2 +... c_k$, the objective is to extract individual constituents. The ultimate objective is to empower multi-color imaging in Fluorescence Microscopy. With semantic unmixing, one would capture a superimposed image containing multiple structures overlapped onto each other (like nucleus and mitochondria), and a deep-learning based setup would extract individual constituents, thereby enabling higher multiplexing and/or better photon efficiency. With self-supervised denoising baked into the setup, this approach promises working with lower SNR images, and in doing so, enables even better photon efficiency.

There are currently two outstanding issues limiting the widespread use of this methodology, both related to generalizability of the  trained models.

1. Generalizability (different microscope configurations): A deep learning model trained on data from one microscope acquisition may not perform optimally on images from a different acquisition with another microscope. To address this, self-supervised fine-tuning is essential. Note that users with their own images would typically only have superimposed versions, without separate structure images for supervision. Handling varying magnification levels would also be a valuable contribution. This approach addresses a key limitation: if superimposed inputs and individual targets can be imaged simultaneously, the method's main benefit is improved photon efficiency. However, training on independently acquired target images—without paired superimposed inputs, and subsequently finetuning with just superimposed input images—enables much broader applications.

2. Generalizability (different structures): The broad question is: we have limited data for any specific set of structures. For example, one would have a limited data to train A vs B task. And a limited data for B vs C task. And a limited data to train X vs Y task. The question we ask is, can we somehow train these together, so that the network learns to unmix structures better jointly when compared with training individual models. 

### Protein Sequence
The objective is to initiate a line of research on protein sequence data (AlphaFold family). To begin, we will target a specific problem: developing computational tools for research on AL-Amyloidosis disease. Compared to other diseases, light chains (LCs)—a sub-component of malfunctioning antibodies—exhibit much greater structural diversity. Our hypothesis is that such diversity implies higher information content in the primary sequence, which can be extracted for a useful objective.

### Segmentation & Tracking
Conversations with image analysis facilities (as I've had the fortune to do) reveal that roughly half of all analysis requests involve segmentation and/or tracking. This underscores the importance of developing methods for these tasks. A specific project for which I have the data focuses on instance segmentation of epithelial cells to better quantify how their shape shifts from circular to hexagonal.