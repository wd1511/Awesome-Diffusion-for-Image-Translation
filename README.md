# Diffusion for Image-to-Image Translation

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/wd1511/Awesome-Diffusion-for-Image-Translation)

A curated bibliography of diffusion-based image translation, editing and style transfer, including closely related diffusion bridges and flow-matching methods.

**Last updated: 2026-10-16.** New entries are checked against arXiv records and official proceedings or author project pages. Unconfirmed publication venues remain labeled as arXiv; affiliations and additional resource links are included when verified. This is a curated collection, not an exhaustive index.

```Latex
**Here is the Paper Name** <br>
*Author 1, ..., Author n.* <br>
**Classification of papers**, Author Affiliation <br>
Conference or Journal Year. [[PDF](link)] [[Project](link)] [[Github](link)] [[Data](link)] <br>
```

Download all PDF files
```
python download.py
```

- [Dataset](#dataset)
- [2026](#2026)
- [2025](#2025)
- [2024](#2024)
- [2023](#2023)
- [2022](#2022)
- [2021](#2021)


## Dataset

### Game Datasets

GTA5 dataset: [[Download](https://download.visinf.tu-darmstadt.de/data/from_games/index.html)] <br>
Viper dataset: [[Download](https://playing-for-benchmarks.org)] <br>

### Real-world Datasets

Cityscapes dataset: [[Download](https://www.cityscapes-dataset.com/downloads/)] <br>
BDD100K dataset: [[Download](https://bdd-data.berkeley.edu)] <br>

### Painter Datasets

Wiki-Art dataset: [[Download1](https://www.kaggle.com/competitions/painter-by-numbers/)] [[Download2](https://huggingface.co/datasets/huggan/wikiart)] <br>

### Common Datasets

ImageNet dataset: [[Download](https://image-net.org/download.php)] <br>
MS-COCO dataset [[Download1](https://cocodataset.org/#download)] [[Download2](https://huggingface.co/datasets/detection-datasets/coco)] <br>
LSUN dataset [[Download1](http://lsun.cs.princeton.edu/2017)] [[Download2](https://hyper.ai/datasets/5675)] [[Download(church)](https://huggingface.co/datasets/tglcourse/lsun_church_train)] [[Download(bedrooms)](https://huggingface.co/datasets/pcuenq/lsun-bedrooms)] <br>
AFHQv2 dataset [[Download1](https://www.dropbox.com/scl/fi/0aha0j1yvhjdnr1r86u0g/?rlkey=ji6v8s9tkma1vg87bwowi9v1e&e=1)] [[Download2](https://huggingface.co/datasets/huggan/AFHQv2)] <br>

### Medical Datasets

Prostate-MRI-US-Biopsy dataset [[Download1](https://www.cancerimagingarchive.net/collection/prostate-mri-us-biopsy/)] [[Download2](https://drive.google.com/file/d/1kF0g8fMR5XPQ2FTbutfTQ-hwG_mTqerx/view)] <br>
LDCT-and-Projection-data  dataset [[Download1](https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=52758026)] [[Download2](https://drive.google.com/file/d/1kF0g8fMR5XPQ2FTbutfTQ-hwG_mTqerx/view)] <br>
BraTS 2018 dataset [[Download1](https://www.med.upenn.edu/sbia/brats2018/)] [[Download2](https://drive.google.com/file/d/1kF0g8fMR5XPQ2FTbutfTQ-hwG_mTqerx/view)] <br>

### Style Transfer and Image Editing Benchmarks

- OmniStyle-1M / OmniStyle-150K (CVPR 2025) [[Paper](https://arxiv.org/abs/2505.14028)] [[Project](https://wangyephd.github.io/projects/OmniStyle/cvpr25_omnistyle.html)] [[Download (150K)](https://huggingface.co/datasets/StyleXX/OmniStyle-150k)] <br>
- HQ-Edit (ICLR 2025) [[Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b639c526a942618f1dba2b7a5fa0bac0-Abstract-Conference.html)] <br>
- ImgEdit and ImgEdit-Bench (NeurIPS 2025) [[Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/bec783f119b969772c35243b1c801090-Abstract-Datasets_and_Benchmarks_Track.html)] <br>
- KRIS-Bench (NeurIPS 2025) [[Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/e619b285582fb12f4c3de3a507b8b99c-Abstract-Datasets_and_Benchmarks_Track.html)] <br>
- I2I-Bench (CVPR 2026) [[Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_I2I-Bench_A_Comprehensive_Benchmark_Suite_for_Image-to-Image_Editing_Models_CVPR_2026_paper.html)] <br>
- Language-based Image Colorization benchmark / Color-Turbo (2025) [[Paper](https://arxiv.org/abs/2503.14974)] [[Github](https://github.com/lyf1212/Color-Turbo)] <br>
- StyleID (SIGGRAPH 2026) [[Paper](https://arxiv.org/abs/2604.21689)] [[Project](https://kwanyun.github.io/StyleID_page/)] <br>

- VeriEdit-Bench (2026) [[Paper](https://arxiv.org/abs/2610.04381)] [[Resource](https://github.com/flare200020/VeriEdit-Bench)] <br>
- ASTRA-Data / ASTRA-Score (2026) [[Paper](https://arxiv.org/abs/2610.10003)] <br>
- ScribbleEdit (2026) [[Paper](https://arxiv.org/abs/2610.09382)] <br>
- SlideBench (2026) [[Paper](https://arxiv.org/abs/2610.14253)] <br>
- InfoEdit (2026) [[Paper](https://arxiv.org/abs/2609.33286)] [[Resource](https://infoedit.github.io)] <br>
- EditJudgeBias (2026) [[Paper](https://arxiv.org/abs/2610.01670)] <br>
- CE-Bench (2026) [[Paper](https://arxiv.org/abs/2610.18819)] <br>
- LME-Bench (2026) [[Paper](https://arxiv.org/abs/2609.35611)] <br>
- ChartStyle-100K / ChartStyle-Bench (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/5569)] [[Resource](https://github.com/yuweiyang-anu/ChartStyle)] <br>
- EditHF-1M (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/4044)] [[Resource](https://github.com/IntMeGroup/EditHF)] <br>
- PhyEditBench (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/5047)] [[Resource](https://github.com/Previsior/PhyEditBench)] <br>
- UniREditBench / UniREdit-Data-100K (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/4175)] <br>
- RCEdit-500K (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/5946)] <br>
- WeEdit (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/4337)] <br>
- GRADE (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/3710)] [[Resource](https://grade-bench.github.io/)] <br>

### Virtual Try-On Benchmarks

- OpenVTON-Bench (NeurIPS 2026) [[Paper](https://arxiv.org/abs/2601.22725)] [[Github](https://github.com/RenxingIntelligence/OpenVTON-Bench)] <br>
- TripVVT (ECCV 2026) [[Paper](https://arxiv.org/abs/2604.27958)] <br>
- MVShoes / MVShoes-clean (NeurIPS 2025) [[Paper](https://arxiv.org/abs/2610.18325)] [[Resource](https://colorful-liyu.github.io/ShoeFit/)] <br>
- VTON-QBench (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/5449)] [[Resource](https://github.com/litelightlite/VTON-IQA)] <br>
- VTEdit-Bench (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/3764)] <br>
- Fit4Men (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/4018)] [[Resource](https://github.com/tiny-smart/FitControler)] <br>
- LVTON (ECCV 2026) [[Paper](https://eccv.ecva.net/virtual/2026/poster/4142)] <br>

## 2026

**SIA: Selective Image Analogy** <br>
*Amir Alimohammadi, Kian Izadpanah, Bardiya Kariminia, Yiorgos Chrysanthou, Ali Mahdavi-Amiri.* <br>
**Image Editing**, Simon Fraser University, Canada & University of Cyprus, Cyprus & Shahid Beheshti University, Iran & CYENS Centre of Excellence, Cyprus <br>
SIGGRAPH Asia 2026. [[Paper](https://selective-image-analogy.github.io/)]
[[Project](https://selective-image-analogy.github.io/)]
[[Github](https://github.com/alimohammadiamirhossein/selective-image-analogy)] <br>

**ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning** <br>
*Sara Dorfman, Nir Goren, Gal Barak, Daniel Cohen-Or, Or Patashnik.* <br>
**Image Editing**, Tel Aviv University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.22328)]
[[Project](https://saradorfman1.github.io/ACEdit/)] <br>

**Rethinking Classifier-Free Guidance for TI2I Flow Matching** <br>
*Andreas Floros, Elena Koritska, Teofilo de Campos, Christoph Vogel, Chu-Tak Li, Anuj Sharma, Alexandros Neophytou.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.21550)] <br>

**Intern Lumina U2: A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding and Image Generation** <br>
*Qian Yu, Zongyang Qiu, Juncheng Yan, Hongliang Li, Qi Qin, Keqi Wang, Siqi Luo, Junkui Ju, Yapeng Mi, Tiantian Lu, Tian Liu, Pengyu Xie, Chenhao Ji, Minghui Zhang, Yiang Zhao, Siyu Yan, Haiying Xu, Yanbo Wang, Jianghan Shen, Yuandong Pu, Jiayi Lei, Borui Zhang, Jinxin Shi, Bo Zhang, Yuhang Zang, Shenglong Ye, Lixin Gu, Hongjie Zhang, Linghan Liu, Xinyuan Chen, Yuewen Cao, Lihe Zhang, Xiaohong Liu, Junjun He, Qiangwei Liu, Qi Zhang, Yu Cheng, Tianfan Xue, Hui Xiong, Chang Xu, Yu Qiao, Yihao Liu, Bin Fu.* <br>
**Image Editing**, Shanghai AI Laboratory & Shanghai Jiao Tong University & Huawei Technologies, Shenzhen, China & Dalian University of Technology & Tsinghua University & Shanghai Innovation Institute & The University of Sydney & HKUST(GZ) & SIAT, CAS & USTC & The Chinese University of Hong Kong <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.20818)]
[[Project](https://internlm.github.io/InternLumina-U2)]
[[Github](https://github.com/InternLM/InternLumina-U2)]
[[Model](https://huggingface.co/internlm/InternLumina-U2)] <br>

**BluePixel: Toward Native 4K Agentic Image Editing** <br>
*Shanyan Guan, Shiyu Li, Xin Li, Zhizhou Chen, Yunzhe Xu, Yuehao Liu, Ruixue Shen, Shiju Zhang, Min Jin, Qiang Liu, Junbo Liu, Penggang Shi, Sheng Sun, Xiao Wang, Yong Zhang, Zhongang Qi, Wei Li, Chao Ma, Ying Tai, Yanhao Ge.* <br>
**Image Editing**, vivo Mobile Communication Co., Ltd. & Nanjing University & Shanghai Jiao Tong University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.19882)]
[[Project](https://tech.vivo.com/BluePixel)]
[[Github](https://github.com/vivo/BluePixel)] <br>

**DuplexBridge: Coordinating Understanding and Generation for Unified Image Editing** <br>
*Yidi Liu, Jie Xiao, Chaojie Mao, Jingfeng Zhang, Xueyang Fu.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.18819)] <br>

**BridgeTwist: Twisting Schrödinger Bridges for Training-Free Conditional Sampling** <br>
*Mengyu Li, Qianqian Qu, Jun S. Liu.* <br>
**Base I2I Translation**, Department of Statistics and Data Science, Tsinghua University, Beijing, China <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2610.18658)] <br>

**Efficient Scene-Text Refinement via Pixel-Space Grouped Image Generation** <br>
*Yaoli Liu, Guo-Hua Wang, Yiyang Chen, Qing-Guo Chen, Zhao Xu, Weihua Luo, Yao-Xiang Ding.* <br>
**Image Editing**, State Key Lab of CAD&CG, Zhejiang University & Alibaba Group & State Key Laboratory of General Artificial Intelligence, Peking University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.18284)] <br>

**SliderEdit++: Improved Slider Trajectories in Instruction-Based Image Editing** <br>
*Arman Zarei, Sayan Nag, Bryan Wang, Franck Dernoncourt, Varun Manjunatha, Nedim Lipka, Soheil Feizi, Samyadeep Basu.* <br>
**Image Editing**, Adobe Research & University of Maryland <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.14253)] <br>

**What We Talk About When We Talk About Emotion Editing** <br>
*Xingzu Zhan, Lin Gu, Ruogu Fang.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.13558)] <br>

**ThinkDrag: Semantic Drag-Based Image Editing with Visual Reasoning** <br>
*Armando Fortes, Tianyi Wei, Chindanai Trakantannarong, Shangchen Zhou, Xingang Pan.* <br>
**Image Editing**, S-Lab, Nanyang Technological University, Singapore <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.13316)]
[[Project](https://atfortes.github.io/projects/thinkdrag/)] <br>

**Temporal Diffusion Bridge Model for Vessel Extraction Using Physics-informed Synthetic Data** <br>
*Jinkui Hao, Donald R. Cantrell, Ramez Abdalla, Sameer A. Ansari, Bo Zhou.* <br>
**Medical Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.14105)]
[[Github](https://github.com/Advanced-AI-in-Medicine-and-Physics-Lab/TDBM)] <br>

**Rubric-CEPR: Self-Evolving Image Editing via Reward-Verified Self-Distillation** <br>
*Ritesh Thawkar, Shubham Patle, Shravan Venkatraman, Rao Muhammad Anwer.* <br>
**Image Editing**, Mohamed bin Zayed University of Artificial Intelligence & Aalto University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.12469)]
[[Github](https://github.com/riteshthawkar/Rubric-CEPR)]
[[Project](https://riteshthawkar.github.io/Rubric-CEPR/)] <br>

**VibeEdit: Image Editing with Canvas Instructions** <br>
*Jinjing Zhao, Fangyun Wei, Yitong Wang, Xiuyu Wu, Yunuo Chen, Yang Yue, Sirui Zhang, Wenbo Wang, Hongyang Zhang, Dong Chen, Yan Lu, Chang Xu.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.12229)]
[[Project](https://zhaojingjing713.github.io/VibeEdit/)] <br>

**Healthy Counterfactual Generation via Diffusion Inpainting for Mammography Classification** <br>
*Inês Cruchinho Garcia, Mariana Mourão, Francisco Maria Calisto, Carlos Santiago, Jacinto Nascimento.* <br>
**Medical Image Translation**, Institute for Systems and Robotics, Instituto Superior Técnico, Lisbon, Portugal <br>
MICCAI Deep-Brea3th Workshop 2026. [[PDF](https://arxiv.org/abs/2610.12147)]
[[Github](https://github.com/ines03garcia/diffusion-based-counterfactual-generation)] <br>

**VINCIE-NExT: Unlocking Video Editing from Images via In-Context Modeling** <br>
*Leigang Qu, Feng Cheng, Ziyan Yang, Bangbang Yang, Zhaoyang Huang, Wei Chow, Yicong Li, Wenjie Wang, Tat-Seng Chua, Yan Zeng.* <br>
**Video Editing**, National University of Singapore & ByteDance Seed & University of Science and Technology of China <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2610.12104)]
[[Project](https://vincie-next.github.io/)]
[[Conference](https://neurips.cc/virtual/2026/poster/152863)] <br>

**Transforming Image Editors into Video Editors** <br>
*Feng Wang, Zijie Li, Ceyuan Yang, Alan Yuille, Peng Wang.* <br>
**Video Editing**, ByteDance Seed & Johns Hopkins University <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2610.11037)]
[[Github](https://github.com/wangf3014/AVE)]
[[Conference](https://neurips.cc/virtual/2026/poster/149320)] <br>

**Perceptually Aligned Evaluation of Style Transfer** <br>
*Yang Deng, Eleftherios Ioannou, David Mould, Steve Maddock, Paul L. Rosin, Yu-Kun Lai.* <br>
**Dataset / Evaluation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.10003)] <br>

**ScribbleEdit: A Benchmark for Scribble-Only Image Editing** <br>
*Jie Ren, Hao Kang, Kai Guo, Yiding Yang, Bo Liu, Liming Jiang, Qing Yan, Zichuan Liu, Yizhi Song, Yue Xing, Hui Liu, Xin Lu.* <br>
**Dataset / Evaluation**, ByteDance & Michigan State University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.09382)] <br>

**Zero-Shot Brain MRI Inpainting with 2.5D Unconditional Flow Priors** <br>
*Arnela Hadzic, Franz Thaler, Simon Johannes Joham, Martin Urschler.* <br>
**Medical Image Translation**, Institute for Medical Informatics, Statistics and Documentation, Medical University of Graz, Graz, Austria <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.08983)]
[[Github](https://github.com/imigraz/brats2026-inpainting)] <br>

**Local Content-Style Control for Diffusion-based Image Stylization** <br>
*Amir Semmo.* <br>
**Image Style Transfer**, Digital Masterpieces GmbH , Potsdam , Germany <br>
SIGGRAPH Asia Technical Communications 2026. [[PDF](https://arxiv.org/abs/2610.08704)] <br>

**Disentangling Dual Image References in Frequency Aware Diffusion Models for Personalized Generation** <br>
*Haipeng Liu, Yang Wang, Meng Wang.* <br>
**Image Style Transfer**, School of Computer Science and Information Engineering, Hefei University of Technology, China <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2610.07684)]
[[Github](https://github.com/htyjers/Dual-FDM)] <br>

**UniSlider: Perceptually Uniform Sliders for Continuous Image Editing** <br>
*David Serrano-Lozano, Duygu Ceylan, Yannick Hold-Geoffroy, Iliyan Georgiev, Javier Vazquez-Corral, Anna Frühstück.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.06831)]
[[Project](https://color.cvc.uab.cat/unislider)] <br>

**Scalable Minimal-Change Learning for Controllable Image Editing** <br>
*Shuo Chen, Fengming Huang, Yu Yao, Mingming Gong, Tongliang Liu.* <br>
**Image Editing**, Sydney AI Centre, The University of Sydney & University of Melbourne <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2610.06021)]
[[Github](https://github.com/Showwwwwwwww/ARRO)]
[[Conference](https://neurips.cc/virtual/2026/poster/153198)] <br>

**FACET: Factorized Asymmetric Conditioning for Efficient Transport in High-Fidelity Fluorescence Microscopy Synthesis** <br>
*Sazan Mahbub, Caleb N. Ellington, Eric P. Xing.* <br>
**Medical Image Translation**, Carnegie Mellon University & GenBio AI & Mohamed bin Zayed University of AI <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.05353)] <br>

**Salvation Lies Within: Eliciting Inherent Style Transfer in Step-Distilled Diffusion Models** <br>
*Shengyin Sun, Yiming Li, Yingzhao Lian, Xing Li, Xingzhi Zhou, Anxin Tian, Zhili Wang, Haoyang Li, Ziqiang Cui, Chen Ma.* <br>
**Image Style Transfer**, Huawei Technologies & Hong Kong Polytechnic University & City University of Hong Kong <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.05066)]
[[Github](https://github.com/sunshy-1/StyleForge)] <br>

**TRACE: Time-Adaptive Residual Attention Control with Content-Style Decomposition for Training-Free Diffusion Style Transfer** <br>
*Duc Khoan Le, Kim Ngoc Tran, Minh Nhat Le, Thanh An Tran, Viet Toan Nguyen, Khanh An Lay, Tran Thai Son, Hoang Pham Minh.* <br>
**Image Style Transfer**, Faculty of Information Technology, University of Science, Ho Chi Minh City, Vietnam & Vietnam National University, Ho Chi Minh City, Vietnam <br>
ACCV 2026. [[PDF](https://arxiv.org/abs/2610.04922)]
[[Github](https://github.com/pixelchemy-research/TRACE)] <br>

**FASTER: Fast Adjoint Stochastic Transport for Endpoint Refinement in Reward-Guided Image Editing** <br>
*Yimiao Zhou, Zejia Zhong, Jingya Wang, Ye Shi.* <br>
**Image Editing**, ShanghaiTech University, Shanghai, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.04538)] <br>

**Beyond Plausibility: Verifiable Fine-Grained Image Editing on Structured Assets** <br>
*Muyao Wang, Chen Zhu, Shiqi Yang, DongHyun Hwan, Hideki Nakayama.* <br>
**Dataset / Evaluation**, SB Intuitions & University of Tokyo <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.04381)]
[[Github](https://github.com/flare200020/VeriEdit-Bench)] <br>

**Uncertainty as a Proxy for Semantic Correctness in Diffusion-Based Medical Image Synthesis** <br>
*Yuxuan Ou, Konstantinos Kamnitsas, OxAAA Study, AICT Consortium, Regent Lee, Vicente Grau.* <br>
**Medical Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.03224)] <br>

**Distributionally Robust Schrödinger Bridge** <br>
*Jinhwan Sul, Panagiotis Theodoropoulos, Vincent Pacelli, Jaemoo Choi, Evangelos Theodorou.* <br>
**Base I2I Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.02043)] <br>

**When Text-to-Image Helps Editing: The Effects of Conditioning During Denoising** <br>
*Lidia Troeshestova, Alexander Ustyuzhanin, Sergey Kastryulin.* <br>
**Image Editing**, HSE University & Yandex <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.01681)] <br>

**Do MLLM Judges Judge the Edit? Auditing Bias in Image Editing Evaluation with Verified Quality Preservation** <br>
*Yuan Huang, Zirui Song, Xiuying Chen.* <br>
**Dataset / Evaluation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.01670)] <br>

**Spatially Gated Diffusion for Localized Counterfactual Chest Radiograph Editing** <br>
*Kamran Ullah Afaq, Basit Raza.* <br>
**Medical Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.00805)] <br>

**CPathOGen: Spatially and Morphologically Controlled H&E Counterfactuals for Probing Pathology Models** <br>
*Samarth Singhal, Varang Rai.* <br>
**Medical Image Translation**, University of North Dakota & Google <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.00602)]
[[Github](https://github.com/a12dongithub/PathOGen)]
[[Model](https://huggingface.co/a12donhf/CPathOGen)] <br>

**TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning** <br>
*Zijing Qin, Jun Zhou, Ruicheng Zhang, Jiaqi Hou, Zunnan Xu, Ronghui Li, Zhenyu Xie, Xiu Li.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.39335)] <br>

**Diffusion Editing with Soft Mask: Pixel Level Redo of Image and Video with Adjustable Strength** <br>
*Candi Zheng, Yuan Lan.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.00359)] <br>

**STEPS: Scene Text Editing with Preserved Style Using Diffusion and Contrastive Style Encoding** <br>
*Nicolas Thiebaut, Nameer Hirschkind, Xiao Yu, Kyle Spence.* <br>
**Image Editing**, Roblox, San Mateo, CA, USA <br>
PAKDD 2026. [[PDF](https://arxiv.org/abs/2609.38636)] <br>

**CLeaR: A Unified Framework for Resolving the Leakage-Degradation Dilemma in Style Transfer** <br>
*Teng Zhou, Yunhao Chen.* <br>
**Image Style Transfer**, Zhejiang University & Fudan University <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2609.38136)]
[[Github](https://github.com/0606zt/CLeaR)]
[[Conference](https://neurips.cc/virtual/2026/poster/151839)] <br>

**The Camera Inside the Editor: Reading the Implicit Camera of Image Editors with Painted Calibration Patterns** <br>
*Sebastian Rückerl.* <br>
**Dataset / Evaluation**, University of Hagen, Germany <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.37732)] <br>

**PCaPaint: Prostate Cancer Inpainting by Mitigating Shortcut Learning** <br>
*Levente Lippenszky, Hongxu Yang, Marcell Dömötör, Krisztian Koos, László Ruskó.* <br>
**Medical Image Translation**, GE HealthCare <br>
MICCAI DGM4MICCAI Workshop 2026. [[PDF](https://arxiv.org/abs/2609.37350)] <br>

**LoRA Direction Extraction for Controllable Light Toggling in FLUX.1 Kontext** <br>
*Petr Golenderov, Dmitry Mazyar, Natalia Sovpel, Alexander Aksenov.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2610.03771)] <br>

**Drag as Evidence: Motion-Grounded Latent Recomposition for Drag-Based Editing** <br>
*Xinyu Pu, Hongsong Wang, Jie Gui, Pan Zhou.* <br>
**Image Editing**, Southeast University & Purple Mountain Laboratories & Singapore Management University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.36755)] <br>

**Mind the RefGAP: Correcting Reference Attention in Diffusion-Based Visual Editing** <br>
*Yanan Wang, Shengcai Liao, Guangyi Liu, Xiaodan Liang.* <br>
**Image Editing**, Mohamed bin Zayed University of Artificial Intelligence, Institute of Foundation Models & United Arab Emirates University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.35708)]
[[Project](https://yanan-wang-cs.github.io/RefGAP/)] <br>

**FlowTool: Controlling Tool Parameter in Image Retouching via Flow Matching** <br>
*Thanh-Long V. Le, Steven Walton, Seunghyun Yoon, Branislav Kveton, Trung Bui, Eunho Yang, Viet Lai.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.35673)] <br>

**On-Policy Self-Distillation for Multi-Turn Image Editing** <br>
*Liangbing Zhao, Le Zhuo, Mohamed Elhoseiny.* <br>
**Image Editing**, KAUST & Krea AI <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.35611)] <br>

**Tilted Schrödinger Bridge Matching** <br>
*Sergei Kholkin, Evgeny Burnaev, Alexander Korotin.* <br>
**Base I2I Translation**, Applied AI Institute <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.34642)] <br>

**Attention-Scoped Guidance: Training-Free Spatial Control for Image Editing** <br>
*Zeyan Li, Wei Zhou, Hadi Amirpour, Minghao Zou, Panqi Yang, Jianfeng Xu.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.37492)] <br>

**DecFlowEdit: Self-Localized Flow-based Image Editing via Guidance Decoupling** <br>
*Zheyuan Zhan, Can Wang, Jiawei Chen, Chun Chen, Siwei Lyu, Zeyu Zheng, Defang Chen.* <br>
**Image Editing**, Zhejiang University & University at Buffalo & University of California, Berkeley <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.34237)] <br>

**Constrained Edit Fields for Training-Free Flow Editing** <br>
*Jingxuan Kang, Yinsong Wang, Che Liu, Chen Qin.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.33735)] <br>

**In-Token Learning for High-Fidelity Image Restoration via Diffusion Transformers** <br>
*Xingfu Yi, Xiaoxue Yu.* <br>
**Image Colorization**, Independent Researcher, Hangzhou, China & Zhejiang University, Hangzhou, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.33523)] <br>

**InfoEdit: Probing Global Layout Reasoning in Infographic Editing** <br>
*Cheng Yang, Chufan Shi, Huijuan Wang, Bo Shui, Yaokang Wu, Muzi Tao, Yibo Yan, Xuezhe Ma, Taylor Berg-Kirkpatrick.* <br>
**Dataset / Evaluation**, University of California San Diego & University of Southern California & University of Illinois Urbana-Champaign & Carnegie Mellon University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.33286)] <br>

**GeoSET: Generalist Foundation Model for SAR-to-EO Image Translation** <br>
*Jeonghyeok Do, Munchurl Kim.* <br>
**SAR Image Translation**, Korea Advanced Institute of Science and Technology (KAIST) <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.37496)]
[[Project](https://kaist-viclab.github.io/GeoSET_site/)] <br>

**RefAdapt-DiT: Adaptive Joint Attention for Reference-Conditioned Diffusion Transformers** <br>
*Jian Tang, Jiawei Fan, Qiannan Zhou, Qingbin Liu, Jiang Bian, Zang Li.* <br>
**Image Editing**, Platform and Content Group, Tencent <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.32415)] <br>

**RefCompose: Multi-Reference Image Generation via LoRA-Conditioned Diffusion** <br>
*Sai Sri Teja Kuppa, Parth Shinde, Priyadharsan Balaji S, Jinka Harshavardhan, Sriprabha Ramanarayanan.* <br>
**Base I2I Translation**, Eros Innovation, India & Indian Institute of Technology Madras, India <br>
ECCV AI for Visual Arts Workshop 2026. [[PDF](https://arxiv.org/abs/2609.32389)] <br>

**PredRA: Fast Medical Image Translation by Deterministic Component Extraction and Controlled Stochastic Refinement** <br>
*Jianhai Zhang, Pattarawut Charatpangoon, Donghao Zhang, Bijoy K. Menon, Wu Qiu, M. Ethan MacDonald, Aravind Ganesh.* <br>
**Medical Image Translation**, Department of Clinical Neurosciences, Cumming School of Medicine, University of Calgary, Calgary, AB, Canada & Ron and Rene Ward Centre for Healthy Brain Aging Research, Hotchkiss Brain Institute, University of Calgary, Calgary, AB, Canada & Department of Biomedical Engineering, School of Life Science and Technology, Huazhong University of Science and Technology, Wuhan, Hubei, China & Department of Biomedical Engineering, Schulich School of Engineering, University of Calgary, Calgary, AB, Canada <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.31912)]
[[Github](https://github.com/jianhai-zhang/RredRA)] <br>

**ContraFM-S2O: Flow Matching-Based One-step SAR-to-Optical Image Translation Model with Contrastive Learning** <br>
*Mingqian Yu, Wei-kuan Chiang, Qiurui Wang, Peilin Zhao.* <br>
**SAR Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.31378)] <br>

**Zero-Shot Object Removal via Attention Masking, Latent Anchoring, and Refinement** <br>
*Arman Taghizadeh, Ulf Krumnack, Kai-Uwe Kühnberger.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.28342)]
[[Github](https://github.com/arman-taghizadeh/zero-shot-diffusion-object-removal)] <br>

**KwaiMind Technical Report** <br>
*Boheng Zhang, Fan Yang, Jia Sun, Junlong Wu, Wenwu Ou, Yuting Hu, Zijun Li, Dewen Fan, Fei Zuo, Honglie Wang, Huaiqing Wang, Pengcheng Wei, Yimin Zhou, Haixuan Gao, Lihui Peng, Tingxuan She, Yuqing Li.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.26375)]
[[Github](https://github.com/KwaiMmu/KwaiMind)] <br>

**Delving into Asymmetric Information Dynamics for High-Fidelity Virtual Try-On** <br>
*Zishu Qin, Zhiyu Jin, Pipei Huang, Hao Zhou.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.25881)] <br>

**InstaEdit: Instant Image Editing via Optimized Noise Prediction** <br>
*Ning Ma, Yangrui Shao.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/9581.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5247)] <br>

**H-Adapter: Pose-Robust Hairstyle Transfer via Attention-Derived, Source-Aligned Hair Masks** <br>
*Seulgi Jeong, Yunseong Cho, Sanghun Park.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.25578)]
[[Project](https://sanghunpark.github.io/hadapter_page/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5686)] <br>

**InnoText: A Unified Model for Visual Text Generation and Editing** <br>
*Haowei Liu, Runze He, Jian Lu, Ao Ma, Run Ling, Ke Cao, Jiasong Feng, Wei Feng, Shuo Lu, Yexing Xu, Yun Wang, Jing Wang, Zhanjie Zhang.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.22101)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3140)] <br>

**V-HOLD: Stabilizing Flow Trajectories to Rethink the Edit–Preservation Trade-off** <br>
*Gahyeon Kim, Dong-oh Kang.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/11268.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5540)] <br>

**Text-Conditioned Background Generation for Editable Multi-Layer Documents** <br>
*Taewon Kang, Joseph K J, Chris Tensmeyer, Jihyung Kil, Wanrong Zhu, Ming C. Lin, Vlad I. Morariu.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2512.17151)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3585)] <br>

**Follow-Your-Mind: Towards Inversion-Free Brain-Driven Visual Context Synthesis and Editing** <br>
*Haodong Jing, Panqi Yang, Rongchao Zhang, Zhipeng Liu, Yajun Liu, Xuehai Bai, Yongqiang Ma, Nanning Zheng.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2275.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3632)] <br>

**Target-aware Image Editing via Cycle-consistent Constraints** <br>
*Yanghao Wang, Zhen Wang, Long Chen.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2510.20212)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4615)] <br>

**DreamLite: A Lightweight On-Device Unified Model for Image Generation and Editing** <br>
*Kailai Feng, Yuxiang Wei, Bo Chen, Yang Pan, Hu Ye, Songwei Liu, Chenqian Yan, Yuan Gao.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.28713)]
[[Project](https://carlofkl.github.io/dreamlite/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4308)] <br>

**GIDE: Unlocking Diffusion LLMs for Precise Training-Free Image Editing** <br>
*Zifeng Zhu, Jiaming Han, Jiaxiang Zhao, Minnan Luo, Xiangyu Yue.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.21176)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5051)] <br>

**DiTailed: Ensuring Visual Object Consistency in Text-Image-to-Image Flow Matching Models** <br>
*Francesco Taioli, Daniel Coelho, Iaroslav Melekhov, Roberto Alcover-Couso, Jose Miguel Grande Saiz, Virginia Fernandez Arguedas, Artur Bekasov.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.12539)]
[[Project](https://francescotaioli.github.io/DiTailed/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3539)] <br>

**SR-Edit: Region-Aware Image Editing via Self-Refinement** <br>
*Andong Wang, Zehua Chen, Yuxuan Jiang, Jun Zhu.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2609.02504)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5892)] <br>

**StereoEdit: A Diffusion-Based Framework for Stereo-Consistent Image Editing** <br>
*Baolin Liu, Zongyuan Yang, Yingde Song, yongping xiong.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/8980.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5131)] <br>

**Unlocking Complex Image Editing via Natively Interleaved Visual Textual CoT with Deep Confidence Reasoning** <br>
*Zhentao Zou, Zhengrong Yue, Kunpeng Du, Binglei Bao, Hanting Li, Haizhen Xie, Guozheng Xu, Yue Zhou, jie hu, Xue Jiang, Xinghao Chen.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/9141.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5162)]
[[Github](https://github.com/zhentao-zou/MURE)] <br>

**Wavelet-Guided Semantic Signal Compensation for Inversion-Free Image Editing** <br>
*Anqi Tang, Wenhao Sun, Zhaoqiang Liu.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.02421)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5053)] <br>

**PhysEdit: Physically Consistent Image Editing via Causal Enforcement** <br>
*Siqi Wan, Jingwen Chen, Yehao Li, Yingwei Pan, Ting Yao, Tao Mei.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/9693.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5273)]
[[Project](https://github.com/HiDream-ai/PhysEdit)] <br>

**VLTR: Vision-Language Tool Reasoning for Instruction-Guided Image Editing** <br>
*Yike Wang, Yitao Yu, Shaohua Sun, Ping Luo.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/14573.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5950)] <br>

**LayerVerse: Finding the Sweet Spot for KV-Injection in Training-Free Image Editing** <br>
*Mikhail Zhirnov, Arsen Kuzhamuratov, Andrey Kuznetsov, Ivan Oseledets, Konstantin Sobolev.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6255.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4504)]
[[Project](https://v-gen-ai.github.io/LayerVerse/)] <br>

**VGEdit: Unlocking Video Generation Priors for Reasoning-Informed Image Editing** <br>
*Haiquan Lu, Gongfan Fang, Xinyin Ma, Xinchao Wang.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/723.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3271)] <br>

**Learn Once, Edit Anywhere: Visual Direction Transfer for Diffusion Models** <br>
*Yusuf Dalva, Hidir Yesiltepe, Pinar Yanardag.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2403.19645)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3264)] <br>

**A$^2$-Edit: Precise Reference-Guided Image Editing of Arbitrary Objects and Ambiguous Masks** <br>
*Huayu Zheng, Guangzhao Li, Baixuan Zhao, Siqi Luo, Hantao Jiang, Guangtao Zhai, Xiaohong Liu.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.10685)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4028)] <br>

**Editing Everything Everywhere All at Once** <br>
*Fabio Quattrini, Carmine Zaccagnino, Enis Simsar, Marta Tintoré Gazulla, Rita Cucchiara, Alessio Tonioni, Silvia Cascianelli.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.31278)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5825)] <br>

**CORE-V: Chain-Of-thought REasoning for Image Editing with Visual Interaction** <br>
*Tianyang Yan, Peisen Zhao, Guanghao Zheng, Mingxing Xu, Zhibo Zhang, Wenrui Dai, Junni Zou, Hongkai Xiong, Xiaopeng Zhang, Qi Tian.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/273.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3188)] <br>

**h-Flow: Flexible Flow-based Image Editing via Doob's h-Transform** <br>
*ZeHui Guo, Zhen Wang, Junwei Shu, Changbo Wang, Long Chen, Yang Li.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/10512.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5419)] <br>

**GeoEdit: Geometry-Aware Object Editing via Dual-Branch Denoising** <br>
*Yi He, Jiangming Wang, Xinyu Wang, Mark Fong, Songchun Zhang, Yuxuan Xue, Hai-Tao Zheng, Yue Ma.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.30003)]
[[Github](https://github.com/Heey731/GeoEdit)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4817)] <br>

**BlenderFusion: 3D-Grounded Visual Editing and Generative Compositing** <br>
*Jiacheng Chen, Ramin Mehran, Xuhui Jia, Saining Xie, Sanghyun Woo.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2506.17450)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5075)] <br>

**Recolour What Matters: Region-Aware Colour Editing via Token-Level Diffusion** <br>
*Yuqi Yang, Dongliang Chang, Yijia Ling, Ruoyi Du, Zhanyu Ma.* <br>
**Image Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.18466)]
[[Project](https://yangyuqi317.github.io/ColourCrafter.github.io/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4439)] <br>

**OpenVE-3M: A Large-Scale High-Quality Dataset for Instruction-Based Video Editing** <br>
*Haoyang He, Jie Wang, Jiangning Zhang, Zhucun Xue, Xingyuan Bu, Qiangpeng Yang, Min Zheng, Lei Xie.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/680.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3261)] <br>

**EditHF-1M: A Million-Scale Rich Human Preference Feedback for Image Editing** <br>
*Zitong Xu, Huiyu Duan, Zhongpeng Ji, Xinyun Zhang, Yutao Liu, Xiongkuo Min, Ke Gu, Jian Zhang, Shusong Xu, Jinwei Chen, Bo Li, Guangtao Zhai.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.14916)]
[[Github](https://github.com/IntMeGroup/EditHF)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4044)] <br>

**PhyEditBench: A Real-World Multi-Stage Benchmark for Physics-Aware Image Editing** <br>
*Shengbin Guo, Shaokang He, Chaoyue Meng, Shengpeng Xiao, Xunzhi Xiang, Shaofeng Zhang, Qi Fan.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.26551)]
[[Github](https://github.com/Previsior/PhyEditBench)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5047)] <br>

**UniREditBench: A Unified Reasoning-based Image Editing Benchmark** <br>
*Feng Han, Yibin Wang, Chenglin Li, Zheming Liang, Dianyi Wang, Yang Jiao, Zhipeng Wei, Chao Gong, Cheng Jin, Jiaqi Wang.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2511.01295)]
[[Project](https://maplebb.github.io/UniREditBench)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4175)] <br>

**Reference-Free Quality Assessment for Virtual Try-On via Human Feedback** <br>
*Yuki Hirakawa, Takashi Wada, Ryotaro Shimizu, Takuya Furusawa, Yuki Saito, Ryosuke Araki, Tianwei Chen, Fan Mo, Yoshimitsu Aoki.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/10675.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5449)]
[[Github](https://github.com/litelightlite/VTON-IQA)] <br>

**VTEdit-Bench: A Comprehensive Benchmark for Multi-Reference Image Editing Models in Virtual Try-On** <br>
*Xiaoye Liang, Zhiyuan Qu, Mingye Zou, Jiaxin Liu, Lai Jiang, Mai Xu, Yiheng Zhu.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.11734)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3764)] <br>

**FED-Bench: A Cross-Granular Benchmark for Disentangled Evaluation of Facial Expression Editing** <br>
*Fengjian Xue, Xuecheng Wu, Heli Sun, Yunyun Shi, Shi Chen, Liangyu Fu, Jinheng Xie, Dingkang Yang, Hao Wang, Junxiao Xue, Liang He.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.29697)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5905)] <br>

**CHARTSTYLE-100K: A Large-Scale Dataset for Structured Visualization Style Transfer** <br>
*Yuwei Yang, Tianchi Xie, Jinhong Ni, Yukai Guo, Jing Zhang, Liang Zheng, Yalong Bai, YUHUI YUAN.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/11449.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5569)]
[[Project](https://chartstyle-100k.github.io/)] <br>

**WeEdit: A Dataset, Benchmark and Glyph-Guided Framework for Text-centric Image Editing** <br>
*Hui Zhang, Juntao Liu, Zongkai Liu, Liqiang Niu, Fandong Meng, Zuxuan Wu, Yu-Gang Jiang.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.11593)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4337)] <br>

**RCEdit-500K: Reference Completion for Image-Conditioned Image Editing** <br>
*Jingxu Zhang, Daneul Kim, Yueming Pan, DONG CHEN, Kai Qiu, Yang Liu, Yifan Yang, Qi Dai, Xiaoyan Sun, Chong Luo.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/14529.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5946)] <br>

**Goku: A Million-Scale Universal Dataset and Benchmark for Instruction-Based Video Editing** <br>
*Sen Liang, Cong Wang, Zhentao Yu, Fengbin Guan, Zhengguang Zhou, Teng Hu, Youliang Zhang, Yuan Zhou, Xin Li, Qinglin Lu, Zhibo Chen.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.30599)]
[[Project](https://flying-sky999.github.io/Goku.github.io/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3375)] <br>

**GRADE: Benchmarking Discipline-Informed Reasoning in Image Editing** <br>
*Mingxin Liu, Ziqian Fan, Zhaokai Wang, Leyao Gu, Zirun Zhu, Yiguo He, Yuchen Yang, Changyao Tian, Xiangyu Zhao, Ning Liao, Shaofeng Zhang, Qibing Ren, Zhihang Zhong, Xuanhe Zhou, Junchi Yan, Xue Yang.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.12264)]
[[Project](https://grade-bench.github.io/)]
[[Github](https://github.com/VisionXLab/GRADE)]
[[Dataset](https://huggingface.co/datasets/VisionXLab/GRADE)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3710)] <br>

**SpecV: Specification Verification for Robust Unified Multimodal Evaluation** <br>
*Weihao Yu, Rongyao Fang, Yuxuan Cai, Linjiang Huang, Yuhuan Yang, Xianwei Zhuang, Junyang Lin, Yixuan Yuan, Shuai Bai.* <br>
**Dataset / Evaluation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6821.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4643)]
[[Github](https://github.com/yuyouxixi/SpecV)] <br>

**Unpaired Geometry-Guided Sim2Real Translation for Autonomous Driving** <br>
*Xinzhuo Chen, Shijie Wang, Chao Gao, Jinguang Gu, Gongjin Lan.* <br>
**Base I2I Translation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/12756.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5751)] <br>

**Improving Image-to-Image Translation via a Rectified Flow Reformulation** <br>
*Satoshi Iizuka, Shun Okamoto, Kazuhiro Fukui.* <br>
**Base I2I Translation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.20186)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5655)] <br>

**Y-diff: Structure-Texture Decoupled Diffusion Distillation for H&E-to-pCLE Translation** <br>
*Haodong Wang, Yan Wen, Hongen Liao, Fang Chen, Tianqi Huang.* <br>
**Medical Image Translation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/9496.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5229)]
[[Github](https://github.com/Hdw2agon/Y_diff)] <br>

**Spectral Consistent Flow for One-step 3D Medical Image Translation** <br>
*Haoqing Li, Jun Shi, Mingchao Li, Zehua Zhu, Qiwei Jia, Jiong Shi, Hong An.* <br>
**Medical Image Translation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.10627)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4006)] <br>

**UniCSG: Unified High-Fidelity Content-Constrained Style-Driven Generation via Staged Semantic and Frequency Disentanglement** <br>
*Jingwei Yang, Ruoxi Wu, Wei Shen, Meng Li, Yulong Liu, Huimin She, Lunxi Yuan.* <br>
**Image Style Transfer** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2604.17850)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4742)] <br>

**Hierarchical Style Aggregation for Versatile Chinese Handwriting Generation** <br>
*Jiangpeng Wang, Fei Gao, Nannan Wang.* <br>
**Image Style Transfer** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/3526.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3883)]
[[Github](https://github.com/IIP-Lab-XDU/HiSAC)] <br>

**D3F-IR: Dual-Domain Deterministic Flow Matching for Visible-to-Infrared Translation** <br>
*Peiyi Zeng, Diedong Feng, Zhen Liu, Zhenming Peng, Bing Zeng, Shuaicheng Liu.* <br>
**Infrared Image Translation** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/6631.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4599)]
[[Github](https://github.com/WanrenZeng/D3F-IR)] <br>

**MTVDiff: Multimodal Conditional Latent Diffusion for Enhanced Thermal-to-Visible Face Translation** <br>
*Zhiyuan Xia, Haojie Li, Jingyu Lin, Yiguo Qiao, Cunjian Chen.* <br>
**Infrared Image Translation** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.19886)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4826)] <br>

**Layering Virtual Try-On** <br>
*Chun Feng, Bowei Chen, Mengyi Shan, Ira Kemelmacher-Shlizerman.* <br>
**Virtual Try-On** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.22924)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4142)] <br>

**FitControler: Toward Fit-Aware Virtual Try-On** <br>
*Lu Yang, Yicheng Liu, Letian Zhou, Yanan Li, Xiang Bai, Hao Lu.* <br>
**Virtual Try-On** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2512.24016)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4018)] <br>

**TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy** <br>
*Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang.* <br>
**Virtual Try-On** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.26092)]
[[Project](https://sunhao242.github.io/TryOnCrafter_web.github.io/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3423)] <br>

**LangDriveCTRL: Natural Language Controllable Driving Scene Editing with Multi-modal Agents** <br>
*Yun He, Francesco Pittaluga, Ziyu Jiang, Matthias Zwicker, Manmohan Chandraker, Zaid Tasneem.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2512.17445)]
[[Project](https://yunhe24.github.io/langdrivectrl/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4542)] <br>

**OSVE: One Step Video Editing with One Step Diffusion Models** <br>
*Habin Lim, Gyeong-Moon Park.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.19895)]
[[Github](https://github.com/KU-VGI/OSVE)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5170)] <br>

**MSEditor: Toward Consistent Multi-Shot Video Editing** <br>
*Kunyu Feng, Yue Ma, Bingyuan Wang, Yuefeng Wang, Zhiyuan Qin, Hao Cheng, Hao Li, Qifeng Chen, Zeyu Wang.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2608.17559)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5638)] <br>

**Versatile Editing of Video Content, Actions, and Dynamics without Training** <br>
*Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.17989)]
[[Project](https://dynaedit.github.io/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5505)] <br>

**StreamGVE: Training-Free Video Editing via Few-Step Streaming Video Generation** <br>
*Guanlong Jiao, Chenyangguang Zhang, Jia Xian, Zewei Zhang, Renjie Liao.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/1050.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3345)]
[[Project](https://dsl-lab.github.io/StreamEdit/)] <br>

**LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing** <br>
*Xinyu Wang, Chongbo Zhao, Fangneng Zhan, Yue Ma.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.26740)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4792)] <br>

**In-Context Sync-LoRA for Portrait Video Editing** <br>
*Sagi Polaczek, Or Patashnik, Ali Mahdavi-Amiri, Daniel Cohen-Or.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2512.03013)]
[[Project](https://sagipolaczek.github.io/Sync-LoRA/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4473)] <br>

**Consistent Video-to-Video Translation via Explicit Correspondences** <br>
*Gaurav Parmar, Zhengqi Li, Richard Zhang, Jun-Yan Zhu, Srinivasa G. Narasimhan, Eli Shechtman, Yotam Nitzan.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/2023.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3572)] <br>

**Memory-V2V: Memory-Augmented Video-to-Video Diffusion for Consistent Multi-Turn Editing** <br>
*Dohun Lee, Chun-Hao Paul Huang, Xuelin Chen, Jong Chul Ye, Duygu Ceylan, Hyeonho Jeong.* <br>
**Video Editing** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2601.16296)]
[[Project](https://dohunlee1.github.io/MemoryV2V)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4121)] <br>

**Stylized Video Generation via Decoupled Data Synthesis and Gated Style Token Injection** <br>
*Xin Wei, Yijie Fang, Yanjia Li, Liangyi Wu, Qin Yang, Mingrui Zhu, Nannan Wang, Xinbo Gao.* <br>
**Video Style Transfer** <br>
ECCV 2026. [[PDF](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/334.pdf)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3198)]
[[Project](https://sixi111.github.io/MoStyle/)] <br>

**Accelerated Image Editing via Consistency-Aware Source Token Pruning** <br>
*Jeongsol Kim, Jong Chul Ye, Yufei Wang, Jian Wang.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=mrTRzrrt4V)]
[[Conference](https://neurips.cc/virtual/2026/poster/149846)] <br>

**AsymPipe: Accelerating Large-scale DiTs Image Editing via Asymmetry-Aware Pipeline Parallelism** <br>
*Huage Deng, LYU WENKAI, WU YONGJIN, Tianyang Zheng, heng Guo, Fangyun Zhou, Yu Shi, Wenxi Zhu, Minwen Deng.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=zvdQTz8byr)]
[[Conference](https://neurips.cc/virtual/2026/poster/148143)] <br>

**Barycentric Guidance: Turning Foundation Image Editors into Continuous Affective Controllers** <br>
*Harvey Mannering, Zhiwu Huang, Adam Prugel-Bennett.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=Nx9IIc3xpv)]
[[Conference](https://neurips.cc/virtual/2026/poster/153096)] <br>

**Delta-Adapter: Scalable Exemplar-Based Image Editing with Single-Pair Supervision** <br>
*Jiacheng Chen, Songze Li, Han Fu, Baoquan Zhao, Wei Liu, Yanyan Liang, Qing Li, Xudong Mao.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://delta-adapter.github.io/)]
[[Conference](https://neurips.cc/virtual/2026/poster/153315)] <br>

**Do Image Editing Models Understand Lighting?** <br>
*Tim Küchler, Johann-Friedrich Feiden, Matthias Niessner, Carsten Rother.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2026. [[Paper](https://tim-kuechler.github.io/3DLP)]
[[Conference](https://neurips.cc/virtual/2026/poster/139308)] <br>

**EditDistill: Is It Possible to Guide Video Editing with Image Editing** <br>
*guojun lei, Hong Li, Hongbing Yang, Lixue Gong, Chi Wang, Zheng Dong.* <br>
**Video Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=C8Uf36RhCB)]
[[Conference](https://neurips.cc/virtual/2026/poster/154635)] <br>

**EditJudge-Bench: Auditing VLM Image-Edit Judges with Synthetic Ground Truth** <br>
*Jens Parslov, Marco Schouten, Dim Papadopoulos.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=eynW4BxY28)]
[[Conference](https://neurips.cc/virtual/2026/poster/139200)] <br>

**GPT-Image-Edit-1M: An Auditable Million-Scale Dataset for Instruction-Guided Image Editing** <br>
*Yuhan Wang, Siwei Yang, Bingchen Zhao, Letian Zhang, Jiawei Mao, Juncheng Wu, Zeyu Zheng, Huaxiu Yao, Qing Liu, Cihang Xie, Yuyin Zhou.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=EL9b5Y17no)]
[[Conference](https://neurips.cc/virtual/2026/poster/139632)] <br>

**Inline Critic Steers Image Editing** <br>
*Weitai Kang, Xiaohang Zhan, Yizhou Wang, Mang Tik Chiu, Jason Kuen, Kangning Liu, Yan Yan.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=RT1DXXQkZm)]
[[Conference](https://neurips.cc/virtual/2026/poster/152644)] <br>

**Mission Impossible: Diagnosing and Fixing Non-Operative Instruction Following in Image Editing** <br>
*Guoyizhe Wei, Feng Wang, Alan Yuille, Rama Chellappa.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=iOwBRaRA9N)]
[[Conference](https://neurips.cc/virtual/2026/poster/139144)] <br>

**OTEdit: Entropic Transport Corrected Trajectory for Inversion-Free Flow-Based Image Editing** <br>
*Rameshwar Mishra, Akshay Modi, A. Subramanyam.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=SnQJpsC6YB)]
[[Conference](https://neurips.cc/virtual/2026/poster/152476)] <br>

**SpatialFlow-GRPO: Where Spatial Credit Drives Image Editing** <br>
*Yankai Yang, Yancheng Long, Wei Chen, Xingyu Lu, Hongyang Wei, Bin Wen, Fan Yang, Tingting Gao, Han Li, Shuo Yang.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=vOr0WAaBeN)]
[[Conference](https://neurips.cc/virtual/2026/poster/148740)] <br>

**StitchEdit: Stitching Depth Priors into Image Editors via Per-Layer Gradient Probing** <br>
*Qin Guo, Dan Xu.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=Q7G74v5nSs)]
[[Conference](https://neurips.cc/virtual/2026/poster/152828)] <br>

**Text-Vision Co-Instructed Image Editing** <br>
*Chenxi Xie, Yuhui Wu, Qiaosi Yi, Lei Zhang.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=yC4H5QD0ot)]
[[Conference](https://neurips.cc/virtual/2026/poster/148391)] <br>

**VTBench: Disentangled and Human-Aligned Evaluation for Image-Based Virtual Try-on** <br>
*Donghao Luo, Yujie Liang, Caoshuo Li, Xiaobin Hu, Zuxuan Wu, Yanwei Fu.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=Don9L8oTcT)]
[[Conference](https://neurips.cc/virtual/2026/poster/139643)] <br>

**Anatomy-Preserving Unpaired Medical Image Translation via Shared Latent Anchoring** <br>
*Zhilin Zou, Hieu Minh Le, Saumya Gupta, Jingyi Xu, Prateek Prasanna, Chao Chen.* <br>
**Medical Image Translation** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=AC5Xd25rUC)]
[[Conference](https://neurips.cc/virtual/2026/poster/154881)] <br>

**AR-Edit: Training-Free Streaming Video Editing without Inversion** <br>
*Hovhannes Margaryan, Vicky Kalogeiton, Quentin Bammey, Christian Sandor.* <br>
**Video Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=Tq0zQSyHNl)]
[[Conference](https://neurips.cc/virtual/2026/poster/152336)] <br>

**Constrained Look-ahead Guidance for Interference-Aware Flow Editing** <br>
*Doudou ZHANG, Qi CHEN.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=YT8RaVa0pT)]
[[Conference](https://neurips.cc/virtual/2026/poster/151736)] <br>

**FlowTrack: Controlling Edit-Signal Execution in Inversion-Free Flow Video Editing** <br>
*Jielun Zhong, Di Wang, Jisheng Dang, Leigang Qu, Bimei Wang, Jingwen Zhao, Wencan Zhang, Hong Peng, Bin Hu.* <br>
**Video Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=USNrqsbBWX)]
[[Conference](https://neurips.cc/virtual/2026/poster/152250)] <br>

**FreqCa: Accelerating Image generation and editing via Frequency-Aware Caching** <br>
*Jiacheng Liu, Peiliang Cai, Qinming Zhou, Yuqi Lin, Deyang Kong, Benhao Huang, Yupei Pan, Haowen Xu, Chang Zou, Junshu Tang, Shikang Zheng, Linfeng Zhang.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=xRAhPVJ1wk)]
[[Conference](https://neurips.cc/virtual/2026/poster/148488)] <br>

**GenScale: A Benchmark for Relative Object Scale in Image Generation and Editing** <br>
*Lingxiao Li, Max Whitton, Ledell Wu, Boqing Gong.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=MN4vF7NV07)]
[[Conference](https://neurips.cc/virtual/2026/poster/139494)] <br>

**GMO-E²DIT: Grounded Multi-Operation Editing for E-Commerce Images** <br>
*Zipeng Guo, Xiaoan Liu, Lichen Ma, Cheng Wang, Yu He, Xiaolong Fu, Jingling Fu, Xinyuan Shan, Shaojie Guo, Luohang Liu, Junshi Huang, Yan Li.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=VXvQ42upd6)]
[[Conference](https://neurips.cc/virtual/2026/poster/152097)] <br>

**Identifying and Mitigating Diversity Collapse in Zero-Shot Personalization with I2I Editing Models** <br>
*Uichan Lee, Jongeon Baek, Sangheum Hwang.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=tDe4M34lN8)]
[[Conference](https://neurips.cc/virtual/2026/poster/149053)] <br>

**Internalize External Competence for Visual Instruction Editing** <br>
*Wenjun Huang, Rui Zhao, Suyang Hou, Jiahao Tang, Wenjia Wang, Zhuobai Dong, Alex Jinpeng Wang, Hu J Guo.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=mKfQzVpQIM)]
[[Conference](https://neurips.cc/virtual/2026/poster/149907)] <br>

**Long Video Instructional Editing in the Wild** <br>
*Yiqi Lin, Guoqiang Liang, Ziyun Zeng, Zechen Bai, Yanzhe Chen, Mike Zheng Shou.* <br>
**Video Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=WxwO1ainQv)]
[[Conference](https://neurips.cc/virtual/2026/poster/151911)] <br>

**NP-LoRA: Null Space Projection for Subject-Style LoRA Fusion** <br>
*Chuheng Chen, Xiaofei Zhou, Geyuan Zhang, Yong Huang, Gang Xiong.* <br>
**Image Style Transfer** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=7ruWsRZRGX)]
[[Conference](https://neurips.cc/virtual/2026/poster/155156)] <br>

**Paint Anything: Toward Any-Color Controllable Image Generation and Editing** <br>
*Ji Xie, Dewei Zhou, Xinyu Huang, Xun Wang.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=pfRkR1nSI5)]
[[Conference](https://neurips.cc/virtual/2026/poster/149500)] <br>

**ProEdit: Inversion-based Editing From Prompts Done Right** <br>
*Zhi Ouyang, Dian Zheng, Xiao-Ming Wu, Jian-Jian Jiang, Kun-Yu Lin, Jingke Meng, Wei-Shi Zheng.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=yr9AcyQrnt)]
[[Conference](https://neurips.cc/virtual/2026/poster/148302)] <br>

**Real In, Real Out: What If We Only Use Real Data for Scene Text Editing?** <br>
*Xingsong Ye, Yongkun Du, Jiaxin Zhang, Chong Sun, Zhineng Chen.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://github.com/YesianRohn/TextRIRO)]
[[Conference](https://neurips.cc/virtual/2026/poster/153296)] <br>

**SteerVTE: Seamless Video Text Editing with Style and Glyph Control** <br>
*Kai Zeng, Moran Li, Zhengwei Wang, Yingchen Yu, Yiheng Lin, Ruichuan An, Ming Lu, Qi She, Wentao Zhang.* <br>
**Video Editing** <br>
NeurIPS 2026. [[Paper](https://zengkaiya.github.io/SteerVTE/)]
[[Conference](https://neurips.cc/virtual/2026/poster/148744)] <br>

**StyleRoute: Diffusion Style Transfer via Regional Routing and Conflict-aware Projection** <br>
*Xunhao Lin, Yu Sun, Xinpeng Ding, Fei Gao, Maoying Qiao, Lihuo He, Nannan Wang.* <br>
**Image Style Transfer** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=4kfUQ7cPeY)]
[[Conference](https://neurips.cc/virtual/2026/poster/155545)] <br>

**UniDG: Universal Defect Generation via Defect-Context Editing** <br>
*Yuanting Fan, Jun Liu, Bin-Bin Gao, Xiaochen Chen, Yuhuan Lin, Zhewei Dai, Jiawei Zhan, Chengjie Wang.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=A3soBL3Ciu)]
[[Conference](https://neurips.cc/virtual/2026/poster/154905)] <br>

**VicEdit: Learning to Edit Videos from Visual In-Context Examples** <br>
*Yuji Wang, Teng Hu, Yuheng Chen, Ran Yi, Han Feng, Weijian Cao, Chengjie Wang, Lizhuang Ma, Jiangning Zhang.* <br>
**Video Editing** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=1P8vkGpb52)]
[[Conference](https://neurips.cc/virtual/2026/poster/155979)] <br>

**ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing** <br>
*Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=fyPHDFABOs)]
[[Conference](https://neurips.cc/virtual/2026/poster/139184)] <br>

**WaveletLoRA: Frequency-Aware Content-Style Decomposition for Personalized Image Generation** <br>
*Peiyao Wang, Jiahui Sun, Weining Wang, Jing Liu.* <br>
**Image Style Transfer** <br>
NeurIPS 2026. [[Paper](https://openreview.net/forum?id=SEc7mCUDGI)]
[[Conference](https://neurips.cc/virtual/2026/poster/152557)] <br>

**Why Do DiT Editors Drift? Plug-and-Play Low Frequency Alignment in VAE Latent Space** <br>
*Xiaoce Wang, Sifan Zhou, Kaifei Wang, Leli Xu, Xuerui Qiu, Tao He, Ming Li.* <br>
**Image Editing** <br>
NeurIPS 2026. [[Paper](https://github.com/ZephinueCode/VAE-LFA)]
[[Conference](https://neurips.cc/virtual/2026/poster/151149)] <br>

**SafeStyle: Calibrated Style Residual Injection for Controllable Style-Leakage Trade-off in Diffusion Stylization** <br>
*Zhangping Yang, Min Li, Song Yan, Rong Gao, Xinliang Bi, Guanye Xiong, Yujie He.* <br>
**Image Style Transfer** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.21242)] <br>

**Refinement Is Inherently Editable: Training-Free Prompt-to-Prompt Image Editing with Generative Refinement Network** <br>
*Yulong Chen, Ziqian Zhang, Haoyu Zhang, Ao He, Yaxing Wang, Senmao Li, Kai Wang.* <br>
**Image Editing**, City University of Hong Kong (Dongguan), Guangdong, China & City University of Hong Kong, Hong Kong, China & Jilin University, Changchun, China & Mohamed bin Zayed University of Artificial Intelligence, Masdar, Abu Dhabi <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.20633)]
[[Github](https://github.com/mura1n/RefineEdit)] <br>

**Bridging Modalities on the Cortex: Surface-based MRI to PET Translation with a Diffusion Bridge** <br>
*Yitong Li, Alexandra Samoylova, Fabian Bongratz, Timo Grimmer, Dennis M. Hedderich, Igor Yakushev, Christian Wachinger.* <br>
**Medical Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.20147)]
[[Github](https://github.com/ai-med/DB-SUiT)] <br>

**JewelTry: Mask-Free Scale Aware Jewelry Virtual Try-On** <br>
*Xinlei Niu, Peixia Li, Jun Wang, Chenchen Xu, Jiayu Yang, Jing Zhang, Pulak Purkait, Hongdong Li.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.16626)] <br>

**Semantically Aligned Gradient-Driven Context-Preserving Image Editing** <br>
*Chiranjeev Chiranjeev, Muskan Dosi, Mayank Vatsa, Richa Singh.* <br>
**Image Editing**, Indian Institute of Technology Jodhpur, India <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2609.12691)]
[[Github](https://github.com/IAB-IITJ/IABEdit)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5901)] <br>

**Overpainting: Localized Context-aware Diffusion Image Editing** <br>
*Sam Sartor, Iliyan Georgiev, Michael Fischer, Valentin Deschaintre, Pieter Peers.* <br>
**Image Editing**, College of William & Mary, Williamsburg, USA & Adobe Research, United Kingdom <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.10811)]
[[Project](https://overpainting.github.io/)] <br>

**Multi-History-Step SDE Inversion for Image Editing with Superior Regional Awareness** <br>
*Haiyan Wei, Yunlong Wang, Huaibo Huang, Zhenan Sun, Kunbo Zhang.* <br>
**Image Editing**, New Laboratory of Pattern Recognition (NLPR), Institute of Automation, Chinese Academy of Sciences & University of Chinese Academy of Sciences <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2609.06602)]
[[Project](https://whywwwzzzg.github.io/MIEdit/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5667)] <br>

**One Model, Two Worlds: Bidirectional Sonar-Optical Translation** <br>
*Shengji Jin, Trung Tien Dong, Ahmed Lamidi, Chen Chen, Xiaomin Lin, Yi Sheng.* <br>
**Sonar Image Translation**, University of South Florida & University of Central Florida <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.06253)] <br>

**LensStyle: Learning the Optical Aesthetics for Controllable Stylized Lens Effect Rendering** <br>
*Yachuan Huang, Liwen Xiao, Liao Shen, Qiwen Wang, Huiqiang Sun, Zhiyu Pan, Zhiguo Cao.* <br>
**Image Style Transfer**, School of AIA, Huazhong University of Science and Technology, Wuhan, China <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2609.04939)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3542)] <br>

**Abstract-LoRA: Unlocking Single-Image Style Transfer through Targeted U-Net Block Training** <br>
*Xinglin Hu.* <br>
**Image Style Transfer**, School of Data Science, The Chinese University of Hong Kong, Shenzhen <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.13239)] <br>

**AffectDelta: Beyond Emotion Labels for Image Editing** <br>
*Xingzu Zhan, Lin Gu, Ruogu Fang.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.02616)] <br>

**RGB-to-IR image translation for infrared vehicle detection in unseen UAV domains** <br>
*Thijs A. Eker, Ella P. Fokkinga, Jan Erik van Woerden, Elfi I. S. Hofmeijer, Sebastiaan P. Snel, Klamer Schutte, Friso G. Heslinga.* <br>
**Infrared Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.02556)] <br>

**CameraEditor: Camera-Controlled Image Editing via Video-Prior Sequential Modeling** <br>
*Xin Shen, Chengyou Jia, Keshuo Xing, Zifeng Zhu, Changliang Xia, Bowen Ping, Zhuohang Dang, Hangwei Qian, Minnan Luo.* <br>
**Image Editing**, Xi’an Jiaotong University, China & Agency for Science, Technology and Research (A*STAR), Singapore <br>
ACMMM 2026. [[PDF](https://arxiv.org/abs/2609.01479)]
[[Github](https://github.com/King-Wood-Shen/CameraEditor)]
[[Model](https://huggingface.co/keenwood/CameraDiT)]
[[Dataset](https://huggingface.co/datasets/keenwood/CamEditor-Bench)]
[[Project](https://king-wood-shen.github.io/CameraEditor-Home/)] <br>

**MegaStyle++: Scaling Image Style Space through Hierarchical Style Definition** <br>
*Junyao Gao, Sibo Liu, Jiaxing Li, Yanan Sun, Weidong Zhang, Jun Zhang, Cairong Zhao.* <br>
**Image Style Transfer**, Tongji University & Tencent & Nanyang Technological University & Hong Kong University of Science and Technology <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.01423)]
[[Github](https://github.com/Tencent/MegaStyle)] <br>

**ReFlowSET: Representation-Aligned Latent Flow Matching for SAR-to-EO Image Translation** <br>
*Jeonghyeok Do, Seungchul Lee, Munchurl Kim.* <br>
**SAR Image Translation**, KAIST & Stellarvision Inc <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2609.00968)]
[[Github](https://github.com/KAIST-VICLab/ReFlowSET)]
[[Project](https://kaist-viclab.github.io/ReFlowSET_site)] <br>

**Discrete Diffusion Bridges for Spatiotemporally Aligned Image Translation and Generation** <br>
*Xing Xie, Jiawei Liu, Shijun Zhou, Huijie Fan, Zhi Han, Yandong Tang, Liangqiong Qu.* <br>
**Base I2I Translation**, State Key Laboratory of Robotics and Intelligent Systems, Shenyang Institute of Automation, Chinese Academy of Sciences, Shenyang, China & University of Chinese Academy of Sciences, Beijing, China & School of Computing and Data Science, The University of Hong Kong, Hong Kong <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2608.29997)]
[[Github](https://github.com/HKU-HealthAI/DDB)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3280)] <br>

**Generative Translation Priors: Bayesian Imaging with Cross-Modality Image Translation** <br>
*Evan Bell, Jiaming Liu, Yifan Chen, Yu Sun.* <br>
**Base I2I Translation**, Johns Hopkins University & Stanford University & University of California, Los Angeles <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.28872)]
[[Github](https://github.com/Hopkins-CIG/GTP)] <br>

**Learning the Target Priors Before Image Translation: A Decoupled Training Paradigm for Cross-Modal Image Translation in Remote Sensing** <br>
*Keyan Hu, Mingtao Wang, Ziyu Zhou, Tiandong Shi, Haifeng Li, Ji Qi, Chao Tao.* <br>
**SAR Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.28517)] <br>

**There and Back Again: Bidirectional Diffusion Bridges for Multimodality Translation** <br>
*Gabe Guo, Elon Litman, Thanawat Sornwanee, Jose Blanchet, Stefano Ermon.* <br>
**Base I2I Translation**, Stanford University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.27885)] <br>

**LiveVVT: High-Fidelity Video Virtual Try-On in Real Time** <br>
*Yushe Cao, Shikun Feng, Ruxiang Duan, Liyong Wang, Dianxi Shi, Chun Yu, Junliang Xing.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.26714)] <br>

**MAMA-FLUX.2: Image-to-Image Synthesis of Post-Contrast Breast DCE-MRI for the MAMA-SYNTH Challenge** <br>
*Kamil Kwarciak, Marek Wodzinski.* <br>
**Medical Image Translation**, Department of Measurement and Electronics, AGH University of Krakow, Krakow, Poland & Sano Centre for Computational Medicine, Krakow, Poland <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.25648)] <br>

**Through the Schrödinger Bridge: Benchmarking Antemortem Image Restoration from Postmortem Autolysis to Enhance Forensic Diagnostics** <br>
*Shuang Hao, Jiacheng Yue, Yaxuan Zhao, Fan Wang, Jianhua Ma, Erwen Huang, Chunfeng Lian.* <br>
**Medical Image Translation**, Key Laboratory of Biomedical Information Engineering of Ministry of Education, School of Life Science and Technology, Xi’an Jiaotong University, Xi’an, China & Research Center for Intelligent Medical Equipment and Devices (IMED), Xi’an Jiaotong University, Xi’an 710049, China & Faculty of Forensic Medicine, Zhongshan School of Medicine, Sun Yat-Sen University, Guangzhou, 510080, China & School of Mathematics and Statistics, Xi’an Jiaotong University, Xi’an, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.21813)]
[[Github](https://github.com/fengluo233/AutolysisBench)] <br>

**DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing** <br>
*Haoxiang Cao, Jiajiong Cao, Xuanpu Zhang, Changqian Yu, Chaoqun Wang.* <br>
**Image Editing**, South China Normal University & KlingAI Research <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.20161)] <br>

**Scale-Separated Conditioning for Style-Encoder-Free Diffusion Stylization** <br>
*Jingtao Zhang, Haorui Gao, Youqing Liang, Zeming Liu.* <br>
**Image Style Transfer**, College of Computing, Georgia Institute of Technology, Atlanta, GA, USA & Courant Institute of Mathematical Sciences, New York University, New York, NY, USA & Department of Computer Science, Brown University, Providence, RI, USA <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.19719)] <br>

**EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing** <br>
*Jiayi Song, Shijie Huang, Fangtai Wu, Yubo Huang, Zhenxiong Tan, Songhua Liu, Jiaming Liu, Ruihua Huang.* <br>
**Image Editing**, Qwen Business Unit of Alibaba & National University of Singapore <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2608.18063)]
[[Project](https://editbridge.github.io/)]
[[Conference](https://neurips.cc/virtual/2026/poster/154973)] <br>

**Unlocking the Potential of Image Editing via Concept Scaling and Dense Supervision** <br>
*Long Cui, Xiaoqian Liu, Qi Qin, Yi Xin, Tao Lin, Jianguo Li, Linfeng Zhang.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.16812)] <br>

**RRFC: Recursive Refinement via Feedback Conditioning for Iterative Image-to-Image Generation** <br>
*Kareem Hassani, Chaymaa Abbas, Hadi Al Mubasher, Mariette Awad.* <br>
**Base I2I Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.15694)] <br>

**Instruction-Based Video Editing by Repurposing an Image Editing Model** <br>
*Yunpeng Bai, Yossi Gandelsman, Michaël Gharbi, Qixing Huang.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.14790)]
[[Project](https://yunpeng1998.github.io/Qwen-Video-Edit-Page)]
[[Github](https://github.com/yunpeng1998/Qwen-Video-Edit)]
[[Model](https://huggingface.co/yunpeng1998/Qwen-Video-Edit)] <br>

**InstructVVT: Instruction-Driven Video Virtual Try-On without Auxiliary Spatial Priors** <br>
*Dingbao Shao, Song Wu, Xinyu Chen, Qian Wang, Jiahang Li, Kuai Jiang, Jiang Lin, Yuhang Liu, Ziyu Chen, Duo Li, Jiaxin Hu, Shengrong Gu, Ziheng Tang, Rongrong Liu, Yanlun Peng, Liang Li, Junlan Feng, Lujia Jin, Ting Zhang, Jian Yang, Zili Yi.* <br>
**Virtual Try-On** <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2608.14070)]
[[Conference](https://neurips.cc/virtual/2026/poster/149716)] <br>

**Source-Agnostic Image Translation Based on Latent Aware Adaptive Masking** <br>
*Tomislav Dobrički, Byung-Woo Hong.* <br>
**Base I2I Translation**, Chung-Ang University, Seoul, South Korea <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2608.14046)]
[[Github](https://github.com/dtoma95/PM-Edit)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3364)] <br>

**Through Van Gogh's Eyes: Global Style Transfer with Diffusion Model** <br>
*Jeongha Lee, Yujin Kim, Ghazanfar Ali, Suhyun Kim, Jae-In Hwang.* <br>
**Image Style Transfer**, Korea Institute of Science and Technology, & University of Science and Technology, & Korea University, & Gachon University, & Kyung Hee University <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2608.11546)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5399)] <br>

**Diffusion Image Editing via Asynchronous Token Decoding** <br>
*Yang Shi, Liangsi Lu, Minzhe Guo, Yifeng Xie, Yanhui Chen, Jingchao Wang, Xuhang Chen.* <br>
**Image Editing**, Guangdong University of Technology, Guangzhou, China & Hong Kong Baptist University, Hong Kong, China & Peking University, Beijing, China & Huizhou University, Huizhou, China <br>
ACMMM 2026. [[PDF](https://arxiv.org/abs/2608.09322)] <br>

**MRI super-resolution in ten sampling steps using a diffusion bridge model** <br>
*Mojtaba Safari, Hang Yu, Zach Eidex, Mingzhe Hu, Ryan J. Sanford, Alexandru Florea, Shansong Wang, Chih-Wei Chang, Erik H Middlebrooks, Aditya Juloori, Stanley L. Liauw, Ralph Weichselbaum, Xiaofeng Yang.* <br>
**Medical Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.08819)] <br>

**SDDBMs: Soft Denoising Diffusion Bridge Models** <br>
*Shiyi Qi, Kun He, Mingmou Liu.* <br>
**Base I2I Translation**, Nanjing University & Renmin University of China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.08594)] <br>

**SC-Diff: Semantically Calibrated Diffusion for Visible-to-Infrared Image Translation** <br>
*Junyin Zhang, Siyu Huang, Jianxiong Ye, Haowei Gong, Ruicheng Zhang, Deyu Meng, Chenqiang Gao.* <br>
**Infrared Image Translation**, Sun Yat-sen University & Tsinghua University & Xi’an Jiaotong University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.08555)] <br>

**Compositional Cross-Modality Translation via Whole-Volume Multitask Latent Flow Matching** <br>
*Daniele Molino, Alessio Zoboli, Camillo Maria Caruso, Valerio Guarrasi, Paolo Soda.* <br>
**Medical Image Translation**, Unit of Artificial Intelligence and Computer Systems, Department of Engineering, Università Campus Bio-Medico di Roma, Rome, Italy & UniCamillus – Saint Camillus International University of Health Sciences, Rome, Italy & Department of Diagnostics and Intervention, Biomedical Engineering and Radiation Physics, Umeå University, Umeå, Sweden <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.08135)]
[[Github](https://github.com/arco-group/Whole-Volume-Latent-FM)] <br>

**Staying True to the Origin: Continuous Image Stylization with Smooth Transitions** <br>
*Rui Xu, Hanmo Zhang, Songhua Liu.* <br>
**Image Style Transfer** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.08125)]
[[Project](https://reychiaro.github.io/StyleController)] <br>

**MaskFlow: Precise, Consistent and Seamless Regional Image Editing** <br>
*Rui Xu, Yang Yong, Shunzi Yang, Ruihao Gong, Chengtao Lv.* <br>
**Image Editing**, SenseTime Research & Beihang University & Nanyang Technological University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.06929)]
[[Project](https://reychiaro.github.io/MaskFlow)] <br>

**UniCycleFlow: Bidirectional Unpaired Image Translation with a Shared Rectified Flow** <br>
*Xianhao Zhou, Jianghao Wu, Shaoting Zhang, Guotai Wang.* <br>
**Base I2I Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.06784)] <br>

**PRISM: Distribution-Gated Flow Matching for Controllable Unpaired Image Translation** <br>
*Elad Yoshai, Natan T. Shaked.* <br>
**Base I2I Translation**, School of Biomedical Engineering, Faculty of Engineering, Tel Aviv University, Tel Aviv, 6997801, Israel <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.06240)] <br>

**Controllable Clothing: Precise Labels and Generation for Virtual Try-On with Latent Diffusion Models** <br>
*Max Rehman Linder.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.05834)] <br>

**UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on** <br>
*Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2608.05745)] <br>

**Instruction-based Image Editing: A Survey on Data, Models, Evaluation, and Applications** <br>
*Xianghao Zang, Zijian Jiang, Jiarong Cheng, Qianrui Teng, Ying He, Yuxuan Mu, Chao Ban, Huayu Zhang, Lanxiang Zhou, Zerun Feng, Chi Zhang.* <br>
**Survey**, Institute of Artificial Intelligence (TeleAI), China Telecom, Beijing, China <br>
Vicinagearth 2026. [[PDF](https://arxiv.org/abs/2607.25642)] <br>

**WearWow: Native 2K Multi-Garment Virtual Try-On via Adaptive Token Packing and Preference Alignment** <br>
*Xujie Zhang, Runyan Du, Song Chang, Jiang Li, Dongliang Shao, Liping Wu, Wei Luo, Xiaochao Qu, Luoqi Liu, Xiaodan Liang.* <br>
**Virtual Try-On**, Shenzhen Campus of Sun Yat-sen University, China & Meitu Lab, China <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.19923)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4590)] <br>

**Image Editing Models are Numerical Solvers** <br>
*Ulysse Mizrahi.* <br>
**Image Editing**, Tel Aviv University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2607.18787)] <br>

**Posterior Samplings are Missing Modalities Generators for Medical Image Translation** <br>
*Jonghun Kim.* <br>
**Medical Image Translation**, Department of Electrical and Computer Engineering, Sungkyunkwan University, Suwon, Korea <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.18763)]
[[Github](https://github.com/jongdory/PS-MIT)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3287)] <br>

**Reviving Ancient Paintings via Poem: A Colorization Framework for Aligning Cultural Semantics** <br>
*Junming Gao, Biao Zhu, Xiaosong Wang, Tan Tang.* <br>
**Image Colorization**, Zhejiang University, Hangzhou, China & Hangzhou Research Institute of AI and Holographic Technology, Hangzhou, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2607.17638)] <br>

**TAMF-VTON: Texture-Aware Mask-Free Virtual Try-On via High-Fidelity Image Synthesis** <br>
*Jie Wang, Qian He, Gaofeng He, Xiaogang Jin, Huamin Wang.* <br>
**Virtual Try-On**, State Key Lab of CAD & CG, Zhejiang University and Style3D Research, China & Style3D Research, China & State Key Lab of CAD & CG, Zhejiang University, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2607.14807)] <br>

**A${}^2$BM: Alignment-Aware Bridge Matching for Image-to-Image Translation** <br>
*Aimi Okabayashi, Georges Le Bellier, Nicolas Audebert, Charlotte Pelletier, Thomas Corpetti, Nicolas Courty.* <br>
**Base I2I Translation**, Université Bretagne Sud, IRISA, UMR CNRS 6074, F-56000 Vannes, France & Inria, ENS de Lyon, CNRS, Université Claude Bernard Lyon 1, LIP, UMR 5668, & Lyon, France & Conservatoire national des arts et métiers, CEDRIC, F-75141 Paris, France & Université Gustave Eiffel, ENSG, IGN, LASTIG, F-94160 Saint-Mandé, France & CNRS, UMR & LETG, Univ. Rennes 2, & Rennes, France <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2607.16294)] <br>

**Heterogeneity-Adaptive Diffusion Schrodinger Bridge for PET-Guided Whole-Body MRI Translation** <br>
*Chengbo Wang, Jiacheng Yu, Linjie Bian, Ming Qi, Xiaosheng Liu, Tongtong Che, Jichang Zhang, Shuyu Li, Shaoli Song, Xiuying Wang.* <br>
**Medical Image Translation**, The University of Sydney, Sydney, Australia & Department of Nuclear Medicine, Fudan University Shanghai Cancer Center, Shanghai, China & State Key Laboratory of Cognitive Neuroscience and Learning, Beijing Normal University, Beijing, China <br>
MICCAI 2026. [[PDF](https://arxiv.org/abs/2607.07401)]
[[Github](https://github.com/xyw-medical-research/HADSB)] <br>

**Tuning-Free Latent Diffusion Models for Ultrahigh-Resolution Image Editing** <br>
*Wanglong Lu, Lingming Su, Kaijie Shi, Minglun Gong, Xiaogang Jin, Hanli Zhao, Xianta Jiang.* <br>
**Image Editing** <br>
IEEE Transactions on Neural Networks and Learning Systems 2026. [[PDF](https://arxiv.org/abs/2607.06136)]
[[Github](https://github.com/LonglongaaaGo/UltraDiffEdit)] <br>

**AnyStyle: A Single LoRA is Sufficient for Image-Guided Style Transfer** <br>
*Yongwen Lai, Chaoqun Wang.* <br>
**Image Style Transfer**, School of Artificial Intelligence, South China Normal University, Guangzhou, China <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2607.04677)]
[[Github](https://github.com/Yvan1001/AnyStyle)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4851)] <br>

**Do Not Break the Vessels: Structure-Preserving Mean Flow for Vascular Image Translation** <br>
*Changjin Sun, Zhuo Hu, Kaini Wang, Baixuan Wu, Shuo Gao, Runan Zheng, Cheng Xue, Yudong Zhang, Guangquan Zhou.* <br>
**Medical Image Translation**, School of Biological Science and Medical Engineering, Southeast University, Nanjing, China & School of Computer Science and Engineering, Southeast University, Nanjing, China & Department of Computer Science and Engineering, The Chinese University of Hong Kong, Hong Kong, China & Zhejiang University, Hangzhou, China & Suzhou Microclear Medical Instruments Co., Suzhou, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.31095)] <br>

**WarpI2I: Image Warping for Image-to-Image Translation** <br>
*Shen Zheng, Anurag Ghosh, Gaurav Parmar, Srinivasa Narasimhan.* <br>
**Base I2I Translation**, Carnegie Mellon University <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.31018)]
[[Project](https://shenzheng2000.github.io/WarpI2I.github.io)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5130)] <br>

**FDM-MFVT: Few-step Sampling Diffusion Model for Mask-Free Virtual Try-On** <br>
*Jiaxin Liu, Xiaoye Liang, Lai Jiang, Mai Xu, Jun Liu.* <br>
**Virtual Try-On**, School of Electronic Information Engineering, Beihang University, Beijing, China & Zhongguancun Academy, Beijing, China & State Key Laboratory of Virtual Reality Technology and Systems, Beihang University, Beijing, China <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.29319)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4709)] <br>

**ASTAD: Asymmetric Style Transfer for Synthetic-to-Real Adaptation in Autonomous Driving** <br>
*Dingyi Yao, Xinqi Zhang, Lihui Peng, Jianming Hu, Danya Yao, Yi Zhang.* <br>
**Image Style Transfer**, Department of Automation, Tsinghua University, Beijing 100084, China <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.29286)]
[[Github](https://github.com/Dingyi-Yao/ASTAD)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4652)] <br>

**ModaFlow: Modality-Aware Flow Matching for High-Fidelity Virtual Try-On** <br>
*Xiangyu Sai, Meysam Madadi, Sergio Escalera, Yong Xu.* <br>
**Virtual Try-On**, South China University of Technology, Guangzhou, China & Universitat de Barcelona, Barcelona, Spain & Computer Vision Center, Bellaterra, Spain & Guangdong Provincial Key Laboratory of Multimodal Big Data Intelligent Analysis, Guangzhou, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.27773)] <br>

**Qwen-Image-2.0-RL Technical Report** <br>
*Yixian Xu, Kaiyuan Gao, Yuxiang Chen, Yilei Chen, Zecheng Tang, Zihao Liu, Zikai Zhou, Deqing Li, Hao Meng, Kuan Cao, Jiahao Li, Jie Zhang, Liang Peng, Lihan Jiang, Ningyuan Tang, Shengming Yin, Tianhe Wu, Xiaoyue Chen, Yan Shu, Yanran Zhang, Yi Wang, Yu Wu, Yujia Wu, Zekai Zhang, Zhendong Wang, Xiao Xu, Kun Yan, Chenfei Wu.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.27608)] <br>

**EchoStyle: Unlocking High-Fidelity Video Stylization with Reverse Data Synthesis** <br>
*Huaqiu Li, Jiahao Wang, Sijia Cai, Hualian Sheng, Bing Deng, Jieping Ye, Wenhan Luo.* <br>
**Video Style Transfer**, The Hong Kong University of Science and Technology & Alibaba Group & Xi’an Jiaotong University <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2606.25465)]
[[Project](https://echostyle2026.github.io/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4480)] <br>

**Bridging the Manifold Gap: Riemannian Residual Line Search for One-Step Image Editing** <br>
*Hongzhu Yi, Zhongtian Luo, Tong Li, Yiyan Fan, Jungang Xu.* <br>
**Image Editing**, UCAS & WashU & SHU <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.24844)] <br>

**Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation** <br>
*Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne, Guillaume Herpe, David Helbert.* <br>
**Medical Image Translation** <br>
Computerized Medical Imaging and Graphics 2026. [[PDF](https://arxiv.org/abs/2606.24313)] <br>

**EPEdit: Redefining Image Editing with Generative AI and User-Centric Design** <br>
*Hoang-Phuc Nguyen, Dinh-Khoi Vo, Trong-Le Do, Hai-Dang Nguyen, Tan-Cong Nguyen, Vinh-Tiep Nguyen, Tam V. Nguyen, Khanh-Duy Le, Minh-Triet Tran, Trung-Nghia Le.* <br>
**Image Editing**, University of Science, VNU-HCM, Ho Chi Minh City, Vietnam & Vietnam National University, Ho Chi Minh City, Vietnam & University of Information Technology, VNU-HCM, Vietnam & University of Dayton, Dayton, Ohio, United States <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.24057)] <br>

**Delta-Diffusion: Modeling Longitudinal Brain Amyloid-PET Trajectories via Conditional Poisson Diffusion Bridge** <br>
*Yongheng Sun, Minhui Yu, Mengqi Wu, Maureen Kohi, Mingxia Liu.* <br>
**Medical Image Translation**, Department of Radiology and BRIC, University of North Carolina at Chapel Hill, Chapel Hill, North Carolina 27599, USA <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.22216)] <br>

**Addressing Detail Bottlenecks in Latent Diffusion for RGB-to-SWIR Image Translation** <br>
*Kaili Wang, Martin Dimitrievski, Jose Maria Salvador, Ben Stoffelen, David Van Hamme, Lore Goetschalckx.* <br>
**Infrared Image Translation**, imec, & Leuven, Belgium & imec-IPI-Ghent University, & Ghent, Belgium & Yale University, New Haven, CT, USA <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.19961)] <br>

**BindEdit: Taming Attention Leakage for Precise Multi-Object Image Editing** <br>
*Chaewon Park, Soyoon Lee, Naeun Lee, Minjung Shin, Seogkyu Jeon, Kibeom Hong.* <br>
**Image Editing**, Sookmyung Women’s University & Yonsei University & Samsung Research <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.18906)] <br>

**Multimodal Image Colorization: Quantifying the Impact of Text-Conditioned Guidance on Grayscale-to-Color Translation** <br>
*Colten Reissmann, Hugo Garrido-Lestache Belinchon.* <br>
**Image Colorization** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.20722)] <br>

**TeleStyle V2: Beyond Content-Preserving Style Transfer with Self-Distillation and Distribution-Matching-Distillation** <br>
*Shiwen Zhang, Yifan Xu, Haibin Huang, Chi Zhang, Xuelong Li.* <br>
**Image Style Transfer**, TeleAI <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.20709)]
[[Github](https://github.com/Tele-AI/TeleStyleV2)]
[[Project](https://witcherofresearch.github.io/TeleStyleV2)] <br>

**Feynman Kac Reweighted Schrödinger Bridge Matching for Surface-Based Tau PET Harmonization** <br>
*Jianwei Zhang, Xinyu Nie, Jiaxin Yue, Yonggang Shi.* <br>
**Medical Image Translation**, University of Southern California <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.17420)]
[[Github](https://github.com/jianweizhang17/FKRSBM)] <br>

**ResEdit: Residual embeddings for precise generative image editing** <br>
*Ahmet Canberk Baykal, Valentin Deschaintre, Yannick Hold-Geoffroy, Michael Fischer, Anna Frühstück, Cengiz Öztireli, Iliyan Georgiev.* <br>
**Image Editing**, Adobe Research & University of Cambridge <br>
EGSR 2026. [[PDF](https://arxiv.org/abs/2606.16457)]
[[Project](https://johnberg1.github.io/resedit/)] <br>

**PPDM: Pixel Puzzling Diffusion Model for Speed and Memory Efficient Volumetric Medical Image Translation** <br>
*Tianqi Chen, Jun Hou, Yinchi Zhou, James S. Duncan, Chi Liu, Bo Zhou.* <br>
**Medical Image Translation**, Northwestern University & Yale University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.15323)] <br>

**Conditioning Matters: Stabilizing Inversion and Attention in Diffusion Image Editing** <br>
*Zheyuan Zhan, Hongchen Li, Can Wang, Yinfei Ma, Mingzhen Huang, Ruoshi Bai, Jiawei Chen, Siwei Lyu, Defang Chen.* <br>
**Image Editing**, HangZhou High-Tech Zong (Binjiang) Institute of Blockchain and Data Security & College of Computer Science, Zhejiang University & State Key Laboratory of Blockchain and Data Security, Zhejiang University & University at Buffalo, State University of New York <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.14125)]
[[Github](https://github.com/zju-pi/SimEdit)] <br>

**HiLo-Token: Input-Adaptive High-Low Frequency Token Compression for Efficient Image Editing** <br>
*Haoran You, Yotam Nitzan, Lingzhi Zhang, Yifan Gong, Mang-Tik Chiu, Connelly Barnes, Yan Kang, Yuqian Zhou, Haitian Zheng, Eli Shechtman, Sohrab Amirghodsi.* <br>
**Image Editing**, Adobe ART AI Lab & Adobe Research <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.13898)] <br>

**Compressing Image Style Training into a Single Model Forward** <br>
*Zhongjie Duan, Yingda Chen.* <br>
**Image Style Transfer**, ModelScope Team, Alibaba Group <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.13809)] <br>

**DuET: Dual Expert Trajectories for Diffusion Image Editing** <br>
*Lidia Troeshestova, Alexander Ustyuzhanin, Sergey Kastryulin.* <br>
**Image Editing**, HSE University & Yandex <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.13303)] <br>

**FitVTON: Fit-aware Virtual Try-On via Body-Garment Size Control** <br>
*Yiqun Ning, Ao Shen, Chenhang He, Lei Zhang.* <br>
**Virtual Try-On**, Department of Computing, The Hong Kong Polytechnic University, Hong Kong & Nuvatech <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.12012)]
[[Project](https://zenoning.github.io/FitVTON/)] <br>

**SheafStain: Sheaf-Theoretic Schrödinger Bridge for Spatially and Biologically Coherent Virtual Staining** <br>
*Hyeongyeol Lim, Hongjun Yoon, Eunjin Jang, Daeky Jeong, Won June Cho, Hwamin Lee.* <br>
**Virtual Staining**, Department of Medical Informatics, College of Medicine, Korea University & DEEPNOID Inc <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2606.11846)] <br>

**AnchorEdit: Maintaining Temporal Consistency in Multi-turn Image Editing via Causal Memory** <br>
*Hang Xu, Xiaoxiao Ma, Guohui Zhang, Yu Hu, Siming Fu, Jie Huang, Lin Song, Haoyang Huang, Nan Duan, Feng Zhao.* <br>
**Image Editing**, University of Science and Technology of China & JD Explore Academy <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.11751)]
[[Github](https://github.com/xuhang07/AnchorEdit)] <br>

**SAM-Flow: Source-Anchored Masked Flow for Training-Free Image Editing** <br>
*Haowang Cui, Rui Chen, Tao Luo, Tao Guo, Zheng Qin, Jiaze Wang.* <br>
**Image Editing**, Tianjin University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.06228)]
[[Github](https://github.com/chwbob/Sam-Flow)] <br>

**Style-CCL: Content-Preserving Style Transfer via Curriculum Continual Learning** <br>
*Shiwen Zhang, Haoyuan Wang, Xianghao Zang, Haibin Huang, Chi Zhang, Xuelong Li.* <br>
**Image Style Transfer**, Institute of Artificial Intelligence (TeleAI), China Telecom <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.14746)]
[[Github](https://github.com/witcherofresearch/Qwen-Image-Style-Transfer/)]
[[Github](https://github.com/Tele-AI/TeleStyle/)] <br>

**Edit-R2: Context-Aware Reinforcement Learning for Multi-Turn Image Editing** <br>
*Yuxiao Ye, Haoran He, Fangyuan Kong, Xintao Wang, Pengfei Wan, Kun Gai, Ling Pan.* <br>
**Image Editing**, Hong Kong University of Science and Technology & Kuaishou Technology <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2606.05950)]
[[Github](https://github.com/yuxiaooye/Edit-R2)]
[[Conference](https://neurips.cc/virtual/2026/poster/150113)] <br>

**MT-EditFlow: Reinforcement Learning for Multi-Turn Image Editing with Flow Matching** <br>
*Jiahui Huang, Yasi Zhang, Tianyu Chen, Shu Wang, Jianwen Xie, Oscar Leong, Mingyuan Zhou, Nanzhu Wang, Ying Nian Wu.* <br>
**Image Editing**, Apple & University of California, Los Angeles & University of Texas at Austin & Lambda, Inc <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.01985)] <br>

**Decoupled Residual Denoising Diffusion Models for Unified and Data Efficient Image-to-Image Translation** <br>
*Ziyue Lin, Jiahe Hou, Hongyu Xia, Xinrui Xie, Feifei Wang, Yuyin Zhou, Wei Wang, Jiawei Liu, Liangqiong Qu.* <br>
**Base I2I Translation**, The University of Hong Kong & Shenyang Institute of Automation, Chinese Academy of Sciences & The Chinese University of Hong Kong & University of California, Santa Cruz <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2606.01048)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Lin_Decoupled_Residual_Denoising_Diffusion_Models_for_Unified_and_Data_Efficient_CVPR_2026_paper.html)]
[[Github](https://github.com/HKU-HealthAI/DRDD)] <br>

**SANA-Streaming: Real-time Streaming Video Editing with Hybrid Diffusion Transformer** <br>
*Yuyang Zhao, Yicheng Pan, Qiyuan He, Jincheng Yu, Junsong Chen, Tian Ye, Haozhe Liu, Enze Xie, Song Han.* <br>
**Video Style Transfer** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.30409)]
[[Project](https://nvlabs.github.io/Sana/Streaming/)] <br>

**BlazeEdit: Generalist Image Editing on Mobile Devices with Image-to-Image Diffusion Models** <br>
*Fei Deng, Yanwu Xu, Zhipeng Bao, Zhixing Zhang, Haolin Jia, Karthik Raveendran, Jianing Wei.* <br>
**Image Editing**, Google <br>
CVPR 2026 Workshops (EDGE). [[PDF](https://arxiv.org/abs/2605.28067)] <br>

**Scheduled Style Injection: Expanding the Style-Content Pareto Frontier in Training-Free Diffusion-based Style Transfer** <br>
*Amey Sunil Kulkarni.* <br>
**Image Style Transfer**, Independent Researcher <br>
CVPR 2026 Workshops (NTIRE). [[PDF](https://arxiv.org/abs/2605.26538)]
[[Github](https://github.com/ameyskulkarni/scheduled_style_injection)] <br>

**iTryOn: Mastering Interactive Video Virtual Try-On with Spatial-Semantic Guidance** <br>
*Jun Zheng, Zhengze Xu, Mengting Chen, Jing Wang, Jinsong Lan, Xiaoyong Zhu, Kaifu Zhang, Bo Zheng, Xiaodan Liang.* <br>
**Virtual Try-On**, Shenzhen Campus of Sun Yat-sen University & Taobao & Tmall Group of Alibaba <br>
ICML 2026. [[PDF](https://arxiv.org/abs/2605.21431)]
[[Project](https://zhengjun-ai.github.io/itryon-page)] <br>

**Semantic Granularity Navigation in Image Editing** <br>
*Liangsi Lu, Minzhe Guo, Xuhang Chen, Yang Shi.* <br>
**Image Editing**, Guangdong University of Technology, Guangzhou, China & Huizhou University, Huizhou, China <br>
ICML 2026. [[PDF](https://arxiv.org/abs/2605.21190)] <br>

**VISTA: Triplet-Supervised Video Style Transfer with Diffusion Transformers** <br>
*Yiren Song, Wangzi Yao, Haofan Wang, Mike Zheng Shou.* <br>
**Video Style Transfer** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.17312)] <br>

**ACE-LoRA: Adaptive Orthogonal Decoupling for Continual Image Editing** <br>
*Yuehao Liu, Weijia Zhang, Xuanming Shang, Zhizhou Chen, Yanhao Ge, Shanyan Guan, Chao Ma.* <br>
**Image Editing**, Shanghai Jiao Tong University & Nanjing University & VIVO <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.14948)] <br>

**LPH-VTON: Resolving the Structure-Texture Dilemma of Virtual Try-On via Latent Process Handover** <br>
*Yixin Liu, Baihong Qian, Jinglin Jiang, Jeffery Wu, Yan Chen, Wei Wang, Yida Wang, Lanqing Yang, Guangtao Xue.* <br>
**Virtual Try-On**, Shanghai Jiao Tong University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.14874)] <br>

**Drag within Prior Distribution: Text-Conditioned Point-Based Image Editing within Distribution Constraints** <br>
*Haoyang Hu, Masataka Seo, Yen-Wei Chen.* <br>
**Image Editing** <br>
ICASSP 2026. [[PDF](https://arxiv.org/abs/2605.13349)] <br>

**DirectTryOn: One-Step Virtual Try-On via Straightened Conditional Transport** <br>
*Xianbing Sun, Jiahui Zhan, Liqing Zhang, Jianfu Zhang.* <br>
**Virtual Try-On**, Shanghai Jiao Tong University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.12939)] <br>

**Stable and Near-Reversible Diffusion ODE Solvers for Image Editing** <br>
*Barbora Barancikova, Daniil Shmelev, Cristopher Salvi.* <br>
**Image Editing**, Department of Computing, Imperial College London, London, United Kingdom & Department of Mathematics, Imperial College London, London, United Kingdom <br>
ICML 2026 Workshops (SPIGM). [[PDF](https://arxiv.org/abs/2605.16399)] <br>

**Qwen-Image-2.0 Technical Report** <br>
*Bing Zhao, Chenfei Wu, Deqing Li, Hao Meng, Jiahao Li, Jie Zhang, Jingren Zhou, Junyang Lin, Kaiyuan Gao, Kuan Cao, Kun Yan, Liang Peng, Lihan Jiang, Niantong Li, Ningyuan Tang, Shengming Yin, Tianhe Wu, Xiao Xu, Xiaoyue Chen, Xihua Wang, Yan Shu, Yanran Zhang, Yi Wang, Yilei Chen, Ying Ba, Yixian Xu, Yujia Wu, Yuxiang Chen, Zecheng Tang, Zekai Zhang, Zhendong Wang, Zihao Liu, Zikai Zhou, An Yang, Chen Cheng, Chenxu Lv, Dayiheng Liu, Fan Zhou, Hantian Xiong, Hongzhu Shi, Hu Wei, Huihong Zhao, Ivy Liu, Jianwei Zhang, Jiawei Zhang, Kai Chen, Kang He, Levon Xue, Lin Qu, Linhan Tang, Luwen Feng, Minggang Wu, Minmin Sun, Na Ni, Rui Men, Shuai Bai, Sishou Zheng, Tao Lan, Tianqi Zhang, Tingkun Wen, Wei Wang, Weixu Qiao, Weiyi Lu, Wenmeng Zhou, Xiaodong Deng, Xiaoxiao Xu, Xinlei Fang, Xionghui Chen, Yanan Wang, Yang Fan, Yichang Zhang, Yixuan Xu, Yu Wu, Zhiyuan Ma, Zhizhi Cai.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.10730)] <br>

**EditTransfer++: Toward Faithful and Efficient Visual-Prompt-Guided Image Editing** <br>
*Lan Chen, Qi Mao, Yiren Song, Yuchao Gu, Siwei Ma.* <br>
**Image Editing**, Communication University of China & National University of Singapore & Peking University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.07455)] <br>

**DBMSolver: A Training-free Diffusion Bridge Sampler for High-Quality Image-to-Image Translation** <br>
*Sankarshana Venugopal, Mohammad Mostafavi, Jonghyun Choi.* <br>
**Base I2I Translation**, Seoul National University <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2605.05889)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Venugopal_DBMSolver_A_Training-free_Diffusion_Bridge_Sampler_for_High-Quality_Image-to-Image_Translation_CVPR_2026_paper.html)]
[[Github](https://github.com/snumprlab/dbmsolver)] <br>

**SpecEdit: Training-Free Acceleration for Diffusion based Image Editing via Semantic Locking** <br>
*Zhengan Yan, Shikang Zheng, Haoran Qin, Xiaobing Tu, Yinggui Wang, Jiacheng Liu, Jiaxuan Ren, Yuqi Lin, Peiliang Cai, Jinkui Ren, Xiantao Zhang, Linfeng Zhang.* <br>
**Image Editing**, EPIC Lab, Shanghai Jiao Tong University & Shandong University & Alibaba Group & UESTC & Jilin University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.02152)] <br>

**Structured Diffusion Bridges: Inductive Bias for Denoising Diffusion Bridges** <br>
*Eitan Kosman, Gabriele Serussi, Chaim Baskin.* <br>
**Base I2I Translation**, Ben-Gurion University of the Negev, Israel <br>
ICML 2026. [[PDF](https://arxiv.org/abs/2605.02973)] <br>

**AttnRouter: Per-Category Attention Routing for Training-Free Image Editing on MMDiT** <br>
*Guandong Li, Mengxia Ye.* <br>
**Image Editing**, iFLYTEK & Aegon THTF <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.01480)] <br>

**SIFT-VTON: Geometric Correspondence Supervision on Cross-Attention for Virtual Try-On** <br>
*Kosuke Takemoto, Takafumi Koshinaka.* <br>
**Virtual Try-On**, The Graduate School of Data Science, Yokohama City University, Kanagawa, Japan <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.01296)]
[[Github](https://github.com/takesukeDS/SIFT-VTON)] <br>

**ScribbleEdit: Synthetic Data for Image Editing with Scribbles and Text** <br>
*Anya Ji, George Ma, Téa Wright, Yiming Zhang, David M. Chan, Alane Suhr, Somayeh Sojoudi.* <br>
**Image Editing**, University of California, Berkeley <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2605.01135)] <br>

**TripVVT: A Large-Scale Triplet Dataset and a Coarse-Mask Baseline for In-the-Wild Video Virtual Try-On** <br>
*Dingbao Shao, Song Wu, Shenyi Wang, Ye Wang, Ziheng Tang, Fei Liu, Jiang Lin, Xinyu Chen, Qian Wang, Ying Tai, Jian Yang, Zili Yi.* <br>
**Virtual Try-On**, Nanjing University, China & JIUTIAN Research, CMCC, China & Jilin University, China & ByteDance Inc., China <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2604.27958)]
[[Project](https://shaodingbao.github.io/TripVVT/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3935)] <br>

**Edit Where You Mean: Region-Aware Adapter Injection for Mask-Free Local Image Editing** <br>
*Honghao Cai, Xiangyuan Wang, Yunhao Bai, Haohua Chen, Tianze Zhou, Runqi Wang, Wei Zhu, Yibo Chen, Xu Tang, Yao Hu, Zhen Li.* <br>
**Image Editing**, The Chinese University of Hong Kong, Shenzhen & Xiaohongshu Inc & Peking University & Beijing University of Aeronautics and Astronautics & Tsinghua University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2604.23763)] <br>

**Probing Visual Planning in Image Editing Models** <br>
*Zhimu Zhou, Yanpeng Zhao, Qiuyu Liao, Bo Zhao, Xiaojian Ma.* <br>
**Image Editing**, Shanghai Jiao Tong University & State Key Laboratory of General Artificial Intelligence, BIGAI & Renmin University of China <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2604.22868)]
[[Github](https://github.com/spatigen/amaze)]
[[Project](https://spatigen.github.io/amaze.io/)]
[[Conference](https://neurips.cc/virtual/2026/poster/154346)] <br>

**StyleID: A Perception-Aware Dataset and Metric for Stylization-Agnostic Facial Identity Recognition** <br>
*Kwan Yun, Changmin Lee, Ayeong Jeong, Youngseo Kim, Seungmi Lee, Junyong Noh.* <br>
**Dataset / Evaluation**, KAIST, South Korea <br>
SIGGRAPH 2026. [[PDF](https://arxiv.org/abs/2604.21689)]
[[Project](https://kwanyun.github.io/StyleID_page/)] <br>

**Rethinking Where to Edit: Task-Aware Localization for Instruction-Based Image Editing** <br>
*Jingxuan He, Xiyu Wang, Mengyu Zheng, Xiangyu Zeng, Yunke Wang, Chang Xu.* <br>
**Image Editing**, The University of Sydney, Sydney, Australia <br>
ACMMM 2026. [[PDF](https://arxiv.org/abs/2604.20258)]
[[Project](https://jessie459.github.io/TAL/)] <br>

**HP-Edit: A Human-Preference Post-Training Framework for Image Editing** <br>
*Fan Li, Chonghuinan Wang, Lina Lei, Yuping Qiu, Jiaqi Xu, Jiaxiu Jiang, Xinran Qin, Zhikai Chen, Fenglong Song, Zhixin Wang, Renjing Pei, Wangmeng Zuo.* <br>
**Image Editing**, Huawei Noah’s Ark Lab Harbin Institute of Technology Nankai University <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2604.19406)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Li_HP-Edit_A_Human-Preference_Post-Training_Framework_for_Image_Editing_CVPR_2026_paper.html)] <br>

**UniGeo: Unifying Geometric Guidance for Camera-Controllable Image Editing via Video Models** <br>
*Hong Jiang, Wensong Song, Zongxin Yang, Ruijie Quan, Yi Yang.* <br>
**Image Editing**, ReLER, CCAI, Zhejiang University & DBMI, HMS, Harvard University <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2604.17565)]
[[Project](https://mo230761.github.io/UniGeo.github.io/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3886)] <br>

**Towards In-Context Tone Style Transfer with A Large-Scale Triplet Dataset** <br>
*Yuhai Deng, Huimin She, Wei Shen, Meng Li, Ruoxi Wu, Lunxi Yuan, Xiang Li.* <br>
**Image Style Transfer**, VCIP, School of Computer Science, Nankai University & Nankai International Advanced Research Institute (Shenzhen Futian) & OPPO AI Center, OPPO Inc & AAIS, Nankai University <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2604.16114)]
[[Project](https://dengyuhai.github.io/ICTone_Project/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4607)] <br>

**Is This Edit Correct? A Multi-Dimensional Benchmark for Reasoning-Aware Image Editing** <br>
*Yixuan Ding, Wei Huang, Ruijie Quan, Xiaojuan Qi, Yi Yang.* <br>
**Dataset / Evaluation**, Zhejiang University & The University of Hong Kong GitHub: github.com/Yixuan-Ding-ZJU/RE-Edit Benchmark: huggingface.co/datasets/Yixuan-Ding-ZJU/RE-Edit <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2606.05172)]
[[Github](https://github.com/Yixuan-Ding-ZJU/RE-Edit)]
[[Dataset](https://huggingface.co/datasets/Yixuan-Ding-ZJU/RE-Edit)] <br>

**DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer** <br>
*Hengye Lyu, Zisu Li, Yue Hong, Yueting Weng, Jiaxin Shi, Hanwang Zhang, Chen Liang.* <br>
**Video Style Transfer**, The Hong Kong University of Science and Technology (Guangzhou) & The Hong Kong University of Science and Technology & XMax.AI Ltd & Nanyang Technological University <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2604.13509)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/5415)] <br>

**MAST: Mask-Guided Attention Control for Training-Free Regional-Multi Style Transfer** <br>
*Dongkyung Kang, Jaeyeon Hwang, Junseo Park, Minji Kang, Yeryeong Lee, Beomseok Ko, Hanyoung Roh, Jeongmin Shin, Hyeryung Jang.* <br>
**Image Style Transfer**, Dongguk University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2604.12281)] <br>

**Energy-oriented Diffusion Bridge for Image Restoration with Foundational Diffusion Models** <br>
*Jinhui Hou, Zhiyu Zhu, Junhui Hou.* <br>
**Image Restoration**, Department of Computer Science, City University of Hong Kong & Department of Computer Science, City University of Hong Kong (Dongguan) <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2604.10983)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/a042566874294a4aaa13c243cef12336-Abstract-Conference.html)]
[[Project](https://jinnh.github.io/E-Bridge/)] <br>

**FineEdit: Fine-Grained Image Edit with Bounding Box Guidance** <br>
*Haohang Xu, Lin Liu, Zhibo Zhang, Rong Cong, Xiaopeng Zhang, Qi Tian.* <br>
**Image Editing**, Huawei Inc <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2604.10954)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4620)] <br>

**EditCrafter: Tuning-free High-Resolution Image Editing via Pretrained Diffusion Model** <br>
*Kunho Kim, Sumin Seo, Yongjun Cho, Hyungjin Chung.* <br>
**Image Editing**, NC AI & Medipixel, Inc & MAUM.AI & EverEx <br>
CVPR 2026 Workshops. [[PDF](https://arxiv.org/abs/2604.10268)]
[[Project](https://editcrafter.github.io/)] <br>

**FREE-Switch: Frequency-based Dynamic LoRA Switch for Style Transfer** <br>
*Shenghe Zheng, Minyu Zhang, Tianhao Liu, Hongzhi Wang.* <br>
**Image Style Transfer**, Harbin Institute of Technology <br>
CVPR 2026 Findings. [[PDF](https://arxiv.org/abs/2604.10023)] <br>

**What Matters in Virtual Try-Off? Dual-UNet Diffusion Model For Garment Reconstruction** <br>
*Loc-Phat Truong, Meysam Madadi, Sergio Escalera.* <br>
**Virtual Try-On**, Computer Vision Center, Spain & Universitat de Barcelona, Spain <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2604.08716)] <br>

**MegaStyle: Constructing Diverse and Scalable Style Dataset via Consistent Text-to-Image Style Mapping** <br>
*Junyao Gao, Sibo Liu, Jiaxing Li, Yanan Sun, Yuanpeng Tu, Fei Shen, Weidong Zhang, Cairong Zhao, Jun Zhang.* <br>
**Image Style Transfer**, Tongji Univeristy & Tencent & Nanyang Technological University & Hong Kong University of Science and Technology & University of Hong Kong & National University of Singapore & Fuzhou University <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2604.08364)]
[[Project](https://jeoyal.github.io/MegaStyle/)]
[[Conference](https://neurips.cc/virtual/2026/poster/139382)] <br>

**HistDiT: A Structure-Aware Latent Conditional Diffusion Model for High-Fidelity Virtual Staining in Histopathology** <br>
*Aasim Bin Saleem, Amr Ahmed, Ardhendu Behera, Hafeezullah Amin, Iman Yi Liao, Mahmoud Khattab, Pan Jia Wern, Haslina Makmur.* <br>
**Virtual Staining**, Edge Hill University, Ormskirk, L39 4QP, United Kingdom & University of Nottingham Malaysia, & Semenyih, Malaysia & University of Southampton Malaysia, & Iskandar Puteri, Malaysia & Cancer Research Malaysia,, & Subang Jaya, Malaysia <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2604.08305)]
[[Github](https://github.com/AasimBinSaleem/HistDiT)] <br>

**Leveraging Image Editing Foundation Models for Data-Efficient CT Metal Artifact Reduction** <br>
*Ahmet Rasim Emirdagi, Süleyman Aslan, Mısra Yavuz, Görkay Aydemir, Yunus Bilge Kurt, Nasrin Rahimi, Burak Can Biner, M. Akın Yılmaz.* <br>
**Image Editing**, Codeway AI Research <br>
CVPR 2026 Workshops (Med-Reasoner). [[PDF](https://arxiv.org/abs/2604.05934)]
[[Github](https://github.com/ahmetemirdagi/CT-EditMAR)] <br>

**Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision** <br>
*Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo.* <br>
**Virtual Try-On**, Seoul National University <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2604.04934)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Cha_Vanast_Virtual_Try-On_with_Human_Image_Animation_via_Synthetic_Triplet_CVPR_2026_paper.html)]
[[Project](https://hyunsoocha.github.io/vanast/)] <br>

**Training-Free Image Editing with Visual Context Integration and Concept Alignment** <br>
*Rui Song, Guo-Hua Wang, Qing-Guo Chen, Weihua Luo, Tongda Xu, Zhening Liu, Yan Wang, Zehong Lin, Jun Zhang.* <br>
**Image Editing**, HKUST & Alibaba International Digital Commerce Group & Institute for AI Industry Research (AIR), Tsinghua University & School of Data Science, Lingnan University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2604.04487)] <br>

**FlowSlider: Training-Free Continuous Image Editing via Fidelity-Steering Decomposition** <br>
*Taichi Endo, Guoqing Hao, Kazuhiko Sumi.* <br>
**Image Editing**, Aoyama Gakuin University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2604.02088)]
[[Demo](https://huggingface.co/spaces/dominoer/FlowSlider)] <br>

**SteerFlow: Steering Rectified Flows for Faithful Inversion-Based Image Editing** <br>
*Thinh Dao, Zhen Wang, Kien T. Pham, Long Chen.* <br>
**Image Editing**, The Hong Kong University of Science and Technology, Clear Water Bay, Hong Kong & VinUniversity, Ha Noi, Viet Nam <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2604.01715)] <br>

**Editing on the Generative Manifold: A Theoretical and Empirical Study of General Diffusion-Based Image Editing Trade-offs** <br>
*Yi Hu, Leying Yi, Emily Davis, Finn Carter.* <br>
**Image Editing**, Xidian University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.29736)] <br>

**ColorFLUX: A Structure-Color Decoupling Framework for Old Photo Colorization** <br>
*Bingchen Li, Zhixin Wang, Fan Li, Jiaqi Xu, Jiaming Guo, Renjing Pei, Xin Li, Zhibo Chen.* <br>
**Image Colorization**, University of Science and Technology of China & Huawei Noah’s Ark Lab <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2603.28162)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Li_ColorFLUX_A_Structure-Color_Decoupling_Framework_for_Old_Photo_Colorization_CVPR_2026_paper.html)] <br>

**InstanceAnimator: Multi-Instance Sketch Video Colorization** <br>
*Yinhan Zhang, Yue Ma, Bingyuan Wang, Kunyu Feng, Yeying Jin, Qifeng Chen, Anyi Rao, Zeyu Wang.* <br>
**Image Colorization**, HKUST(GZ) & NUS & HKUST <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.25357)]
[[Project](https://yinhan-zhang.github.io/animator)] <br>

**BiFM: Bidirectional Flow Matching for Few-Step Image Editing and Generation** <br>
*Yasong Dai, Zeeshan Hayder, David Ahmedt-Aristizabal, Hongdong Li.* <br>
**Image Editing**, Australian National University, Australia & Data61-CSIRO, Australia <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2603.24942)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Dai_BiFM_Bidirectional_Flow_Matching_for_Few-Step_Image_Editing_and_Generation_CVPR_2026_paper.html)] <br>

**HAM: A Training-Free Style Transfer Approach via Heterogeneous Attention Modulation for Diffusion Models** <br>
*Yeqi He, Liang Li, Zhiwen Yang, Xichun Sheng, Zhidong Zhao, Chenggang Yan.* <br>
**Image Style Transfer**, Hangzhou Dianzi University Institute of Computing Technology, Chinese Academy of Sciences Macao Polytechnic University <br>
CVPR 2026 Findings. [[PDF](https://arxiv.org/abs/2603.24043)] <br>

**A training-free framework for high-fidelity appearance transfer via diffusion transformers** <br>
*Shengrong Gu, Ye Wang, Song Wu, Rui Ma, Qian Wang, Lanjun Wang, Zili Yi.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.26767)] <br>

**Dress-ED: Instruction-Guided Editing for Virtual Try-On and Try-Off** <br>
*Davide Lobba, Fulvio Sanguigni, Bin Ren, Marcella Cornia, Rita Cucchiara, Nicu Sebe.* <br>
**Virtual Try-On**, University of Trento, Italy & University of Pisa, Italy & University of Modena and Reggio Emilia, Italy & MBZUAI, United Arab Emirates <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2603.22607)]
[[Github](https://github.com/aimagelab/Dress-ED)]
[[Project](https://aimagelab.github.io/Dress-ED/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4939)] <br>

**AdaEdit: Adaptive Temporal and Channel Modulation for Flow-Based Image Editing** <br>
*Guandong Li, Zhaobin Chu.* <br>
**Image Editing**, iFLYTEK <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.21615)]
[[Github](https://github.com/leeguandong/AdaEdit)] <br>

**Translating MRI to PET through Conditional Diffusion Models with Enhanced Pathology Awareness** <br>
*Yitong Li, Igor Yakushev, Dennis M. Hedderich, Christian Wachinger.* <br>
**Medical Image Translation**, Lab for Artificial Intelligence in Medical Imaging, Institute for Diagnostic and Interventional Radiology, School of Medicine and Health, TUM Klinikum, Technical University of Munich (TUM), Munich, 81675, Germany & Munich Center for Machine Learning (MCML), Munich, Germany & Department of Nuclear Medicine, School of Medicine and Health, TUM Klinikum, Munich, 81675, Germany & Department of Neuroradiology, School of Medicine and Health, TUM Klinikum, Munich, 81675, Germany <br>
Medical Image Analysis 2026. [[PDF](https://arxiv.org/abs/2603.18896)]
[[Github](https://github.com/ai-med/PASTA)] <br>

**Mixture of Style Experts for Diverse Image Stylization** <br>
*Shihao Zhu, Ziheng Ouyang, Yijia Kang, Qilong Wang, Mi Zhou, Bo Li, Ming-Ming Cheng, Qibin Hou.* <br>
**Image Style Transfer**, VCIP, CS, Nankai University NKIARI, Shenzhen Futian Tianjin University vivo BlueImage Lab <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2603.16649)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Mixture_of_Style_Experts_for_Diverse_Image_Stylization_CVPR_2026_paper.html)]
[[Project](https://hh-lg.github.io/StyleExpert-Page/)] <br>

**PROMO: Promptable Outfitting for Efficient High-Fidelity Virtual Try-On** <br>
*Haohua Chen, Tianze Zhou, Wei Zhu, Runqi Wang, Yandong Guan, Dejia Song, Yibo Chen, Xu Tang, Yao Hu, Lu Sheng, Zhiyong Wu.* <br>
**Virtual Try-On**, Xiaohongshu Inc & Beihang University & Tsinghua University <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2603.11675)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_PROMO_Promptable_Outfitting_for_Efficient_High-Fidelity_Virtual_Try-On_CVPR_2026_paper.html)] <br>

**VeloEdit: Training-Free Consistent and Continuous Instruction-Based Image Editing via Velocity Field Decomposition** <br>
*Zongqing Li, Zhihui Liu, Yujie Xie, Shansiyuan Wu, Hongshen Lv, Songzhi Su.* <br>
**Image Editing**, Xiamen University & Truesight <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.13388)]
[[Github](https://github.com/xmulzq/VeloEdit)] <br>

**StyleGallery: Training-free and Semantic-aware Personalized Style Transfer from Arbitrary Image References** <br>
*Boyu He, Yunfan Ye, Chang Liu, Weishang Wu, Fang Liu, Zhiping Cai.* <br>
**Image Style Transfer**, College of Computer Science and Technology, National University of Defense Technology & School of Design, Hunan University <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2603.10354)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/He_StyleGallery_Training-free_and_Semantic-aware_Personalized_Style_Transfer_from_Arbitrary_Image_CVPR_2026_paper.html)]
[[Github](https://github.com/iiiiiiiword/StyleGallery)] <br>

**Component-Aware Sketch-to-Image Generation Using Self-Attention Encoding and Coordinate-Preserving Fusion** <br>
*Ali Zia, Muhammad Umer Ramzan, Usman Ali, Muhammad Faheem, Abdelwahed Khamis, Shahnawaz Qureshi.* <br>
**Sketch-to-Image Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.09484)] <br>

**BridgeDiff: Bridging Human Observations and Flat-Garment Synthesis for Virtual Try-Off** <br>
*Shuang Liu, Ao Yu, Linkang Cheng, Xiwen Huang, Li Zhao, Junhui Liu, Zhiting Lin, Yu Liu.* <br>
**Virtual Try-On**, School of Integrated Circuits, Anhui University, Hefei, China & School of Astronautics, Northwestern Polytechnical University, Xi’an,China & Anhui Provincial High-performance Integrated Circuit Engineering Research Center <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.09236)] <br>

**CARE-Edit: Condition-Aware Routing of Experts for Contextual Image Editing** <br>
*Yucheng Wang, Zedong Wang, Yuetong Wu, Yue Ma, Dan Xu.* <br>
**Image Editing**, The Hong Kong University of Science and Technology <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2603.08589)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_CARE-Edit_Condition-Aware_Routing_of_Experts_for_Contextual_Image_Editing_CVPR_2026_paper.html)]
[[Project](https://care-edit.github.io/)] <br>

**Fourier Transform Infrared microspectroscopy-based super-resolution virtual staining of unlabeled tissues by pixel Diffusion Transformer** <br>
*Yudong Tian, Xiangyu Zhao, Yuqing Liu, Bofei Yang, Chongzhao Wu.* <br>
**Virtual Staining** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.08143)] <br>

**ImageEdit-R1: Boosting Multi-Agent Image Editing via Reinforcement Learning** <br>
*Yiran Zhao, Yaoqi Ye, Xiang Liu, Michael Qizhe Shieh, Trung Bui.* <br>
**Image Editing**, National University of Singapore & Adobe Research <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.08059)]
[[Github](https://github.com/zhaoyiran924/ImageEdit-R1)] <br>

**Virtual Try-On for Cultural Clothing: A Benchmarking Study** <br>
*Muhammad Tausif Ul Islam, Shahir Awlad, Sameen Yeaser Adib, Md. Atiqur Rahman, Sabbir Ahmed, Md. Hasanul Kabir.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.07291)] <br>

**DMD-augmented Unpaired Neural Schrödinger Bridge for Ultra-Low Field MRI Enhancement** <br>
*Youngmin Kim, Jaeyun Shin, Jeongchan Kim, Taehoon Lee, Jaemin Kim, Peter Hsu, Jelle Veraart, Jong Chul Ye.* <br>
**Medical Image Translation**, Korea University, Seoul, Republic of Korea & KAIST, Daejeon, Republic of Korea & NYU Langone Health, New York, NY, USA <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.03769)] <br>

**Mobile-VTON: High-Fidelity On-Device Virtual Try-On** <br>
*Zhenchen Wan, Ce Chen, Runqi Lin, Jiaxin Huang, Tianxi Chen, Yanwu Xu, Tongliang Liu, Mingming Gong.* <br>
**Virtual Try-On**, MBZUAI & University of Melbourne & Google <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2603.00947)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Wan_Mobile-VTON_High-Fidelity_On-Device_Virtual_Try-On_CVPR_2026_paper.html)]
[[Project](https://zhenchenwan.github.io/Mobile-VTON/)] <br>

**A Proper Scoring Rule for Virtual Staining** <br>
*Samuel Tonks, Steve Hood, Ryan Musso, Ceridwen Hopely, Steve Titus, Minh Doan, Iain Styles, Alexander Krull.* <br>
**Virtual Staining**, School of Computer Science, University of Birmingham, Birmingham, UK & GSK Drug Metabolism & Pharmacokinetics, GSK Medicines Research Centre, Stevenage, UK & GSK Genome Biology, Collegeville, PA, USA & School of Electronics, Electrical Engineering and Computer Science, Queen’s University Belfast, UK <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.23305)] <br>

**Uni-Animator: Towards Unified Visual Colorization** <br>
*Xinyuan Chen, Yao Xu, Shaowen Wang, Pengjie Song, Bowen Deng.* <br>
**Image Colorization**, Mississippi State University & UIUC & Hunan University & HKUST <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.23191)] <br>

**From Statics to Dynamics: Physics-Aware Image Editing with Latent Transition Priors** <br>
*Liangbing Zhao, Le Zhuo, Sayak Paul, Hongsheng Li, Mohamed Elhoseiny.* <br>
**Image Editing**, KAUST & CUHK MMLab & Krea AI & Huggingface <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.21778)]
[[Project](https://liangbingzhao.github.io/statics2dynamics/)] <br>

**Training-Free Multi-Concept Image Editing** <br>
*Niki Foteinopoulou, Ignas Budvytis, Stephan Liwicki.* <br>
**Image Editing**, Cambridge Research Laboratory, Toshiba Europe, Cambridge, UK & Independent Researcher, UK <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2602.20839)]
[[Project](https://nickyfot.github.io/cds/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3799)] <br>

**CleanStyle: Plug-and-Play Style Conditioning Purification for Text-to-Image Stylization** <br>
*Xiaoman Feng, Mingkun Lei, Yang Wang, Dingwen Fu, Chi Zhang.* <br>
**Image Style Transfer**, Westlake University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.20721)]
[[Github](https://github.com/Westlake-AGI-Lab/CleanStyle)] <br>

**RegionRoute: Regional Style Transfer with Diffusion Model** <br>
*Bowen Chen, Jake Zuena, Alan C. Bovik, Divya Kothandaraman.* <br>
**Image Style Transfer**, The University of Texas at Austin & Dolby Laboratories, Inc <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2602.19254)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_RegionRoute_Regional_Style_Transfer_with_Diffusion_Model_CVPR_2026_paper.html)] <br>

**CRAFT-LoRA: Content-Style Personalization via Rank-Constrained Adaptation and Training-Free Fusion** <br>
*Yu Li, Yujun Cai, Chi Zhang.* <br>
**Image Style Transfer**, AGI Lab, Westlake University & George Washington University & The University of Queensland <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2602.18936)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CRAFT-LoRA_Content-Style_Personalization_via_Rank-Constrained_Adaptation_and_Training-Free_Fusion_CVPR_2026_paper.html)]
[[Github](https://github.com/Skylanding/CraftLoRA)] <br>

**Dual-Channel Attention Guidance for Training-Free Image Editing Control in Diffusion Transformers** <br>
*Guandong Li.* <br>
**Image Editing**, iFLYTEK <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.18022)] <br>

**CORAL: Correspondence Alignment for Improved Virtual Try-On** <br>
*Jiyoung Kim, Youngjin Shin, Siyoon Jin, Dahyun Chung, Jisu Nam, Tongmin Kim, Jongjae Park, Hyeonwoo Kang, Seungryong Kim.* <br>
**Virtual Try-On**, KAIST AI & NC AI Co., Ltd <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2602.17636)]
[[Project](https://cvlab-kaist.github.io/CORAL)]
[[Conference](https://neurips.cc/virtual/2026/poster/151032)] <br>

**Unpaired Image-to-Image Translation via a Self-Supervised Semantic Bridge** <br>
*Jiaming Liu, Felix Petersen, Yunhe Gao, Yabin Zhang, Hyojin Kim, Akshay S. Chaudhari, Yu Sun, Stefano Ermon, Sergios Gatidis.* <br>
**Base I2I Translation**, Stanford University & LLNL & Johns Hopkins University <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.16664)]
[[Github](https://github.com/StanfordMIMI/SemanticBridge)] <br>

**OmniVTON++: Training-Free Universal Virtual Try-On with Principal Pose Guidance** <br>
*Zhaotong Yang, Yong Du, Shengfeng He, Yuhui Li, Xinzhe Li, Yangyang Xu, Junyu Dong, Jian Yang.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.14552)]
[[Github](https://github.com/Jerome-Young/OmniVTON-PlusPlus)] <br>

**CoCoDiff: Correspondence-Consistent Diffusion Model for Fine-grained Style Transfer** <br>
*Wenbo Nie, Zixiang Li, Renshuai Tao, Bin WU, Yunchao Wei, Yao Zhao.* <br>
**Image Style Transfer**, Institute of Information Science, Beijing Jiaotong University & Visual Intelligence + X International Joint Laboratory of the Ministry of Education <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2602.14464)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/fd946a6c99541fddc3d64a3ea39a1bc2-Abstract-Conference.html)]
[[Github](https://github.com/Wenbo-Nie/CoCoDiff)] <br>

**UniRef-Image-Edit: Towards Scalable and Consistent Multi-Reference Image Editing** <br>
*Hongyang Wei, Bin Wen, Yancheng Long, Yankai Yang, Yuhang Hu, Tianke Zhang, Wei Chen, Haonan Fan, Kaiyu Jiang, Jiankang Chen, Changyi Liu, Kaiyu Tang, Haojie Ding, Xiao Yang, Jia Sun, Huaiqing Wang, Zhenyu Yang, Xinyu Wei, Xianglong He, Yangguang Li, Fan Yang, Tingting Gao, Lei Zhang, Guorui Zhou, Han Li.* <br>
**Image Editing**, Tsinghua University & Kuaishou Technology & Harbin Institute of Technology, Shenzhen & Hong Kong Polytechnic University & CUHK MMLab <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.14186)] <br>

**FireRed-Image-Edit-1.0 Technical Report** <br>
* Super Intelligence Team, Changhao Qiao, Chao Hui, Chen Li, Cunzheng Wang, Dejia Song, Jiale Zhang, Jing Li, Qiang Xiang, Runqi Wang, Shuang Sun, Wei Zhu, Xu Tang, Yao Hu, Yibo Chen, Yuhao Huang, Yuxuan Duan, Zhiyi Chen, Ziyuan Guo.* <br>
**Image Editing** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.13344)]
[[Github](https://github.com/FireRedTeam/FireRed-Image-Edit/)]
[[Model](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0)]
[[Demo](https://huggingface.co/spaces/FireRedTeam/FireRed-Image-Edit-1.0)] <br>

**Geometric Image Editing via Effects-Sensitive In-Context Inpainting with Diffusion Transformers** <br>
*Shuo Zhang, Wenzhuo Wu, Huayu Zhang, Cheng Jiarong, Xianghao Zang, Chao Ban, Hao Sun, Zhongjiang He, Tianwei Cao, Kongming Liang, Zhanyu Ma.* <br>
**Image Editing**, PRIS, Beijing University of Posts and Telecommunications & Institute of Artificial Intelligence (TeleAI), China Telecom & Beijing Institute of Technology <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2602.08388)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/0429ececfb199efc93182990169e73bb-Abstract-Conference.html)] <br>

**SIGMA: Selective-Interleaved Generation with Multi-Attribute Tokens** <br>
*Xiaoyan Zhang, Zechen Bai, Haofan Wang, Yiren Song.* <br>
**Image Editing**, Creatly AI & University of Michigan & Lovart AI & National University of Singapore <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2602.07564)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_SIGMA_Selective-Interleaved_Generation_with_Multi-Attribute_Tokens_CVPR_2026_paper.html)] <br>

**RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing** <br>
*Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra.* <br>
**Video Style Transfer** <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2602.06871)]
[[Project](https://smsd75.github.io/RFDM_page/)] <br>

**Style-Instructed Mask-Free Virtual Try On** <br>
*Mengqi Zhang, Qi Li, Mehmet Saygin Seyfioglu, Karim Bouyarmane.* <br>
**Virtual Try-On**, Amazon & Georgia Institute of Technology <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2603.29587)]
[[Project](https://smf-vto.github.io)] <br>

**FlowBypass: Rectified Flow Trajectory Bypass for Training-Free Image Editing** <br>
*Menglin Han, Zhangkai Ni.* <br>
**Image Editing**, School of Computer Science and Technology, Tongji University, Shanghai, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2602.01805)] <br>

**Neural Clothing Tryer: Customized Virtual Try-On via Semantic Enhancement and Controlling Diffusion Model** <br>
*Zhijing Yang, Weiwei Zhang, Mingliang Yang, Siyuan Peng, Yukai Shi, Junpeng Tan, Tianshui Chen, Liruo Zhong.* <br>
**Virtual Try-On** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2601.22838)] <br>

**OpenVTON-Bench: A Large-Scale High-Resolution Benchmark for Controllable Virtual Try-On Evaluation** <br>
*Jin Li, Tao Chen, Kai Wen, Siqi Yin, Shuai Jiang, Weijie Wang, Jingwen Luo, Chenhui Wu.* <br>
**Virtual Try-On**, Renxing Intelligence, Hangzhou, China & Hangzhou Dianzi University, Hangzhou, China <br>
NeurIPS 2026. [[PDF](https://arxiv.org/abs/2601.22725)]
[[Github](https://github.com/RenxingIntelligence/OpenVTON-Bench)]
[[Conference](https://neurips.cc/virtual/2026/poster/139156)] <br>

**Unifying Heterogeneous Degradations: Uncertainty-Aware Diffusion Bridge Model for All-in-One Image Restoration** <br>
*Luwei Tu, Jiawei Wu, Xing Luo, Zhi Jin.* <br>
**Image Restoration**, School of Intelligent Systems Engineering, Shenzhen Campus of Sun Yat-sen University, Shenzhen, Guangdong 518107, China & Department of Frontier Research, Peng Cheng Laboratory, Shenzhen, Guangdong 518055, China & Guangdong Provincial Key Laboratory of Fire Science and Technology, Guangzhou 510006, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2601.21592)]
[[Github](https://github.com/Jabruson/UDBM)] <br>

**TeleStyle: Content-Preserving Style Transfer in Images and Videos** <br>
*Shiwen Zhang, Xiaoyan Yang, Bojia Zi, Haibin Huang, Chi Zhang, Xuelong Li.* <br>
**Image Style Transfer**, TeleAI <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2601.20175)]
[[Github](https://github.com/Tele-AI/TeleStyle)]
[[Project](https://tele-ai.github.io/TeleStyle/)] <br>

**FBSDiff++: Improved Frequency Band Substitution of Diffusion Features for Efficient and Highly Controllable Text-Driven Image-to-Image Translation** <br>
*Xiang Gao, Yunpeng Jia.* <br>
**Base I2I Translation** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2601.19115)] <br>

**Adaptive Domain Shift in Diffusion Models for Cross-Modality Image Translation** <br>
*Zihao WANG, Yuzhou Chen, Shaogang Ren.* <br>
**Base I2I Translation**, Laplace Lab at University of Tennessee & University of California Riverside & University of Tennessee at Chattanooga <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2601.18623)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/8a47fb6a26596c405e5f8db81c9c7d9f-Abstract-Conference.html)] <br>

**Edge-Aware Image Manipulation via Diffusion Models with a Novel Structure-Preservation Loss** <br>
*Minsu Gong, Nuri Ryu, Jungseul Ok, Sunghyun Cho.* <br>
**Image Editing**, Planby Technologies & POSTECH <br>
WACV 2026. [[PDF](https://arxiv.org/abs/2601.16645)]
[[Github](https://github.com/gongms00/SPL)] <br>

**OmniTransfer: All-in-one Framework for Spatio-temporal Video Transfer** <br>
*Pengze Zhang, Yanze Wu, Mengtian Li, Xu Bai, Songtao Zhao, Fulong Ye, Chong Mou, Xinghui Li, Zhuowei Chen, Qian He, Mingyuan Gao.* <br>
**Video Style Transfer** <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2601.14250)]
[[Project](https://pangzecheung.github.io/OmniTransfer/)] <br>

**GO-MLVTON: Garment Occlusion-Aware Multi-Layer Virtual Try-On with Diffusion Models** <br>
*Yang Yu, Yunze Deng, Yige Zhang, Yanjie Xiao, Youkun Ou, Wenhao Hu, Mingchao Li, Bin Feng, Wenyu Liu, Dandan Zheng, Jingdong Chen.* <br>
**Virtual Try-On** <br>
ICASSP 2026. [[PDF](https://arxiv.org/abs/2601.13524)]
[[Project](https://upyuyang.github.io/go-mlvton/)] <br>

**QwenStyle: Content-Preserving Style Transfer with Qwen-Image-Edit** <br>
*Shiwen Zhang, Haibin Huang, Chi Zhang, Xuelong Li.* <br>
**Image Style Transfer**, Institute of Artificial Intelligence (TeleAI), China Telecom <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2601.06202)]
[[Github](https://github.com/witcherofresearch/Qwen-Image-Style-Transfer)] <br>

**DreamStyle: A Unified Framework for Video Stylization** <br>
*Mengtian Li, Jinshu Chen, Songtao Zhao, Wanquan Feng, Pengqi Tu, Qian He.* <br>
**Video Style Transfer** <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2601.02785)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Li_DreamStyle_A_Unified_Framework_for_Video_Stylization_CVPR_2026_paper.html)]
[[Project](https://lemonsky1995.github.io/dreamstyle/)] <br>

**TimeColor: Flexible Reference Colorization via Temporal Concatenation** <br>
*Bryan Constantine Sadihin, Yihao Meng, Michael Hua Wang, Matteo Jiahao Chen, Hang Su.* <br>
**Image Colorization**, Computer Science and Technology Tsinghua University Beijing, China & Computer Science and Engineering HKUST Hong Kong, China <br>
arXiv 2026. [[PDF](https://arxiv.org/abs/2601.00296)]
[[Project](https://bconstantine.github.io/TimeColor/)] <br>

**Style-GRPO: Semantic-Aware Preference Optimization for Image Style Transfer Guided by Reward Modeling** <br>
*Jianbin Zhao, Chaoran Feng, Miao Yu, Yingtao Li, Zhenyu Tang, Wangbo Yu, Yian Zhao, Xiaomin Li, Li Yuan, Yonghong Tian.* <br>
**Image Style Transfer** <br>
CVPR 2026. [[PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Zhao_Style-GRPO_Semantic-Aware_Preference_Optimization_for_Image_Style_Transfer_Guided_by_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Zhao_Style-GRPO_Semantic-Aware_Preference_Optimization_for_Image_Style_Transfer_Guided_by_CVPR_2026_paper.html)] <br>

**EmoStyle: Emotion-Driven Image Stylization** <br>
*Jingyuan Yang, Zihuan Bai, Hui Huang.* <br>
**Image Style Transfer** <br>
CVPR 2026. [[PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Yang_EmoStyle_Emotion-Driven_Image_Stylization_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_EmoStyle_Emotion-Driven_Image_Stylization_CVPR_2026_paper.html)] <br>

**Resolving Endpoint Underfitting in Diffusion Bridges via Noise Alignment** <br>
*Yurong Gao, Zicheng Zhang, Congying Han, Tiande Guo, Xinmin Qiu.* <br>
**Base I2I Translation** <br>
CVPR 2026. [[PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Gao_Resolving_Endpoint_Underfitting_in_Diffusion_Bridges_via_Noise_Alignment_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Gao_Resolving_Endpoint_Underfitting_in_Diffusion_Bridges_via_Noise_Alignment_CVPR_2026_paper.html)]
[[Github](https://github.com/gyr02/NADB)] <br>

**TherA: Thermal-Aware Visual-Language Prompting for Controllable RGB-to-Thermal Infrared Translation** <br>
*Dong-Guw Lee, Tai Hyoung Rhee, Hyunsoo Jang, Young-Sik Shin, Ukcheol Shin, Ayoung Kim.* <br>
**Infrared Image Translation** <br>
CVPR 2026. [[PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Lee_TherA_Thermal-Aware_Visual-Language_Prompting_for_Controllable_RGB-to-Thermal_Infrared_Translation_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Lee_TherA_Thermal-Aware_Visual-Language_Prompting_for_Controllable_RGB-to-Thermal_Infrared_Translation_CVPR_2026_paper.html)] <br>

**SynthRGB-T: Language-Vision Guided Image Translation for Diversity Synthesis** <br>
*Jiangang Ding, Yiquan Du, Pengxiang Li, Lili Pei, Yuanlin Zhao, Wei Li.* <br>
**Infrared Image Translation** <br>
CVPR 2026. [[PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Ding_SynthRGB-T_Language-Vision_Guided_Image_Translation_for_Diversity_Synthesis_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Ding_SynthRGB-T_Language-Vision_Guided_Image_Translation_for_Diversity_Synthesis_CVPR_2026_paper.html)] <br>

**ConsistCompose: Unified Multimodal Layout Control for Image Composition** <br>
*Xuanke Shi, Boxuan Li, Xiaoyang Han, Zhongang Cai, Lei Yang, Quan Wang, Dahua Lin.* <br>
**Image Editing** <br>
CVPR 2026. [[PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Shi_ConsistCompose_Unified_Multimodal_Layout_Control_for_Image_Composition_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_ConsistCompose_Unified_Multimodal_Layout_Control_for_Image_Composition_CVPR_2026_paper.html)] <br>

**I2I-Bench: A Comprehensive Benchmark Suite for Image-to-Image Editing Models** <br>
*Juntong Wang, Jiarui Wang, Huiyu Duan, Jiaxiang Kang, Guangtao Zhai, Xiongkuo Min.* <br>
**Dataset / Evaluation** <br>
CVPR 2026. [[PDF](https://openaccess.thecvf.com/content/CVPR2026/papers/Wang_I2I-Bench_A_Comprehensive_Benchmark_Suite_for_Image-to-Image_Editing_Models_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_I2I-Bench_A_Comprehensive_Benchmark_Suite_for_Image-to-Image_Editing_Models_CVPR_2026_paper.html)] <br>

**ChronoEdit: Towards Temporal Reasoning for In-Context Image Editing and World Simulation** <br>
*Jay Zhangjie Wu, Xuanchi Ren, Tianchang Shen, Tianshi Cao, Kai He, Yifan Lu, Ruiyuan Gao, Enze Xie, Shiyi Lan, Jose M. Alvarez, Jun Gao, Sanja Fidler, Zian Wang, Huan Ling.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/10b99813d5992673da90a499b6bcd5f0-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/10b99813d5992673da90a499b6bcd5f0-Abstract-Conference.html)] <br>

**Follow-Your-Shape: Shape-Aware Image Editing via Trajectory-Guided Region Control** <br>
*Zeqian Long, Mingzhe Zheng, Kunyu Feng, Xinhua Zhang, Hongyu Liu, Harry Yang, Linfeng Zhang, Qifeng Chen, Yue Ma.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/6b315c0b736711b56f33cbacfb6d5d67-Abstract-Conference.html)] <br>

**RegionE: Adaptive Region-Aware Generation for Efficient Image Editing** <br>
*Pengtao Chen, Xianfang Zeng, Maosen Zhao, Mingzhu Shen, Peng Ye, Bangyin Xiang, Zhibo Wang, Wei Cheng, Gang Yu, Tao Chen.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/70270a1bc28ecb2a2aefad566c5e556b-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/70270a1bc28ecb2a2aefad566c5e556b-Abstract-Conference.html)] <br>

**Draw-In-Mind: Rebalancing Designer-Painter Roles in Unified Multimodal Models Benefits Image Editing** <br>
*Ziyun Zeng, David Junhao Zhang, Wei Li, Mike Zheng Shou.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/87f476af4053961667c2c08e9f4b850e-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/87f476af4053961667c2c08e9f4b850e-Abstract-Conference.html)]
[[Github](https://github.com/showlab/DIM)] <br>

**FaSTA*: Fast-Slow Toolpath Agent with Subroutine Mining for Efficient Multi-turn Image Editing** <br>
*Advait Gupta, Rishie Raj, Dang Nguyen, Tianyi Zhou.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/d01db5cd2555ba11f75da0454d57b903-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/d01db5cd2555ba11f75da0454d57b903-Abstract-Conference.html)] <br>

**W-EDIT: A Wavelet-Based Frequency-Aware Framework for Text-Driven Image Editing** <br>
*Jiahui Sun, Weining Wang, Mingzhen Sun, Peiyao Wang, Xinxin Zhu, Jing Liu.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/f049728dc51a393a6d8c7d6e25198ee5-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f049728dc51a393a6d8c7d6e25198ee5-Abstract-Conference.html)] <br>

**Dragging with Geometry: From Pixels to Geometry-Guided Image Editing** <br>
*Xinyu Pu, Hongsong Wang, Jie Gui, Pan Zhou.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/f6775d49c75d819d275148c9902bac57-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f6775d49c75d819d275148c9902bac57-Abstract-Conference.html)]
[[Project](https://xinyu-pu.github.io/projects/geodrag)] <br>

**EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling** <br>
*Xin Luo, Jiahao Wang, Chenyuan Wu, Shitao Xiao, Xiyan Jiang, Defu Lian, Jiajun Zhang, Dong Liu, Zheng Liu.* <br>
**Dataset / Evaluation** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/381ceeae4a1feb1abc59c773f7e61839-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/381ceeae4a1feb1abc59c773f7e61839-Abstract-Conference.html)] <br>

**WorldEdit: Towards Open-World Image Editing with a Knowledge-Informed Benchmark** <br>
*Wang Lin, Feng Wang, Majun Zhang, Wentao Hu, Tao Jin, Zhou Zhao, Fei Wu, Jingyuan Chen, Sucheng Ren, Alan Yuille.* <br>
**Dataset / Evaluation** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/3b576711b12ab036b45130fc8eb78504-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3b576711b12ab036b45130fc8eb78504-Abstract-Conference.html)] <br>

**EditReward: A Human-Aligned Reward Model for Instruction-Guided Image Editing** <br>
*Keming Wu, Sicong Jiang, Max Ku, PING NIE, Minghao Liu, Wenhu Chen.* <br>
**Dataset / Evaluation** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/4d68af3056842229f8b356d686aec914-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/4d68af3056842229f8b356d686aec914-Abstract-Conference.html)] <br>

**PICABench: How Far are We from Physical Realistic  Image Editing?** <br>
*Yuandong Pu, Le Zhuo, Songhao Han, Jinbo Xing, Kaiwen Zhu, Shuo Cao, Bin Fu, Si Liu, Hongsheng Li, Yu Qiao, Wenlong Zhang, Xi Chen, Yihao Liu.* <br>
**Dataset / Evaluation** <br>
ICLR 2026. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/ae0509bfd3e0c2414164209949708e4e-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ae0509bfd3e0c2414164209949708e4e-Abstract-Conference.html)] <br>

**The devil is in the details: Enhancing Video Virtual Try-On via Keyframe-Driven Details Injection** <br>
*Qingdong He, Xueqin Chen, Yanjie Pan, Peng Tang, Pengcheng Xu, Zhenye Gan, Chengjie Wang, Xiaobin Hu, Jiangning Zhang, Yabiao Wang.* <br>
**Virtual Try-On**, Tencent Youtu Lab & Fudan University & Western University & TU Delft <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2512.20340)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/He_The_devil_is_in_the_details_Enhancing_Video_Virtual_Try-On_CVPR_2026_paper.html)]
[[Dataset](https://huggingface.co/datasets/zijiyingcai/ViT-HD)] <br>

**RePlan: Reasoning-guided Region Planning for Complex Instruction-based Image Editing** <br>
*Tianyuan Qu, Lei Ke, Xiaohang Zhan, Longxiang Tang, Yuqi Liu, Bohao Peng, Bei Yu, Dong Yu, Jiaya Jia.* <br>
**Image Editing**, Tencent AI Lab, China & The Chinese University of Hong Kong, China & The Hong Kong University of Science and Technology, China <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2512.16864)]
[[Project](https://replan-iv-edit.github.io)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3410)] <br>

**Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition** <br>
*Shengming Yin, Zekai Zhang, Zecheng Tang, Kaiyuan Gao, Xiao Xu, Kun Yan, Jiahao Li, Yilei Chen, Yuxiang Chen, Heung-Yeung Shum, Lionel M. Ni, Junyang Lin, Chenfei Wu.* <br>
**Image Editing**, HKUST(GZ) Alibaba HKUST <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2512.15603)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_Qwen-Image-Layered_Towards_Inherent_Editability_via_Layer_Decomposition_CVPR_2026_paper.html)]
[[Github](https://github.com/QwenLM/Qwen-Image-Layered)] <br>

**The Devil is in Attention Sharing: Improving Complex Non-rigid Image Editing Faithfulness via Attention Synergy** <br>
*Zhuo Chen, Fanyue Wei, Runze Xu, Jingjing Li, Lixin Duan, Angela Yao, Wen Li.* <br>
**Image Editing**, University of Electronic Science and Technology of China & National University of Singapore Project: <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2512.14423)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_The_Devil_is_in_Attention_Sharing_Improving_Complex_Non-rigid_Image_CVPR_2026_paper.html)]
[[Project](https://synps26.github.io/)] <br>

**CogniEdit: Dense Gradient Flow Optimization for Fine-Grained Image Editing** <br>
*Yan Li, Lin Liu, Xiaopeng Zhang, Wei Xue, Wenhan Luo, Yike Guo, Qi Tian.* <br>
**Image Editing** <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2512.13276)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Li_CogniEdit_Dense_Gradient_Flow_Optimization_for_Fine-Grained_Image_Editing_CVPR_2026_paper.html)] <br>

**SCAdapter: Content-Style Disentanglement for Diffusion Style Transfer** <br>
*Luan Thanh Trinh, Kenji Doi, Atsuki Osanai.* <br>
**Image Style Transfer**, LY Corporation <br>
WACV 2026. [[PDF](https://arxiv.org/abs/2512.12963)] <br>

**FlowDC: Flow-Based Decoupling-Decay for Complex Image Editing** <br>
*Yilei Jiang, Zhen Wang, Yanghao Wang, Jun Yu, Yueting Zhuang, Jun Xiao, Long Chen.* <br>
**Image Editing**, Zhejiang University & HKUST & Harbin Institute of Technology (Shenzhen) <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2512.11395)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_FlowDC_Flow-Based_Decoupling-Decay_for_Complex_Image_Editing_CVPR_2026_paper.html)] <br>

**MotionEdit: Benchmarking and Learning Motion-Centric Image Editing** <br>
*Yixin Wan, Lei Ke, Wenhao Yu, Kai-Wei Chang, Dong Yu.* <br>
**Dataset / Evaluation**, Tencent AI, Seattle University of California, Los Angeles <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2512.10284)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Wan_MotionEdit_Benchmarking_and_Learning_Motion-Centric_Image_Editing_CVPR_2026_paper.html)]
[[Github](https://github.com/elainew728/motion-edit/)]
[[Project](https://motion-edit.github.io/)] <br>

**MagicQuill V2: Precise and Interactive Image Editing with Layered Visual Cues** <br>
*Zichen Liu, Yue Yu, Hao Ouyang, Qiuyu Wang, Shuailei Ma, Ka Leong Cheng, Wen Wang, Qingyan Bai, Yuxuan Zhang, Yanhong Zeng, Yixuan Li, Xing Zhu, Yujun Shen, Qifeng Chen.* <br>
**Image Editing**, HKUST & Ant Group & NEU & ZJU & CUHK <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2512.03046)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_MagicQuill_V2_Precise_and_Interactive_Image_Editing_with_Layered_Visual_CVPR_2026_paper.html)] <br>

**ReasonEdit: Towards Reasoning-Enhanced Image Editing Models** <br>
*Fukun Yin, Shiyu Liu, Yucheng Han, Zhibo Wang, Peng Xing, Rui Wang, Wei Cheng, Yingming Wang, Aojie Li, Zixin Yin, Pengtao Chen, Xianfang Zeng, Gang Yu, Daxin Jiang.* <br>
**Image Editing** <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2511.22625)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_ReasonEdit_Towards_Reasoning-Enhanced_Image_Editing_Models_CVPR_2026_paper.html)]
[[Github](https://github.com/stepfun-ai/Step1X-Edit)] <br>

**Rethinking Garment Conditioning in Diffusion-based Virtual Try-On: Decouple, Don't Denoise** <br>
*Kihyun Na, Jinyoung Choi, Injung Kim.* <br>
**Virtual Try-On**, Advanced AI Talent Education and Research Group for Industrial Innovation, Handong Global University, Pohang 37554, Republic of Korea & Department of Artificial Intelligence, Computer and Electrical Engineering, Handong Global University, Pohang 37554, Republic of Korea <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2511.18775)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4096)] <br>

**FIA-Edit: Frequency-Interactive Attention for Efficient and High-Fidelity Inversion-Free Text-Guided Image Editing** <br>
*Kaixiang Yang, Boyang Shen, Xin Li, Yuchen Dai, Yuxuan Luo, Yueran Ma, Wei Fang, Qiang Li, Zhiwei Wang.* <br>
**Image Editing** <br>
AAAI 2026. [[PDF](https://arxiv.org/abs/2511.12151)]
[[Github](https://github.com/kk42yy/FIA-Edit)] <br>

**OmniText: A Training-Free Generalist for Controllable Text-Image Manipulation** <br>
*Agus Gunawan, Samuel Teodoro, Yun Chen, Soo Ye Kim, Jihyong Oh, Munchurl Kim.* <br>
**Image Editing**, KAIST & Adobe Research & Chung-Ang University <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2510.24093)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/9f0e11daf595e33ed9fe1d0c0069d19b-Abstract-Conference.html)]
[[Project](https://kaist-viclab.github.io/omnitext-site)] <br>

**Residual Diffusion Bridge Model for Image Restoration** <br>
*Hebaixu Wang, Jing Zhang, Haoyang Chen, Haonan Guo, Di Wang, Jiayi Ma, Bo Du.* <br>
**Image Restoration**, School of Electronic Information, Wuhan University, Wuhan, China & Zhongguancun Academy, Beijing, China & School of Computer Science, Wuhan University, Wuhan, China & State Key Laboratory of Information Engineering in Surveying, Mapping and Remote SensingWuhan University, Wuhan, China & School of Robotics, Wuhan University, Wuhan, China <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2510.23116)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Residual_Diffusion_Bridge_Model_for_Image_Restoration_CVPR_2026_paper.html)]
[[Github](https://github.com/MiliLab/RDBM)] <br>

**Coupled Diffusion Sampling for Training-Free Multi-View Image Editing** <br>
*Hadi Alzayer, Yunzhi Zhang, Chen Geng, Jia-Bin Huang, Jiajun Wu.* <br>
**Image Editing**, Stanford University & University of Maryland, College Park <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2510.14981)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Alzayer_Coupled_Diffusion_Sampling_for_Training-Free_Multi-View_Image_Editing_CVPR_2026_paper.html)]
[[Project](https://coupled-diffusion.github.io)] <br>

**Learning an Image Editing Model without Image Editing Pairs** <br>
*Nupur Kumari, Sheng-Yu Wang, Cherry Zhao, Yotam Nitzan, Yuheng Li, Krishna Kumar Singh, Richard Zhang, Eli Shechtman, Jun-Yan Zhu, Xun Huang.* <br>
**Image Editing** <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2510.14978)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b4995cbd0b7f6a1a366ee65f9c4b02ac-Abstract-Conference.html)]
[[Project](https://nupurkmr9.github.io/npedit/)] <br>

**PickStyle: Video-to-Video Style Transfer with Context-Style Adapters** <br>
*Soroush Mehraban, Vida Adeli, Jacob Rommann, Kyryl Truskovskyi, Harrison Sanborn, Babak Taati, Cole Clifford.* <br>
**Video Style Transfer**, Pickford AI University of Toronto Vector Institute <br>
ECCV 2026 Workshops. [[PDF](https://arxiv.org/abs/2510.07546)] <br>

**FreeViS: Training-free Video Stylization with Inconsistent References** <br>
*Jiacong Xu, Yiqun Mei, Ke Zhang, Vishal Patel.* <br>
**Video Style Transfer**, Johns Hopkins University & Adobe Research <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2510.01686)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/1458726f6d5280ae99aee06ddbe455f3-Abstract-Conference.html)]
[[Project](https://xujiacong.github.io/FreeViS/)] <br>

**Training-Free Reward-Guided Image Editing via Trajectory Optimal Control** <br>
*Jinho Chang, Jaemin Kim, Jong Chul YE.* <br>
**Image Editing**, Graduate School of Artificial Intelligence & Korea Advanced Institute of Science and Technology & Seoul, South Korea <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2509.25845)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/2c3b636b64ca1dfdae3e096e4deeaa42-Abstract-Conference.html)]
[[Github](https://github.com/jinhojsk515/ITOC)] <br>

**OmniStyle2: Learning to Stylize by Learning to Destylize** <br>
*Ye Wang, Zili Yi, Yibo Zhang, Peng Zheng, Xuping Xie, Jiang Lin, Yijun Li, Yilin Wang, Rui Ma.* <br>
**Image Style Transfer** <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2509.05970)]
[[Project](https://wangyephd.github.io/projects/DeStyle/index.html)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3668)] <br>

**Delta Rectified Flow Sampling for Text-to-Image Editing** <br>
*Gaspard Beaudouin, Minghan Li, Jaeyeon Kim, Sung-Hoon Yoon, Mengyu Wang.* <br>
**Image Editing**, Harvard AI and Robotics Lab, Harvard University & École Nationale des Ponts et Chaussées, Institut Polytechnique de Paris & Computer Science Department, Harvard University & Multimodal Intelligence and Perception Lab, DGIST & Kempner Institute for the Study of Natural and Artificial Intelligence, Harvard University <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2509.05342)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Beaudouin_Delta_Rectified_Flow_Sampling_for_Text-to-Image_Editing_CVPR_2026_paper.html)]
[[Github](https://github.com/Harvard-AI-and-Robotics-Lab/DeltaRectifiedFlowSampling)] <br>

**Efficient Image-to-Image Schrödinger Bridge for CT Field of View Extension** <br>
*Zhenhao Li, Song Ni, Long Yang, Xiaojie Yin, Haijun Yu, Jiazhou Wang, Hongbin Han, Weigang Hu, Yixing Huang.* <br>
**Medical Image Translation** <br>
IEEE Transactions on Radiation and Plasma Medical Sciences 2026. [[PDF](https://arxiv.org/abs/2508.11211)] <br>

**TweezeEdit: Consistent and Efficient Image Editing with Path Regularization** <br>
*Jianda Mao, Kaibo Wang, Yang Xiang, Kani Chen.* <br>
**Image Editing**, Department of Mathematics, The Hong Kong University of Science and Technology, Hong Kong SAR <br>
AAAI 2026. [[PDF](https://arxiv.org/abs/2508.10498)] <br>

**X2Edit: Revisiting Arbitrary-Instruction Image Editing through Self-Constructed Data and Task-Aware Representation Learning** <br>
*Jian Ma, Xujie Zhu, Zihao Pan, Qirong Peng, Xu Guo, Chen Chen, Haonan Lu.* <br>
**Image Editing** <br>
AAAI 2026. [[PDF](https://arxiv.org/abs/2508.07607)]
[[Github](https://github.com/OPPO-Mente-Lab/X2Edit)] <br>

**CycleDiff: Cycle Diffusion Models for Unpaired Image-to-image Translation** <br>
*Shilong Zou, Yuhang Huang, Renjiao Yi, Chenyang Zhu, Kai Xu.* <br>
**Base I2I Translation**, National University of Defense Technology & Fudan University & Xiangjiang Laboratory & Chinese Academy of Sciences <br>
IEEE TIP 2026. [[PDF](https://arxiv.org/abs/2508.06625)]
[[Project](https://zoushilong1024.github.io/CycleDiff/)] <br>

**UniEdit-I: Training-free Image Editing for Unified VLM via Iterative Understanding, Editing and Verifying** <br>
*Chengyu Bai, Jintao Chen, Xiang Bai, Yilong Chen, Qi She, Ming Lu, Shanghang Zhang.* <br>
**Image Editing** <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2508.03142)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Bai_UniEdit-I_Training-free_Image_Editing_for_Unified_VLM_via_Iterative_Understanding_CVPR_2026_paper.html)] <br>

**CoCoLIT: ControlNet-Conditioned Latent Image Translation for MRI to Amyloid PET Synthesis** <br>
*Alec Sargood, Lemuel Puglisi, James H. Cole, Neil P. Oxtoby, Daniele Ravì, Daniel C. Alexander.* <br>
**Medical Image Translation** <br>
AAAI 2026. [[PDF](https://arxiv.org/abs/2508.01292)]
[[Github](https://github.com/brAIn-science/CoCoLIT)] <br>

**Reasoning to Edit: Hypothetical Instruction-Based Image Editing with Visual Reasoning** <br>
*Qingdong He, Xueqin Chen, Chaoyi Wang, Yanjie Pan, Xiaobin Hu, Zhenye Gan, Yabiao Wang, Chengjie Wang, Xiangtai Li, Jiangning Zhang.* <br>
**Image Editing**, Tencent Youtu Lab, China & Sichuan University, China & University of the Chinese Academy of Sciences, China & Fudan University, China & National University of Singapore, Singapore & Nanyang Technological University, Singapore & Zhejiang University, China <br>
ICML 2026. [[PDF](https://arxiv.org/abs/2507.01908)]
[[Github](https://github.com/hithqd/ReasonBrain)] <br>

**OmniGen2: Towards Instruction-Aligned Multimodal Generation** <br>
*Chenyuan Wu, Jiahao Wang, Pengfei Zheng, Ruiran Yan, Shitao Xiao, Xin Luo, Yueze Wang, Wanli Li, Xiyan Jiang, Yexin Liu, Junjie Zhou, Ziyi Xia, Ze Liu, Chaofan Li, Haoge Deng, Kun Luo, Bo Zhang, Jiajun Zhang, Dong Liu, Defu Lian, Xinlong Wang, Zhongyuan Wang, Tiejun Huang, Zheng Liu.* <br>
**Image Editing**, Beijing Academy of Artificial Intelligence & University of Science and Technology of China & Zhejiang University & Institute of Automation, Chinese Academy of Sciences <br>
CVPR 2026. [[PDF](https://arxiv.org/abs/2506.18871)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Wu_OmniGen2_Towards_Instruction-Aligned_Multimodal_Generation_CVPR_2026_paper.html)]
[[Project](https://vectorspacelab.github.io/OmniGen2)]
[[Github](https://github.com/VectorSpaceLab/OmniGen2)] <br>

**VINCIE: Unlocking In-context Image Editing from Video** <br>
*Leigang Qu, Feng Cheng, Ziyan Yang, Qi Zhao, Shanchuan Lin, Yichun Shi, Yicong Li, Wenjie Wang, Tat-Seng Chua, Lu Jiang.* <br>
**Image Editing**, National University of Singapore ByteDance Seed <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2506.10941)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/baf0fab890edc9dce805d7c518058712-Abstract-Conference.html)]
[[Project](https://vincie2025.github.io/)] <br>

**FlowAlign: Trajectory-Regularized, Inversion-Free Flow-based Image Editing** <br>
*Jeongsol Kim, Yeobin Hong, Jonghyun Park, Jong Chul YE.* <br>
**Image Editing**, KAIST <br>
ICLR 2026. [[PDF](https://arxiv.org/abs/2505.23145)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/c613667b7f11fbf478293266a156aabe-Abstract-Conference.html)] <br>

**SAEdit: Token-level control for continuous image editing via Sparse AutoEncoder** <br>
*Ronen Kamenetsky, Sara Dorfman, Daniel Garibi, Roni Paiss, Or Patashnik, Daniel Cohen-Or.* <br>
**Image Editing**, Tel Aviv University & Google DeepMind <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2510.05081)]
[[Project](https://ronen94.github.io/SAEdit/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3936)] <br>

**Query-Kontext: An Unified Multimodal Model for Image Generation and Editing** <br>
*Yuxin Song, Wenkai Dong, Shizun Wang, Qi Zhang, Song Xue, Tao Yuan, Hu Yang, Haocheng Feng, Hang Zhou, Xinyan Xiao, Jingdong Wang.* <br>
**Image Editing**, Baidu VIS & National University of Singapore <br>
ECCV 2026. [[PDF](https://arxiv.org/abs/2509.26641)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/3482)] <br>

## 2025

**ShoeFit: A New Dataset and Dual-image-stream DiT Framework for Virtual Footwear Try-On** <br>
*Yuhan Li, Zhiyu Jin, Yifan Tong, Wenxiang Shang, Benlei Cui, Xuanhong Chen, Ran Lin, Bingbing Ni.* <br>
**Virtual Try-On**, Alibaba Group & Shanghai Jiao Tong University <br>
NeurIPS 2025. [[Paper](https://papers.neurips.cc/paper_files/paper/2025/hash/2e9f9cde1b709281a06dd14f679e4c51-Abstract-Conference.html)]
[[arXiv](https://arxiv.org/abs/2610.18325)]
[[Project](https://colorful-liyu.github.io/ShoeFit/)] <br>

**QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing** <br>
*Tiancheng Shen, Zilong Huang, Xiangtai Li, Zhijie Lin, Jiyang Liu, Yitong Wang, Jiashi Feng, Ming-Hsuan Yang, Jun Hao Liew.* <br>
**Image Editing**, UC Merced & ByteDance Seed & ByteDance Intelligent Creation & CUHK <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2610.17829)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Shen_QK-Edit_Revisiting_Attention-based_Injection_in_MM-DiT_for_Image_and_Video_ICCV_2025_paper.html)] <br>

**Instruction-based Image Editing with Planning, Reasoning, and Generation** <br>
*Liya Ji, Chenyang Qi, Qifeng Chen.* <br>
**Image Editing**, HKUST <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2602.22624)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Ji_Instruction-based_Image_Editing_with_Planning_Reasoning_and_Generation_ICCV_2025_paper.html)] <br>

**Deterministic Image-to-Image Translation via Denoising Brownian Bridge Models with Dual Approximators** <br>
*Bohan Xiao, Peiyong Wang, Qisheng He, Ming Dong.* <br>
**Base I2I Translation** <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2512.23463)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Xiao_Deterministic_Image-to-Image_Translation_via_Denoising_Brownian_Bridge_Models_with_Dual_CVPR_2025_paper.html)]
[[Github](https://github.com/bohan95/dual-app-bridge)] <br>

**Multi-Attribute guided Thermal Face Image Translation based on Latent Diffusion Model** <br>
*Mingshu Cai, Osamu Yoshie, Yuya Ieiri.* <br>
**Infrared Image Translation**, Graduate School of Information, Production and Systems, Waseda University & Kitakyushu, Fukuoka, Japan <br>
IJCB 2025. [[PDF](https://arxiv.org/abs/2512.21032)] <br>

**Plasticine: A Traceable Diffusion Model for Medical Image Translation** <br>
*Tianyang Zhang, Xinxing Cheng, Jun Cheng, Shaoming Zheng, He Zhao, Huazhu Fu, Alejandro F Frangi, Jiang Liu, Jinming Duan.* <br>
**Medical Image Translation** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2512.18455)] <br>

**ContextDrag: Precise Drag-Based Image Editing via Context-Preserving Token Injection and Position-Aligned Attention** <br>
*Huiguo He, Pengyu Yan, Ziqi Yi, Weizhi Zhong, Zheng Liu, Yejun Tang, Huan Yang, Guanbin Li, Lianwen Jin.* <br>
**Image Editing**, Huiguo He, Pengyu Yan, Ziqi Yi, and Lianwen Jin are with the School of Electronic and Information Engineering, South China University of Technology, Guangzhou, China ( & Zheng Liu, Yejun Tang, and Huan Yang are with KlingAI Research, Kuaishou Technology, Beijing, China ( & Weizhi Zhong is with The University of Hong Kong, Hong Kong, China & Guanbin Li is with Shenzhen Loop Area Institute, Shenzhen, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2512.08477)] <br>

**DirectDrag: High-Fidelity, Mask-Free, Prompt-Free Drag-based Image Editing via Readout-Guided Feature Alignment** <br>
*Sheng-Hao Liao, Shang-Fu Chen, Tai-Ming Huang, Wen-Huang Cheng, Kai-Lung Hua.* <br>
**Image Editing**, National Taiwan University of Science and Technology & National Taiwan University & Microsoft Taiwan <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2512.03981)]
[[Project](https://frakw.github.io/DirectDrag/)]
[[Github](https://github.com/frakw/DirectDrag)] <br>

**Zero-Shot Video Translation and Editing with Frame Spatial-Temporal Correspondence** <br>
*Shuai Yang, Junxin Lin, Yifan Zhou, Ziwei Liu, Chen Change Loy.* <br>
**Video Style Transfer** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2512.03905)]
[[Github](https://github.com/Sunnycookies/FRESCO-v2)]
[[Project](https://williamyang1991.github.io/projects/FRESCOv2/)] <br>

**NumeriKontrol: Adding Numeric Control to Diffusion Transformers for Instruction-based Image Editing** <br>
*Zhenyu Xu, Xiaoqi Shen, Haotian Nan, Xinyu Zhang.* <br>
**Image Editing**, East China Normal University & South China University of Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.23105)] <br>

**Prompt-based Consistent Video Colorization** <br>
*Silvia Dani, Tiberio Uricchio, Lorenzo Seidenari.* <br>
**Image Colorization**, University of Firenze, Italy & University of Pisa, Italy <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.22330)] <br>

**MIRA: Multimodal Iterative Reasoning Agent for Image Editing** <br>
*Ziyun Zeng, Hang Hua, Jiebo Luo.* <br>
**Image Editing**, University of Rochester & MIT-IBM Watson AI Lab <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.21087)] <br>

**Inversion-Free Style Transfer with Dual Rectified Flows** <br>
*Yingying Deng, Xiangyu He, Fan Tang, Weiming Dong, Xucheng Yin.* <br>
**Image Style Transfer** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.20986)]
[[Github](https://github.com/HolmesShuan/Inversion-Free-Style-Transfer-with-Dual-Rectified-Flows)] <br>

**TReFT: Taming Rectified Flow Models For One-Step Image Translation** <br>
*Shengqian Li, Ming Gao, Yi Liu, Zuzeng Lin, Feng Wang, Feng Dai.* <br>
**Base I2I Translation**, University of Chinese Academy of Sciences, Beijing, China & Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China & CreateAI, Beijing, China & Beihang University, Beijing, China & Tianjin University, Tianjin, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.20307)] <br>

**Video4Edit: Viewing Image Editing as a Degenerate Temporal Process** <br>
*Xiaofan Li, Yanpeng Sun, Chenming Wu, Fan Duan, YuAn Wang, Weihao Bo, Yumeng Zhang, Dingkang Liang.* <br>
**Image Editing**, Baidu Inc <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.18131)] <br>

**OT-ALD: Aligning Latent Distributions with Optimal Transport for Accelerated Image-to-Image Translation** <br>
*Zhanpeng Wang, Shuting Cao, Yuhang Lu, Yuhan Li, Na Lei, Zhongxuan Luo.* <br>
**Base I2I Translation** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.11162)] <br>

**V-Shuffle: Zero-Shot Style Transfer via Value Shuffle** <br>
*Haojun Tang, Qiwei Lin, Tongda Xu, Lida Huang, Yan Wang.* <br>
**Image Style Transfer**, Tsinghua University & Dalian University of Technology & Beijing Institute of Radio Measurement <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.06365)]
[[Project](https://xinr-tang.github.io/V-Shuffle)] <br>

**Personalized Image Editing in Text-to-Image Diffusion Models via Collaborative Direct Preference Optimization** <br>
*Connor Dunlop, Matthew Zheng, Kavana Venkatesh, Pinar Yanardag.* <br>
**Image Editing**, Virginia Tech, Blacksburg, VA <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2511.05616)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/f503d55f1b711673591c88e943c59695-Abstract-Conference.html)]
[[Project](http://personalized-editing.github.io)] <br>

**Fractional Diffusion Bridge Models** <br>
*Gabriel Nobis, Maximilian Springenberg, Arina Belova, Rembert Daems, Christoph Knochenhauer, Manfred Opper, Tolga Birdal, Wojciech Samek.* <br>
**Base I2I Translation** <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2511.01795)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html)] <br>

**Understanding the Implicit User Intention via Reasoning with Large Language Model for Image Editing** <br>
*Yijia Wang, Yiqing Shen, Weiming Chen, Zhihai He.* <br>
**Image Editing**, Southern University of Science and Technology, Shenzhen, China & Johns Hopkins University, Baltimore, USA & Pengcheng Laboratory, Shenzhen, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.27335)]
[[Github](https://github.com/Jia-shao/Reasoning-Editing)] <br>

**SplitFlow: Flow Decomposition for Inversion-Free Text-to-Image Editing** <br>
*Sung-Hoon Yoon, Minghan Li, Gaspard Beaudouin, Congcong Wen, Muhammad Rafay Azhar, Mengyu Wang.* <br>
**Image Editing**, École des Ponts, Institut Polytechnique de Paris & Harvard AI and Robotics Lab, Harvard University & New York University Abu Dhabi & Kempner Institute for the Study of Natural and Artificial Intelligence, Harvard University <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2510.25970)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/e124f1547f7ac87e33d348b827d4291b-Abstract-Conference.html)]
[[Github](https://github.com/Harvard-AI-and-Robotics-Lab/SplitFlow)] <br>

**LGCC: Enhancing Flow Matching Based Text-Guided Image Editing with Local Gaussian Coupling and Context Consistency** <br>
*Fangbing Liu, Pengfei Duan, Wen Li, Yi He.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2511.01894)] <br>

**Group Relative Attention Guidance for Image Editing** <br>
*Xuanpu Zhang, Xuesong Niu, Ruidong Chen, Dan Song, Jianhao Zeng, Penghui Du, Haoxiang Cao, Kai Wu, An-an Liu.* <br>
**Image Editing**, Tianjin University & Kolors Team, Kuaishou Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.24657)]
[[Github](https://github.com/little-misfit/GRAG-Image-Editing)]
[[Project](https://little-misfit.github.io/GRAG-Image-Editing/)] <br>

**Towards General Modality Translation with Contrastive and Predictive Latent Diffusion Bridge** <br>
*Nimrod Berman, Omkar Joglekar, Eitan Kosman, Dotan Di Castro, Omri Azencot.* <br>
**Base I2I Translation**, Bosch AI Center & Ben-Gurion University of the Negev & Technical University of Munich <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2510.20819)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/d5470483dd38f71f7bd9e68ce1b94145-Abstract-Conference.html)] <br>

**Uniworld-V2: Reinforce Image Editing with Diffusion Negative-aware Finetuning and MLLM Implicit Feedback** <br>
*Zongjian Li, Zheyuan Liu, Qihui Zhang, Bin Lin, Feize Wu, Shenghai Yuan, Zhiyuan Yan, Yang Ye, Wangbo Yu, Yuwei Niu, Shaodong Wang, Xinhua Cheng, Li Yuan.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.16888)]
[[Github](https://github.com/PKU-YuanGroup/Uniworld)]
[[Model](https://huggingface.co/collections/chestnutlzj/edit-r1-68dc3ecce74f5d37314d59f4)] <br>

**Diffusion Bridge Networks Simulate Clinical-grade PET from MRI for Dementia Diagnostics** <br>
*Yitong Li, Ralph Buchert, Benita Schmitz-Koep, Timo Grimmer, Björn Ommer, Dennis M. Hedderich, Igor Yakushev, Christian Wachinger.* <br>
**Medical Image Translation**, Lab for AI in Medical Imaging, Institute for Diagnostic and Interventional Radiology, School of Medicine and Health, Technical University of Munich (TUM), Munich, 81675, Germany & Munich Center for Machine Learning (MCML), Munich, Germany & Department of Nuclear Medicine, University Medical Center Hamburg-Eppendorf, Hamburg, 20246, Germany & Department of Neuroradiology, TUM University Hospital, School of Medicine and Health, Munich, 81675, Germany & Department of Neurology, TUM University Hospital, School of Medicine and Health, Munich, 81675, Germany & CompVis, Ludwig-Maximilians-University Munich (LMU), Munich, 80539, Germany & Department of Nuclear Medicine, TUM University Hospital, School of Medicine and Health, Munich, 81675, Germany <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.15556)]
[[Github](https://github.com/Yiiitong/SiM2P)] <br>

**Generating healthy counterfactuals with denoising diffusion bridge models** <br>
*Ana Lawry Aguila, Peirong Liu, Marina Crespo Aguirre, Juan Eugenio Iglesias.* <br>
**Medical Image Translation**, Athinoula A. Martinos Center for Biomedical ImagingMassachusetts General Hospital and Harvard Medical School, Boston, USA & ETH Zurich, Zurich, Switzerland & Computer Science & Artificial Intelligence LabMassachusetts Institute of Technology, Boston, USA & Hawkes Institute, University College London, London, UK <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.13684)] <br>

**SceneTextStylizer: A Training-Free Scene Text Style Transfer Framework with Diffusion Model** <br>
*Honghui Yuan, Keiji Yanai.* <br>
**Image Style Transfer**, The University of Electro-Communications & Tokyo <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.10910)] <br>

**InstructUDrag: Joint Text Instructions and Object Dragging for Interactive Image Editing** <br>
*Haoran Yu, Yi Shi.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.08181)] <br>

**Once Is Enough: Lightweight DiT-Based Video Virtual Try-On via One-Time Garment Appearance Injection** <br>
*Yanjie Pan, Qingdong He, Lidong Wang, Bo Peng, Mingmin Chi.* <br>
**Virtual Try-On** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.07654)] <br>

**StyleKeeper: Prevent Content Leakage using Negative Visual Query Guidance** <br>
*Jaeseok Jeong, Junho Kim, Gayoung Lee, Yunjey Choi, Youngjung Uh.* <br>
**Image Style Transfer**, Yonsei University & NAVER AI Lab <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2510.06827)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Jeong_StyleKeeper_Prevent_Content_Leakage_using_Negative_Visual_Query_Guidance_ICCV_2025_paper.html)]
[[Github](https://github.com/naver-ai/StyleKeeper)] <br>

**Efficient High-Resolution Image Editing with Hallucination-Aware Loss and Adaptive Tiling** <br>
*Young D. Kwon, Abhinav Mehrotra, Malcolm Chadwick, Alberto Gil Ramos, Sourav Bhattacharya.* <br>
**Image Editing**, Samsung AI Center-Cambridge <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.06295)] <br>

**Contrastive-SDE: Guiding Stochastic Differential Equations with Contrastive Learning for Unpaired Image-to-Image Translation** <br>
*Venkata Narendra Kotyada, Revanth Eranki, Nagesh Bhattu Sristy.* <br>
**Base I2I Translation**, Department of Computer Science & Engineering & National Institute of Technology & Andhra Pradesh <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2510.03821)] <br>

**DiT-VTON: Diffusion Transformer Framework for Unified Multi-Category Virtual Try-On and Virtual Try-All with Integrated Image Editing** <br>
*Qi Li, Shuwen Qiu, Julien Han, Xingzi Xu, Mehmet Saygin Seyfioglu, Kee Kiat Koo, Karim Bouyarmane.* <br>
**Virtual Try-On**, Amazon & University of California, Los Angeles (UCLA) & Duke University <br>
CVPR 2025 Workshops (AI4CC). [[PDF](https://arxiv.org/abs/2510.04797)]
[[Project](https://dit-vton.github.io/DiT-VTON/)] <br>

**Editable Noise Map Inversion: Encoding Target-image into Noise For High-Fidelity Image Manipulation** <br>
*Mingyu Kang, Yong Suk Choi.* <br>
**Image Editing**, Department of Artificial Intelligence, University of Hanyang, Seoul, Korea & Department of Computer Science, University of Hanyang, Seoul, Korea <br>
ICML 2025. [[PDF](https://arxiv.org/abs/2509.25776)] <br>

**ART-VITON: Measurement-Guided Latent Diffusion for Artifact-Free Virtual Try-On** <br>
*Junseo Park, Hyeryung Jang.* <br>
**Virtual Try-On**, Department of Computer Science & Artificial Intelligence, Dongguk University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.25749)] <br>

**ThermalGen: Style-Disentangled Flow-Based Generative Models for RGB-to-Thermal Image Translation** <br>
*Jiuhong Xiao, Roshan Nayak, Ning Zhang, Daniel Tortei, Giuseppe Loianno.* <br>
**Infrared Image Translation**, New York University & Technology Innovation Institute & University of California, Berkeley <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2509.24878)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/2f9e10c28c4052570ef9e39cc4dd69b9-Abstract-Conference.html)]
[[Project](http://xjh19971.github.io/ThermalGen)] <br>

**FlashEdit: Decoupling Speed, Structure, and Semantics for Precise Image Editing** <br>
*Junyi Wu, Zhiteng Li, Haotong Qin, Yulun Zhang, Xiaokang Yang.* <br>
**Image Editing**, Shanghai Jiao Tong University ETH Zürich <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.22244)]
[[Github](https://github.com/JunyiWuCode/FlashEdit)] <br>

**Comparative Analysis of GAN and Diffusion for MRI-to-CT translation** <br>
*Emily Honey, Anders Helbo, Jens Petersen.* <br>
**Medical Image Translation**, Department of Computer Science, University of Copenhagen, Copenhagen, Denmark & Department of Oncology, Rigshospitalet, Copenhagen, Denmark <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.22049)] <br>

**TDEdit: A Unified Diffusion Framework for Text-Drag Guided Image Manipulation** <br>
*Qihang Wang, Yaxiong Wang, Lechao Cheng, Zhun Zhong.* <br>
**Image Editing**, Hefei University of Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.21905)] <br>

**FreeInsert: Personalized Object Insertion with Geometric and Style Control** <br>
*Yuhong Zhang, Han Wang, Yiwen Wang, Rong Xie, Li Song.* <br>
**Image Editing**, Shanghai Jiao Tong University, Shanghai, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.20756)] <br>

**Clothing agnostic Pre-inpainting Virtual Try-ON** <br>
*Sehyun Kim, Hye Jun Lee, Jiwoo Lee, Taemin Lee.* <br>
**Virtual Try-On**, Department of Artificial Intelligence and Software, Kangwon National University, Korea & Department of Electronic and AI System Engineering, Kangwon National University, Korea <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.17654)]
[[Github](https://github.com/DevChoco/CAP-VTON)] <br>

**AutoEdit: Automatic Hyperparameter Tuning for Image Editing** <br>
*Chau Pham, Quan Dao, Mahesh Bhosale, Yunjie Tian, Dimitris Metaxas, DAVID DOERMANN.* <br>
**Image Editing**, University at Buffalo & Rutgers University <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2509.15031)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/092c2d45005ea2db40fc24c470663416-Abstract-Conference.html)]
[[Github](https://github.com/chaupham1709/AutoEdit.git)] <br>

**DEFT-VTON: Efficient Virtual Try-On with Consistent Generalised H-Transform** <br>
*Xingzi Xu, Qi Li, Shuwen Qiu, Julien Han, Karim Bouyarmane.* <br>
**Virtual Try-On**, Amazon & University of California, Los Angeles (UCLA) & Duke University <br>
CVPR 2025 Workshops. [[PDF](https://arxiv.org/abs/2509.13506)]
[[Project](https://deft-vton.github.io/)] <br>

**Beyond Sliders: Mastering the Art of Diffusion-based Image Manipulation** <br>
*Yufei Tang, Daiheng Gao, Pingyu Wu, Wenbo Zhou, Bang Zhang, Weiming Zhang.* <br>
**Image Editing**, FUYAO University Of Science And Technology & University of Science and Technology of China & Anhui Province Key Laboratory of Digital Security & Alibaba TongYi Lab <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.11213)] <br>

**LADB: Latent Aligned Diffusion Bridges for Semi-Supervised Domain Translation** <br>
*Xuqin Wang, Tao Wu, Yanfeng Zhang, Lu Liu, Dong Wang, Mingwei Sun, Yongliang Wang, Niclas Zeller, Daniel Cremers.* <br>
**Base I2I Translation**, Huawei Technologies & Technical University of Munich & Karlsruhe University of Applied Sciences <br>
DAGM GCPR 2025. [[PDF](https://arxiv.org/abs/2509.08628)] <br>

**LUIVITON: Learned Universal Interoperable VIrtual Try-ON** <br>
*Cong Cao, Xianhang Cheng, Jingyuan Liu, Yujian Zheng, Zhenhui Lin, Ren Li, Meriem Chkir, Hao Li.* <br>
**Virtual Try-On**, MBZUAI, Abu Dhabi, United Arab Emirates & The University of Tokyo, Tokyo, Japan & SUSTech, China & Pinscreen, USA & MBZUAI, United Arab Emirates <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.05030)]
[[Project](https://cao-cong0.github.io/LUIVITON-Learned-Universal-Interoperable-VIrtual-Try-ON/)] <br>

**Neural Scene Designer: Self-Styled Semantic Image Manipulation** <br>
*Jianman Lin, Tianshui Chen, Chunmei Qing, Zhijing Yang, Shuangping Huang, Yuheng Ren, Liang Lin.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2509.01405)] <br>

**FastFit: Accelerating Multi-Reference Virtual Try-On via Cacheable Diffusion Models** <br>
*Zheng Chong, Yanwei Lei, Shiyue Zhang, Zhuandi He, Zhen Wang, Xujie Zhang, Xiao Dong, Yiling Wu, Dongmei Jiang, Xiaodan Liang.* <br>
**Virtual Try-On**, Sun Yat-sen University & LavieAI & Pengcheng Laboratory <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.20586)]
[[Github](https://github.com/Zheng-Chong/FastFit)] <br>

**USO: Unified Style and Subject-Driven Generation via Disentangled and Reward Learning** <br>
*Shaojin Wu, Mengqi Huang, Yufeng Cheng, Wenxu Wu, Jiahe Tian, Yiming Luo, Fei Ding, Qian He.* <br>
**Image Style Transfer**, ByteDance <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.18966)]
[[Github](https://github.com/bytedance/USO)]
[[Project](https://bytedance.github.io/USO/)] <br>

**SpotEdit: Evaluating Visually-Guided Image Editing Methods** <br>
*Sara Ghazanfari, Wei-An Lin, Haitong Tian, Ersin Yumer.* <br>
**Dataset / Evaluation**, New York University, US & Adobe Inc <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.18159)]
[[Github](https://github.com/SaraGhazanfari/SpotEdit)] <br>

**JCo-MVTON: Jointly Controllable Multi-Modal Diffusion Transformer for Mask-Free Virtual Try-on** <br>
*Aowen Wang, Wei Li, Hao Luo, Mengxing Ao, Chenyu Zhu, Xinyang Li, Fan Wang.* <br>
**Virtual Try-On** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.17614)]
[[Github](https://github.com/damo-cv/JCo-MVTON)] <br>

**PosBridge: Multi-View Positional Embedding Transplant for Identity-Aware Image Editing** <br>
*Peilin Xiong, Junwen Chen, Honghui Yuan, Keiji Yanai.* <br>
**Image Editing**, Department of Informatics The University of Electro-Communications Tokyo, Japan <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.17302)] <br>

**Styleclone: Face Stylization with Diffusion Based Data Augmentation** <br>
*Neeraj Matiyali, Siddharth Srivastava, Gaurav Sharma.* <br>
**Image Style Transfer** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.17045)] <br>

**Leveraging Diffusion Models for Stylization using Multiple Style Images** <br>
*Dan Ruta, Abdelaziz Djelouah, Raphael Ortiz, Christopher Schroers.* <br>
**Image Style Transfer**, DisneyResearch|Studios <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.12784)] <br>

**Single-Reference Text-to-Image Manipulation with Dual Contrastive Denoising Score** <br>
*Syed Muhmmad Israr, Feng Zhao.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.12718)] <br>

**DualFit: A Two-Stage Virtual Try-On via Warping and Synthesis** <br>
*Minh Tran, Johnmark Clements, Annie Prasanna, Tri Nguyen, Ngan Le.* <br>
**Virtual Try-On**, University of Arkansas & Coupang, Inc <br>
ICCV 2025 Workshops (Retail Vision). [[PDF](https://arxiv.org/abs/2508.12131)] <br>

**SPG: Style-Prompting Guidance for Style-Specific Content Creation** <br>
*Qian Liang, Zichong Chen, Yang Zhou, Hui Huang.* <br>
**Image Style Transfer** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.11476)]
[[Github](https://github.com/Rumbling281441/SPG)] <br>

**MangaDiT: Reference-Guided Line Art Colorization with Hierarchical Attention in Diffusion Transformers** <br>
*Qianru Qiu, Jiafeng Mao, Kento Masui, Xueting Wang.* <br>
**Image Colorization** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.09709)] <br>

**MuGa-VTON: Multi-Garment Virtual Try-On via Diffusion Transformers with Prompt Customization** <br>
*Ankan Deria, Dwarikanath Mahapatra, Behzad Bozorgtabar, Mohna Chakraborty, Snehashis Chakraborty, Sudipta Roy.* <br>
**Virtual Try-On** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.08488)] <br>

**Exploring Multimodal Diffusion Transformers for Enhanced Prompt-based Image Editing** <br>
*Joonghyuk Shin, Alchan Hwang, Yujin Kim, Daneul Kim, Jaesik Park.* <br>
**Image Editing**, Seoul National University <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2508.07519)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Shin_Exploring_Multimodal_Diffusion_Transformers_for_Enhanced_Prompt-based_Image_Editing_ICCV_2025_paper.html)] <br>

**InstantEdit: Text-Guided Few-Step Image Editing with Piecewise Rectified Flow** <br>
*Yiming Gong, Zhen Zhu, Minjia Zhang.* <br>
**Image Editing**, University of Illinois at Urbana-Champaign <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2508.06033)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Gong_InstantEdit_Text-Guided_Few-Step_Image_Editing_with_Piecewise_Rectified_Flow_ICCV_2025_paper.html)]
[[Github](https://github.com/Supercomputing-System-AI-Lab/InstantEdit)] <br>

**Voost: A Unified and Scalable Diffusion Transformer for Bidirectional Virtual Try-On and Try-Off** <br>
*Seungyong Lee, Jeong-gi Kwak.* <br>
**Virtual Try-On**, NXN Labs & University of British Columbia <br>
SIGGRAPH Asia 2025. [[PDF](https://arxiv.org/abs/2508.04825)]
[[Project](https://nxnai.github.io/Voost/)] <br>

**LORE: Latent Optimization for Precise Semantic Control in Rectified Flow-based Image Editing** <br>
*Liangyang Ouyang, Jiafeng Mao.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.03144)]
[[Github](https://github.com/oyly16/LORE)] <br>

**DreamVVT: Mastering Realistic Video Virtual Try-On in the Wild via a Stage-Wise Diffusion Transformer Framework** <br>
*Tongchun Zuo, Zaiyu Huang, Shuliang Ning, Ente Lin, Chao Liang, Zerong Zheng, Jianwen Jiang, Yuan Zhang, Mingyuan Gao, Xin Dong.* <br>
**Virtual Try-On**, ByteDance Intelligent Creation & Shenzhen International Graduate School, Tsinghua <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.02807)]
[[Project](https://virtu-lab.github.io/)] <br>

**Optimal Transport for Rectified Flow Image Editing: Unifying Inversion-Based and Direct Methods** <br>
*Marian Lupascu, Mihai-Sorin Stupariu.* <br>
**Image Editing**, University of Bucharest <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.02363)]
[[Github](https://github.com/marianlupascu/OT-RF)] <br>

**Qwen-Image Technical Report** <br>
*Chenfei Wu, Jiahao Li, Jingren Zhou, Junyang Lin, Kaiyuan Gao, Kun Yan, Sheng-ming Yin, Shuai Bai, Xiao Xu, Yilei Chen, Yuxiang Chen, Zecheng Tang, Zekai Zhang, Zhengyi Wang, An Yang, Bowen Yu, Chen Cheng, Dayiheng Liu, Deqing Li, Hang Zhang, Hao Meng, Hu Wei, Jingyuan Ni, Kai Chen, Kuan Cao, Liang Peng, Lin Qu, Minggang Wu, Peng Wang, Shuting Yu, Tingkun Wen, Wensen Feng, Xiaoxiao Xu, Yi Wang, Yichang Zhang, Yongqiang Zhu, Yujia Wu, Yuxuan Cai, Zenan Liu.* <br>
**Image Editing**, Qwen Team, Alibaba Group <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.02324)]
[[Github](https://github.com/QwenLM/Qwen-Image)]
[[Model](https://huggingface.co/Qwen/Qwen-Image)] <br>

**Subject or Style: Adaptive and Training-Free Mixture of LoRAs** <br>
*Jia-Chen Zhang, Yu-Jie Xiong.* <br>
**Image Style Transfer**, School of Electronic and Electrical Engineering & Shanghai University of Engineering Science <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.02165)] <br>

**StyDeco: Unsupervised Style Transfer with Distilling Priors and Semantic Decoupling** <br>
*Yuanlin Yang, Quanjian Song, Zhexian Gao, Ge Wang, Shanshan Li, Xiaoyan Zhang.* <br>
**Image Style Transfer** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2508.01215)]
[[Github](https://github.com/QuanjianSong/StyDeco)] <br>

**Training-free Geometric Image Editing on Diffusion Models** <br>
*Hanshen Zhu, Zhen Zhu, Kaile Zhang, Yiming Gong, Yuliang Liu, Xiang Bai.* <br>
**Image Editing**, Huazhong University of Science and Technology & University of Illinois at Urbana-Champaign <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2507.23300)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Training-free_Geometric_Image_Editing_on_Diffusion_Models_ICCV_2025_paper.html)]
[[Github](https://github.com/CIawevy/FreeFine)] <br>

**AnimeColor: Reference-based Animation Colorization with Diffusion Transformers** <br>
*Yuhong Zhang, Liyao Wang, Han Wang, Danni Wu, Zuzeng Lin, Feng Wang, Li Song.* <br>
**Image Colorization**, Shanghai Jiao Tong University, Shanghai, China & Tianjin University, Tianjin, China & Communication University of China, Beijing, China & CreateAI, Beijing, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2507.20158)]
[[Github](https://github.com/IamCreateAI/AnimeColor)] <br>

**RealDeal: Enhancing Realism and Details in Brain Image Generation via Image-to-Image Diffusion Models** <br>
*Shen Zhu, Yinzhu Jin, Tyler Spears, Ifrah Zawar, P. Thomas Fletcher.* <br>
**Medical Image Translation**, University of Virginia, Charlottesville, VA, USA <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2507.18830)] <br>

**OmniVTON: Training-Free Universal Virtual Try-On** <br>
*Zhaotong Yang, Yuhui Li, Shengfeng He, Xinzhe Li, Yangyang Xu, Junyu Dong, Yong Du.* <br>
**Virtual Try-On**, Ocean University of China & Singapore Management University, Harbin Institute of Technology (Shenzhen) <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2507.15037)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_OmniVTON_Training-Free_Universal_Virtual_Try-On_ICCV_2025_paper.html)]
[[Github](https://github.com/Jerome-Young/OmniVTON)] <br>

**Human-Guided Shade Artifact Suppression in CBCT-to-MDCT Translation via Schrödinger Bridge with Conditional Diffusion** <br>
*Sung Ho Kang, Hyun-Cheol Park.* <br>
**Medical Image Translation**, National Institute for Mathematical Sciences, Yuseong-gu, Daejeon 34047, Republic of Korea & Department of Computer Engineering, Korea National University of TransportationChungju-si, Chungcheongbuk-do 27469, Republic of Korea <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2507.11025)] <br>

**When Schrodinger Bridge Meets Real-World Image Dehazing with Unpaired Training** <br>
*Yunwei Lan, Zhigao Cui, Xin Luo, Chang Liu, Nian Wang, Menglin Zhang, Yanzhao Su, Dong Liu.* <br>
**Image Restoration**, Rocket Force University of Engineering, Xi’an 710025, China & MOE Key Laboratory of Brain-Inspired Intelligent Perception and CognitionUniversity of Science and Technology of China, Hefei 230093, China <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2507.09524)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Lan_When_Schrodinger_Bridge_Meets_Real-World_Image_Dehazing_with_Unpaired_Training_ICCV_2025_paper.html)]
[[Github](https://github.com/ywxjm/DehazeSB)] <br>

**Neural-Driven Image Editing** <br>
*Pengfei Zhou, Jie Xia, Xiaopeng Peng, Wangbo Zhao, Zilong Ye, Zekai Li, Suorong Yang, Jiadong Pan, Yuanxiang Chen, Ziqiao Wang, Kai Wang, Qian Zheng, Xiaojun Chang, Gang Pan, Shurong Dong, Kaipeng Zhang, Yang You.* <br>
**Image Editing**, ZJU & NUS & Hangzhou RongNao & NJU & USTC & Shanghai AI Lab & RIT & SII <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2507.05397)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/9138f908b3cfe807ee3288dbfd1156d3-Abstract-Conference.html)]
[[Project](https://loongx1.github.io)] <br>

**Beyond Simple Edits: X-Planner for Complex Instruction-Based Image Editing** <br>
*Chun-Hsiao Yeh, Yilin Wang, Nanxuan Zhao, Richard Zhang, Yuheng Li, Yi Ma, Krishna Kumar Singh.* <br>
**Image Editing**, UC Berkeley & Adobe & HKU <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2507.05259)]
[[Project](https://danielchyeh.github.io/x-planner/)] <br>

**QR-LoRA: Efficient and Disentangled Fine-tuning via QR Decomposition for Customized Generation** <br>
*Jiahui Yang, Yongjia Ma, Donglin Di, Jianxun Cui, Hao Li, Wei Chen, Yan Xie, Xun Yang, Wangmeng Zuo.* <br>
**Image Style Transfer**, Harbin Institute of Technology & Li Auto & University of Science and Technology of China <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2507.04599)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_QR-LoRA_Efficient_and_Disentangled_Fine-tuning_via_QR_Decomposition_for_Customized_ICCV_2025_paper.html)]
[[Project](https://luna-ai-lab.github.io/QR-LoRA/)] <br>

**S$^2$Edit: Text-Guided Image Editing with Precise Semantic and Spatial Control** <br>
*Xudong Liu, Zikun Chen, Ruowei Jiang, Ziyi Wu, Kejia Yin, Han Zhao, Parham Aarabi, Igor Gilitschenski.* <br>
**Image Editing**, Department of Computer Science, University of Toronto & ModiFace Inc & Department of Computer Science, University of Illinois Urbana-Champaign <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2507.04584)] <br>

**Domain Generalizable Portrait Style Transfer** <br>
*Xinbo Wang, Wenju Xu, Qing Zhang, Wei-Shi Zheng.* <br>
**Image Style Transfer**, Sun Yat-sen University & Amazon <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2507.04243)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Domain_Generalizable_Portrait_Style_Transfer_ICCV_2025_paper.html)]
[[Github](https://github.com/wangxb29/DGPST)] <br>

**System-Embedded Diffusion Bridge Models** <br>
*Bartlomiej Sobieski, Matthew Tivnan, Yuang Wang, Siyeop yoon, Pengfei Jin, Dufan Wu, Quanzheng Li, Przemyslaw Biecek.* <br>
**Base I2I Translation**, Harvard University & Massachusetts General Hospital & University of Warsaw & Warsaw University of Technology <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2506.23726)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/18b0b4c788c8f2cf6c2943b989ad18c8-Abstract-Conference.html)] <br>

**DiffFit: Disentangled Garment Warping and Texture Refinement for Virtual Try-On** <br>
*Xiang Xu.* <br>
**Virtual Try-On**, China Jiliang University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.23295)] <br>

**Video Virtual Try-on with Conditional Diffusion Transformer Inpainter** <br>
*Cheng Zou, Senlin Cheng, Bolei Xu, Dandan Zheng, Xiaobo Li, Jingdong Chen, Ming Yang.* <br>
**Virtual Try-On**, Ant Group <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.21270)] <br>

**Improving Diffusion-Based Image Editing Faithfulness via Guidance and Scheduling** <br>
*Hansam Cho, Seoung Bum Kim.* <br>
**Image Editing**, Korea University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.21045)] <br>

**ThermalDiffusion: Visual-to-Thermal Image-to-Image Translation for Autonomous Navigation** <br>
*Shruti Bansal, Wenshan Wang, Yifei Liu, Parv Maheshwari.* <br>
**Infrared Image Translation**, Carnegie Mellon University <br>
ICRA 2025 Workshops (TIRO). [[PDF](https://arxiv.org/abs/2506.20969)] <br>

**Style Transfer: A Decade Survey** <br>
*Tianshan Zhang, Hao Tang.* <br>
**Survey**, Dalian Jiaotong University & Peking University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.19278)] <br>

**Inverse-and-Edit: Effective and Fast Image Editing by Cycle Consistency Models** <br>
*Ilia Beletskii, Andrey Kuznetsov, Aibek Alanov.* <br>
**Image Editing**, HSE University, AIRI & AIRI, Sber, Innopolis <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.19103)]
[[Github](https://github.com/ControlGenAI/Inverse-and-Edit)] <br>

**GANs vs. Diffusion Models for virtual staining with the HER2match dataset** <br>
*Pascal Klöckner, José Teixeira, Diana Montezuma, Jaime S. Cardoso, Hugo M. Horlings, Sara P. Oliveira.* <br>
**Virtual Staining**, The Netherlands Cancer Institute, Amsterdam, The Netherlands & Faculty of Engineering, University of Porto, Porto, Portugal & IMP Diagnostics, Porto, Portugal <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.18484)] <br>

**CPAM: Context-Preserving Adaptive Manipulation for Zero-Shot Real Image Editing** <br>
*Dinh-Khoi Vo, Thanh-Toan Do, Tam V. Nguyen, Minh-Triet Tran, Trung-Nghia Le.* <br>
**Image Editing**, University of Science, VNU-HCM & Monash University & University of Dayton <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.18438)]
[[Project](https://vdkhoi20.github.io/CPAM)] <br>

**FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space** <br>
*Black Forest Labs, Stephen Batifol, Andreas Blattmann, Frederic Boesel, Saksham Consul, Cyril Diagne, Tim Dockhorn, Jack English, Zion English, Patrick Esser, Sumith Kulal, Kyle Lacey, Yam Levi, Cheng Li, Dominik Lorenz, Jonas Müller, Dustin Podell, Robin Rombach, Harry Saini, Axel Sauer, Luke Smith.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.15742)] <br>

**AttentionDrag: Exploiting Latent Correlation Knowledge in Pre-trained Diffusion Models for Image Editing** <br>
*Biao Yang, Muqi Huang, Yuhui Zhang, Yun Xiong, Kun Zhou, Xi Chen, Shiyang Zhou, Huishuai Bao, Chuan Li, Feng Shi, Hualei Liu.* <br>
**Image Editing**, Shanghai Key Laboratory of Data Science, School of Computer Science, Fudan University & Rajax Network Technology (ele.me), Alibaba Group <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.13301)] <br>

**Only-Style: Stylistic Consistency in Image Generation without Content Leakage** <br>
*Tilemachos Aravanis, Panagiotis Filntisis, Petros Maragos, George Retsinas.* <br>
**Image Style Transfer**, School of Electrical & Computer Engineering, National Technical University of Athens, Greece & Robotics Institute, Athena Research Center, & Maroussi, Greece & HERON - Center of Excellence in Robotics, Athens, Greece <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.09916)]
[[Project](https://tilemahosaravanis.github.io/Only-Style-PP/)] <br>

**Training-Free Diffusion Framework for Stylized Image Generation with Identity Preservation** <br>
*Mohammad Ali Rezaei, Helia Hajikazem, Saeed Khanehgir, Mahdi Javanmardi.* <br>
**Image Style Transfer**, Computer Vision Group, Part AI Research Center, Tehran, Iran & Department of Computer Engineering, Amirkabir University of Technology, Tehran, Iran <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.06802)] <br>

**ChronoTailor: Harnessing Attention Guidance for Fine-Grained Video Virtual Try-On** <br>
*Jinjuan Wang, Wenzhang Sun, Ming Li, Yun Zheng, Fanyao Li, Zhulin Tao, Donglin Di, Hao Li, Wei Chen, Xianglin Huang.* <br>
**Virtual Try-On**, Communication University of China & Li Auto <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.05858)] <br>

**SeedEdit 3.0: Fast and High-Quality Generative Image Editing** <br>
*Peng Wang, Yichun Shi, Xiaochen Lian, Zhonghua Zhai, Xin Xia, Xuefeng Xiao, Weilin Huang, Jianchao Yang.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.05083)] <br>

**Image Editing As Programs with Diffusion Models** <br>
*Yujia Hu, Songhua Liu, Zhenxiong Tan, Xingyi Yang, Xinchao Wang.* <br>
**Image Editing**, National University of Singapore <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2506.04158)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/1aa1fde3661b23ba9b043082069fd144-Abstract-Conference.html)]
[[Github](https://github.com/YujiaHu1109/IEAP)] <br>

**SSIMBaD: Sigma Scaling with SSIM-Guided Balanced Diffusion for AnimeFace Colorization** <br>
*Junpyo Seo, HanbinKoo, jieun yook, Byung-Ro Moon.* <br>
**Image Colorization**, Department of Computer Science & Seoul National University <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2506.04283)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/b6e928d867dc272be2ba2d25ecb9e1ab-Abstract-Conference.html)]
[[Github](https://github.com/Giventicket/SSIMBaD-Sigma-Scaling-with-SSIM-Guided-Balanced-Diffusion-for-AnimeFace-Colorization)] <br>

**ByteMorph: Benchmarking Instruction-Guided Image Editing with Non-Rigid Motions** <br>
*Di Chang, Mingdeng Cao, Yichun Shi, Bo Liu, Shengqu Cai, Shijie Zhou, Weilin Huang, Gordon Wetzstein, Mohammad Soleymani, Peng Wang.* <br>
**Dataset / Evaluation**, ByteDance Seed & University of Southern California & University of Tokyo & University of California Berkeley & Stanford University & University of California Los Angeles <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.03107)]
[[Project](https://boese0601.github.io/bytemorph)]
[[Dataset](https://huggingface.co/datasets/ByteDance-Seed/BM-6M)]
[[Dataset](https://huggingface.co/datasets/ByteDance-Seed/BM-Bench)]
[[Github](https://github.com/ByteDance-Seed/BM-code)]
[[Demo](https://huggingface.co/spaces/Boese0601/ByteMorph-Demo)] <br>

**DCI: Dual-Conditional Inversion for Boosting Diffusion-Based Image Editing** <br>
*Zixiang Li, Haoyu Wang, Wei Wang, Chuangchuang Tan, Yunchao Wei, Yao Zhao.* <br>
**Image Editing**, Institute of Information Science, Beijing Jiaotong University & Visual Intelligence +X International Cooperation Joint Laboratory of MOE <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2506.02560)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/00da4ead8d212a0bd5818a83bf380c9e-Abstract-Conference.html)] <br>

**IMAGHarmony: Controllable Image Editing with Consistent Object Quantity and Layout** <br>
*Fei Shen, Yutong Gao, Jian Yu, Xiaoyu Du, Jinhui Tang.* <br>
**Image Editing**, NExT++ Research Centre, National University of Singapore, Singapore & Nanjing University of Science and Technology, Nanjing, China & Nanjing Forestry University, Nanjing, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.01949)]
[[Github](https://github.com/muzishen/IMAGHarmony)] <br>

**DS-VTON: An Enhanced Dual-Scale Coarse-to-Fine Framework for Virtual Try-On** <br>
*Xianbing Sun, Yan Hong, Jiahui Zhan, Jun Lan, Huijia Zhu, Weiqiang Wang, Liqing Zhang, Jianfu Zhang.* <br>
**Virtual Try-On**, Shanghai Jiao Tong University & Ant Group <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.00908)]
[[Project](https://fu61.github.io/ds-vton.github.io/)] <br>

**MR2US-Pro: Prostate MR to Ultrasound Image Translation and Registration Based on Diffusion Models** <br>
*Xudong Ma, Nantheera Anantrasirichai, Stefanos Bolomytis, Alin Achim.* <br>
**Medical Image Translation**, Visual Information Laboratory, University of Bristol, Bristol, UK & Southmead Hospital, North Bristol NHS Trust, UK <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.00591)] <br>

**Cora: Correspondence-aware image editing using few step diffusion** <br>
*Amirhossein Alimohammadi, Aryan Mikaeili, Sauradip Nag, Negar Hassanpour, Andrea Tagliasacchi, Ali Mahdavi-Amiri.* <br>
**Image Editing**, Simon Fraser University, Canada & Huawei, Canada & University of Toronto, Canada & Google DeepMind, Canada <br>
SIGGRAPH 2025. [[PDF](https://arxiv.org/abs/2505.23907)]
[[Project](https://cora-edit.github.io/)]
[[Github](https://github.com/alimohammadiamirhossein/cora)] <br>

**Training Free Stylized Abstraction** <br>
*Aimon Rahman, Kartik Narayan, Vishal M. Patel.* <br>
**Image Style Transfer**, Johns Hopkins University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.22663)]
[[Project](https://kartik-3004.github.io/TF-SA/)] <br>

**Collaborative Learning for Unsupervised Multimodal Remote Sensing Image Registration: Integrating Self-Supervision and MIM-Guided Diffusion-Based Image Translation** <br>
*Xiaochen Wei, Weiwei Guo, Wenxian Yu.* <br>
**SAR Image Translation**, organization=Shanghai Key Laboratory of Intelligent Sensing and Recognition, city=Shanghai, postcode=200240, country=China & organization=School of Sensing Science and Engineering, city=Shanghai, postcode=200240, country=China & organization=Shanghai Jiao Tong University, city=Shanghai, postcode=200240, country=China & organization=Center for Digital Innovation, Tongji University, city=Shanghai, postcode=200092, country=China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.22000)] <br>

**MagicTryOn: Harnessing Diffusion Transformer for Garment-Preserving Video Virtual Try-on** <br>
*Guangyuan Li, Siming Zheng, Hao Zhang, Jinwei Chen, Junsheng Luan, Binkai Ou, Lei Zhao, Bo Li, Peng-Tao Jiang.* <br>
**Virtual Try-On**, College of Computer Science and Technology, Zhejiang University & vivo Mobile Communication Co., Ltd & Innovation Research & Development, BoardWare Information System Limited <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.21325)]
[[Project](https://vivocameraresearch.github.io/magictryon)] <br>

**InstGenIE: Generative Image Editing Made Efficient with Mask-aware Caching and Scheduling** <br>
*Xiaoxiao Jiang, Suyi Li, Lingyun Yang, Tianyu Feng, Zhipeng Di, Weiyi Lu, Guoxuan Zhu, Xiu Lin, Kan Liu, Yinghao Yu, Tao Lan, Guodong Yang, Lin Qu, Liping Zhang, Wei Wang.* <br>
**Image Editing**, The Hong Kong University of Science and Technology & Alibaba Group <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.20600)] <br>

**Training-free Stylized Text-to-Image Generation with Fast Inference** <br>
*Xin Ma, Yaohui Wang, Xinyuan Chen, Tien-Tsin Wong, Cunjian Chen.* <br>
**Image Style Transfer**, Monash University & Shanghai AI Laboratory <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.19063)]
[[Project](https://maxin-cn.github.io/omnipainter_project)] <br>

**OmniConsistency: Learning Style-Agnostic Consistency from Paired Stylization Data** <br>
*Yiren Song, Cheng Liu, Mike Zheng Shou.* <br>
**Image Style Transfer**, Show Lab, National University of Singapore <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2505.18445)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/e4cd50120b6d7e8daff1749d6bbaa889-Abstract-Conference.html)]
[[Github](https://github.com/showlab/OmniConsistency)] <br>

**A Unified and Fast-Sampling Diffusion Bridge Framework via Stochastic Optimal Control** <br>
*Mokai Pan, Kaizhen Zhu, Yuexin Ma, Yanwei Fu, Jingyi Yu, Jingya Wang, Ye Shi.* <br>
**Base I2I Translation**, ShanghaiTech University & Fudan University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.21528)]
[[Github](https://github.com/2769433owo/UniDB-plusplus)] <br>

**R-Genie: Reasoning-Guided Generative Image Editing** <br>
*Dong Zhang, Lingfeng He, Rui Yan, Fei Shen, Jinhui Tang.* <br>
**Image Editing**, Nanjing University of Science and Technology & The Hong Kong University of Science and Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.17768)]
[[Project](https://dongzhang89.github.io/RGenie.github.io/)] <br>

**CDST: Color Disentangled Style Transfer for Universal Style Reference Customization** <br>
*Shiwen Zhang, Zhuowei Chen, Lang Chen, Yanze Wu.* <br>
**Image Style Transfer**, ByteDance <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2506.13770)] <br>

**Pursuing Temporal-Consistent Video Virtual Try-On via Dynamic Pose Interaction** <br>
*Dong Li, Wenqi Zhong, Wei Yu, Yingwei Pan, Dingwen Zhang, Ting Yao, Junwei Han, Tao Mei.* <br>
**Virtual Try-On**, HiDream.ai & Northwestern Polytechnical University <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2505.16980)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Pursuing_Temporal-Consistent_Video_Virtual_Try-On_via_Dynamic_Pose_Interaction_CVPR_2025_paper.html)] <br>

**Incorporating Visual Correspondence into Diffusion Model for Virtual Try-On** <br>
*Siqi Wan, Jingwen Chen, Yingwei Pan, Ting Yao, Tao Mei.* <br>
**Virtual Try-On**, University of Science and Technology of China & HiDream.ai <br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2505.16977)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/697200c9d1710c2799720b660abd11bb-Abstract-Conference.html)]
[[Github](https://github.com/HiDream-ai/SPM-Diff)] <br>

**Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation** <br>
*Estelle Chigot, Dennis G. Wilson, Meriem Ghrib, Thomas Oberlin.* <br>
**Image Style Transfer**, ISAE-Supaero, University of Toulouse, France & Airbus, France <br>
Computer Vision and Image Understanding 2025. [[PDF](https://arxiv.org/abs/2505.16360)]
[[Github](https://github.com/echigot/cactif)] <br>

**Image-to-Image Translation with Diffusion Transformers and CLIP-Based Image Conditioning** <br>
*Qiang Zhu, Kuan Lu, Menghao Huo, Yuxiao Li.* <br>
**Base I2I Translation**, University of Houston & Santa Clara University & Cornell University & Northeastern University <br>
CVIDL 2025. [[PDF](https://arxiv.org/abs/2505.16001)] <br>

**Leveraging the Powerful Attention of a Pre-trained Diffusion Model for Exemplar-based Image Colorization** <br>
*Satoshi Kosugi.* <br>
**Image Colorization**, Institute of Science Tokyo <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.15812)]
[[Github](https://github.com/satoshi-kosugi/powerful-attention)] <br>

**Emerging Properties in Unified Multimodal Pretraining** <br>
*Chaorui Deng, Deyao Zhu, Kunchang Li, Chenhui Gou, Feng Li, Zeyu Wang, Shu Zhong, Weihao Yu, Xiaonan Nie, Ziang Song, Guang Shi, Haoqi Fan.* <br>
**Image Editing**, ByteDance <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.14683)]
[[Project](https://bagel-ai.org/)]
[[Github](https://github.com/bytedance-seed/BAGEL)] <br>

**OmniStyle: Filtering High Quality Style Transfer Data at Scale** <br>
*Ye Wang, Ruiqi Liu, Jiang Lin, Fei Liu, Zili Yi, Yilin Wang, Rui Ma.* <br>
**Image Style Transfer**, Jilin University & Nanjing University & ByteDance & Adobe <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2505.14028)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_OmniStyle_Filtering_High_Quality_Style_Transfer_Data_at_Scale_CVPR_2025_paper.html)]
[[Project](https://wangyephd.github.io/projects/OmniStyle/cvpr25_omnistyle.html)]
[[Github](https://github.com/StyleX-Research/OmniStyle)]
[[Dataset](https://huggingface.co/datasets/StyleXX/OmniStyle-150k)] <br>

**DragLoRA: Online Optimization of LoRA Adapters for Drag-based Image Editing in Diffusion Model** <br>
*Siwei Xia, Li Sun, Tiantian Sun, Qingli Li.* <br>
**Image Editing**, Shanghai Key Laboratory of Multidimensional Information Processing & Key Laboratory of Advanced Theory and Application in Statistics and Data Science, East China Normal University, Shanghai, China <br>
ICML 2025. [[PDF](https://arxiv.org/abs/2505.12427)]
[[Github](https://github.com/Sylvie-X/DragLoRA)] <br>

**Don't Forget your Inverse DDIM for Image Editing** <br>
*Guillermo Gomez-Trenado, Pablo Mesejo, Oscar Cordón, Stéphane Lathuilière.* <br>
**Image Editing**, University of Granada and DaSCI Research Institute, Granada 18014, Spain & Panacea Cooperative Research, Ponferrada 24402, Spain & Inria at University Grenoble Alpes, Montbonnot-Saint-Martin, 38330, France <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.09571)]
[[Project](https://guillermogotre.github.io/sage/)] <br>

**IntrinsicEdit: Precise generative image manipulation in intrinsic space** <br>
*Linjie Lyu, Valentin Deschaintre, Yannick Hold-Geoffroy, Miloš Hašan, Jae Shin Yoon, Thomas Leimkühler, Christian Theobalt, Iliyan Georgiev.* <br>
**Image Editing**, Max-Planck-Institute for Informatics, Saarland Informatics Campus, Saarbrücken, Germany & Adobe Research, London, UK & Adobe Research, Quebec, Canada & Adobe Research, San Jose, USA <br>
SIGGRAPH 2025. [[PDF](https://arxiv.org/abs/2505.08889)] <br>

**Instance-aware Image Colorization with Controllable Textual Descriptions and Segmentation Masks** <br>
*Yanru An, Ling Gui, Chunlei Cai, Tianxiao Ye, JIangchao Yao, Guangtao Zhai, Qiang Hu, Xiaoyun Zhang.* <br>
**Image Colorization**, organization=Shanghai Jiao Tong University, city=Shanghai, postcode=200240, country=China & organization=Bilibili Inc, city=Shanghai, country=China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.08705)] <br>

**MDE-Edit: Masked Dual-Editing for Multi-Object Image Editing via Diffusion Models** <br>
*Hongyang Zhu, Haipeng Liu, Bo Fu, Yang Wang.* <br>
**Image Editing**, School of Computer Science and Information Engineering, Hefei University of Technology, Hefei, China & School of computer and artificial intelligence, Liaoning Normal University, Dalian, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2505.05101)] <br>

**Multi-turn Consistent Image Editing** <br>
*Zijun Zhou, Yingying Deng, Xiangyu He, Weiming Dong, Fan Tang.* <br>
**Image Editing**, Institute of Automation, Chinese Academy of Sciences, Beijing, China & Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2505.04320)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Multi-turn_Consistent_Image_Editing_ICCV_2025_paper.html)] <br>

**In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer** <br>
*Zechuan Zhang, Ji Xie, Yu Lu, Zongxin Yang, Yi Yang.* <br>
**Image Editing**, ReLER, CCAI, Zhejiang University & DBMI, HMS, Harvard University <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2504.20690)]
[[Project](https://river-zhang.github.io/ICEdit-gh-pages/)]
[[Github](https://github.com/River-Zhang/ICEdit)] <br>

**REED-VAE: RE-Encode Decode Training for Iterative Image Editing with Diffusion Models** <br>
*Gal Almog, Ariel Shamir, Ohad Fried.* <br>
**Image Editing**, Reichman University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.18989)]
[[Github](https://github.com/galmog/REED-VAE)]
[[Project](https://reed-vae.github.io/)] <br>

**Step1X-Edit: A Practical Framework for General Image Editing** <br>
*Shiyu Liu, Yucheng Han, Peng Xing, Fukun Yin, Rui Wang, Wei Cheng, Jiaqi Liao, Yingming Wang, Honghao Fu, Chunrui Han, Guopeng Li, Yuang Peng, Quan Sun, Jingwei Wu, Yan Cai, Zheng Ge, Ranchen Ming, Lei Xia, Xianfang Zeng, Yibo Zhu, Binxing Jiao, Xiangyu Zhang, Gang Yu, Daxin Jiang.* <br>
**Image Editing**, StepFun <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.17761)]
[[Github](https://github.com/stepfun-ai/Step1X-Edit)] <br>

**Structure-Preserving Zero-Shot Image Editing via Stage-Wise Latent Injection in Diffusion Models** <br>
*Dasol Jeong, Donggoo Kang, Jiwon Park, Hyebean Lee, Joonki Paik.* <br>
**Image Editing**, Department of Image and & Department of Artificial IntelligenceChung-Ang University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.15723)] <br>

**Diffusion Bridge Models for 3D Medical Image Translation** <br>
*Shaorong Zhang, Tamoghna Chattopadhyay, Sophia I. Thomopoulos, Jose-Luis Ambite, Paul M. Thompson, Greg Ver Steeg.* <br>
**Medical Image Translation**, University of California Riverside, CA, United States & Imaging Genetics Center, Mark and Mary Stevens Neuroimaging and Informatics Institute, Keck School of Medicine, University of Southern California, Marina del Rey, CA, United States & Information Sciences Institute, University of Southern California, Marina del Rey, CA, United States <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.15267)] <br>

**Fashion-RAG: Multimodal Fashion Image Editing via Retrieval-Augmented Generation** <br>
*Fulvio Sanguigni, Davide Morelli, Marcella Cornia, Rita Cucchiara.* <br>
**Image Editing**, University of Modena and Reggio Emilia, Italy & University of Pisa, Italy <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.14011)] <br>

**Early Timestep Zero-Shot Candidate Selection for Instruction-Guided Image Editing** <br>
*Joowon Kim, Ziseok Lee, Donghyeon Cho, Sanghyun Jo, Yeonsung Jung, Kyungsu Kim, Eunho Yang.* <br>
**Image Editing**, KAIST & Seoul National University & OGQ <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2504.13490)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Kim_Early_Timestep_Zero-Shot_Candidate_Selection_for_Instruction-Guided_Image_Editing_ICCV_2025_paper.html)]
[[Github](https://github.com/Joow0n-Kim/ELECT)] <br>

**MGT: Extending Virtual Try-Off to Multi-Garment Scenarios** <br>
*Riza Velioglu, Petra Bevandic, Robin Chan, Barbara Hammer.* <br>
**Virtual Try-On**, Bielefeld University <br>
ICCV 2025 Workshops. [[PDF](https://arxiv.org/abs/2504.13078)]
[[Project](https://rizavelioglu.github.io/tryoffdiff/)] <br>

**Image Editing with Diffusion Models: A Survey** <br>
*Jia Wang, Jie Hu, Xiaoqi Ma, Hanghang Ma, Xiaoming Wei, Enhua Wu.* <br>
**Survey** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.13226)] <br>

**ICAS: IP Adapter and ControlNet-based Attention Structure for Multi-Subject Style Transfer Optimization** <br>
*Fuwei Liu.* <br>
**Image Style Transfer** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.13224)] <br>

**SPIE: Semantic and Structural Post-Training of Image Editing Diffusion Models with AI feedback** <br>
*Elior Benarous, Yilun Du, Heng Yang.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.12833)] <br>

**Cobra: Efficient Line Art COlorization with BRoAder References** <br>
*Junhao Zhuang, Lingen Li, Xuan Ju, Zhaoyang Zhang, Chun Yuan, Ying Shan.* <br>
**Image Colorization**, Tsinghua University, China & The Chinese University of Hong Kong, China & Tencent ARC Lab, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.12240)]
[[Project](https://zhuang2002.github.io/Cobra/)] <br>

**SAR-to-RGB Translation with Latent Diffusion for Earth Observation** <br>
*Kaan Aydin, Joelle Hanna, Damian Borth.* <br>
**SAR Image Translation**, University of St. Gallen <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.11154)] <br>

**SPICE: A Synergistic, Precise, Iterative, and Customizable Image Editing Workflow** <br>
*Kenan Tang, Yanhong Li, Yao Qin.* <br>
**Image Editing**, University of California, Santa Barbara & Allen Institute for AI <br>
NeurIPS 2025 Creative AI Track. [[PDF](https://arxiv.org/abs/2504.09697)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/4051771acaf5ba90abe0539e1dc2821e-Abstract-Creative_AI_Track.html)]
[[Github](https://github.com/kenantang/spice)] <br>

**Structure-Accurate Medical Image Translation via Dynamic Frequency Balance and Knowledge Guidance** <br>
*Jiahua Xu, Dawei Zhou, Lei Hu, Zaiyi Liu, Nannan Wang, Xinbo Gao.* <br>
**Medical Image Translation**, Xidian University & Guangdong Provincial People’s Hospital & Chongqing University of Posts and Telecommunications <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.09441)] <br>

**Routing to the Right Expertise: A Trustworthy Judge for Instruction-based Image Editing** <br>
*Chenxi Sun, Hongzhi Zhang, Qi Wang, Fuzheng Zhang.* <br>
**Image Editing**, Kuaishou Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.07424)]
[[Github](https://github.com/Cyyyyyrus/JURE.git)] <br>

**ColorizeDiffusion v2: Enhancing Reference-based Sketch Colorization Through Separating Utilities** <br>
*Dingkun Yan, Xinrui Wang, Yusuke Iwasawa, Yutaka Matsuo, Suguru Saito, Jiaxian Guo.* <br>
**Image Colorization**, Institute of Science Tokyo, School of Computing, Japan & University of Tokyo, Japan <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.06895)]
[[Github](https://github.com/tellurion-kanata/colorizeDiffusion)] <br>

**Tuning-Free Image Editing with Fidelity and Editability via Unified Latent Diffusion Model** <br>
*Qi Mao, Lan Chen, Yuchao Gu, Mike Zheng Shou, Ming-Hsuan Yang.* <br>
**Image Editing**, Communication University of China & National University of Singapore & University of California, Merced & Yonsei University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.05594)]
[[Github](https://github.com/CUC-MIPG/UnifyEdit)] <br>

**Disentangling Instruction Influence in Diffusion Transformers for Parallel Multi-Instruction-Guided Image Editing** <br>
*Hui Liu, Bin Zou, Suiyun Zhang, Kecheng Chen, Rui Liu, Haoliang Li.* <br>
**Image Editing**, City University of Hong Kong & Huawei Noah’s Ark Lab & The University of Hong Kong <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.04784)] <br>

**Multimodal Diffusion Bridge with Attention-Based SAR Fusion for Satellite Image Cloud Removal** <br>
*Yuyang Hu, Suhas Lohit, Ulugbek S. Kamilov, Tim K. Marks.* <br>
**SAR Image Translation**, Washington University in St. Louis & Mitsubishi Electric Research Laboratories <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.03607)] <br>

**Concept Lancet: Image Editing with Compositional Representation Transplant** <br>
*Jinqi Luo, Tianjiao Ding, Kwan Ho Ryan Chan, Hancheng Min, Chris Callison-Burch, Rene Vidal.* <br>
**Image Editing**, University of Pennsylvania <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2504.02828)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Luo_Concept_Lancet_Image_Editing_with_Compositional_Representation_Transplant_CVPR_2025_paper.html)]
[[Project](https://peterljq.github.io/project/colan)] <br>

**Diffusion Model-Based Size Variable Virtual Try-On Technology and Evaluation Method** <br>
*Shufang Zhang, Hang Qian, Minxue Ni, Yaxuan Li, Wenxin Ding, Jun Liu.* <br>
**Virtual Try-On** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2504.00562)] <br>

**Deterministic Medical Image Translation via High-fidelity Brownian Bridges** <br>
*Qisheng He, Nicholas Summerfield, Peiyong Wang, Carri Glide-Hurst, Ming Dong.* <br>
**Medical Image Translation**, Department of Computer Science, Wayne State University, MI, USA & Department of Human Oncology, University of Wisconsin-Madison, WI, USA & Department of Medical Physics, University of Wisconsin-Madison, WI, USA <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.22531)] <br>

**LOCATEdit: Graph Laplacian Optimized Cross Attention for Localized Text-Guided Image Editing** <br>
*Achint Soni, Meet Soni, Sirisha Rambhatla.* <br>
**Image Editing**, University of Waterloo & Stony Brook University <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2503.21541)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Soni_LOCATEdit_Graph_Laplacian_Optimized_Cross_Attention_for_Localized_Text-Guided_Image_ICCV_2025_paper.html)]
[[Github](https://github.com/LOCATEdit/LOCATEdit/)] <br>

**ITA-MDT: Image-Timestep-Adaptive Masked Diffusion Transformer Framework for Image-Based Virtual Try-On** <br>
*Ji Woo Hong, Tri Ton, Trung X. Pham, Gwanhyeong Koo, Sunjae Yoon, Chang D. Yoo.* <br>
**Virtual Try-On**, Korea Advanced Institute of Science and Technology (KAIST), South Korea <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.20418)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Hong_ITA-MDT_Image-Timestep-Adaptive_Masked_Diffusion_Transformer_Framework_for_Image-Based_Virtual_Try-On_CVPR_2025_paper.html)]
[[Project](https://jiwoohong93.github.io/ita-mdt/)] <br>

**FireEdit: Fine-grained Instruction-based Image Editing via Region-aware Vision Language Model** <br>
*Jun Zhou, Jiahao Li, Zunnan Xu, Hanhui Li, Yiji Cheng, Fa-Ting Hong, Qin Lin, Qinglin Lu, Xiaodan Liang.* <br>
**Image Editing**, Shenzhen Campus of Sun Yat-sen University & Hunyuan, Tencent & Tsinghua University & HKUST <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.19839)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_FireEdit_Fine-grained_Instruction-based_Image_Editing_via_Region-aware_Vision_Language_Model_CVPR_2025_paper.html)]
[[Project](https://zjgans.github.io/fireedit.github.io)] <br>

**FDS: Frequency-Aware Denoising Score for Text-Guided Latent Diffusion Image Editing** <br>
*Yufan Ren, Zicong Jiang, Tong Zhang, Søren Forchhammer, Sabine Süsstrunk.* <br>
**Image Editing**, School of Computer and Communication Sciences, EPFL & Department of Electrical and Photonics Engineering, DTU & Department of Electrical Engineering, Chalmers University of Technology <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.19191)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Ren_FDS_Frequency-Aware_Denoising_Score_for_Text-Guided_Latent_Diffusion_Image_Editing_CVPR_2025_paper.html)]
[[Project](https://ivrl.github.io/fds-webpage/)] <br>

**Instruct-CLIP: Improving Instruction-Guided Image Editing with Automated Data Refinement Using Contrastive Learning** <br>
*Sherry X. Chen, Misha Sra, Pradeep Sen.* <br>
**Image Editing**, University of California, Santa Barbara <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.18406)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Instruct-CLIP_Improving_Instruction-Guided_Image_Editing_with_Automated_Data_Refinement_Using_CVPR_2025_paper.html)]
[[Github](https://github.com/SherryXTChen/Instruct-CLIP.git)] <br>

**Guidance Free Image Editing via Explicit Conditioning** <br>
*Mehdi Noroozi, Alberto Gil Ramos, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Abhinav Mehrotra, Sourav Bhattacharya.* <br>
**Image Editing**, Samsung AI Cambridge <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.17593)] <br>

**Follow-Your-Color: Multi-Instance Sketch Colorization** <br>
*Yinhan Zhang, Yue Ma, Bingyuan Wang, Qifeng Chen, Zeyu Wang.* <br>
**Image Colorization**, The Hong Kong University of Science and Technology (Guangzhou) & The Hong Kong University of Science and Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.16948)]
[[Project](https://yinhan-zhang.github.io/color)] <br>

**DCEdit: Dual-Level Controlled Image Editing via Precisely Localized Semantics** <br>
*Yihan Hu, Jianing Peng, Yiheng Lin, Ting Liu, Xiaochao Qu, Luoqi Liu, Yao Zhao, Yunchao Wei.* <br>
**Image Editing**, Beijing Jiaotong University & Meitu & Pengcheng Laboratory <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.16795)] <br>

**FreeFlux: Understanding and Exploiting Layer-Specific Roles in RoPE-Based MMDiT for Versatile Image Editing** <br>
*Tianyi Wei, Yifan Zhou, Dongdong Chen, Xingang Pan.* <br>
**Image Editing**, S-Lab, Nanyang Technological University Microsoft GenAI <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2503.16153)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Wei_FreeFlux_Understanding_and_Exploiting_Layer-Specific_Roles_in_RoPE-Based_MMDiT_for_ICCV_2025_paper.html)]
[[Project](https://wtybest.github.io/projects/FreeFlux/)] <br>

**Shining Yourself: High-Fidelity Ornaments Virtual Try-on with Diffusion Model** <br>
*Yingmao Miao, Zhanpeng Huang, Rui Han, Zibin Wang, Chenhao Lin, Chao Shen.* <br>
**Virtual Try-On**, Xi’an Jiaotong University, SenseTime Research <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.16065)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Miao_Shining_Yourself_High-Fidelity_Ornaments_Virtual_Try-on_with_Diffusion_Model_CVPR_2025_paper.html)] <br>

**TF-TI2I: Training-Free Text-and-Image-to-Image Generation via Multi-Modal Implicit-Context Learning In Text-to-Image Models** <br>
*Teng-Fang Hsiao, Bo-Kai Ruan, Yi-Lun Wu, Tzu-Ling Lin, Hong-Han Shuai.* <br>
**Image Editing**, National Yang Ming Chiao Tung University <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2503.15283)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Hsiao_TF-TI2I_Training-Free_Text-and-Image-to-Image_Generation_via_Multi-Modal_Implicit-Context_Learning_In_Text-to-Image_ICCV_2025_paper.html)]
[[Project](https://bluedyee.github.io/TF-TI2I_page/)] <br>

**Language-based Image Colorization: A Benchmark and Beyond** <br>
*Yifan Li, Shuai Yang, Jiaying Liu.* <br>
**Image Colorization** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.14974)]
[[Github](https://github.com/lyf1212/Color-Turbo)] <br>

**Free-Lunch Color-Texture Disentanglement for Stylized Image Generation** <br>
*Jiang Qin, Alexandra Gomez-Villa, Senmao Li, Shiqi Yang, Yaxing Wang, Kai Wang, Joost van de Weijer.* <br>
**Image Style Transfer**, Harbin Institute of Technology, China & Computer Vision Center, Spain & Universitat Autònoma de Barcelona, Spain & VCIP, CS, Nankai University, China & Program of Computer Science, City University of Hong Kong (Dongguan), China & City University of Hong Kong, HK SAR, China <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2503.14275)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/c376f801570bee349ec1f18f1dd0bcc8-Abstract-Conference.html)]
[[Project](https://deepffff.github.io/sadis.github.io/)] <br>

**BlobCtrl: Taming Controllable Blob for Element-level Image Editing** <br>
*Yaowei Li, Lingen Li, Zhaoyang Zhang, Xiaoyu Li, Guangzhi Wang, Hongxiang Li, Xiaodong Cun, Ying Shan, Yuexian Zou.* <br>
**Image Editing**, SECE, Peking University, China & The Chinese University of Hong Kong, Hongkong, China & ARC Lab, Tencent, China & The Hong Kong University of Science and Technology, Hongkong, China & GVC Lab, Great Bay University, China <br>
SIGGRAPH Asia 2025. [[PDF](https://arxiv.org/abs/2503.13434)]
[[Project](https://liyaowei-stu.github.io/project/BlobCtrl/)] <br>

**V-Stylist: Video Stylization via Collaboration and Reflection of MLLM Agents** <br>
*Zhengrong Yue, Shaobin Zhuang, Kunchang Li, Yanbo Ding, Yali Wang.* <br>
**Video Style Transfer**, Shanghai Jiao Tong University Shanghai AI Laboratory & Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences & University of Chinese Academy of Sciences <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.12077)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Yue_V-Stylist_Video_Stylization_via_Collaboration_and_Reflection_of_MLLM_Agents_CVPR_2025_paper.html)] <br>

**LUSD: Localized Update Score Distillation for Text-Guided Image Editing** <br>
*Worameth Chinchuthakun, Tossaporn Saengja, Nontawat Tritrong, Pitchaporn Rewatbowornwong, Pramook Khungurn, Supasorn Suwajanakorn.* <br>
**Image Editing**, VISTEC & Siam Commercial Bank & Faculty of Medicine Siriraj Hospital & Pixiv <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2503.11054)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Chinchuthakun_LUSD_Localized_Update_Score_Distillation_for_Text-Guided_Image_Editing_ICCV_2025_paper.html)]
[[Github](https://github.com/sincostanx/LUSD)] <br>

**CoSTA$\ast$: Cost-Sensitive Toolpath Agent for Multi-turn Image Editing** <br>
*Advait Gupta, NandaKiran Velaga, Dang Nguyen, Tianyi Zhou.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.10613)]
[[Github](https://github.com/tianyi-lab/CoSTAR)] <br>

**MoEdit: On Learning Quantity Perception for Multi-object Image Editing** <br>
*Yanfeng Li, Kahou Chan, Yue Sun, Chantong Lam, Tong Tong, Zitong Yu, Keren Fu, Xiaohong Liu, Tao Tan.* <br>
**Image Editing**, Macao Polytechnic University & Fuzhou University & Great Bay University & Sichuan University & Shanghai Jiao Tong University <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.10112)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Li_MoEdit_On_Learning_Quantity_Perception_for_Multi-object_Image_Editing_CVPR_2025_paper.html)]
[[Github](https://github.com/Tear-kitty/MoEdit)] <br>

**MF-VITON: High-Fidelity Mask-Free Virtual Try-On with Minimal Input** <br>
*Zhenchen Wan, Yanwu xu, Dongting Hu, Weilun Cheng, Tianxi Chen, Zhaoqing Wang, Feng Liu, Tongliang Liu, Mingming Gong.* <br>
**Virtual Try-On**, University of Melbourne, Melbourne, Australia & The University of Sydney, Sydney, Australia & Mohamed bin Zayed University of Artificial Intelligence, Abu Dhabi, UAE <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.08650)]
[[Project](https://zhenchenwan.github.io/MF-VITON/)] <br>

**U-StyDiT: Ultra-high Quality Artistic Style Transfer Using Diffusion Transformers** <br>
*Zhanjie Zhang, Ao Ma, Ke Cao, Jing Wang, Shanyuan Liu, Yuhang Ma, Bo Cheng, Dawei Leng, Yuhui Yin.* <br>
**Image Style Transfer**, College of Computer Science and Technology, Zhejiang University & AI Research <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.08157)] <br>

**Balanced Image Stylization with Style Matching Score** <br>
*Yuxin Jiang, Liming Jiang, Shuai Yang, Jia-Wei Liu, Ivor W. Tsang, Mike Zheng Shou.* <br>
**Image Style Transfer**, Show Lab, National University of Singapore & Agency for Science, Technology and Research (A*STAR) & Nanyang Technological University & Wangxuan Institute of Computer Technology, Peking University <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2503.07601)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_Balanced_Image_Stylization_with_Style_Matching_Score_ICCV_2025_paper.html)]
[[Github](https://github.com/showlab/SMS)]
[[Project](https://yuxinn-j.github.io/projects/SMS.html)] <br>

**LBM: Latent Bridge Matching for Fast Image-to-Image Translation** <br>
*Clément Chadebec, Onur Tasar, Sanjeev Sreetharan, Benjamin Aubin.* <br>
**Base I2I Translation**, Jasper Research <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2503.07535)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Chadebec_LBM_Latent_Bridge_Matching_for_Fast_Image-to-Image_Translation_ICCV_2025_paper.html)]
[[Github](https://github.com/gojasper/LBM)] <br>

**Inversion-Free Video Style Transfer with Trajectory Reset Attention Control and Content-Style Bridging** <br>
*Jiang Lin, Zili Yi.* <br>
**Video Style Transfer**, Nanjing University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.07363)] <br>

**SOYO: A Tuning-Free Approach for Video Style Morphing via Style-Adaptive Interpolation in Diffusion Models** <br>
*Haoyu Zheng, Qifan Yu, Binghe Yu, Yang Dai, Wenqiao Zhang, Juncheng Li, Siliang Tang, Yueting Zhuang.* <br>
**Video Style Transfer**, Zhejiang University & University of Electronic Science and Technology of China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.06998)] <br>

**Energy-Guided Optimization for Personalized Image Editing with Pretrained Text-to-Image Diffusion Models** <br>
*Rui Jiang, Xinghe Fu, Guangcong Zheng, Teng Li, Taiping Yao, Xi Li.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.04215)] <br>

**Diffusion-based Virtual Staining from Polarimetric Mueller Matrix Imaging** <br>
*Xiaoyu Zheng, Jing Wen, Jiaxin Zhuang, Yao Du, Jing Cong, Limei Guo, Chao He, Lin Luo, Hao Chen.* <br>
**Virtual Staining**, The Hong Kong University of Science and Technology, Hong Kong SAR, China & Peking University, China & Beijing Institute of Collaborative Innovation, China & Peking University Health Science Center, China & University of Oxford, United Kingdom <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.01352)] <br>

**Tight Inversion: Image-Conditioned Inversion for Real Image Editing** <br>
*Edo Kadosh, Nir Goren, Or Patashnik, Daniel Garibi, Daniel Cohen-Or.* <br>
**Image Editing** <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.20376)]
[[Project](https://tight-inversion.github.io)] <br>

**Image Referenced Sketch Colorization Based on Animation Creation Workflow** <br>
*Dingkun Yan, Xinrui Wang, Zhuoru Li, Suguru Saito, Yusuke Iwasawa, Yutaka Matsuo, Jiaxian Guo.* <br>
**Image Colorization**, Institute of Science Tokyo & The University of Tokyo & Project HAT <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2502.19937)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Yan_Image_Referenced_Sketch_Colorization_Based_on_Animation_Creation_Workflow_CVPR_2025_paper.html)]
[[Github](https://github.com/tellurion-kanata/colorizeDiffusion)] <br>

**K-LoRA: Unlocking Training-Free Fusion of Any Subject and Style LoRAs** <br>
*Ziheng Ouyang, Zhen Li, Qibin Hou.* <br>
**Image Style Transfer** <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2502.18461)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Ouyang_K-LoRA_Unlocking_Training-Free_Fusion_of_Any_Subject_and_Style_LoRAs_CVPR_2025_paper.html)]
[[Project](https://k-lora.github.io/K-LoRA.io/)] <br>

**Bidirectional Diffusion Bridge Models** <br>
*Duc Kieu, Kien Do, Toan Nguyen, Dang Nguyen, Thin Nguyen.* <br>
**Base I2I Translation**, Applied Artificial Intelligence Institute (A2I2), Deakin University, Australia <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.09655)]
[[Github](https://github.com/kvmduc/BDBM)] <br>

**PartEdit: Fine-Grained Image Editing using Pre-Trained Diffusion Models** <br>
*Aleksandar Cvejic, Abdelrahman Eldesokey, Peter Wonka.* <br>
**Image Editing**, King Abdullah University of Science and Technology (KAUST), Thuwal, Saudi Arabia <br>
SIGGRAPH 2025. [[PDF](https://arxiv.org/abs/2502.04050)]
[[Project](https://gorluxor.github.io/part-edit/)] <br>

**MFP-VTON: Enhancing Mask-Free Person-to-Person Virtual Try-On via Diffusion Transformer** <br>
*Le Shen, Yanting Kang, Rong Huang, Zhijie Wang.* <br>
**Virtual Try-On**, Donghua University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.01626)] <br>

**Consistent Video Colorization via Palette Guidance** <br>
*Han Wang, Yuang Zhang, Yuhong Zhang, Lingxiao Lu, Li Song.* <br>
**Image Colorization**, Shanghai Jiao Tong University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.19331)] <br>

**ITVTON: Virtual Try-On Diffusion Transformer Based on Integrated Image and Text** <br>
*Haifeng Ni, Ming Xu.* <br>
**Virtual Try-On**, School of Software Engineering, East China Normal University, Shanghai, China <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.16757)] <br>

**Fully Guided Neural Schrödinger bridge for Brain MR image synthesis** <br>
*Hanyeol Yang, Sunggyu Kim, Mi Kyung Kim, Yongseon Yoo, Yu-Mi Kim, Min-Ho Shin, Insung Chung, Sang Baek Koh, Hyeon Chang Kim, Jong-Min Lee.* <br>
**Medical Image Translation**, Hanyang University, Department of Artificial Intelligence, & Wangsimni-ro, Seongdong-gu, Seoul, 04763, Seoul, Republic of Korea & Hanyang University, Department of Biomedical Engineering, & Wangsimni-ro, Seongdong-gu, Seoul, 04763, Seoul, Republic of Korea & Hanyang University College of Medicine, Department of Preventive Medicine, & Wangsimni-ro, Seongdong-gu, Seoul, 04763, Seoul, Republic of Korea & Chonnam National University Medical School, Department of Preventive Medicine, 160, Baekseo-ro, Dong-gu, Gwangju, 61469, Gwangju, Republic of Korea & Keimyung University School of Medicine, Department of Occupational and Environmental Medicine, & Dalgubeoldaero, Dalseo-gu, Daegu, 42601, Daegu, Republic of Korea & Yonsei Wonju College of Medicine, Department of Preventive Medicine and Institute of Occupational Medicine, & Ilsan-Dong, Wonju, 220-701, Wonju, Republic of Korea & Yonsei University College of Medicine, Department of Preventive Medicine, 50-1, Yonsei-Ro, Seodaemun-gu, Seoul, 03722, Seoul, Republic of Korea <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.14171)] <br>

**LLM-guided Instance-level Image Manipulation with Diffusion U-Net Cross-Attention Maps** <br>
*Andrey Palaev, Adil Khan, Syed M. Ahsan Kazmi.* <br>
**Image Editing**, AIDecisions, SW20 ODS, London, UK & School of Computer Science, University of Hull, HU6 7RX, Hull, UK & Department of Computer Science, University of the West of England, BS16 1QY, Bristol, UK <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.14046)]
[[Github](https://github.com/Palandr123/DiffusionU-NetLLM)] <br>

**CatV2TON: Taming Diffusion Transformers for Vision-Based Virtual Try-On with Temporal Concatenation** <br>
*Zheng Chong, Wenqing Zhang, Shiyue Zhang, Jun Zheng, Xiao Dong, Haoxiang Li, Yiling Wu, Dongmei Jiang, Xiaodan Liang.* <br>
**Virtual Try-On**, Sun Yat-sen University & National University of Singapore & Pixocial Technology & Pengcheng Laboratory <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.11325)]
[[Github](https://github.com/Zheng-Chong/CatV2TON)] <br>

**VanGogh: A Unified Multimodal Diffusion-based Framework for Video Colorization** <br>
*Zixun Fang, Zhiheng Liu, Kai Zhu, Yu Liu, Ka Leong Cheng, Wei Zhai, Yang Cao, Zheng-Jun Zha.* <br>
**Image Colorization**, USTC & HKU & Independent Researcher & HKUST <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.09499)]
[[Project](https://becauseimbatman0.github.io/VanGogh)] <br>

**MangaNinja: Line Art Colorization with Precise Reference Following** <br>
*Zhiheng Liu, Ka Leong Cheng, Xi Chen, Jie Xiao, Hao Ouyang, Kai Zhu, Yu Liu, Yujun Shen, Qifeng Chen, Ping Luo.* <br>
**Image Colorization**, HKU & HKUST & Tongyi Lab,Ant Group <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2501.08332)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_MangaNinja_Line_Art_Colorization_with_Precise_Reference_Following_CVPR_2025_paper.html)]
[[Project](https://johanan528.github.io/MangaNinjia/)] <br>

**FramePainter: Endowing Interactive Image Editing with Video Diffusion Priors** <br>
*Yabo Zhang, Xinpeng Zhou, Yihan Zeng, Hang Xu, Hui Li, Wangmeng Zuo.* <br>
**Image Editing**, Harbin Institute of Technology & Huawei Noah’s Ark Lab <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2501.08225)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_FramePainter_Endowing_Interactive_Image_Editing_with_Video_Diffusion_Priors_ICCV_2025_paper.html)]
[[Github](https://github.com/YBYBZhang/FramePainter)] <br>

**HYB-VITON: A Hybrid Approach to Virtual Try-On Combining Explicit and Implicit Warping** <br>
*Kosuke Takemoto, Takafumi Koshinaka.* <br>
**Virtual Try-On** <br>
ICASSP 2025. [[PDF](https://arxiv.org/abs/2501.03910)] <br>

**MC-VTON: Minimal Control Virtual Try-On Diffusion Transformer** <br>
*Junsheng Luan, Guangyuan Li, Lei Zhao, Wei Xing.* <br>
**Virtual Try-On**, Zhejiang University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.03630)] <br>

**Textualize Visual Prompt for Image Editing via Diffusion Bridge** <br>
*Pengcheng Xu, Qingnan Fan, Fei Kou, Shuai Qin, Hong Gu, Ruoyu Zhao, Charles Ling, Boyu Wang.* <br>
**Image Editing** <br>
AAAI 2025. [[PDF](https://arxiv.org/abs/2501.03495)] <br>

**CAMILA: Context-Aware Masking for Image Editing with Language Alignment** <br>
*Hyunseung Kim, Chiho Choi, Srikanth Malla, Sai Padmanabhan, Saurabh Bagchi, Joon Hee Choi.* <br>
**Image Editing** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/1df27e31a0c0b916797a49198cb28d6a-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/1df27e31a0c0b916797a49198cb28d6a-Abstract-Conference.html)] <br>

**PairEdit: Learning Semantic Variations for Exemplar-based Image Editing** <br>
*Haoguang Lu, Jiacheng Chen, Zhenguo Yang, Aurele Gnanha, Fu Lee Wang, Qing Li, Xudong Mao.* <br>
**Image Editing** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/2df1817654de9744db00c951dd7727be-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/2df1817654de9744db00c951dd7727be-Abstract-Conference.html)]
[[Github](https://github.com/xudonmao/PairEdit)] <br>

**Counterfactual Image Editing with Disentangled Causal Latent Space** <br>
*Yushu Pan, Elias Bareinboim.* <br>
**Image Editing** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/54e1419b1cbca8ada96a87c96567e954-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/54e1419b1cbca8ada96a87c96567e954-Abstract-Conference.html)] <br>

**CamEdit: Continuous Camera Parameter Control for Photorealistic Image Editing** <br>
*Xinran Qin, Zhixin Wang, Fan Li, Haoyu Chen, Renjing Pei, Wenbo Li, Xiaochun Cao.* <br>
**Image Editing** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/a60567166d738f4c43e563fdf8a2afe4-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/a60567166d738f4c43e563fdf8a2afe4-Abstract-Conference.html)] <br>

**FSI-Edit: Frequency and Stochasticity Injection for Flexible Diffusion-Based Image Editing** <br>
*Kaixiang Yang, Xin Li, Yuxi Li, Qiang Li, Zhiwei Wang.* <br>
**Image Editing** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/c0d7b7a75dc49664bfc6ac9cb935792d-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/c0d7b7a75dc49664bfc6ac9cb935792d-Abstract-Conference.html)] <br>

**Enhancing Consistency of Flow-Based Image Editing through Kalman Control** <br>
*Haozhe Chi, Zhicheng Sun, Yang Jin, Yi Ma, Jing Wang, Yadong Mu.* <br>
**Image Editing** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/d01db5cd2555ba11f75da0454d57b903-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/d01db5cd2555ba11f75da0454d57b903-Abstract-Conference.html)] <br>

**CREA: A Collaborative Multi-Agent Framework for Creative Image Editing and Generation** <br>
*Kavana Venkatesh, Connor Dunlop, Pinar Yanardag.* <br>
**Image Editing** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/fa41e9d5dfcc97cd9eed99f001aa28e5-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/fa41e9d5dfcc97cd9eed99f001aa28e5-Abstract-Conference.html)] <br>

**Exploring the Design Space of Diffusion Bridge Models** <br>
*Shaorong Zhang, Yuanbin Cheng, Greg Ver Steeg.* <br>
**Base I2I Translation** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/44cb9aa2897a288f7e6d9dd66659d523-Paper-Conference.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/44cb9aa2897a288f7e6d9dd66659d523-Abstract-Conference.html)] <br>

**ImgEdit: A Unified Image Editing Dataset and Benchmark** <br>
*Yang Ye, Xianyi He, Zongjian Li, lin bin, Shenghai Yuan, Zhiyuan Yan, Bohan Hou, Li Yuan.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/bec783f119b969772c35243b1c801090-Paper-Datasets_and_Benchmarks_Track.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/bec783f119b969772c35243b1c801090-Abstract-Datasets_and_Benchmarks_Track.html)] <br>

**KRIS-Bench: Benchmarking Next-Level Intelligent Image Editing Models** <br>
*Yongliang Wu, Zonghui Li, Xinting Hu, Xinyu Ye, Xianfang Zeng, Gang Yu, Wenbo Zhu, Bernt Schiele, Ming-Hsuan Yang, Xu Yang.* <br>
**Dataset / Evaluation** <br>
NeurIPS 2025. [[PDF](https://papers.neurips.cc/paper_files/paper/2025/file/e619b285582fb12f4c3de3a507b8b99c-Paper-Datasets_and_Benchmarks_Track.pdf)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/e619b285582fb12f4c3de3a507b8b99c-Abstract-Datasets_and_Benchmarks_Track.html)] <br>

**HSI: A Holistic Style Injector for Arbitrary Style Transfer** <br>
*Shuhao Zhang, Hui Kang, Yang Liu, Fang Mei, Hongjuan Li.* <br>
**Image Style Transfer** <br>
CVPR 2025. [[PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_HSI_A_Holistic_Style_Injector_for_Arbitrary_Style_Transfer_CVPR_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_HSI_A_Holistic_Style_Injector_for_Arbitrary_Style_Transfer_CVPR_2025_paper.html)] <br>

**Multitwine: Multi-Object Compositing with Text and Layout Control** <br>
*Gemma Canet Tarrés, Zhe Lin, Zhifei Zhang, He Zhang, Andrew Gilbert, John Collomosse, Soo Ye Kim.* <br>
**Image Editing** <br>
CVPR 2025. [[PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Tarres_Multitwine_Multi-Object_Compositing_with_Text_and_Layout_Control_CVPR_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Tarres_Multitwine_Multi-Object_Compositing_with_Text_and_Layout_Control_CVPR_2025_paper.html)] <br>

**Finding Local Diffusion Schrodinger Bridge using Kolmogorov-Arnold Network** <br>
*Xingyu Qiu, Mengying Yang, Xinghua Ma, Fanding Li, Dong Liang, Gongning Luo, Wei Wang, Kuanquan Wang, Shuo Li.* <br>
**Base I2I Translation** <br>
CVPR 2025. [[PDF](https://openaccess.thecvf.com/content/CVPR2025/papers/Qiu_Finding_Local_Diffusion_Schrodinger_Bridge_using_Kolmogorov-Arnold_Network_CVPR_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Qiu_Finding_Local_Diffusion_Schrodinger_Bridge_using_Kolmogorov-Arnold_Network_CVPR_2025_paper.html)]
[[Github](https://github.com/PerceptionComputingLab/LDSB)] <br>

**Wasserstein Style Distribution Analysis and Transform for Stylized Image Generation** <br>
*Xi Yu, Xiang Gu, Zhihao Shi, Jian Sun.* <br>
**Image Style Transfer** <br>
ICCV 2025. [[PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Wasserstein_Style_Distribution_Analysis_and_Transform_for_Stylized_Image_Generation_ICCV_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Yu_Wasserstein_Style_Distribution_Analysis_and_Transform_for_Stylized_Image_Generation_ICCV_2025_paper.html)] <br>

**Co-Painter: Fine-Grained Controllable Image Stylization via Implicit Decoupling and Adaptive Injection** <br>
*Bowen Fu, Wei Wei, Jiaqi Tang, Jiangtao Nie, Yanyu Ye, Xiaogang Xu, Ying-Cong Chen, Lei Zhang.* <br>
**Image Style Transfer** <br>
ICCV 2025. [[PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Fu_Co-Painter_Fine-Grained_Controllable_Image_Stylization_via_Implicit_Decoupling_and_Adaptive_ICCV_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Fu_Co-Painter_Fine-Grained_Controllable_Image_Stylization_via_Implicit_Decoupling_and_Adaptive_ICCV_2025_paper.html)] <br>

**Frequency-Guided Diffusion for Training-Free Text-Driven Image Translation** <br>
*Zheng Gao, Jifei Song, Zhensong Zhang, Jiankang Deng, Ioannis Patras.* <br>
**Image Editing** <br>
ICCV 2025. [[PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Gao_Frequency-Guided_Diffusion_for_Training-Free_Text-Driven_Image_Translation_ICCV_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_Frequency-Guided_Diffusion_for_Training-Free_Text-Driven_Image_Translation_ICCV_2025_paper.html)] <br>

**CreatiLayout: Siamese Multimodal Diffusion Transformer for Creative Layout-to-Image Generation** <br>
*Hui Zhang, Dexiang Hong, Yitong Wang, Jie Shao, Xinglong Wu, Zuxuan Wu, Yu-Gang Jiang.* <br>
**Layout-to-Image Generation** <br>
ICCV 2025. [[PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_CreatiLayout_Siamese_Multimodal_Diffusion_Transformer_for_Creative_Layout-to-Image_Generation_ICCV_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_CreatiLayout_Siamese_Multimodal_Diffusion_Transformer_for_Creative_Layout-to-Image_Generation_ICCV_2025_paper.html)] <br>

**OmniEdit: Building Image Editing Generalist Models Through Specialist Supervision** <br>
*Cong Wei, Zheyang Xiong, Weiming Ren, Xeron Du, Ge Zhang, Wenhu Chen.* <br>
**Image Editing** <br>
ICLR 2025. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/0113ef4642264adc2e6924a3cbbdf532-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0113ef4642264adc2e6924a3cbbdf532-Abstract-Conference.html)] <br>

**PostEdit: Posterior Sampling for Efficient Zero-Shot Image Editing** <br>
*Feng Tian, Yixuan Li, Yichao Yan, Shanyan Guan, Yanhao Ge, Xiaokang Yang.* <br>
**Image Editing** <br>
ICLR 2025. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/0252a434b18962c94910c07cd9a7fecc-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/0252a434b18962c94910c07cd9a7fecc-Abstract-Conference.html)] <br>

**CLIPDrag: Combining Text-based and Drag-based Instructions for Image Editing** <br>
*Ziqi Jiang, Zhen Wang, Long Chen.* <br>
**Image Editing** <br>
ICLR 2025. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/10162500bd9745ac0d4dc321b726e49e-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/10162500bd9745ac0d4dc321b726e49e-Abstract-Conference.html)] <br>

**PixWizard: Versatile Image-to-Image Visual Assistant with Open-Language Instructions** <br>
*Weifeng Lin, Xinyu Wei, Renrui Zhang, Le Zhuo, Shitian Zhao, Siyuan Huang, Junlin Xie, Gao Peng, Hongsheng Li.* <br>
**Image Editing** <br>
ICLR 2025. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/6075d47368ddf560e92efd53264b5405-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6075d47368ddf560e92efd53264b5405-Abstract-Conference.html)] <br>

**Multi-Reward as Condition for Instruction-based Image Editing** <br>
*Xin Gu, Ming Li, Libo Zhang, Fan Chen, Longyin Wen, Tiejian Luo, Sijie Zhu.* <br>
**Image Editing** <br>
ICLR 2025. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc82fe357440ce3f43e1939f4f795478-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/cc82fe357440ce3f43e1939f4f795478-Abstract-Conference.html)]
[[Github](https://github.com/bytedance/Multi-Reward-Editing)] <br>

**HQ-Edit: A High-Quality Dataset for Instruction-based Image Editing** <br>
*MUDE HUI, Siwei Yang, Bingchen Zhao, Yichun Shi, Heng Wang, Peng Wang, Cihang Xie, Yuyin Zhou.* <br>
**Dataset / Evaluation** <br>
ICLR 2025. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/b639c526a942618f1dba2b7a5fa0bac0-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b639c526a942618f1dba2b7a5fa0bac0-Abstract-Conference.html)] <br>

**$\text{I}^2\text{AM}$: Interpreting Image-to-Image Latent Diffusion Models via Bi-Attribution Maps** <br>
*Junseo Park, Hyeryung Jang.* <br>
**Dataset / Evaluation** <br>
ICLR 2025. [[PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4a59e985de8b134328f41a47bc7dfac-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c4a59e985de8b134328f41a47bc7dfac-Abstract-Conference.html)] <br>

**AniDoc: Animation Creation Made Easier** <br>
*Yihao Meng, Hao Ouyang, Hanlin Wang, Qiuyu Wang, Wen Wang, Ka Leong Cheng, Zhiheng Liu, Yujun Shen, Huamin Qu.* <br>
**Image Colorization**, HKUST & Ant Group & NJU & ZJU & HKU <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2412.14173)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Meng_AniDoc_Animation_Creation_Made_Easier_CVPR_2025_paper.html)]
[[Project](https://yihao-meng.github.io/AniDoc_demo)] <br>

**FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models** <br>
*Vladimir Kulikov, Matan Kleiner, Inbar Huberman-Spiegelglas, Tomer Michaeli.* <br>
**Image Editing** <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2412.08629)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Kulikov_FlowEdit_Inversion-Free_Text-Based_Editing_Using_Pre-Trained_Flow_Models_ICCV_2025_paper.html)]
[[Project](https://matankleiner.github.io/flowedit/)] <br>

**StyleStudio: Text-Driven Style Transfer with Selective Control of Style Elements** <br>
*Mingkun Lei, Xue Song, Beier Zhu, Hao Wang, Chi Zhang.* <br>
**Image Style Transfer**, AGI Lab, Westlake University & Fudan University & Nanyang Technological University & The Hong Kong University of Science and Technology (Guangzhou) <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2412.08503)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Lei_StyleStudio_Text-Driven_Style_Transfer_with_Selective_Control_of_Style_Elements_CVPR_2025_paper.html)]
[[Project](https://stylestudio-official.github.io/)] <br>

**StyleMaster: Stylize Your Video with Artistic Generation and Translation** <br>
*Zixuan Ye, Huijuan Huang, Xintao Wang, Pengfei Wan, Di Zhang, Wenhan Luo.* <br>
**Video Style Transfer**, Hong Kong University of Science and Technology & KuaiShou Technology <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2412.07744)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Ye_StyleMaster_Stylize_Your_Video_with_Artistic_Generation_and_Translation_CVPR_2025_paper.html)]
[[Project](https://zixuan-ye.github.io/stylemaster)] <br>

**UnZipLoRA: Separating Content and Style from a Single Image** <br>
*Chang Liu, Viraj Shah, Aiyu Cui, Svetlana Lazebnik.* <br>
**Image Style Transfer** <br>
ICCV 2025. [[PDF](https://arxiv.org/abs/2412.04465)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_UnZipLoRA_Separating_Content_and_Style_from_a_Single_Image_ICCV_2025_paper.html)]
[[Project](https://unziplora.github.io)] <br>

**CSGO: Content-Style Composition in Text-to-Image Generation** <br>
*Peng Xing, Haofan Wang, Yanpeng Sun, wangqixun, Baixu, Hao Ai, Jen-Yuan Huang, Zechao Li.* <br>
**Image Style Transfer** <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2408.16766)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/9144c7c014bf4c30e88f650bef8f68dd-Abstract-Conference.html)]
[[Project](https://csgo-gen.github.io/)] <br>

**RB-Modulation: Training-Free Stylization using Reference-Based Modulation** <br>
*Litu Rout, Yujia Chen, Nataniel Ruiz, Abhishek Kumar, Constantine Caramanis, Sanjay Shakkottai, Wen-Sheng Chu.* <br>
**Image Style Transfer** <br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2405.17401)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8f3705d6354fcecf48515cc43aa16023-Abstract-Conference.html)] <br>

**Looking Backward: Streaming Video-to-Video Translation with Feature Banks** <br>
*Feng Liang, Akio Kodaira, Chenfeng Xu, Masayoshi Tomizuka, Kurt Keutzer, Diana Marculescu.* <br>
**Video Style Transfer**, UT Austin & UC Berkeley <br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2405.15757)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7280f65ed571b7b28321f2c7cf4c60c8-Abstract-Conference.html)]
[[Project](https://jeff-liangf.github.io/projects/streamv2v)] <br>

**Semantix: An Energy-guided Sampler for Semantic Style Transfer** <br>
*Huiang He, Minghui Hu, Chuanxia Zheng, Chaoyue Wang, Tat-Jen Cham.* <br>
**Image Style Transfer**, South China University of Technology <br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2503.22344)]
[[Project](https://huiang-he.github.io/semantix/)]
[[Github](https://github.com/Huiang-He/Semantix-Styler)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4cf53c9fa86318d37bbeadac59c1a34d-Abstract-Conference.html)] <br>

**Contrastive Learning Guided Latent Diffusion Model for Image-to-Image Translation** <br>
*Qi Si, Bo Wang, Zhao Zhang, Mingbo Zhao, Xiaojie Jin, Mingliang Xu, Meng Wang.* <br>
**Image Editing**, Hefei University of Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.20484)] <br>

**Unpaired Object-Level SAR-to-Optical Image Translation for Aircraft with Keypoints-Guided Diffusion Models** <br>
*Ruixi You, Hecheng Jia, Feng Xu.* <br>
**SAR Image Translation**, Fudan University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.19798)] <br>

**Color Conditional Generation with Sliced Wasserstein Guidance** <br>
*Alexander Lobashev, Maria Larchenko, Dmitry Guskov.* <br>
**Image Style Transfer**, Skolkovo Institute of Science and Technology <br>
NeurIPS 2025. [[PDF](https://arxiv.org/abs/2503.19034)]
[[Github](https://github.com/alobashev/sw-guidance/)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/f093c712465ae554e7a14a23b04afbca-Abstract-Conference.html)] <br>

**DiffV2IR: Visible-to-Infrared Diffusion Model via Vision-Language Understanding** <br>
*Lingyan Ran, Lidong Wang, Guangcong Wang, Peng Wang, Yanning Zhang.* <br>
**Infrared Image Translation**, Northwestern Polytechnical University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.19012)]
[[Project](https://diffv2ir.github.io)]
[[Github](https://github.com/LidongWang-26/DiffV2IR)] <br>

**Single-Step Bidirectional Unpaired Image Translation Using Implicit Bridge Consistency Distillation** <br>
*Suhyeon Lee, Kwanyoung Kim, Jong Chul Ye.* <br>
**Base I2I Translation**, KAIST & Samsung Research <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.15056)]
[[Project](https://hyn2028.github.io/project_page/IBCD/index.html)] <br>

**ConsisLoRA: Enhancing Content and Style Consistency for LoRA-based Style Transfer** <br>
*Bolin Chen, Baoquan Zhao, Haoran Xie, Yi Cai, Qing Li, Xudong Mao.* <br>
**Image Style Transfer**, Sun Yat-sen University & Lingnan University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.10614)]
[[Project](https://consislora.github.io)]
[[Github](https://github.com/000linlin/ConsisLoRA)] <br>

**CM-Diff: A Single Generative Network for Bidirectional Cross-Modality Translation Diffusion Model Between Infrared and Visible Images** <br>
*Bin Hu, Chenqiang Gao, Shurui Liu, Junjie Guo, Fang Chen, Fangcen Liu.* <br>
**Infrared Image Translation**, Chongqing University of Posts and Telecommunications <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.09514)] <br>

**DyArtbank: Diverse Artistic Style Transfer via Pre-trained Stable Diffusion and Dynamic Style Prompt Artbank** <br>
*Zhanjie Zhang, Quanwei Zhang, Guangyuan Li, Junsheng Luan, Mengyuan Yang, Yun Wang, Lei Zhao.* <br>
**Image Style Transfer**, Zhejiang University & City University of Hong Kong <br>
Knowledge-Based Systems 2025. [[PDF](https://arxiv.org/abs/2503.08392)]
[[PDF(official)](https://www.sciencedirect.com/science/article/pii/S0950705125000073)]
[[Github](https://github.com/Jamie-Cheung/DyArtbank)] <br>

**AttenST: A Training-Free Attention-Driven Style Transfer Framework with Pre-Trained Diffusion Models** <br>
*Bo Huang, Wenlun Xu, Qizhuo Han, Haodong Jing, Ying Li.* <br>
**Image Style Transfer**, Northwestern Polytechnical University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2503.07307)] <br>

**SCSA: A Plug-and-Play Semantic Continuous-Sparse Attention for Arbitrary Semantic Style Transfer** <br>
*Chunnan Shang, Zhizhong Wang, Hongwei Wang, Xiangming Meng.* <br>
**Image Style Transfer**, Zhejiang University <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2503.04119)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Shang_SCSA_A_Plug-and-Play_Semantic_Continuous-Sparse_Attention_for_Arbitrary_Semantic_Style_CVPR_2025_paper.html)] <br>

**DiffuseFIST: A Fast Image-guided Style Transfer Method for Adapting Large-scale Diffusion Models** <br>
*Miaomiao Da, Qianyu Zhou, Ran Yi, Lizhuang Ma.* <br>
**Image Style Transfer**, Shanghai Jiao Tong University <br>
ICASSP 2025. [[PDF](https://ieeexplore.ieee.org/abstract/document/10889203)] <br>

**Unsupervised Image-to-Image Style Transfer via Dual-Condition Diffusion Models** <br>
*Anfei Fan, Jun Yang, Wei Li, Chiyu Zhang.* <br>
**Image Style Transfer**, Sichuan Normal University <br>
ICASSP 2025. [[PDF](https://ieeexplore.ieee.org/document/10889157)] <br>

**CAPAST: Content Affinity Preserved Arbitrary Style Transfer** <br>
*Xinyuan Zheng, Xiaojie Li, Canghong Shi, Jia He, Zhan Ao Huang, Xian Zhang.* <br>
**Image Style Transfer**, Chengdu University of Information Technology <br>
ICASSP 2025. [[PDF](https://ieeexplore.ieee.org/abstract/document/10890339)] <br>

**Low-Rank Transformer Adaptation for Arbitrary Style Transfer** <br>
*Wenjie Xu, Meichen Liu, Bihan Wen.* <br>
**Image Style Transfer**, Nanyang Technological University <br>
ICASSP 2025. [[PDF](https://ieeexplore.ieee.org/abstract/document/10887739)] <br>

**Dual-Modality Guided Artistic Style Transfer with Pre-trained Diffusion Models** <br>
*Jiaxiong Liu, Xiaolong Xiong, Jun Zhou.* <br>
**Image Style Transfer**, Southwest University <br>
ICASSP 2025. [[PDF](https://ieeexplore.ieee.org/abstract/document/10888654)]
[[Github](https://github.com/BBABM/DMG)] <br>

**SSDM: Generated image interaction method based on spatial sparsity for diffusion models** <br>
*Zhuochao Yang, Jingjing Liu, Haozhe Zhu, Jianhua Zhang, Wanquan Liu.* <br>
**Image Editing**, Shanghai University & Fudan University <br>
Neurocomputing 2025. [[PDF](https://www.sciencedirect.com/science/article/abs/pii/S0925231225004771)] <br>

**Attention Distillation: A Unified Approach to Visual Characteristics Transfer** <br>
*Yang Zhou, Xu Gao, Zichong Chen, Hui Huang.* <br>
**Image Style Transfer**, Shenzhen University <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2502.20235)]
[[Github](https://github.com/xugao97/AttentionDistillation)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Attention_Distillation_A_Unified_Approach_to_Visual_Characteristics_Transfer_CVPR_2025_paper.html)] <br>

**PQDAST: Depth-Aware Arbitrary Style Transfer for Games via Perceptual Quality-Guided Distillation** <br>
*Eleftherios Ioannou, Steve Maddock.* <br>
**Image Style Transfer**, The University of Sheffield <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.16996)] <br>

**PhotoDoodle: Learning Artistic Image Editing from Few-Shot Pairwise Data** <br>
*Shijie Huang, Yiren Song, Yuxuan Zhang, Hailong Guo, Xueyin Wang, Mike Zheng Shou, Jiaming Liu.* <br>
**Image Editing**, National University of Singapore & Tiamat <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.14397v1)]
[[Github](https://github.com/showlab/PhotoDoodle)] <br>

**SigStyle: Signature Style Transfer via Personalized Text-to-Image Models** <br>
*Ye Wang, Tongyuan Bai, Xuping Xie, Zili Yi, Yilin Wang, Rui Ma.* <br>
**Image Style Transfer**, Jilin University & Nanjing University & Adobe <br>
AAAI 2025. [[PDF](https://arxiv.org/abs/2502.13997)]
[[Github](https://github.com/wangyePHD/SigStyle)]
[[Project](https://wangyephd.github.io/projects/SigStyle/sigstyle.html)]
[[Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/32868)] <br>

**Image Inversion: A Survey from GANs to Diffusion and Beyond** <br>
*Yinan Chen, Jiangning Zhang, Yali Bi, Xiaobin Hu, Teng Hu, Zhucun Xue, Ran Yi, Yong Liu, Ying Tai.* <br>
**Else Papers**, Zhejiang University & Tencent <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.11974)]
[[Github](https://github.com/RyanChenYN/ImageInversion)] <br>

**Less is More: Masking Elements in Image Condition Features Avoids Content Leakages in Style Transfer Diffusion Models** <br>
*Lin Zhu, Xinbing Wang, Chenghu Zhou, Qinying Gu, Nanyang Ye.* <br>
**Image Style Transfer**,  Shanghai Jiao Tong University & Chinese Academy of Sciences & Shanghai AI Laboratory <br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2502.07466)]
[[Github](https://github.com/linllll/maskst)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a547d86953a4e36aa8a1390e6f4708e2-Abstract-Conference.html)] <br>

**UniDB: A Unified Diffusion Bridge Framework via Stochastic Optimal Control** <br>
*Kaizhen Zhu, Mokai Pan, Yuexin Ma, Yanwei Fu, Jingyi Yu, Jingya Wang, Ye Shi.* <br>
**Base I2I Translation**, ShanghaiTech University & Fudan University <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.05749)]
[[Github](https://github.com/UniDB-SOC/UniDB/)] <br>

**Inverse Bridge Matching Distillation** <br>
*Nikita Gushchin, David Li, Daniil Selikhanovych, Evgeny Burnaev, Dmitry Baranchuk, Alexander Korotin.* <br>
**Base I2I Translation**, Skolkovo Institute of Science and Technology & Yandex Research & HSE University & Artificial Intelligence Research Institute <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.01362)]
[[Github](https://github.com/ngushchin/IBMD)] <br>

**Style transfer as data augmentation: evaluating unpaired image-to-image translation models in mammography** <br>
*Emir Ahmed, Spencer A. Thomas, Ciaran Bench.* <br>
**Medical Image Translation**, National Physical Laboratory <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2502.02475)]
[[PDF(old)](https://arxiv.org/abs/2501.17570)] <br>

**Training-Free Style and Content Transfer by Leveraging U-Net Skip Connections in Stable Diffusion** <br>
*Ludovica Schaerf, Andrea Alfarano, Fabrizio Silvestri, Leonardo Impett.* <br>
**Image Style Transfer**, Max Planck Society University of Zurich Zurich <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.14524)] <br>

**Generating Realistic Forehead-Creases for User Verification via Conditioned Piecewise Polynomial Curves** <br>
*Abhishek Tandon, Geetanjali Sharma, Gaurav Jaswal, Aditya Nigam, Raghavendra Ramachandra.* <br>
**Base I2I Translation**, Indian Institute of Technology Mandi <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.13889)] <br>

**AMM-Diff: Adaptive Multi-Modality Diffusion Network for Missing Modality Imputation** <br>
*Aghiles Kebaili, Jérôme Lapuyade-Lahorgue, Pierre Vera, Su Ruan.* <br>
**Medical Image Translation**, University of Rouen-Normandy & CLCC Henri Becquerel <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.12840)] <br>

**EfficientVITON: An Efficient Virtual Try-On Model using Optimized Diffusion Process** <br>
*Mostafa Atef, Mariam Ayman, Ahmed Rashed, Ashrakat Saeed, Abdelrahman Saeed, Ahmed Fares.* <br>
**Virtual Try-On**, Egypt-Japan University of Science and Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.11776)] <br>

**StyleSSP: Sampling StartPoint Enhancement for Training-free Diffusion-based Method for Style Transfer** <br>
*Ruojun Xu, Weijie Xi, Xiaodi Wang, Yongbo Mao, Zach Cheng.* <br>
**Image Style Transfer**, Zhejiang University & Dcar <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2501.11319)]
[[Github](https://github.com/bytedance/StyleSSP)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_StyleSSP_Sampling_StartPoint_Enhancement_for_Training-free_Diffusion-based_Method_for_Style_CVPR_2025_paper.html)] <br>

**Origin Identification for Text-Guided Image-to-Image Diffusion Models** <br>
*Wenhao Wang, Yifan Sun, Zongxin Yang, Zhentao Tan, Zhengdong Hu, Yi Yang.* <br>
**Base I2I Translation**, University of Technology Sydney & Baidu Inc & Zhejiang University <br>
ICML 2025. [[PDF](https://arxiv.org/abs/2501.02376)]
[[Project](https://id2icml.github.io)] <br>

**ArtCrafter: Text-Image Aligning Style Transfer via Embedding Reframing** <br>
*Nisha Huang, Kaer Huang, Yifan Pu, Jiangshan Wang, Jie Guo, Yiqiang Yan, Xiu Li.* <br>
**Image Style Transfer**, Tsinghua University & Peng Cheng Laboratory & Lenovo Research <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.02064)] <br>

**Conditional Consistency Guided Image Translation and Enhancement** <br>
*Amil Bhagat, Milind Jain, A. V. Subramanyam.* <br>
**Base I2I Translation**, Indraprastha Institute of Information Technology <br>
arXiv 2025. [[PDF](https://arxiv.org/abs/2501.01223)]
[[Github](https://github.com/amilbhagat/Conditional-Consistency-Models)] <br>

**Conditional Balance: Improving Multi-Conditioning Trade-Offs in Image Generation** <br>
*Nadav Z. Cohen, Oron Nir, Ariel Shamir.* <br>
**Image Style Transfer**, Reichman University & Microsoft Corporation <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2412.19853)]
[[Project](https://nadavc220.github.io/conditional-balance.github.io/)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Cohen_Conditional_Balance_Improving_Multi-Conditioning_Trade-Offs_in_Image_Generation_CVPR_2025_paper.html)] <br>

**Diffusion-Based Conditional Image Editing through Optimized Inference with Guidance** <br>
*Hyunsoo Lee, Minsoo Kang, Bohyung Han.* <br>
**Base I2I Translation**, ECE & Seoul National University <br>
WACV 2025. [[PDF](https://arxiv.org/abs/2412.15798)] <br>

**Efficient Fine-Tuning and Concept Suppression for Pruned Diffusion Models** <br>
*Reza Shirkavand, Peiran Yu, Shangqian Gao, Gowthami Somepalli, Tom Goldstein, Heng Huang.* <br>
**Image Style Transfer**, University of Maryland & Florida State University <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2412.15341)]
[[Github](https://github.com/rezashkv/diffusion_pruning)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Shirkavand_Efficient_Fine-Tuning_and_Concept_Suppression_for_Pruned_Diffusion_Models_CVPR_2025_paper.html)] <br>

**LineArt: A Knowledge-guided Training-free High-quality Appearance Transfer for Design Drawing with Diffusion Model** <br>
*Xi Wang, Hongzhen Li, Heng Fang, Yichen Peng, Haoran Xie, Xi Yang, Chuntao Li.* <br>
**Image Style Transfer**, KTH Royal Institute of Technology & Tokyo Institute of Technology & Japan Advanced Institute of Science and Technology (JAIST) <br>
CVPR 2025. [[PDF](https://arxiv.org/abs/2412.11519)]
[[Project](https://meaoxixi.github.io/LineArt/)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_LineArt_A_Knowledge-guided_Training-free_High-quality_Appearance_Transfer_for_Design_Drawing_CVPR_2025_paper.html)] <br>

**Tuning Timestep-Distilled Diffusion Model Using Pairwise Sample Optimization** <br>
*Zichen Miao, Zhengyuan Yang, Kevin Lin, Ze Wang, Zicheng Liu, Lijuan Wang, Qiang Qiu.* <br>
**Image Style Transfer**, Purdue University & Microsoft & AMD <br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2410.03190)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/243697ace81f57daef8737ff2c5cffd3-Abstract-Conference.html)] <br>

**Prompt-Softbox-Prompt: A Free-Text Embedding Control for Image Editing** <br>
*Yitong Yang, Yinglin Wang, Jing Wang, Tian Zhang.* <br>
**Image Editing**, Shanghai University of Finance and Economics <br>
ACMMM 2025. [[PDF](https://arxiv.org/pdf/2408.13623)]
[[Github](https://github.com/huggingface/diffusers)]
[[Github](https://github.com/yangyt46/PSP)] <br>

**Diffusion Bridge Implicit Models** <br>
*Kaiwen Zheng, Guande He, Jianfei Chen, Fan Bao, Jun Zhu.* <br>
**Base I2I Translation**,  Tsinghua University & Shengshu Technology <br>
ICLR 2025. [[PDF](https://arxiv.org/abs/2405.15885)]
[[Github](https://github.com/thu-ml/DiffusionBridge)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/cb8a878dc5afad501474efa554926771-Abstract-Conference.html)] <br>

**GeoDiffuser: Geometry-Based Image Editing with Diffusion Models** <br>
*Rahul Sajnani, Jeroen Vanbaar, Jie Min, Kapil Katyal, Srinath Sridhar.* <br>
**Image Editing**, Brown University & Amazon Robotics <br>
WACV 2025. [[PDF](https://arxiv.org/abs/2404.14403)] <br>

**Dequantization and Color Transfer with Diffusion Models** <br>
*Vaibhav Vavilala, David Forsyth.* <br>
WACV 2025. [[PDF](https://arxiv.org/abs/2307.02698)] <br>

**StyO: Stylize Your Face in Only One-shot** <br>
*Bonan Li, Zicheng Zhang, Xuecheng Nie, Congying Han, Yinhan Hu, Tiande Guo.* <br>
AAAI 2025. [[PDF](https://arxiv.org/abs/2303.03231)]
[[Github](https://github.com/JiauZhang/StyO)] <br>

## 2024

**Towards Efficient Exemplar Based Image Editing with Multimodal VLMs** <br>
*Avadhoot Jadhav, Ashutosh Srivastava, Abhinav Java, Silky Singh, Tarun Ram Menta, Surgan Jandial, Balaji Krishnamurthy.* <br>
**Image Editing**, Adobe MDSR & Indian Institute of Technology, Bombay & Indian Institute of Technology, Roorkee & Microsoft Research & Stanford University & Carnegie Mellon University <br>
ECCV 2024 Workshops (AI4VA). [[PDF](https://arxiv.org/abs/2506.20155)] <br>

**EasyRef: Omni-Generalized Group Image Reference for Diffusion Models via Multimodal LLM** <br>
*Zhuofan Zong, Dongzhi Jiang, Bingqi Ma, Guanglu Song, Hao Shao, Dazhong Shen, Yu Liu, Hongsheng Li.* <br>
**Image Style Transfer**, CUHK MMLab SenseTime Research Shanghai AI Laboratory <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2412.09618)]
[[Project](https://easyref-gen.github.io/)] <br>

**UniVST: A Unified Framework for Training-free Localized Video Style Transfer** <br>
*Quanjian Song, Mingbao Lin, Wengyi Zhan, Shuicheng Yan, Liujuan Cao, Rongrong Ji.* <br>
**Video Style Transfer** <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2410.20084)]
[[Github](https://github.com/QuanjianSong/UniVST)]
[[Project](https://quanjiansong.github.io/projects/UniVST)] <br>

**Conditional Image Synthesis with Diffusion Models: A Survey** <br>
*Zheyuan Zhan, Defang Chen, Jian-Ping Mei, Zhenghe Zhao, Jiawei Chen, Chun Chen, Siwei Lyu, Can Wang.* <br>
**Survey**, State Key Laboratory of Blockchain and Data Security, Zhejiang University & College of Computer Science, Zhejiang University & University at Buffalo, State University of New York & College of Computer Science, Zhejiang University of Technology & Hangzhou High-Tech Zone (Binjiang) Institute of Blockchain and Data Security <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2409.19365)]
[[Github](https://github.com/zju-pi/Awesome-Conditional-Diffusion-Models)] <br>

**Latent Space Disentanglement in Diffusion Transformers Enables Zero-shot Fine-grained Semantic Editing** <br>
*Zitao Shuai, Chenwei Wu, Zhengxu Tang, Bowen Song, Liyue Shen.* <br>
**Image Editing**, University of Michigan <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.13335)] <br>

**Diffusion-Based Visual Art Creation: A Survey and New Perspectives** <br>
*Bingyuan Wang, Qifeng Chen, Zeyu Wang.* <br>
**Survey**, The Hong Kong University of Science and Technology (Guangzhou), No. 1, Duxue Road, Dongchong Town, Nansha District., Guangzhou, Guangdong, China & The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong SAR, China <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.12128)] <br>

**Live2Diff: Live Stream Translation via Uni-directional Attention in Video Diffusion Models** <br>
*Zhening Xing, Gereon Fox, Yanhong Zeng, Xingang Pan, Mohamed Elgharib, Christian Theobalt, Kai Chen.* <br>
**Video Style Transfer**, Shanghai Artificial Intelligence Laboratory & Saarland Informatics Campus, Max Planck Institute for Informatics & S-Lab, Nanyang Technological University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.08701)]
[[Project](https://live2diff.github.io/)] <br>

**StyleShot: A Snapshot on Any Style** <br>
*Junyao Gao, Yanchen Liu, Yanan Sun, Yinhao Tang, Yanhong Zeng, Kai Chen, Cairong Zhao.* <br>
**Image Style Transfer**, Tongji University & Shanghai AI Laboratory <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.01414)]
[[Project](https://styleshot.github.io/)] <br>

**ArtWeaver: Advanced Dynamic Style Integration via Diffusion Model** <br>
*Chengming Xu, Kai Hu, Qilin Wang, Donghao Luo, Jiangning Zhang, Xiaobin Hu, Yanwei Fu, Chengjie Wang.* <br>
**Image Style Transfer**, Youtu Lab, Tencent & Carnegie Mellon University & Fudan University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2405.15287)] <br>

**Customizing Text-to-Image Models with a Single Image Pair** <br>
*Maxwell Jones, Sheng-Yu Wang, Nupur Kumari, David Bau, Jun-Yan Zhu.* <br>
**Image Style Transfer**, Carnegie Mellon University & Northeastern University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2405.01536)]
[[Project](https://paircustomization.github.io/)] <br>

**StyleBooth: Image Style Editing with Multimodal Instruction** <br>
*Zhen Han, Chaojie Mao, Zeyinzi Jiang, Yulin Pan, Jingfeng Zhang.* <br>
**Image Style Transfer**, Tongyi Lab, Alibaba Group <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2404.12154)]
[[Project](https://ali-vilab.github.io/stylebooth-page/)] <br>

**Break-for-Make: Modular Low-Rank Adaptations for Composable Content-Style Customization** <br>
*Yu Xu, Fan Tang, Juan Cao, Yuxin Zhang, Oliver Deussen, Weiming Dong, Jintao Li, Tong-Yee Lee.* <br>
**Image Style Transfer**, Institute of Computing Technology, Chinese Academy of Sciences & University of Chinese Academy of Sciences & Institute of Automation, Chinese Academy of Sciences & University of Konstanz & National Cheng-Kung University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2403.19456)] <br>

**Implicit Style-Content Separation using B-LoRA** <br>
*Yarden Frenkel, Yael Vinker, Ariel Shamir, Daniel Cohen-Or.* <br>
**Image Style Transfer**, Tel Aviv University & Reichman University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2403.14572)]
[[Project](https://b-lora.github.io/B-LoRA/)] <br>

**AnyV2V: A Tuning-Free Framework For Any Video-to-Video Editing Tasks** <br>
*Max Ku, Cong Wei, Weiming Ren, Harry Yang, Wenhu Chen.* <br>
**Video Style Transfer**, University of Waterloo & Harmony.AI <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2403.14468)]
[[Github](https://github.com/TIGER-AI-Lab/AnyV2V)] <br>

**FRESCO: Spatial-Temporal Correspondence for Zero-Shot Video Translation** <br>
*Shuai Yang, Yifan Zhou, Ziwei Liu, Chen Change Loy.* <br>
**Video Style Transfer**, Wangxuan Institute of Computer Technology, Peking University & S-Lab, Nanyang Technological University <br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2403.12962)]
[[Github](https://github.com/williamyang1991/FRESCO)] <br>

**Diffusion Model-Based Image Editing: A Survey** <br>
*Yi Huang, Jiancheng Huang, Yifan Liu, Mingfu Yan, Jiaxi Lv, Jianzhuang Liu, Wei Xiong, He Zhang, Liangliang Cao, Shifeng Chen.* <br>
**Survey** <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2402.17525)]
[[Github](https://github.com/SiatMMLab/Awesome-Diffusion-Model-Based-Image-Editing-Methods)] <br>

**Visual Style Prompting with Swapping Self-Attention** <br>
*Jaeseok Jeong, Junho Kim, Yunjey Choi, Gayoung Lee, Youngjung Uh.* <br>
**Image Style Transfer**, Yonsei University & NAVER AI Lab <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2402.12974)]
[[Project](https://curryjung.github.io/VisualStylePrompt/)] <br>

**Diffutoon: High-Resolution Editable Toon Shading via Diffusion Models** <br>
*Zhongjie Duan, Chengyu Wang, Cen Chen, Weining Qian, Jun Huang.* <br>
**Video Style Transfer**, East China Normal University, Shanghai, China & Alibaba Group, Hangzhou, China <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2401.16224)]
[[Project](https://ecnu-cilab.github.io/DiffutoonProjectPage/)] <br>

**d-Sketch: Improving Visual Fidelity of Sketch-to-Image Translation with Pretrained Latent Diffusion Models without Retraining** <br>
*Prasun Roy, Saumik Bhattacharya, Subhankar Ghosh, Umapada Pal, Michael Blumenstein.* <br>
**Sketch-to-Image Translation**, University of Technology Sydney <br>
ICPR 2024. [[PDF](https://arxiv.org/abs/2502.14007)]
[[Github](https://github.com/prasunroy/dsketch)]<br>

**StyleRWKV: High-Quality and High-Efficiency Style Transfer with RWKV-like Architecture** <br>
*Miaomiao Dai, Qianyu Zhou, Lizhuang Ma.* <br>
**Image Style Transfer**, Shanghai Jiao Tong University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2412.19535)] <br>

**Single Trajectory Distillation for Accelerating Image and Video Style Transfer** <br>
*Sijie Xu, Runqi Wang, Wei Zhu, Dejia Song, Nemo Chen, Xu Tang, Yao Hu.* <br>
**Image Style Transfer**, Xiaohongshu & ShanghaiTech University<br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2412.18945)]
[[Project](https://single-trajectory-distillation.github.io/)] <br>

**Unpaired Multi-Domain Histopathology Virtual Staining using Dual Path Prompted Inversion** <br>
*Bing Xiong, Yue Peng, RanRan Zhang, Fuqiang Chen, JiaYe He, Wenjian Qin.* <br>
**Virtual Staining**, Shenzhen Institutes of Advanced Technology <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2412.11106v1)]
[[Github](https://github.com/bairdxiong/StainPromptInversion)] <br>

**SHMT: Self-supervised Hierarchical Makeup Transfer via Latent Diffusion Models** <br>
*Zhaoyang Sun, Shengwu Xiong, Yaxiong Chen, Fei Du, Weihua Chen, Fan Wang, Yi Rong.* <br>
**Image Style Transfer**, Wuhan University of Technology & Alibaba & Hupan Laboratory & Shanghai AI Laboratory <br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2412.11058)]
[[Github](https://github.com/Snowfallingplum/SHMT)] <br>

**Learning Artistic Signatures: Symmetry Discovery and Style Transfer** <br>
*Emma Finn, T. Anderson Keller, Emmanouil Theodosis, Demba E. Ba.* <br>
**Image Style Transfer**, Harvard University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2412.04441)] <br>

**Structure-Aware Stylized Image Synthesis for Robust Medical Image Segmentation** <br>
*Jie Bao, Zhixin Zhou, Wen Jung Li, Rui Luo.* <br>
**Medical Image Translation**, Huaiyin Institute of Technology & Alpha Benito Research & City University of Hong Kong <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2412.04296)]
[[Github](https://github.com/luo-lorry/Stylized-Medical-Segmentation)] <br>

**Z-STAR+: A Zero-shot Style Transfer Method via Adjusting Style Distribution** <br>
*Yingying Deng, Xiangyu He, Fan Tang, Weiming Dong.* <br>
**Image Style Transfer**, Chinese Academy of Sciences <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2411.19231)] <br>

**Latent Schrodinger Bridge: Prompting Latent Diffusion for Fast Unpaired Image-to-Image Translation** <br>
*Jeongsol Kim, Beomsu Kim, Jong Chul Ye.* <br>
**Base I2I Translation**, KAIST <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2411.14863)] <br>

**C-DiffSET: Leveraging Latent Diffusion for SAR-to-EO Image Translation with Confidence-Guided Reliable Object Generation** <br>
*Jeonghyeok Do, Jaehyup Lee, Munchurl Kim.* <br>
**SAR Image Translation**, KAIST & KNU <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2411.10788)]
[[Project](https://kaist-viclab.github.io/C-DiffSET_site)]
[[Github](https://github.com/KAIST-VICLab/C-DiffSET)] <br>

**Towards Multi-View Consistent Style Transfer with One-Step Diffusion via Vision Conditioning** <br>
*Yushen Zuo, Jun Xiao, Kin-Chung Chan, Rongkang Dong, Cuixin Yang, Zongqi He, Hao Xie, Kin-Man Lam.* <br>
**Image Style Transfer**, The Hong Kong Polytechnic University <br>
ECCV 2024 Workshops. [[PDF](https://arxiv.org/abs/2411.10130)]
[[Github](https://github.com/YushenZuo/OSDiffST)] <br>

**Diff-TST: Diffusion model for one-shot text-image style transfer** <br>
*Sizhe Pang, Xinyuan Chen, Yangchen Xie, Hongjian Zhan, Bing Yin, Yue Lu.* <br>
**Image Style Transfer**, East China Normal University & Shanghai AI Lab <br>
Expert Systems With Applications. [[PDF](https://www.sciencedirect.com/science/article/pii/S0957417424026149)] <br>

**Multi-layer Feature Fusion based Image Style Transfer with Arbitrary Text Condition** <br>
*Yue Yua, Jingshuo Xing, Nengli Li.* <br>
**Image Style Transfer**, Beijing Institute of Technology <br>
Signal Processing: Image Communication. [[PDF](https://www.sciencedirect.com/science/article/pii/S0923596524001449)] <br>

**DiT4Edit: Diffusion Transformer for Image Editing** <br>
*Kunyu Feng, Yue Ma, Bingyuan Wang, Chenyang Qi, Haozhe Chen, Qifeng Chen, Zeyu Wang.* <br>
**Image Editing**, PKU & HKUST <br>
arXiv 2024. [[PDF](https://arxiv.org/pdf/2411.03286)]
[[Github](https://github.com/fkyyyy/DiT4Edit)] <br>

**AdvI2I: Adversarial Image Attack on Image-to-Image Diffusion models** <br>
*Yaopei Zeng, Yuanpu Cao, Bochuan Cao, Yurui Chang, Jinghui Chen, Lu Lin.* <br>
**Base I2I Translation**, Pennsylvania State University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2410.21471)]
[[Github](https://github.com/Spinozaaa/AdvI2I)]<br>

**Beyond Color and Lines: Zero-Shot Style-Specific Image Variations with Coordinated Semantics** <br>
*Jinghao Hu, Yuhe Zhang, GuoHua Geng, Liuyuxin Yang, JiaRui Yan, Jingtao Cheng, YaDong Zhang, Kang Li.* <br>
**Image Style Transfer**, Northwest University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2410.18537)] <br>

**StyleAdapter: A Unified Stylized Image Generation Model** <br>
*Zhouxia Wang, Xintao Wang, Liangbin Xie, Zhongang Qi, Ying Shan, Wenping Wang, Ping Luo.* <br>
**Image Style Transfer**, The University of Hong Kong & Tencent PCG <br>
IJCV 2024. [[PDF1](https://link.springer.com/article/10.1007/s11263-024-02253-x)]
[[PDF2](https://openreview.net/pdf?id=NaxbdRi8Rv)] <br>
[[PDF](https://arxiv.org/abs/2309.01770)] <br>

**FashionR2R: Texture-preserving Rendered-to-Real Image Translation with Diffusion Models** <br>
*Rui Hu, Qian He, Gaofeng He, Jiedong Zhuang, Huang Chen, Huafeng Liu, Huamin Wang.* <br>
**Else Papers**, Zhejiang University & Style3D Research <br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2410.14429)]
[[Project](https://rickhh.github.io/FashionR2R/)]
[[Github](https://github.com/Style3D/FashionR2R)] <br>

**HiCo: Hierarchical Controllable Diffusion Model for Layout-to-image Generation** <br>
*Bo Cheng, Yuhang Ma, Liebucha Wu, Shanyuan Liu, Ao Ma, Xiaoyu Wu, Dawei Leng, Yuhui Yin.* <br>
**Layout2Image**, 360 AI Research <br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2410.14324)]
[[Github](https://github.com/360CVGroup/HiCo_T2I)] <br>

**Harnessing the Latent Diffusion Model for Training-Free Image Style Transfer** <br>
*Kento Masui, Mayu Otani, Masahiro Nomura, Hideki Nakayama.* <br>
**Image Style Transfer**, CyberAgent <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2410.01366)] <br>

**PixelShuffler: A Simple Image Translation Through Pixel Rearrangement** <br>
*Omar Zamzam.* <br>
**Image Style Transfer**, University of Southern California <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2410.03021)]
[[Github](https://github.com/OmarSZamzam/PixelShuffler)] <br>

**EBDM: Exemplar-guided Image Translation with Brownian-bridge Diffusion Models** <br>
*Eungbean Lee, Somi Jeong, Kwanghoon Sohn.* <br>
**Base I2I Translation**, Yonsei University & NAVER LABS & KIST <br>
ECCV 2024, [[PDF](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/02096.pdf)]
[[Github](https://github.com/eungbean/ebdm)] <br>

**A Training-Free Latent Diffusion Style Transfer Method** <br>
*Zhengtao Xiang, Xing Wan, Libo Xu, Xin Yu, Yuhan Mao.* <br>
**Image Style Transfer**, Hubei University of Automotive Technology <br>
Information, [[PDF](https://www.mdpi.com/2078-2489/15/10/588/pdf?version=1727347041)] <br>

**Cross-conditioned Diffusion Model for Medical Image to Image Translation** <br>
*Zhaohu Xing, Sicheng Yang, Sixiang Chen, Tian Ye, Yijun Yang, Jing Qin, Lei Zhu.* <br>
**Medical Image Translation**, HKUST <br>
miccai 2024. [[PDF](https://arxiv.org/abs/2409.08500)] <br>

**MagicStyle: Portrait Stylization Based on Reference Image** <br>
*Zhaoli Deng, Kaibin Zhou, Fanyi Wang, Zhenpeng Mi.* <br>
**Image Style Transfer**, Honor & Tongji University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2409.08156)] <br>

**Diffusion-Based Image-to-Image Translation by Noise Correction via Prompt Interpolation** <br>
*Junsung Lee, Minsoo Kang, Bohyung Han.* <br>
**Base I2I Translation**, ECE & Seoul National University <br>
ECCV 2024, [[PDF](https://arxiv.org/abs/2409.08077)]
[[Github](https://github.com/jslee525/PIC)] <br>

**TCDiff: Triple Condition Diffusion Model with 3D Constraints for Stylizing Synthetic Faces** <br>
*Bernardo Biesseck, Pedro Vidal, Luiz Coelho, Roger Granada, David Menotti.* <br>
**Face style**, Federal University of Parana <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2409.03600)]
[[Github](https://github.com/BOVIFOCR/tcdiff)] <br>

**StyleTokenizer: Defining Image Style by a Single Instance for Controlling Diffusion Models** <br>
*Wen Li, Muyuan Fang, Cheng Zou, Biao Gong, Ruobing Zheng, Meng Wang, Jingdong Chen, Ming Yang.* <br>
**Image Style Transfer**, Ant Group <br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2409.02543)]
[[Github](https://github.com/alipay/style-tokenizer)] <br>

**Training-free Color-Style Disentanglement for Constrained Text-to-Image Synthesis** <br>
*Aishwarya Agarwal, Srikrishna Karanam, Balaji Vasan Srinivasan.* <br>
**Image Style Transfer**, Adobe <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2409.02429)] <br>

**Seed-to-Seed: Unpaired Image Translation in Diffusion Seed Space** <br>
*Or Greenberg, Eran Kishon, Dani Lischinski.* <br>
**Base I2I Translation**, The Hebrew University of Jerusalem & GM R&D <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2409.00654)] <br>

**JieHua Paintings Style Feature Extracting Model using Stable Diffusion with ControlNet** <br>
*Yujia Gu, Haofeng Li, Xinyu Fang, Zihan Peng, Yinan Peng.* <br>
**Image Style Transfer**, California State University et al. <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.11744)] <br>

**FAGStyle: Feature Augmentation on Geodesic Surface for Zero-shot Text-guided Diffusion Image Style Transfer** <br>
*Yuexing Han, Liheng Ruan, Bing Wang.* <br>
**Image Style Transfer**, Shanghai University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.10533)]
[[Github](https://github.com/P2i42/FAGStyle)] <br>

**SurgicaL-CD: Generating Surgical Images via Unpaired Image Translation with Latent Consistency Diffusion Models** <br>
*Danush Kumar Venkatesh, Dominik Rivoir, Micha Pfeiffer, Stefanie Speidel.* <br>
**Medical Image Translation**, NCT/UCC Dresden et al. <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.09822)]
[[Github](https://gitlab.com/nct_tso_public/gan2diffusion)] <br>

**Unpaired Volumetric Harmonization of Brain MRI with Conditional Latent Diffusion** <br>
*Mengqi Wu, Minhui Yu, Shuaiming Jing, Pew-Thian Yap, Zhengwu Zhang, Mingxia Liu.* <br>
**Medical Image Translation**, University of North Carolina <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.09315)]
[[Github](https://github.com/MW1798/HCLD)] <br>

**Conditional Brownian Bridge Diffusion Model for VHR SAR to Optical Image Translation** <br>
*Seon-Hoon Kim, Dae-won Chung.* <br>
**SAR Image Translation**, Korea National University of Science and Technology et al. <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.07947)]
[[Github](https://github.com/egshkim/ConditionalBBDM-for-VHR-SAR-to-Optical)] <br>

**D2Styler: Advancing Arbitrary Style Transfer with Discrete Diffusion Methods** <br>
*Onkar Susladkar, Gayatri Deshmukh, Sparsh Mittal, Parth Shastri.* <br>
**Image Style Transfer**, Indian Institute of Technology et al. <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.03558)]
[[Github](https://github.com/onkarsus13/d2styler)] <br>

**FastEdit: Fast Text-Guided Single-Image Editing via Semantic-Aware Diffusion Fine-Tuning** <br>
*Zhi Chen, Zecheng Zhao, Yadan Luo, Zi Huang.* <br>
**Image Editing**, University of Queensland <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.03355)] <br>

**Smoothed Energy Guidance: Guiding Diffusion Models with Reduced Energy Curvature of Attention** <br>
*Susung Hong.* <br>
**Else Papers**, Korea University<br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2408.00760)]
[[Github](https://github.com/susunghong/seg-sdxl)] <br>

**TurboEdit: Text-Based Image Editing Using Few-Step Diffusion Models** <br>
*Gilad Deutch, Rinon Gal, Daniel Garibi, Or Patashnik, Daniel Cohen-Or.* <br>
**Image Editing**, Tel-Aviv University & NVIDIA <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2408.00735)]
[[Github](https://github.com/GiilDe/turbo-edit)]
[[Project](https://turboedit-paper.github.io/)] <br>

**$Z^*$: Zero-shot Style Transfer via Attention Rearrangement** <br>
*Yingying Deng, Xiangyu He, Fan Tang, Weiming Dong.* <br>
**Image Style Transfer**, Chinese Academy of Sciences <br>
CVPR2024. [[PDF](https://openaccess.thecvf.com/content/CVPR2024/papers/Deng_Z_Zero-shot_Style_Transfer_via_Attention_Reweighting_CVPR_2024_paper.pdf)]
[[PDF(old)](https://arxiv.org/abs/2311.16491)]
[[Github](https://github.com/HolmesShuan/Zero-shot-Style-Transfer-via-Attention-Rearrangement)] <br>

**A Diffusion Model Translator for Efficient Image-to-Image Translation** <br>
*Mengfei Xia, Yu Zhou, Ran Yi, Yong-Jin Liu, Wenping Wang.* <br>
**Base I2I Translation**, Tsinghua University & Shanghai Jiao Tong University & Texas A&M University <br>
TPAMI 2024. [[PDF](https://ieeexplore.ieee.org/abstract/document/10614866)]
[[Github](https://github.com/THU-LYJ-Lab/dmt)] <br>
[[PDF](https://arxiv.org/abs/2502.00307)] <br>

**InstantStyle-Plus: Style Transfer with Content-Preserving in Text-to-Image Generation** <br>
*Haofan Wang, Peng Xing, Renyuan Huang, Hao Ai, Qixun Wang, Xu Bai.* <br>
**Image Style Transfer**, InstantX Team <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.00788)]
[[Project](instantstyle-plus.github.io)]
[[Github](https://github.com/instantx-research/instantstyle-plus)] <br>

**SAR to Optical Image Translation with Color Supervised Diffusion Model** <br>
*Xinyu Bai, Feng Xu.* <br>
**SAR Image Translation**, Fudan University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.16921)] <br>

**A Survey of Text Style Transfer: Applications and Ethical Implications** <br>
*Sourabrata Mukherjee, Mateusz Lango, Zdenek Kasner, Ondrej Dušek.* <br>
**Else Papers**, Charles University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.16737)] <br>

**SMooDi: Stylized Motion Diffusion Model** <br>
*Lei Zhong, Yiming Xie, Varun Jampani, Deqing Sun, Huaizu Jiang.* <br>
**Motion Transfer**, Northeastern University & Stability AI & Google Research <br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2407.12783)]
[[Github](https://github.com/neu-vi/SMooDi)]
[[Project](https://neu-vi.github.io/SMooDi/)] <br>

**PID: Physics-Informed Diffusion Model for Infrared Image Generation** <br>
*Fangyuan Mao, Jilin Mei, Shun Lu, Fuyang Liu, Liang Chen, Fangzhou Zhao, Yu Hu.* <br>
**Infrared Image Translation**, Chinese Academy of Sciences <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.09299)]
[[Github](https://github.com/fangyuanmao/pid)] <br>

**AirSketch: Generative Motion to Sketch** <br>
*Hui Xian Grace Lim, Xuanming Cui, Yogesh S Rawat, Ser-Nam Lim.* <br>
**Else Papers**, University of Central Florida <br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2407.08906)]
[[Github](https://github.com/hxgr4ce/AirSketch)] <br>

**VisioBlend: Sketch and Stroke-Guided Denoising Diffusion Probabilistic Model for Realistic Image Generation** <br>
*Harshkumar Devmurari, Gautham Kuckian, Prajjwal Vishwakarma, Krunali Vartak.* <br>
**Sketch-to-Image Translation**, Vidyavardhini’s College of Engineering and Technology <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.05209)] <br>

**Slice-Consistent 3D Volumetric Brain CT-to-MRI Translation with 2D Brownian Bridge Diffusion Model** <br>
*Kyobin Choo, Youngjun Jun, Mijin Yun, Seong Jae Hwang.* <br>
**Medical Image Translation**, Yonsei University <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2407.05059)]
[[Github](https://github.com/MICV-yonsei/CT2MRI)] <br>

**Every Pixel Has its Moments: Ultra-High-Resolution Unpaired Image-to-Image Translation via Dense Normalization** <br>
*Ming-Yang Ho, Che-Ming Wu, Min-Sheng Wu, Yufeng Jane Tseng.* <br>
**Base I2I Translation**, National Taiwan University & Amazon Web Services & aetherAI <br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2407.04245)]
[[Project](https://kaminyou.com/Dense-Normalization/)]
[[Github](https://github.com/Kaminyou/Dense-Normalization)] <br>

**Frequency-Controlled Diffusion Model for Versatile Text-Guided Image-to-Image Translation** <br>
*Xiang Gao, Zhengbo Xu, Junhan Zhao, Jiaying Liu.* <br>
**Base I2I Translation**, Peking University <br>
AAAI 2024. [[PDF](https://arxiv.org/abs/2407.03006)]
[[Github](https://github.com/xianggao1102/fcdiffusion)]
[[Project](https://xianggao1102.github.io/FCDiffusion/)] <br>

**MUMU: Bootstrapping Multimodal Image Generation from Text-to-Image Data** <br>
*William Berman, Alexander Peysakhovich.* <br>
**Else Papers**, Residence Sutter Hill Ventures <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2406.18790)] <br>

**Regularized Distribution Matching Distillation for One-step Unpaired Image-to-Image Translation** <br>
*Denis Rakitin, Ivan Shchekotov, Dmitry Vetrov.* <br>
**Base I2I Translation**, HSE University <br>
ICML 2024 workshop. [[PDF](https://arxiv.org/abs/2406.14762)] <br>

**AnyTrans: Translate AnyText in the Image with Large Scale Models** <br>
*Zhipeng Qian, Pei Zhang, Baosong Yang, Kai Fan, Yiwei Ma, Derek F. Wong, Xiaoshuai Sun, Rongrong Ji.* <br>
**Else Papers**, Xiamen University & Alibaba Group Inc <br>
EMNLP 2024. [[PDF](https://arxiv.org/abs/2406.11432)]
[[Github](https://github.com/qzp2018/AnyTrans)] <br>

**Rethinking Score Distillation as a Bridge Between Image Distributions** <br>
*David McAllister, Songwei Ge, Jia-Bin Huang, David W. Jacobs, Alexei A. Efros, Aleksander Holynski, Angjoo Kanazawa.* <br>
**Else Papers**, UC Berkeley & University of Maryland <br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2406.09417)]
[[Project](https://sds-bridge.github.io/)]
[[Github](https://github.com/davidmcall/SDS-Bridge)] <br>

**PASTA: Pathology-Aware MRI to PET Cross-Modal Translation with Diffusion Models** <br>
*Yitong Li, Igor Yakushev, Dennis M. Hedderich, Christian Wachinger.* <br>
**Medical Image Translation**, Technical University of Munich & MCML <br>
MICCAI 2024. [[PDF](https://arxiv.org/abs/2405.16942)]
[[Github](https://github.com/ai-med/pasta)] <br>

**Fast-DDPM: Fast Denoising Diffusion Probabilistic Models for Medical Image-to-Image Generation** <br>
*Hongxu Jiang, Muhammad Imran, Linhai Ma, Teng Zhang, Yuyin Zhou, Muxuan Liang, Kuang Gong, Wei Shao.* <br>
**Medical Image Translation**, University of Florida & University of California <br>
arXiv 2024, [[PDF](https://arxiv.org/abs/2405.14802)]
[[Github](https://github.com/mirthai/fast-ddpm)] <br>

**Self-Consistent Recursive Diffusion Bridge for Medical Image Translation** <br>
*Jose-Luis Poza-Lujan, Pedro Uribe-Chavert, Juan-Luis Posadas-Yagüe.* <br>
**Medical Image Translation**, Bilkent University & University of Illinois Urbana-Champaign <br>
arXiv 2024, [[PDF](http://arxiv.org/abs/2405.06789v1)]
[[PDF(old)](https://arxiv.org/abs/2405.06789)]
[[Github](https://github.com/icon-lab/SelfRDB)] <br>

**F2FLDM: Latent Diffusion Models with Histopathology Pre-Trained Embeddings for Unpaired Frozen Section to FFPE Translation** <br>
*Man M. Ho, Shikha Dubey, Yosep Chong, Beatrice Knudsen, Tolga Tasdizen.* <br>
**Medical Image Translation**, University of Utah & The Catholic University of Korea College of Medicine <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2404.12650)]
[[Github](https://github.com/minhmanho/f2f_ldm)]
[[Project](https://minhmanho.github.io/f2f_ldm/)] <br>

**Towards Highly Realistic Artistic Style Transfer via Stable Diffusion with Step-aware and Layer-aware Prompt** <br>
*Zhanjie Zhang, Quanwei Zhang, Huaizhong Lin, Wei Xing, Juncheng Mo, Shuaicheng Huang, Jinheng Xie, Guangyuan Li, Junsheng Luan, Lei Zhao, Dalong Zhang, Lixia Chen.* <br>
**Image Style Transfer**, Zhejiang University <br>
IJCAI 2024. [[PDF](https://arxiv.org/abs/2404.11474)]
[[Github](https://github.com/jamie-cheung/lsast)] <br>

**Multi-Sensor Diffusion-Driven Optical Image Translation for Large-Scale Applications** <br>
*Joao Gabriel Vinholi, Marco Chini, Anis Amziane, Renato Machado, Danilo Silva, Patrick Matgen.* <br>
**Base I2I Translation**, Luxembourg Institute of Science and Technology <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2404.11243)] <br>

**MultiColor: Image Colorization by Learning from Multiple Color Spaces** <br>
*Xiangcheng Du, Zhao Zhou, Xingjiao Wu, Yanlong Wang, Zhuoyao Wang, Yingbin Zheng, Cheng Jin.* <br>
**Image Colorization**, Fudan University <br>
ACMMM 2024. [[PDF](https://openreview.net/pdf?id=Zo4P2F7xLY)] <br>

**Tackling Structural Hallucination in Image Translation with Local Diffusion** <br>
*Seunghoi Kim, Chen Jin, Tom Diethe, Matteo Figini, Henry F. J. Tregidgo, Asher Mullokandov, Philip Teare, Daniel C. Alexander.* <br>
**Base I2I Translation**, University College London <br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2404.05980)]
[[Github](https://github.com/edshkim98/LocalDiffusion-Hallucination)] <br>

**Automatic Controllable Colorization via Imagination** <br>
*Xiaoyan Cong, Yue Wu, Qifeng Chen, Chenyang Lei.* <br>
**Image Colorization**, CAIR, HKISI-CAS et al. <br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2404.05661)]
[[Project](https://xy-cong.github.io/imagine-colorization/)]
[[Github](https://github.com/xy-cong/imagine-colorization)] <br>

**InstantStyle: Free Lunch towards Style-Preserving in Text-to-Image Generation** <br>
*Haofan Wang, Matteo Spinelli, Qixun Wang, Xu Bai, Zekui Qin, Anthony Chen.* <br>
**Image Style Transfer**, InstantX Team <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2404.02733)]
[[Project](https://instantstyle.github.io)]
[[Github](https://github.com/instantX-research/InstantStyle)]
[[Github](https://github.com/InstantStyle/InstantStyle)] <br>

**DEADiff: An Efficient Stylization Diffusion Model with Disentangled Representations** <br>
*Tianhao Qi, Shancheng Fang, Yanze Wu, Hongtao Xie, Jiawei Liu, Lang Chen, Qian He, Yongdong Zhang.* <br>
**Image Style Transfer**, University of Science and Technology of China & ByteDance <br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2403.06951)]
[[PDF2](https://openaccess.thecvf.com/content/CVPR2024/papers/Qi_DEADiff_An_Efficient_Stylization_Diffusion_Model_with_Disentangled_Representations_CVPR_2024_paper.pdf)]
[[Project](https://tianhao-qi.github.io/DEADiff/)]
[[Github](https://github.com/bytedance/DEADiff)] <br>

**One-Shot Structure-Aware Stylized Image Synthesis** <br>
*Hansam Cho, Jonghyun Lee, Seunggyu Chang, Yonghyun Jeong.* <br>
**Image Style Transfer**, Korea University & NAVER Cloud <br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2402.17275v1)]
[[Github](https://github.com/hansam95/osasis)] <br>

**UnlearnCanvas: Stylized Image Dataset for Enhanced Machine Unlearning Evaluation in Diffusion Models** <br>
*Yihua Zhang, Yimeng Zhang, Yuguang Yao, Jinghan Jia, Jiancheng Liu, Xiaoming Liu, Sijia Liu.* <br>
**Image Style Transfer**, Michigan State University & IBM Research & Cisco Research <br>
NeurIPS 2024. [[PDF](https://arxiv.org/abs/2402.11846)]
[[Github](https://github.com/OPTML-Group/UnlearnCanvas)] <br>

**Control Color: Multimodal Diffusion-based Interactive Image Colorization** <br>
*Zhexin Liang, Zhaochen Li, Shangchen Zhou, Chongyi Li, Chen Change Loy.* <br>
**Image Colorization**, Nanyang Technological University <br>
Arxiv 2024, [[PDF](https://arxiv.org/abs/2402.10855)]
[[Github](https://github.com/ZhexinLiang/Control-Color)]
[[Project](https://zhexinliang.github.io/Control_Color/)] <br>

**Diffusion Model Compression for Image-to-Image Translation** <br>
(Task-Oriented Diffusion Model Compression) <br>
*Geonung Kim, Beomsu Kim, Eunhyeok Park, Sunghyun Cho.* <br>
**Else Papers**, POSTECH <br>
ACCV 2024. [[PDF](https://arxiv.org/abs/2401.17547)]
[[Project](https://kimgeonung.github.io/id-compression/)]
[[Github](https://github.com/KIMGEONUNG/ID-compression)] <br>

**Image Translation as Diffusion Visual Programmers** <br>
*Cheng Han, James C. Liang, Qifan Wang, Majid Rabbani, Sohail Dianat, Raghuveer Rao, Ying Nian Wu, Dongfang Liu.* <br>
**Base I2I Translation**, Rochester Institute of Technology & Meta AI <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2401.09742)] <br>

**HiCAST: Highly Customized Arbitrary Style Transfer with Adapter Enhanced Diffusion Models** <br>
*Hanzhang Wang, Haoran Wang, Jinze Yang, Zhongrui Yu, Zeke Xie, Lei Tian, Xinyan Xiao, Junjun Jiang, Xianming Liu, Mingming Sun.* <br>
**Image Style Transfer**, Harbin Institute of Technology & Baidu <br>
arXiv 2024. [[PDF](https://arxiv.org/abs/2401.05870)]
[[Github](https://github.com/wd1511/HiCAST)] <br>

**Adaptive latent diffusion model for 3d medical image to image translation: Multi-modal magnetic resonance imaging study** <br>
*Jonghun Kim, Hyunjin Park.* <br>
**Medical Image Translation**, Sungkyunkwan University <br>
WACV 2024. [[Paper](https://openaccess.thecvf.com/content/WACV2024/papers/Kim_Adaptive_Latent_Diffusion_Model_for_3D_Medical_Image_to_Image_WACV_2024_paper.pdf)]
[[Github](https://github.com/jongdory/aldm)] <br>

**Artfusion: A Diffusion Model-Based Style Synthesis Framework for Portraits** <br>
*Hyemin Yang, Heekyung Yang, Kyungha Min.* <br>
**Image Style Transfer**, Sangmyung University <br>
Electronics 2024. [[Paper](https://www.mdpi.com/2079-9292/13/3/509)] <br>

**MirrorDiffusion: Stabilizing Diffusion Process in Zero-shot Image Translation by Prompts Redescription and Beyond** <br>
*Yupei Lin, Xiaoyu Xian, Yukai Shi, Liang Lin.* <br>
**Base I2I Translation**, Guangdong University of Technology & CRRC Academy & Sun Yat-sen University <br>
IEEE Signal Processing Letters(SPL) 2024. [[PDF](https://arxiv.org/abs/2401.03221)]
[[Project](https://mirrordiffusion.github.io)]
[[Github](https://github.com/MirrorDiffusion/MirrorDiffusion)] <br>

**Style Injection in Diffusion: A Training-free Approach for Adapting Large-scale Diffusion Models for Style Transfer** <br>
*Jiwoo Chung, Sangeek Hyun, Jae-Pil Heo.* <br>
**Image Style Transfer**, Sungkyunkwan University <br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2312.09008)]
[[Github](https://github.com/jiwoogit/StyleID)]
[[Project](https://jiwoogit.github.io/StyleID_site)] <br>

**ZipLoRA: Any Subject in Any Style by Effectively Merging LoRAs** <br>
*Viraj Shah, Nataniel Ruiz, Forrester Cole, Erika Lu, Svetlana Lazebnik, Yuanzhen Li, Varun Jampani.* <br>
**Image Style Transfer**, Google Research & UIUC <br>
ECCV 2024. [[PDF](https://arxiv.org/abs/2311.13600)]
[[Project](https://ziplora.github.io)]
[[Github](https://github.com/mkshing/ziplora-pytorch)] <br>

**Cross-Image Attention for Zero-Shot Appearance Transfer** <br>
*Yuval Alaluf, Daniel Garibi, Or Patashnik, Hadar Averbuch-Elor, Daniel Cohen-Or.* <br>
**Image Style Transfer**, Tel Aviv University <br>
SIGGRAPH 2024. [[PDF](https://arxiv.org/abs/2311.03335)]
[[Project](https://garibida.github.io/cross-image-attention/)]
[[Github](https://github.com/garibida/cross-image-attention)] <br>

**DreamStyler: Paint by Style Inversion with Text-to-Image Diffusion Models** <br>
*Namhyuk Ahn, Junsoo Lee, Chunggi Lee, Kunhee Kim, Daesik Kim, Seung-Hun Nam, Kibeom Hong.* <br>
AAAI 2024. [[PDF](https://arxiv.org/abs/2309.06933)]
[[Project](https://nmhkahn.github.io/dreamstyler/)]
[[Github](https://github.com/nmhkahn/dreamstyler)] <br>

**SSMG: Spatial-Semantic Map Guided Diffusion Model for Free-form Layout-to-Image Generation** <br>
*Chengyou Jia, Minnan Luo, Zhuohang Dang, Guang Dai, Xiaojun Chang, Mengmeng Wang, Jingdong Wang.* <br>
AAAI 2024. [[PDF](https://arxiv.org/abs/2308.10156)] <br>

**MeDM: Mediating Image Diffusion Models for Video-to-Video Translation with Temporal Correspondence Guidance** <br>
*Ernie Chu, Tzuhsuan Huang, Shuo-Yen Lin, Jun-Cheng Chen.* <br>
AAAI 2024. [[PDF](https://arxiv.org/abs/2308.10079)]
[[Project](https://medm2023.github.io/)]
[[Github](https://github.com/jwliao1209/diffqrcode)] <br>

**Unpaired Image-to-Image Translation via Neural Schrödinger Bridge** <br>
*Beomsu Kim, Gihyun Kwon, Kwanyoung Kim, Jong Chul Ye.* <br>
ICLR 2024. [[PDF](https://arxiv.org/abs/2305.15086)]
[[Github](https://github.com/cyclomon/UNSB)] <br>

**PAIR-Diffusion: A Comprehensive Multimodal Object-Level Image Editor** <br>
*Vidit Goel, Elia Peruzzo, Yifan Jiang, Dejia Xu, Xingqian Xu, Nicu Sebe, Trevor Darrell, Zhangyang Wang, Humphrey Shi.* <br>
CVPR 2024. [[PDF](https://arxiv.org/abs/2303.17546)]
[[Github](https://github.com/Picsart-AI-Research/PAIR-Diffusion)]
[[Project](https://vidit98.github.io/publication/conference-paper/pair_diff.html)] <br>

## 2023

**Conditional diffusion for SAR to optical image translation** <br>
*Xinyu Bai, Xinyang Pu, Feng Xu.* <br>
**SAR Image Translation**, Fudan University <br>
IEEE Geoscience and Remote Sensing Letters 2023 [[PDF](https://ieeexplore.ieee.org/document/10330015)]
[[Github](https://github.com/Coordi777/Conditional-Diffusion-for-SAR-to-Optical-Image-Translation)] <br>

**Diffusion Cocktail: Mixing Domain-Specific Diffusion Models for Diversified Image Generations** <br>
*Haoming Liu, Yuanhe Guo, Shengjie Wang, Hongyi Wen.* <br>
**Image Style Transfer**, NYU Shanghai <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.08873)]
[[Project](https://maps-research.github.io/Ditail/)]
[[Github](https://github.com/MAPS-research/Ditail)] <br>

**Diffusing Colors: Image Colorization with Text Guided Diffusion** <br>
*Nir Zabari, Aharon Azulay, Alexey Gorkor, Tavi Halperin, Ohad Fried.* <br>
**Image Colorization**, Lightricks <br>
SIGGRAPH Asia 2023. [[PDF](https://arxiv.org/abs/2312.04145)]
[[Project](https://aharonazulay.github.io/project_page_colorization/)] <br>

**Personalized Face Inpainting with Diffusion Models by Parallel Visual Attention** <br>
*Jianjin Xu, Saman Motamed, Praneetha Vaddamanu, Chen Henry Wu, Christian Haene, Jean-Charles Bazin, Fernando de la Torre.* <br>
**Image Editing**, Carnegie Mellon University <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.03556)] <br>

**Open-DDVM: A Reproduction and Extension of Diffusion Model for Optical Flow Estimation** <br>
*Qiaole Dong, Bo Zhao, Yanwei Fu.* <br>
**Else Papers**, Fudan University <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.01746)]
[[Github](https://github.com/dqiaole/flowdiffusion_pytorch)] <br>

**S2ST: Image-to-Image Translation in the Seed Space of Latent Diffusion** <br>
*Or Greenberg, Eran Kishon, Dani Lischinski.* <br>
**Base I2I Translation**, GM R&D & Hebrew University <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2312.00116)] <br>

**CycleNet: Rethinking Cycle Consistency in Text-Guided Diffusion for Image Manipulation** <br>
*Sihan Xu, Ziqiao Ma, Yidong Huang, Honglak Lee, Joyce Chai.* <br>
**Image Manipulation**, University of Michigan & LG AI Research <br>
NeurIPS 2023. [[PDF](https://arxiv.org/abs/2310.13165)]
[[Github](https://github.com/sled-group/cyclenet)]
[[Project](https://cyclenetweb.github.io/)] <br>

**Latent Diffusion Counterfactual Explanations** <br>
*Karim Farid, Simon Schrodi, Max Argus, Thomas Brox.* <br>
**Base I2I Translation**, University of Freiburg <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.06668)]
[[Github](https://github.com/lmb-freiburg/ldce)] <br>

**MedPrompt: Cross-Modal Prompting for Multi-Task Medical Image Translation** <br>
*Xuhang Chen, Chi-Man Pun, Shuqiang Wang.* <br>
**Medical Image Translation**, Shenzhen Institutes of Advanced Technology & University of Macau <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2310.02663)] <br>

**Steered Diffusion: A Generalized Framework for Plug-and-Play Conditional Image Synthesis** <br>
*Nithin Gopalakrishnan Nair, Anoop Cherian, Suhas Lohit, Ye Wang, Toshiaki Koike-Akino, Vishal M. Patel, Tim K. Marks.* <br>
**Base I2I Translation**, Johns Hopkins University <br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2310.00224)]
[[Github](https://github.com/merlresearch/SteeredDiffusion)] <br>

**Denoising Diffusion Bridge Models** <br>
*Linqi Zhou, Aaron Lou, Samar Khanna, Stefano Ermon.* <br>
**Base I2I Translation**, Stanford University <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.16948)]
[[Github-1](https://github.com/alexzhou907/DDBM)]
[[Github-2](https://github.com/galaxygliese/Latent-DDBM)] <br>

**Multiple Noises in Diffusion Model for Semi-Supervised Multi-Domain Translation** <br>
*Tsiry Mayet, Simon Bernard, Clement Chatelain, Romain Herault.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.14394)] <br>

**Cartoondiff: Training-free Cartoon Image Generation with Diffusion Transformer Models** <br>
*Feihong He, Gang Li, Lingyu Si, Leilei Yan, Shimeng Hou, Hongwei Dong, Fanzhang Li.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.08251)]
[[Project](https://cartoondiff.github.io)]
[[Github](https://github.com/CartoonDiff/CartoonDiff)] <br>

**PAI-Diffusion: Constructing and Serving a Family of Open Chinese Diffusion Models for Text-to-image Synthesis on the Cloud** <br>
*Chengyu Wang, Zhongjie Duan, Bingyan Liu, Xinyi Zou, Cen Chen, Kui Jia, Jun Huang.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.05534)] <br>

**Create Your World: Lifelong Text-to-Image Diffusion** <br>
*Gan Sun, Wenqi Liang, Jiahua Dong, Jun Li, Zhengming Ding, Yang Cong.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2309.04430)] <br>

**Phasic Content Fusing Diffusion Model with Directional Distribution Consistency for Few-Shot Model Adaption** <br>
*Teng Hu, Jiangning Zhang, Liang Liu, Ran Yi, Siqi Kou, Haokun Zhu, Xu Chen, Yabiao Wang, Chengjie Wang, Lizhuang Ma.* <br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2309.03729)]
[[Github](https://github.com/sjtuplayer/few-shot-diffusion)] <br>

**Latent Painter** <br>
*Shih-Chieh Su.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.16490)] <br>

**ParaGuide: Guided Diffusion Paraphrasers for Plug-and-Play Textual Style Transfer** <br>
*Zachary Horvitz, Ajay Patel, Chris Callison-Burch, Zhou Yu and Kathleen McKeown.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.15459)]
[[Github](https://github.com/zacharyhorvitz/ParaGuide)] <br>

**Textual and Visual Prompt Fusion for Image Editing via Step-Wise Alignment** <br>
*Zhanbo Feng, Zenan Ling, Ci Gong, Feng Zhou, Jie Li, Robert C. Qiu.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.15854)] <br>

**Pixel-Aware Stable Diffusion for Realistic Image Super-resolution and Personalized Stylization** <br>
*Tao Yang, Peiran Ren, Xuansong Xie, Lei Zhang.* <br>
arXiv 2023.[[PDF](https://arxiv.org/abs/2308.14469)]
[[Github](https://github.com/yangxy/PASD)] <br>

**DiffI2I: Efficient Diffusion Model for Image-to-Image Translation** <br>
*Bin Xia, Yulun Zhang, Shiyin Wang, Yitong Wang, Xinglong Wu, Yapeng Tian, Wenming Yang, Radu Timotfe, Luc Van Gool.* <br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2308.13767v1)] <br>

**Diffusion-based Image Translation with Label Guidance for Domain Adaptive Semantic Segmentation** <br>
*Duo Peng, Ping Hu, Qiuhong Ke, Jun Liu.* <br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2308.12350)]
[[Github](https://github.com/xXCoffeeColaXc/DiffusionBasedImageTranlationWithGradientGuidance)] <br>

**StyleDiffusion: Controllable Disentangled Style Transfer via Diffusion Models** <br>
*Zhizhong Wang, Lei Zhao, Wei Xing.* <br>
**Image Style Transfer**, Zhejiang University <br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2308.07863)]
[[Github](https://github.com/rafaelheid-it/StyleDiffusion)] <br>

**Inversion-by-Inversion: Exemplar-based Sketch-to-Photo Synthesis via Stochastic Differential Equations without Training** <br>
*Ximing Xing, Chuang Wang, Haitao Zhou, Zhihao Hu, Chongxuan Li, Dong Xu, Qian Yu.* <br>
**Sketch-to-Image Translation**, Beihang University & Renmin University of China & The University of Hong Kong <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.07665)]
[[Project](https://ximinng.github.io/inversion-by-inversion-project/)]
[[Github](https://github.com/ximinng/inversion-by-inversion)] <br>

**Taming the Power of Diffusion Models for High-Quality Virtual Try-On with Appearance Flow** <br>
*Junhong Gou, Siyu Sun, Jianfu Zhang, Jianlou Si, Chen Qian, Liqing Zhang.* <br>
**Virtual Try-On**, Shanghai Jiao Tong University & SenseTime Research<br>
ACMMM 2023. [[PDF](https://arxiv.org/abs/2308.06101)]
[[Github](https://github.com/bcmi/DCI-VTON-Virtual-Try-On)] <br>

**Illumination and Shadows in Head Rotation: experiments with Denoising Diffusion Models** <br>
*Andrea Asperti, Gabriele Colasuonno, Antonio Guerra.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.06057)]
[[Github](https://github.com/asperti/head-rotation)] <br>

**Photorealistic and Identity-Preserving Image-Based Emotion Manipulation with Latent Diffusion Models** <br>
*Ioannis Pikoulis, Panagiotis P. Filntisis, Petros Maragos.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2308.03183)]
[[Github](https://github.com/giannispikoulis/dsml-thesis)] <br>

**SDDM: Score-Decomposed Diffusion Models on Manifolds for Unpaired Image-to-Image Translation** <br>
*Shikun Sun, Longhui Wei, Junliang Xing, Jia Jia, Qi Tian.* <br>
ICML 2023. [[PDF](https://arxiv.org/abs/2308.02154)] <br>

**Interpolating between Images with Diffusion Models** <br>
*Clinton J. Wang, Polina Golland.* <br>
ICML 2023 Workshops. [[PDF](https://arxiv.org/abs/2307.12560)]
[[Project](https://clintonjwang.github.io/interpolation)]
[[Github](https://github.com/clintonjwang/ControlNet)] <br>

**TF-ICON: Diffusion-Based Training-Free Cross-Domain Image Composition** <br>
*Shilin Lu, Yanzhu Liu, Adams Wai-Kin Kong.* <br>
ICCV 2023. [[PDF](https://arxiv.org/abs/2307.12493)]
[[Github](https://github.com/Shilin-LU/TF-ICON)] <br>

**DiffuseGAE: Controllable and High-fidelity Image Manipulation from Disentangled Representation** <br>
*Yipeng Leng, Qiangjuan Huang, Zhiyuan Wang, Yangyang Liu, Haoyu Zhang.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2307.05899)]
[[Github](https://github.com/ecai2023/DiffuseGAE)] <br>

**DIFF-NST: Diffusion Interleaving For deFormable Neural Style Transfer** <br>
*Dan Ruta, Gemma Canet Tarrés, Andrew Gilbert, Eli Shechtman, Nicholas Kolkin, John Collomosse.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2307.04157)] <br>

**DragonDiffusion: Enabling Drag-style Manipulation on Diffusion Models** <br>
*Chong Mou, Xintao Wang, Jiechong Song, Ying Shan, Jian Zhang.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2307.02421)]
[[Project](https://mc-e.github.io/project/DragonDiffusion/)]
[[Github-1](https://github.com/MC-E/DragonDiffusion)]
[[Github-2](https://github.com/stroopwafl/dragon_diffusion)] <br>

**DragDiffusion: Harnessing Diffusion Models for Interactive Point-based Image Editing** <br>
*Yujun Shi, Chuhui Xue, Jiachun Pan, Wenqing Zhang, Vincent Y. F. Tan, Song Bai.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.14435)]
[[Github-1](https://github.com/Yujun-Shi/DragDiffusion)]
[[Github-2](https://github.com/JiauZhang/DragDiffusion)] <br>

**ArtFusion: Controllable Arbitrary Style Transfer using Dual Conditional Latent Diffusion Models** <br>
*Dar-Yen Chen.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.09330)]
[[Github](https://github.com/ChenDarYen/ArtFusion)] <br>

**Improving Diffusion-based Image Translation using Asymmetric Gradient Guidance** <br>
*Gihyun Kwon, Jong Chul Ye.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.04396)]
[[Github](https://github.com/submissionanon18/agg)] <br>

**Interpretable Style Transfer for Text-to-Speech with ControlVAE and Diffusion Bridge** <br>
*Wenhao Guan, Tao Li, Yishuang Li, Hukai Huang, Qingyang Hong, Lin Li.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2306.04301)] <br>

**Fine-grained Text Style Transfer with Diffusion-Based Language Models** <br>
*Yiwei Lyu, Tiange Luo, Jiacheng Shi, Todd C. Hollon, Honglak Lee.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.19512)]
[[Github](https://github.com/lvyiwei1/diffuseq_styleptb)] <br>

**DiffSketching: Sketch Control Image Synthesis with Diffusion Models** <br>
*Qiang Wang, Di Kong, Fengyin Lin, Yonggang Qi.* <br>
**Sketch-to-Image Translation**, Beijing University of Posts and Telecommunications <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.18812)]
[[Github](https://github.com/XDUWQ/DiffSketching)] <br>

**Real-World Image Variation by Aligning Diffusion Inversion Chain** <br>
*Yuechen Zhang, Jinbo Xing, Eric Lo, Jiaya Jia* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.18729)]
[[Project](https://rival-diff.github.io)]
[[Github](https://github.com/JulianJuaner/RIVAL)]
[[Github](https://github.com/dvlab-research/RIVAL/)] <br>

**Photoswap: Personalized Subject Swapping in Images** <br>
*Jing Gu, Yilin Wang, Nanxuan Zhao, Tsu-Jui Fu, Wei Xiong, Qing Liu, Zhifei Zhang, He Zhang, Jianming Zhang, HyunJoon Jung, Xin Eric Wang.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.18286)]
[[Project](https://photoswap.github.io/)]
[[Github](https://github.com/eric-ai-lab/photoswap)] <br>

**Diversify Your Vision Datasets with Automatic Diffusion-Based Augmentation** <br>
*Lisa Dunlap, Alyssa Umino, Han Zhang, Jiezhi Yang, Joseph E. Gonzalez, Trevor Darrell.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.16289)]
[[Github](https://github.com/lisadunlap/ALIA)] <br>

**ProSpect: Prompt Spectrum for Attribute-Aware Personalization of Diffusion Models** <br>
*Yuxin Zhang, Weiming Dong, Fan Tang, Nisha Huang, Haibin Huang, Chongyang Ma, Tong-Yee Lee, Oliver Deussen, Changsheng Xu.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.16225)]
[[Github](https://github.com/zyxElsa/ProSpect)] <br>

**SAR-to-Optical Image Translation via Thermodynamics-inspired Network** <br>
*Mingjin Zhang, Jiamin Xu, Chengyu He, Wenteng Shang, Yunsong Li, Xinbo Gao.* <br>
**SAR Image Translation**, Xidian University <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2305.13839)] <br>

**Null-text Guidance in Diffusion Models is Secretly a Cartoon-style Creator** <br>
*Jing Zhao, Heliang Zheng, Chaoyue Wang, Long Lan, Wanrong Huang, Wenjing Yang.* <br>
ACMMM 2023. [[PDF](https://arxiv.org/abs/2305.06710)]
[[Project](https://nulltextforcartoon.github.io/)]
[[Github](https://github.com/NullTextforCartoon/NullTextforCartoon)] <br>

**ReGeneration Learning of Diffusion Models with Rich Prompts for Zero-Shot Image Translation** <br>
*Yupei Lin, Sen Zhang, Xiaojun Yang, Xiao Wang, Yukai Shi.* <br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2305.04651v1)]
[[Project](https://yupeilin2388.github.io/publication/ReDiffuser)] <br>

**Hierarchical Diffusion Autoencoders and Disentangled Image Manipulation** <br>
*Zeyu Lu, Chengyue Wu, Xinyuan Chen, Yaohui Wang, Yu Qiao, Xihui Liu.* <br>
WACV 2023. [[PDF](https://arxiv.org/abs/2304.11829)]
[[Github](https://github.com/whlzy/Hierarchical-Diffusion-Autoencoders)] <br>

**Improved Diffusion-based Image Colorization via Piggybacked Models** <br>
*Hanyuan Liu, Jinbo Xing, Minshan Xie, Chengze Li, Tien-Tsin Wong.* <br>
**Image Colorization**, The Chinese University of Hong Kong & Caritas Institute of Higher Education <br>
arXiv 2023. [[PDF](https://arxiv.org/pdf/2304.11105)]
[[Project](https://piggyback-color.github.io)]
[[Github](https://github.com/hyliu/piggyback-color)] <br>

**Reference-based Image Composition with Sketch via Structure-aware Diffusion Model** <br>
*Kangyeol Kim, Sunghyun Park, Junsoo Lee, Jaegul Choo.* <br>
**Sketch-to-Image Translation**, KAIST & Letsur Inc. & Naver Webtoon <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2304.09748)]
[[Github](https://github.com/kangyeolk/paint-by-sketch)] <br>

**Face Animation with an Attribute-Guided Diffusion Model** <br>
*Bohan Zeng, Xuhui Liu, Sicheng Gao, Boyu Liu, Hong Li, Jianzhuang Liu, Baochang Zhang.* <br>
arXiv 2023. [[PDF](http://arxiv.org/abs/2304.03199v1)] [[PDF(old)](https://arxiv.org/abs/2304.03199)]
[[Github](https://github.com/zengbohan0217/fadm)] <br>

**StyleDiffusion: Prompt-Embedding Inversion for Text-Based Editing** <br>
*Senmao Li, Joost van de Weijer, Taihang Hu, Fahad Shahbaz Khan, Qibin Hou, Yaxing Wang, Jian Yang.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.15649)]
[[Github](https://github.com/sen-mao/StyleDiffusion)] <br>

**Training-free Content Injection using h-space in Diffusion Models** <br>
*Jaeseok Jeong, Mingi Kwon, Youngjung Uh.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.15403)]
[[Project](https://curryjung.github.io/DiffStyle/)]
[[Github](https://github.com/curryjung/DiffStyle_official)]
[[Project](https://curryjung.github.io/InjectFusion/)] <br>

**Diffusion-based Target Sampler for Unsupervised Domain Adaptation** <br>
*Yulong Zhang, Shuhao Chen, Yu Zhang, Jiangang Lu.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.12724)] <br>

**Zero-Shot Contrastive Loss for Text-Guided Diffusion Image Style Transfer** <br>
*Serin Yang, Hyunmin Hwang, Jong Chul Ye.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2303.08622)]
[[Github](https://github.com/ouhenio/text-guided-diffusion-style-transfer)] <br>

**DiffFashion: Reference-based Fashion Design with Structure-aware Transfer by Diffusion Models** <br>
*Shidong Cao, Wenhao Chai, Shengyu Hao, Yanting Zhang, Hangyue Chen, Gaoang Wang.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2302.06826)]
[[Github](https://github.com/Rem105-210/DiffFashion)] <br>

**I$^2$SB: Image-to-Image Schrödinger Bridge** <br>
*Guan-Horng Liu, Arash Vahdat, De-An Huang, Evangelos A. Theodorou, Weili Nie, Anima Anandkumar.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2302.05872)]
[[Project](https://i2sb.github.io/)]
[[Github](https://github.com/NVlabs/I2SB)] <br>

**Zero-shot-Learning Cross-Modality Data Translation Through Mutual Information Guided Stochastic Diffusion** <br>
*Zihao Wang, Yingyu Yang, Maxime Sermesant, Hervé Delingette, Ona Wu.* <br>
arXiv 2023. [[PDF](https://arxiv.org/abs/2301.13743)] <br>

**ControlStyle: Text-Driven Stylized Image Generation Using Diffusion Priors** <br>
*Jingwen Chen, Yingwei Pan, Ting Yao, Tao Mei.* <br>
ACMMM 2023. [[PDF](https://arxiv.org/abs/2311.05463)]
[[Github](https://github.com/winnechan/ControlStyle)] <br>

**General Image-to-Image Translation with One-Shot Image Guidance** <br>
*Bin Cheng, Zuhao Liu, Yunbo Peng, Yue Lin.* <br>
ICCV 2023. [[PDF](https://openaccess.thecvf.com/content/ICCV2023/papers/Cheng_General_Image-to-Image_Translation_with_One-Shot_Image_Guidance_ICCV_2023_paper.pdf)]
[[PDF(old)](https://arxiv.org/abs/2307.14352)]
[[Github](https://github.com/crystalneuro/visual-concept-translator)] <br>

**MultiDiffusion: Fusing Diffusion Paths for Controlled Image Generation** <br>
*Omer Bar-Tal, Lior Yariv, Yaron Lipman, Tali Dekel.* <br>
ICML 2023.[[PDF](https://openreview.net/pdf?id=D4ajVWmgLB)]
[[Github](https://github.com/omerbt/MultiDiffusion)] <br>

**InfoDiffusion: Representation Learning Using Information Maximizing Diffusion Models** <br>
*Yingheng Wang, Yair Schiff, Aaron Gokaslan, Weishen Pan, Fei Wang, Christopher De Sa, Volodymyr Kuleshov.* <br>
ICML 2023. [[PDF](https://arxiv.org/abs/2306.08757)]
[[Github](https://github.com/gregversteeg/InfoDiffusionSimple)] <br>

**TryOnDiffusion: A Tale of Two UNets** <br>
*Luyang Zhu, Dawei Yang, Tyler Zhu, Fitsum Reda, William Chan, Chitwan Saharia, Mohammad Norouzi, Ira Kemelmacher-Shlizerman.* <br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2306.08276)]
[[Github](https://github.com/fashn-AI/tryondiffusion)]
[[Project](https://tryondiffusion.github.io/)] <br>

**DiffusionRig: Learning Personalized Priors for Facial Appearance Editing** <br>
*Zheng Ding, Xuaner Zhang, Zhihao Xia, Lars Jebe, Zhuowen Tu, Xiuming Zhang.* <br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2304.06711)]
[[Project](https://diffusionrig.github.io/)]
[[Github](https://github.com/adobe-research/diffusion-rig)] <br>

**InstructPix2Pix: Learning to Follow Image Editing Instructions** <br>
*Tim Brooks, Aleksander Holynski, Alexei A. Efros.*   <br>
CVPR 2023. [[PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Brooks_InstructPix2Pix_Learning_To_Follow_Image_Editing_Instructions_CVPR_2023_paper.pdf)]
[[GitHub](https://github.com/timothybrooks/instruct-pix2pix)] <br>

**EDICT: Exact Diffusion Inversion via Coupled Transformations** <br>
*Bram Wallace, Akash Gokul, Nikhil Naik.* <br>
CVPR 2023. [[PDF](https://openaccess.thecvf.com/content/CVPR2023/papers/Wallace_EDICT_Exact_Diffusion_Inversion_via_Coupled_Transformations_CVPR_2023_paper.pdf)]
[[Github](https://github.com/salesforce/edict)] <br>

**High-Fidelity Guided Image Synthesis with Latent Diffusion Models** <br>
*Jaskirat Singh, Stephen Gould, Liang Zheng.* <br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.17084)]
[[Github](https://1jsingh.github.io/gradop)] <br>

**Inversion-Based Style Transfer with Diffusion Models** <br>
*Yuxin Zhang, Nisha Huang, Fan Tang, Haibin Huang, Chongyang Ma, Weiming Dong, Changsheng Xu.* <br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.13203)]
[[Github](https://github.com/zyxElsa/InST)] <br>

**Plug-and-Play Diffusion Features for Text-Driven Image-to-Image Translation** <br>
*Narek Tumanyan, Michal Geyer, Shai Bagon, Tali Dekel.* <br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.12572)]
[[Github](https://github.com/MichalGeyer/plug-and-play)] <br>

**Person Image Synthesis via Denoising Diffusion Model** <br>
*Ankan Kumar Bhunia, Salman Khan, Hisham Cholakkal, Rao Muhammad Anwer, Jorma Laaksonen, Mubarak Shah, Fahad Shahbaz Khan.* <br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2211.12500)]
[[Github](https://github.com/ankanbhunia/PIDM)] <br>

**Diffusion-based Image Translation using Disentangled Style and Content Representation** <br>
*Gihyun Kwon, Jong Chul Ye.* <br>
ICLR 2023. [[PDF](https://arxiv.org/abs/2209.15264)]
[[Project](https://pnp-diffusion.github.io)]
[[Github](https://github.com/anon294384/DiffuseIT)] <br>

**Dual Diffusion Implicit Bridges for Image-to-Image Translation** <br>
*Xuan Su, Jiaming Song, Chenlin Meng, Stefano Ermon.* <br>
ICLR 2023. [[PDF](https://arxiv.org/abs/2203.08382)]
[[Github](https://github.com/suxuann/ddib)] <br>

**Restoring Vision in Adverse Weather Conditions with Patch-Based Denoising Diffusion Models** <br>
*Ozan Özdenizci, Robert Legenstein.* <br>
TPAMI 2023. [[PDF](https://arxiv.org/abs/2207.14626)]
[[Github](https://github.com/IGITUGraz/WeatherDiffusion)] <br>

**Discrete Contrastive Diffusion for Cross-Modal Music and Image Generation** <br>
*Ye Zhu, Yu Wu, Kyle Olszewski, Jian Ren, Sergey Tulyakov, Yan Yan.* <br>
ICLR 2023. [[PDF](https://arxiv.org/abs/2206.07771)]
[[Github](https://github.com/L-YeZhu/CDCD)] <br>

## 2022

**DiffFace: Diffusion-based Face Swapping with Facial Guidance** <br>
*Kihong Kim, Yunho Kim, Seokju Cho, Junyoung Seo, Jisu Nam, Kychul Lee, Seungryong Kim, KwangHee Lee.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2212.13344)]
[[Project](https://hxngiee.github.io/DiffFace/)]
[[Github](https://github.com/hxngiee/DiffFace)] <br>

**HS-Diffusion: Semantic-Mixing Diffusion for Head Swapping** <br>
*Qinghe Wang, Lijie Liu, Miao Hua, Qian He, Pengfei Zhu, Bing Cao, Qinghua Hu.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2212.06458)]
[[Github](https://github.com/qinghew/HS-Diffusion)] <br>

**DiffStyler: Controllable Dual Diffusion for Text-Driven Image Stylization** <br>
*Nisha Huang, Yuxin Zhang, Fan Tang, Chongyang Ma, Haibin Huang, Yong Zhang Weiming Dong, Changsheng Xu.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2211.10682)]
[[Github](https://github.com/haha-lisa/Diffstyler.git)] <br>

**DiffGAR: Model-Agnostic Restoration from Generative Artifacts Using Image-to-Image Diffusion Models** <br>
*Yueqin Yin, Lianghua Huang, Yu Liu, Kaiqi Huang.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2210.08573)] <br>

**Unifying Diffusion Models' Latent Space, with Applications to CycleDiffusion and Guidance** <br>
*Chen Henry Wu, Fernando De la Torre.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2210.05559)]
[[Github-1](https://github.com/ChenWu98/cycle-diffusion)]
[[Github-2](https://github.com/ChenWu98/unified-generative-zoo)] <br>

**Anatomically constrained CT image translation for heterogeneous blood vessel segmentation** <br>
*Giammarco La Barbera, Haithem Boussaid, Francesco Maso, Sabine Sarnacki, Laurence Rouet, Pietro Gori, Isabelle Bloch.* <br>
BMVC 2022. [[PDF](https://arxiv.org/abs/2210.01713)] <br>

**Draw Your Art Dream: Diverse Digital Art Synthesis with Multimodal Guided Diffusion** <br>
*Nisha Huang, Fan Tang, Weiming Dong, Changsheng Xu.* <br>
ACMMM 2022. [[PDF](https://arxiv.org/abs/2209.13360)]
[[Github](https://github.com/haha-lisa/mgad-multimodal-guided-artwork-diffusion)] <br>

**MIDMs: Matching Interleaved Diffusion Models for Exemplar-based Image Translation** <br>
*Junyoung Seo, Gyuseong Lee, Seokju Cho, Jiyoung Lee, Seungryong Kim.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2209.11047)]
[[Project](https://ku-cvlab.github.io/MIDMs/)]
[[Github](https://github.com/KU-CVLAB/MIDMs/)] <br>

**Non-Uniform Diffusion Models** <br>
*Georgios Batzolis, Jan Stanczuk, Carola-Bibiane Schönlieb, Christian Etmann.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2207.09786)] <br>

**Unsupervised Medical Image Translation with Adversarial Diffusion Models** <br>
*Muzaffer Özbey, Salman UH Dar, Hasan A Bedel, Onat Dalmaz, Şaban Özturk, Alper Güngör, Tolga Çukur.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2207.08208)]
[[Github](https://github.com/icon-lab/syndiff)] <br>

**EGSDE: Unpaired Image-to-Image Translation via Energy-Guided Stochastic Differential Equations** <br>
*Min Zhao, Fan Bao, Chongxuan Li, Jun Zhu.* <br>
NeurIPS 2022. [[PDF](https://arxiv.org/abs/2207.06635)]
[[Github](https://github.com/ML-GSAI/EGSDE)] <br>

**Pretraining is All You Need for Image-to-Image Translation** <br>
*Tengfei Wang, Ting Zhang, Bo Zhang, Hao Ouyang, Dong Chen, Qifeng Chen, Fang Wen.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2205.12952)]
[[Project](https://tengfei-wang.github.io/PITI/index.html)]
[[Github](https://github.com/PITI-Synthesis/PITI)] <br>

**BBDM: Image-to-image Translation with Brownian Bridge Diffusion Models** <br>
*Bo Li, Kaitao Xue, Bin Liu, Yu-Kun Lai.* <br>
CVPR 2023. [[PDF](https://arxiv.org/abs/2205.07680)]
[[Github](https://github.com/xuekt98/BBDM)] <br>

**The Swiss Army Knife for Image-to-Image Translation: Multi-Task Diffusion Models** <br>
*Julia Wolleb, Robin Sandkühler, Florentin Bieder, Philippe C. Cattin.* <br>
arXiv 2022. [[PDF](https://arxiv.org/abs/2204.02641)] <br>

**Denoising Diffusion Restoration Models** <br>
*Bahjat Kawar, Michael Elad, Stefano Ermon, Jiaming Song.* <br>
NeurIPS 2022. [[PDF](https://arxiv.org/abs/2201.11793)]
[[Github](https://github.com/bahjat-kawar/ddrm)]
[[Project](https://ddrm-ml.github.io/)] <br>

**DiffusionCLIP: Text-Guided Diffusion Models for Robust Image Manipulation** <br>
*Gwanghyun Kim, Taesung Kwon, Jong Chul Ye.* <br>
**Else Papers**, KAIST <br>
CVPR 2022. [[PDF](https://arxiv.org/abs/2110.02711)]
[[Github](https://github.com/gwang-kim/DiffusionCLIP)]
[[Github](https://github.com/gwang-kim/DiffusionCLIP.git)] <br>

## 2021

**DiffuseMorph: Unsupervised Deformable Image Registration Using Diffusion Model** <br>
*Boah Kim, Inhwa Han, Jong Chul Ye.* <br>
**Medical Image Translation**, KAIST <br>
arXiv 2021. [[PDF](https://arxiv.org/abs/2112.05149)]
[[Github](https://github.com/DiffuseMorph/DiffuseMorph)] <br>

**Diffusion Autoencoders: Toward a Meaningful and Decodable Representation** <br>
*Konpat Preechakul, Nattanat Chatthee, Suttisak Wizadwongsa, Supasorn Suwajanakorn* <br>
**Base I2I Translation**, VISTEC <br>
arXiv 2021. [[PDF](https://arxiv.org/abs/2111.15640)]
[[Project](https://diff-ae.github.io/)]
[[Github](https://github.com/phizaz/diffae)] <br>

**Conditional Image Generation with Score-Based Diffusion Models** <br>
*Georgios Batzolis, Jan Stanczuk, Carola-Bibiane Schönlieb, Christian Etmann.* <br>
**Base I2I Translation**, University of Cambridge <br>
arXiv 2021. [[PDF](https://arxiv.org/abs/2111.13606)]
[[Github](https://github.com/GBATZOLIS/conditional_score_diffusion)] <br>

**Palette: Image-to-Image Diffusion Models** <br>
*Chitwan Saharia, William Chan, Huiwen Chang, Chris A. Lee, Jonathan Ho, Tim Salimans, David J. Fleet, Mohammad Norouzi.* <br>
**Base I2I Translation**, Google Research <br>
SIGRAPH 2021. [[PDF](https://arxiv.org/abs/2111.05826)]
[[Github](https://github.com/Janspiry/Palette-Image-to-Image-Diffusion-Models)]
[[Project](https://diffusion-palette.github.io)] <br>

**ILVR: Conditioning Method for Denoising Diffusion Probabilistic Models** <br>
*Jooyoung Choi, Sungwon Kim, Yonghyun Jeong, Youngjune Gwon, Sungroh Yoon.* <br>
**Base I2I Translation**, Seoul National University & Samsung <br>
ICCV 2021 (Oral). [[PDF](https://arxiv.org/abs/2108.02938)]
[[Github](https://github.com/jychoi118/ilvr_adm)] <br>

**UNIT-DDPM: UNpaired Image Translation with Denoising Diffusion Probabilistic Models** <br>
*Hiroshi Sasaki, Chris G. Willcocks, Toby P. Breckon.* <br>
**Base I2I Translation**, Durham University <br>
arXiv 2021. [[PDF](https://arxiv.org/abs/2104.05358)]
[[Github](https://github.com/konkuad/UNIT-DDPM-Unofficial)] <br>
