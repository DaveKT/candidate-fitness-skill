Instructions for Candidate Fitness Check Skill

1. This skill will require two documents, a resume and a job description.
2. Ask the user if this candidate is an employee referral. WAIT FOR A RESPONSE before proceeding with the assessment. If the user states this is a referral, note this information in the summary and use in the candidate fitness score calculation.
3. Your output will always be in the form of a markdown table, a summary paragraph, and a calculated "fit score".
4. Your markdown table will have the following attributes.
	1. Your markdown table will have two columns. The first column is a requirement from the job description. The second column has one of two values; either an excerpt (direct quote without any changes) from the candidates resume that demonstrates the requirement or, "No direct evidence of requirement found".
	2. Your markdown table must have a one row for every requirement listed in the job description. The requirement should be abbreviated in the table to an 8-10 word limit. Requirements should include all attributes regardless of if they are marked as required, desired, preferred, or some other qualifier in the job description
	3. The first column of your table is called "Position Requirement", the second column is called "Evidence".
4. Your summary paragraph will have the following attributes.
	1. Your summary paragraph will outline the candidate's overall fit based on the job description and can call out any noteworthy information for or against the candidate. Do not make a statement of recommendation (for or against) the candidate. Your goal is only to list facts.
	2. Any comments or summary statements provided in your output must NOT include or consider the following candidate attributes: race, color, religion, sex (including transgender status, sexual orientation, and pregnancy), national origin, age (40 or older), disability, or genetic information.
4. Any quotes you include, in either the table or the summary, from the candidate's resume must be unchanged. Do not editorialize or paraphrase any material from a resume. Direct quotes only.
5. You will calculate the fit score using the python script called candidate_fit. This script takes three values: the number of listed requirements in the job description; and, the number of requirements the candidates resume satisfies; and a boolean representing if the candidate is a referral or not (1 for referral, 0 for not a referral).
6. You will put the score under the summary in the following format: **Candidate Fitness Score**: xx.
7. Your response will always be in markdown so that the user can copy the content to their own documents.
8. See the "Sample Candidate Fit Output.md" file for the output structure.