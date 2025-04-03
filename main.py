from llm_interface.llm_predictor import generate_cot_prompt, load_prompt_template, generate_prompt, query_llm
from config import MODEL_SOURCE, MODEL_NAME


############################################################### ZERO SHOT ###############################################################
prompt = '''You are a commit risk analysis assistant.\n
            Your job is to analyze a commit information and diff and determine if, it introduces a software bug.\n
            Respond only with 0 (clean) or 1 (risky). Do not include explanations.\n
            Commit info is as below:\n
            Title: Fix API version in pom.xml  Change-Id: Id96d71ccb150c18a15291c01296a8152c6ec3eb0\n
            Diff: --git a/pom.xml b/pom.xml\n
                  --- a/pom.xml\n
                  +++ b/pom.xml\n
                  @@ -22,7 +22,7 @@\n
                  -  <version>2.12-SNAPSHOT</version>\n
                  +  <version>2.12</version>\n
            Risk:'''

print("\n✅ Testing Zero-Shot:")
prediction = query_llm(prompt, model_source=MODEL_SOURCE, model_name=MODEL_NAME)
print("("+MODEL_NAME+")"+"Zero-Shot Prediction:", prediction)  # Expecting: 0 (clean) or 1 (risky)

#You can also use other models by changing model_name: "mistral", "deepseek-coder", "llama3:8b", "codellama"

############################################################### FEW SHOT ###############################################################
prompt_template = load_prompt_template("prompts/few_shot.json")

test_commit_info = "Title: Remove Maven build"
test_diff = """diff --git a/pom.xml b/pom.xml
deleted file mode 100644
index d33e954..0000000
--- a/pom.xml
+++ /dev/null
@@ -1,86 +0,0 @@
-<project>
-  <groupId>com.example</groupId>
-  <artifactId>example-project</artifactId>
-  <version>1.0-SNAPSHOT</version>
-</project>
"""

# Generate the full few-shot prompt
prompt = generate_prompt(prompt_template, test_commit_info, test_diff)

print("\n✅ Testing Few-Shot:")
prediction = query_llm(prompt, model_source=MODEL_SOURCE, model_name=MODEL_NAME)
print("("+MODEL_NAME+")"+"Few-Shot Prediction:", prediction)  # Expecting: 0 (clean) or 1 (risky)

#You can also use other models by changing model_name: "mistral", "deepseek-coder", "llama3:8b", "codellama"

############################################################### CHAIN OF THOUGHT ###############################################################
# https://www.promptingguide.ai/techniques/cot
# Refer 3. Section: https://www.kaggle.com/code/youssef19/chain-of-thought-reasoning?scriptVersionId=167457230&cellId=8


cot_template = load_prompt_template("prompts/cot.json")

test_commit_info = "Title: Add null check in API handler"
test_diff = """--- a/api.js
+++ b/api.js
@@ -20,6 +20,8 @@
+ if (data == null) {
+   return;
+ }
"""

prompt = generate_cot_prompt(cot_template, test_commit_info, test_diff)

print("\n🧠 Testing Chain-of-Thought:")
prediction = query_llm(prompt, model_source=MODEL_SOURCE, model_name=MODEL_NAME)
print("("+MODEL_NAME+")"+"Chain-of-Thought Prediction:", prediction)  # Expecting: 0 (clean) or 1 (risky)