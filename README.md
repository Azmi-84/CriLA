# CriLA

CriLA is a machine-learning (ML) project that I have been using to learn how things work at an industry level. There, I used the [Social Media User Analysis](https://www.kaggle.com/datasets/rockyt07/social-media-user-analysis) dataset. It helped me a lot to understand all the underlying mechanisms, especially logging, pipeline, and central code execution procedures, which are crucial, or you can say hear of the software industry, to mitigate any issues related to software crashing, debugging, optimization, and the feature-adding process.

## Technology

- Core Tech: Python

## Effective use of AI

Yeah, I have used artificial intelligence (AI) in my project, but not blindly. Initially, I have taken the decision on which project I will accomplish. Then, I chose the models and necessary parameters that will help me to optimize the model. Then, I developed the project architecture on my own. After that, I started the coding. There, whenever I stucked in a problem, I then used the AI, but the control was in my hands. I used Claude, Gemini, and ChatGPT to get an answer to my problem. I strictly prohibited using agents in my project directly, as I was still confused about how to use them effectively. Moreover, my personal experience of using the agent is very bad as they write bull-shit and unnecessary code which later becomes very difficult to track and clean. Also, as a learner, these agent tools hinder my brainstorming process and critical thinking development. That’s why I also stopped using these tools.

## Project Architecture

<!-- readme-tree start -->
```
.
├── .github
│   └── workflows
│       ├── Auto_Tree.yaml
│       └── Auto_Tree.yaml:Zone.Identifier
├── .gitignore
├── .gradio
│   └── flagged
│       └── dataset1.csv
├── 02_Notebooks
│   ├── 01_Data_Collection
│   │   ├── 01_Raw_Data_Collection.py
│   │   └── 02_Raw_Data_Cleaning.py
│   ├── 02_Data_Preprocessing
│   │   ├── 01_Exploratory_Data_Analysis.py
│   │   └── 02_Principal_Component_Analysis.py
│   ├── 03_Model_Selection
│   │   ├── 01_Model_Selection_with_PCA
│   │   │   ├── 01_Random_Forest
│   │   │   │   ├── 01_Model_Training.py
│   │   │   │   └── 02_Hyperparameters_Optimization.py
│   │   │   ├── 02_K_Nearest_Neighbors
│   │   │   │   ├── 01_Model_Training.py
│   │   │   │   └── 02_Hyperparameters_Optimization.py
│   │   │   ├── 03_Gradient_Boosting
│   │   │   │   ├── 01_Model_Training.py
│   │   │   │   └── 02_Hyperparameters_Optimization.py
│   │   │   ├── 04_Extreme_Gradient_Boosting
│   │   │   │   ├── 01_Model_Training.py
│   │   │   │   └── 02_Hyperparameters_Optimization.py
│   │   │   ├── 05_Adaptive_Boosting
│   │   │   │   ├── 01_Model_Training.py
│   │   │   │   └── 02_Hyperparameters_Optimization.py
│   │   │   └── 06_Light_Gradient_Boosting_Machine
│   │   │       ├── 01_Model_Training.py
│   │   │       └── 02_Hyperparameters_Optimization.py
│   │   └── 02_Model_Selection_without_PCA
│   │       ├── 01_Random_Forest
│   │       │   ├── 01_Model_Training.py
│   │       │   └── 02_Hyperparameters_Optimization.py
│   │       ├── 02_K_Nearest_Neighbors
│   │       │   ├── 01_Model_Training.py
│   │       │   └── 02_Hyperparameters_Optimization.py
│   │       ├── 03_Gradient_Boosting
│   │       │   ├── 01_Model_Training.py
│   │       │   └── 02_Hyperparameters_Optimization.py
│   │       ├── 04_Extreme_Gradient_Boosting
│   │       │   ├── 01_Model_Training.py
│   │       │   └── 02_Hyperparameters_Optimization.py
│   │       ├── 05_Adaptive_Boosting
│   │       │   ├── 01_Model_Training.py
│   │       │   └── 02_Hyperparameters_Optimization.py
│   │       └── 06_Light_Gradient_Boosting_Machine
│   │           ├── 01_Model_Training.py
│   │           └── 02_Hyperparameters_Optimization.py
│   ├── 04_Model_Training
│   │   └── 01_Model_Training.py
│   └── crimson_nebula.py
├── 03_Resources
│   ├── 1-s2.0-S1359836825012260-main.pdf
│   └── Docs
│       └── EDA_Decisions.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── Source
│   ├── Gradio
│   │   └── app.py
│   └── Models
│       ├── best_model.pkl
│       ├── best_model_full_dataset.pkl
│       └── crimson_nebula.pkl
├── requirements.txt
└── tree.bak

29 directories, 46 files
```
<!-- readme-tree end -->
