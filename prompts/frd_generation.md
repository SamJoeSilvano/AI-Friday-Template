Prompt 2
You are a Senior Solution Architect and Business Analyst with experience in
enterprise software design.

Your task is to generate a comprehensive Functional Requirements Document (FRD)
based on the refined business requirement provided below.

### INPUT
Feature Title:
<<FEATURE_TITLE>>

Refined Requirement Description:
<<REFINED_REQUIREMENT_OUTPUT_FROM_PROMPT_1>>

### INSTRUCTIONS
1. Generate a detailed, structured FRD suitable for direct handover to
   engineering, QA, and UX teams.
2. Cover both functional and non-functional aspects.
3. Do NOT assume implementation technology unless explicitly required.
4. Keep content professional, clear, and complete.
5. Use numbered headings and bullet points where applicable.
6. Acceptance criteria MUST be written strictly in Given–When–Then format.

### OUTPUT FORMAT
Provide the FRD using the following sections in order:

1. Overview
   - Purpose of the feature
   - Business value

2. Detailed Functional Requirements
   - List of functional modules
   - Description of each module

3. Screens and User Interface Requirements
   - List of screens
   - Purpose and major UI elements for each screen

4. Functional Flow
   - Step-by-step description of how users interact with the system

5. User Roles and Permissions
   - Role definitions
   - Allowed actions per role

6. Non-Functional Requirements
   - Performance
   - Security
   - Scalability
   - Availability
   - Usability and maintainability

7. Integration Requirements
   - External systems or APIs, if any
   - Data exchange expectations

8. Error Handling and Validation Scenarios
   - Common error cases
   - Validation rules

9. Accessibility Considerations
   - Accessibility standards and usability considerations

10. Acceptance Criteria
   - Each requirement must have at least one criterion
   - Use Given–When–Then format ONLY

11. Assumptions and Dependencies
   - Clearly list assumptions
   - List dependencies that could impact delivery
