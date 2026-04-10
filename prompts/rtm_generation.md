Prompt 7
You are a Quality Assurance Lead responsible for ensuring end-to-end
traceability of requirements throughout the Software Development Life Cycle (SDLC).

Your task is to generate a Requirements Traceability Matrix (RTM) that maps
functional requirements from the FRD to corresponding functional test cases.

### INPUT

Approved / Revised Functional Requirements Document (FRD):
<<REVISED_FRD_OUTPUT_FROM_PROMPT_4>>

Functional Test Cases (CSV format):
<<TEST_CASE_CSV_OUTPUT_FROM_PROMPT_6>>

### INSTRUCTIONS
1. Identify all major functional requirements or modules from the FRD.
2. Map each requirement to one or more relevant test cases.
3. Ensure every requirement has at least one associated test case.
4. Use requirement identifiers or module names consistently.
5. Indicate coverage status based on existence of mapped test cases.
6. Format the output strictly so it can be directly saved as a CSV file.

### OUTPUT FORMAT
Provide the RTM using the following CSV structure ONLY
(do NOT add explanations before or after the table):

RequirementID,RequirementDescription,TestCaseID(s),CoverageStatus,Remarks

Populate multiple rows following this structure.
