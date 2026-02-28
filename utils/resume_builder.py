def build_resume_prompt(
    name: str,
    location: str,
    experience: str,
    skills: str,
    physical_ability: str,
    availability: list[str],
    has_gap: bool,
) -> str:
    avail_str = ", ".join(availability) if availability else "Flexible"
    gap_note = (
        "The applicant has a gap in their work history and would like help "
        "framing it positively."
        if has_gap
        else ""
    )

    return (
        f"Create a resume for the following person:\n\n"
        f"Name: {name}\n"
        f"Location: {location}\n"
        f"Work Experience: {experience}\n"
        f"Skills: {skills}\n"
        f"Physical Ability Level: {physical_ability}\n"
        f"Availability: {avail_str}\n"
        f"{gap_note}"
    )


RESUME_SYSTEM_PROMPT = (
    "You are a compassionate professional resume writer helping someone "
    "experiencing homelessness re-enter the workforce.\n"
    "Write a clean, honest, 1-page resume in plain text. Use the address "
    "'(Address available upon request)'.\n"
    "Frame any employment gaps constructively — e.g., 'Career transition "
    "period: focused on personal development and community support.'\n"
    "Highlight transferable skills. Do not fabricate experience. Use a "
    "simple, clean format with sections: Summary, Skills, Experience, "
    "Availability."
)
