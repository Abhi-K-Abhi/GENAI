Folder Structure.

commit-risk-predictor/               <-- 🗂️ Main Project Folder
│
├── data/                            <-- 🗂️ Folder (for your datasets)
│
├── prompts/                         <-- 🗂️ Folder (for storing prompt templates)
│   └── few_shot_example.json        <-- 📄 File (JSON prompt template)
│
├── models/                          <-- 🗂️ Folder (for ML model training code)
│   └── train_ml_model.py            <-- 📄 File (Python script to train ML models)
│
├── llm_interface/                   <-- 🗂️ Folder (for LLM-related code)
│   ├── prompt_engineer.py           <-- 📄 File (optional helper for prompt crafting)
│   └── llm_predictor.py             <-- 📄 File (sends prompt + gets LLM prediction)
│
├── ensemble/                        <-- 🗂️ Folder (for hybrid ensemble logic)
│   └── hybrid_predictor.py          <-- 📄 File (combines ML + LLM outputs)
│
├── utils/                           <-- 🗂️ Folder (for helper functions/utilities)
│   └── data_loader.py               <-- 📄 File (loads + preprocesses dataset)
│
├── main.py                          <-- 📄 File (entry point to run everything)
├── requirements.txt                 <-- 📄 File (Python libraries to install)
└── README.md                        <-- 📄 File (Project overview/documentation)

-------------------------------------------------------------------------------------------------------