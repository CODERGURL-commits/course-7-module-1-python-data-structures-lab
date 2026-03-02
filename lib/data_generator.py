def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily using a generator expression.
    """
    return (s for s in student_list if s[2].lower() == major.lower())