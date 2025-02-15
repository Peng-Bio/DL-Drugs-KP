Overview:  
This project employs deep learning techniques to accelerate drug discovery for combating Klebsiella pneumoniae (KP) infections. KP, a highly 
antibiotic-resistant pathogen, poses a significant global health challenge. Our approach integrates convolutional neural networks (CNN) and 
evolutionary scale modeling (ESM) to identify promising drug candidates from a dataset of biotech and small-molecule drugs extracted from DrugBank.

The figure below illustrates the overall process flow, including DDIs and unique drug extraction, NLP, CNN modeling, ESM with drug-bacteria 
similarity analysis, and the Drug Repurposing Knowledge Graph (DRKG), used in the deep learning framework to identify potential drug candidates 
against Klebsiella pneumoniae (KP).

![image](https://github.com/user-attachments/assets/b9989338-757a-42d2-89be-e0abe0670186)

Dataset
		
1. DrugBank 5.1.11 version 
    https://go.drugbank.com/releases/latest
2. Klebsiella Pneumonia (KP) strain fasta dataset
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9769640/pdf/spectrum.02306-22.pdf
3. National Center for Biotechnology Information (NCBI) databases

Key Features
•	Data-Driven Drug Discovery: Utilizes 3,475 biotech and small-molecule drugs from DrugBank, focusing on potential candidates for KP treatment 
as shown in Data Flow I.

![image](https://github.com/user-attachments/assets/ca428ce2-acb5-46ba-b9c5-31f110f2f785)

•	Deep Learning Models:  as illustrated in Data Process Few II.

◦	Convolutional Neural Networks (CNN): Applied for classification and interaction prediction.
◦	Drug-Drug Interaction Analysis: Incorporates drug-drug interaction (DDI) data for improved predictions.

![image](https://github.com/user-attachments/assets/fcd917a0-14e0-446c-9f0f-80c1a182794f)

•	Evolutionary Scale Modeling (ESM) with Similarity Metrics: Used for similarity analysis of drug molecules to KP strains. Employs cosine similarity 
to identify candidates with >85% molecular similarity to KP strains as seen in Drug-Bacterial Pairs Data Process Flow.

![image](https://github.com/user-attachments/assets/66f3aa35-171e-4888-9635-12257669f2e4)

Results
1.	Accuracy: Achieved approximately 72% validation accuracy for the CNN model.
2.	Candidate Identification: Five promising drugs were identified with molecular similarities exceeding 85% to KP strains.
3.	Efficiency: Reduced the drug discovery timeline from years to months.
4.	Robustness: PairRE outperformed other models across evaluation metrics for predictive ranking.

Significance
This project provides a scalable framework for drug discovery, offering a faster and more efficient alternative to traditional laboratory-based approaches. It holds potential for addressing bacterial pathogens like KP, aiding in effective treatment and minimizing side effects.
Repository Contents
•	/data/: Contains DrugBank-derived dataset used for training and evaluation.
•	/models/: Includes implementations of CNN and ESM models.
•	/scripts/: Python scripts for data preprocessing, training, and evaluation.
•	/results/: Output files, including accuracy metrics and identified drug candidates.
•	README.md: This file, describing the project.
