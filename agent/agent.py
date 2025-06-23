
# agent.py
from google.adk.agents import LlmAgent, SequentialAgent
from agent.tools import generate_quiz_docx, create_dynamic_presentation

# 1. Curriculum Agent
describe_curriculum_agent = LlmAgent(
    name="curriculum_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a curriculum designer. Given a topic, create a course outline with the following format:
    {
        "courseTitle": "...",
        "modules": [
            {
                "moduleTitle": "...",
                "learningObjectives": ["...", "..."],
                "topics": ["...", "..."]
            },
            ...
        ]
    }
    Output only the JSON. Do not explain or describe anything else.
    """,
    description="Generates a structured course outline from a topic.",
    output_key="generated_module"
)


# 3. Quiz Word Generator Agent
quiz_word_generator_agent = LlmAgent(
    name="quiz_word_generator",
    model="gemini-2.0-flash",
    description="Generates a quiz in Word format from the course module.",
    instruction="""
    You are a quiz generator. Using the course module in state['generated_module'], generate a quiz for each module
    with 3 short questions. Then call the generate_quiz_docx tool to save it as a Word file.
    """,
    tools=[generate_quiz_docx],
    output_key="quiz_status"
)

generate_ppt_agent = LlmAgent(
    name="generate_ppt_agent",
    model="gemini-2.0-flash",
    description=(
        """Generates a json file based on the provided specification.
        The specification includes a title and a list of slides with varying layouts and content.
        The agent can handle title-only slides, title + content slides, bullet point slides, and image slides."""  
    ),
    instruction=(
    """
    You are a presentation designer agent. Your task is to:
    
    1. Read the course structure from `state['generated_module']`.
    2. Convert it into a PowerPoint specification with the format:
        {
            "title": "...",
            "slides": [
                { "layout": "title_only", "title": "..." },
                { "layout": "bullet_slide", "title": "...", "bullets": [...] },
                ...
            ]
        }
    3. Save the JSON in `state['ppt_status']`.
    4. The next tool to be called is `ppt_saver_agent`, which will use this JSON to create the PowerPoint file.
    5. The next agent to be called is `ppt_saver_agent`, which will use this JSON to create the PowerPoint file.
    """),
    output_key="ppt_status"
)

# PPT Saver Agent — Now in the same format as quiz_word_generator_agent
ppt_saver_agent = LlmAgent(
    name="ppt_saver_agent",
    model="gemini-2.0-flash",
    description="Uses the PowerPoint spec JSON to create a presentation file.",
    instruction="""
    You are a file-saving utility. Use the PowerPoint specification in state['ppt_status']
    and call the create_dynamic_presentation tool to save it as a PowerPoint file.
    """,
    tools=[create_dynamic_presentation],
    output_key="ppt_generation_status"
)



root_agent = SequentialAgent(
    name="CourseCrafterAgent",
    description="Generates curriculum, PowerPoint, and quizzes for a course topic.",
    sub_agents=[describe_curriculum_agent,
                quiz_word_generator_agent,
                generate_ppt_agent,
                ppt_saver_agent
                ]
)
