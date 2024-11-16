class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        """Allows the programmer to watch a course and gain skills if the language matches."""
        if language == self.language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name} and earned {skills_earned} skills."
        else:
            return f"{self.name} does not know {language}."

    def change_language(self, new_language: str, skills_needed: int) -> str:
        """Changes the programmer's language if skills are sufficient."""
        if skills_needed <= self.skills and new_language != self.language:
            previous_language = self.language
            self.language = new_language
            return f"{self.name} switched from {previous_language} to {new_language}."
        elif skills_needed <= self.skills and new_language == self.language:
            return f"{self.name} already knows {self.language}."
        else:
            return f"{self.name} needs {skills_needed - self.skills} more skills to switch to {new_language}."


# Execute exercise:
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))  # John does not know Python.
print(programmer.change_language("Java", 30))  # John already knows Java.
print(programmer.change_language("Python", 100))  # John needs 50 more skills to switch to Python.
print(programmer.watch_course("Java: Zero to Hero", "Java", 50))  # John watched Java: Zero to Hero and earned 50 skills.
print(programmer.change_language("Python", 100))  # John switched from Java to Python.
print(programmer.watch_course("Python Masterclass", "Python", 84))  # John watched Python Masterclass and earned 84 skills.
