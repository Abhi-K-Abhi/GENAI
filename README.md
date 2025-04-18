GENAI/
├── config/                         # Configuration files (YAML/JSON/INI)
├── data/                           # Input datasets or raw data
├── models/                         # Model architectures and scripts
│   ├── codebart/
│   ├── codellama/
│   ├── common/
│   ├── deepseek/
│   │   ├── __init__.py
│   │   ├── fewshot_gerrit.py
│   │   ├── fewshot_go.py
│   │   ├── fewshot_jdt.py
│   │   ├── fewshot_openstack.py
│   │   ├── fewshot_platform.py
│   │   ├── fewshot_qt.py
│   │   ├── predictor.py
│   │   ├── prompt_template.txt
│   │   ├── run_gerrit.py
│   │   ├── run_go.py
│   │   ├── run_jdt.py
│   │   ├── run_openstack.py
│   │   ├── run_platform.py
│   │   └── run_qt.py
│   ├── llama3/
│   │   ├── __init__.py
│   │   ├── fewshot_gerrit.py
│   │   ├── fewshot_go.py
│   │   ├── fewshot_jdt.py
│   │   ├── fewshot_openstack.py
│   │   ├── fewshot_platform.py
│   │   ├── fewshot_qt.py
│   │   ├── predictor.py
│   │   ├── prompt_template.txt
│   │   ├── run_gerrit.py
│   │   ├── run_go.py
│   │   ├── run_jdt.py
│   │   ├── run_openstack.py
│   │   ├── run_platform.py
│   │   └── run_qt.py
│   ├── mistral/
│   │   ├── __init__.py
│   │   ├── fewshot_gerrit.py
│   │   ├── fewshot_go.py
│   │   ├── fewshot_jdt.py
│   │   ├── fewshot_openstack.py
│   │   ├── fewshot_platform.py
│   │   ├── fewshot_qt.py
│   │   ├── predictor.py
│   │   ├── prompt_template.txt
│   │   ├── run_gerrit.py
│   │   ├── run_go.py
│   │   ├── run_jdt.py
│   │   ├── run_openstack.py
│   │   ├── run_platform.py
│   │   └── run_qt.py
│   ├── ollama/
│   └── openai/
│       └── __init__.py
├── outputs/                        # Generated outputs or model predictions
├── prompts/                        # Prompt JSON configurations
│   ├── CoT.json
│   └── few_shot.json
├── test/                           # Unit tests and test cases
├── utils/                          # Helper scripts and utility functions
│   ├── dataset_loader.py
│   ├── evaluation.py
│   └── prompt_utils.py
├── .env                            # Environment variables (should be in .gitignore)
├── .gitignore                      # Specifies untracked files
├── .gitattributes                  # Git configuration attributes
├── main.py                         # Main entry point
├── README.md                       # Project documentation
└── requirements.txt                # Dependency list
