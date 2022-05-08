def save_file(lesson, file):
    return f"lessons/{lesson.course.title}/{lesson.number}/{file}"


def save_video(lesson, file):
    _, ext = file.split('.')
    return f'lesson/{lesson.course.title}/{lesson.number}/video.{ext}'

def save_homework(lesson, file):
    _, ext = file.split('.')
    return f'lesson/{lesson.course.title}/{lesson.number}/homework.{ext}'

def save_materials(lesson, file):
    _, ext = file.split('.')
    return f'lesson/{lesson.course.title}/{lesson.number}/materials.{ext}'

def save_additional_materials(lesson, file):
    _, ext = file.split('.')
    return f'lesson/{lesson.course.title}/{lesson.number}/additional_materials.{ext}'