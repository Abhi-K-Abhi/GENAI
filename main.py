from llm_interface.llm_predictor import load_prompt_template, generate_prompt, query_llm

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

prompt = generate_prompt(prompt_template, test_commit_info, test_diff)
prediction = query_llm(prompt)

print("LLM Prediction:", prediction)  # Expecting: 0 (clean) or 1 (risky)