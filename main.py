import configparser

from google import genai

config = configparser.ConfigParser()
config.read("config.ini")

client = genai.Client(api_key=config["GOOGLE"]["GEMINI_API_KEY"])


def get_files(
    client: genai.Client,
    assignment_path: str,
    anwser_path: str,
    solution_path: str | None,
) -> list:
    assignment = client.files.upload(file=assignment_path)
    anwser = client.files.upload(file=anwser_path)
    ret = [assignment, anwser]
    if solution_path:
        solution = client.files.upload(file=solution_path)
        ret.append(solution)
    return ret


prompt = "Pls grade the given assignment using the assignment problem set, anwsers, and an optional solutions file provided. Pls make sure to grade slightly harshly and output all your reasoning and feedback. The weightage of each individual question is in the solutions set."
ret = get_files(
    client,
    "assignments/PHYS 271ProblemAssignment1.pdf",
    "assignments/Phys271Assignment1.pdf",
    "assignments/PHYS271ProblemAssignment1SOLUTIONS.pdf",
)
contents = [prompt] + ret
response = client.models.generate_content(
    model=config["GOOGLE"]["MODEL"], contents=contents
)

print(response.text)
