from app.models import Result


def check_answer(request, questions, category):
    correct = 0
    for q in questions:
        if q.is_correct_check(request.POST.get(q.name)):
            correct += 1

    result = Result.objects.create(
        user=request.user,
        category=category,
        total_question=len(questions),
        total_correct=correct
    )
    context = {
        'result': result
    }

    return context
